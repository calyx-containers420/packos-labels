"""Read a local UTF-8 ERP CSV and emit only the identifiers used by PackOS."""
import argparse
import csv
import json
import re
import sys


def prepare(source, customer_column, sku_column, product_column):
    reader = csv.DictReader(source, strict=True)
    columns = [customer_column, sku_column]
    if product_column is not None:
        columns.append(product_column)
    if len(set(columns)) != len(columns):
        raise ValueError("Select a different CSV column for each identifier.")
    headers = reader.fieldnames or []
    if any(headers.count(name) != 1 for name in columns):
        raise ValueError("Each selected column must appear exactly once in the header.")

    rows = []
    for number, fields in enumerate(reader, 1):
        if number > 100:
            raise ValueError("Select an export sample of at most 100 records.")
        if None in fields or None in fields.values():
            raise ValueError(f"Record {number} has a different column count from the header.")
        row = {}
        customer = fields[customer_column]
        if customer:
            digits = customer.lstrip("0")
            if not re.fullmatch(r"[0-9]{1,9}", digits):
                raise ValueError(f"Record {number} has an invalid LabelTraxx customer number.")
            row["customerNumber"] = int(digits)
        for column, key, pattern in [(sku_column, "sku", r"[A-Za-z0-9_.:-]{1,100}"),
                                     (product_column, "productNumber", r"[A-Za-z0-9._-]{1,40}")]:
            if column is not None and fields[column]:
                if not re.fullmatch(pattern, fields[column]):
                    raise ValueError(f"Record {number} has an invalid {key}.")
                row[key] = fields[column]
        rows.append(row)
    if not rows:
        raise ValueError("Select a CSV with at least one data record.")
    return {"sample": rows}


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("csv_file")
    cli.add_argument("--customer-column", required=True)
    cli.add_argument("--sku-column", required=True)
    cli.add_argument("--product-column")
    args = cli.parse_args()
    try:
        with open(args.csv_file, encoding="utf-8-sig", newline="") as source:
            output = prepare(source, args.customer_column, args.sku_column, args.product_column)
    except (ValueError, csv.Error, OSError) as exc:
        cli.exit(2, f"Could not prepare the sample. {exc}\n")
    json.dump(output, sys.stdout)
    print()


if __name__ == "__main__":
    main()
