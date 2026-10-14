#!/bin/sh
# The claude.ai build: the plugin WITHOUT commands/.
#
# claude.ai offers a plugin's commands to the model as skills, and it ignores disable-model-invocation, so the three
# shortcuts (quote, quote-artwork, compare) were picked instead of quote-labels: asked "Quote 10,000 of my label from
# its artwork PDF", Claude loaded the quote-artwork shortcut, never loaded the PackOS tools and asked for an attachment
# (2026-10-13). The shortcuts stay in the repo for Claude Code, where commands are only ever typed.
#
#   scripts/build-claude-ai.sh                     -> dist/packos-labels-claude-ai.zip (mcp.packos.ai)
#   scripts/build-claude-ai.sh --mcp-url URL --test  a TEST build against another gateway (name, title and
#                                                   description say so, so it is never mistaken for the real one)
set -eu
cd "$(dirname "$0")/.."
MCP_URL=""; TEST=0
while [ $# -gt 0 ]; do
  case "$1" in
    --mcp-url) MCP_URL="$2"; shift 2 ;;
    --test) TEST=1; shift ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
done
OUT="$PWD/dist"; STAGE="$(mktemp -d)"; trap 'rm -rf "$STAGE"' EXIT
mkdir -p "$OUT"
cp -R .claude-plugin skills LICENSE NOTICE README.md .mcp.json "$STAGE"/
VERSION=$(node -p "require('./.claude-plugin/plugin.json').version")
node - "$STAGE" "$MCP_URL" "$TEST" <<'JS'
const fs = require('fs'), path = require('path');
const [stage, url, test] = process.argv.slice(2);
const pj = path.join(stage, '.claude-plugin/plugin.json');
const p = JSON.parse(fs.readFileSync(pj, 'utf8'));
if (test === '1') {
  p.name += '-test'; p.displayName = (p.displayName || p.name) + ' (test)'; p.version += '-test';
  p.description = 'TEST BUILD: ' + p.description + (url ? ' Points at a temporary test server.' : '');
}
fs.writeFileSync(pj, JSON.stringify(p, null, 2) + '\n');
if (url) {
  const mj = path.join(stage, '.mcp.json');
  const m = JSON.parse(fs.readFileSync(mj, 'utf8'));
  m.mcpServers.packos.url = url;
  fs.writeFileSync(mj, JSON.stringify(m, null, 2) + '\n');
}
JS
NAME="packos-labels-claude-ai"; [ "$TEST" = 1 ] && NAME="$NAME-test"
rm -f "$OUT/$NAME-$VERSION.zip"
(cd "$STAGE" && zip -qr "$OUT/$NAME-$VERSION.zip" . -x '.DS_Store' '*/.DS_Store')
if unzip -l "$OUT/$NAME-$VERSION.zip" | grep -q ' commands/'; then echo "commands/ leaked into the claude.ai build" >&2; exit 1; fi
echo "$OUT/$NAME-$VERSION.zip"
