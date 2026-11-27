import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/integration-setup/scripts/prepare_erp_sample.py'


class PrepareSampleTest(unittest.TestCase):
    def prepare(self, csv):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            path.write_bytes(csv.encode("utf-8-sig"))
            return subprocess.run([sys.executable, SCRIPT, path, "--customer-column", "Customer",
                                   "--sku-column", "SKU", "--product-column", "Product"],
                                  capture_output=True, text=True)

    def test_selected_columns_only(self):
        result = self.prepare('Customer,SKU,Private,Product\r\n007,Mixed_Case,"irrelevant,\nnote",0001\r\n,Other,,\r\n')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"sample": [
            {"customerNumber": 7, "sku": "Mixed_Case", "productNumber": "0001"}, {"sku": "Other"}]})

    def test_rejects_incomplete_or_ambiguous_input_without_a_partial_sample(self):
        for content in ["Customer,SKU,SKU,Product\n1,2,3,4\n", "Customer,SKU,Product\n1,x\n",
                        "Customer,SKU,Product\n1,x,4\n2,invalid sku,5\n",
                        "Customer,SKU,Product\n"+"1,x,1\n"*101]:
            with self.subTest(content=content[:32]):
                result = self.prepare(content)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
