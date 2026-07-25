#!/usr/bin/env python3
"""Render template.html + site.yaml -> index.html. No dependencies.

site.yaml is a flat key: value map (a deliberate YAML subset so this
script needs no PyYAML). Unknown or unrendered {{tokens}} fail the build.
"""
import re
import sys

def load_config(path="site.yaml"):
    config = {}
    for lineno, raw in enumerate(open(path, encoding="utf-8"), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            sys.exit(f"site.yaml:{lineno}: expected 'key: value', got: {line}")
        key, _, value = line.partition(":")
        value = value.strip().strip("'\"")
        config[key.strip()] = value
    return config

def main():
    config = load_config()
    html = open("template.html", encoding="utf-8").read()

    used = set()
    def sub(match):
        key = match.group(1)
        if key not in config:
            sys.exit(f"template.html references {{{{{key}}}}} but site.yaml has no such key")
        used.add(key)
        return config[key]

    html = re.sub(r"\{\{\s*([a-z0-9_]+)\s*\}\}", sub, html)

    unused = set(config) - used
    if unused:
        print(f"note: unused site.yaml keys: {', '.join(sorted(unused))}")

    open("index.html", "w", encoding="utf-8").write(html)
    print(f"rendered index.html ({len(used)} keys substituted)")

if __name__ == "__main__":
    main()
