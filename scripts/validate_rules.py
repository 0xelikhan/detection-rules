#!/usr/bin/env python3
"""
Sigma rule validation script.
Runs in GitHub Actions CI — checks every .yml in sigma/ for
required fields and valid YAML before anything merges to main.
"""

import yaml
import sys
import glob

REQUIRED_FIELDS = ["title", "status", "description", "logsource", "detection"]
errors = []

rules = glob.glob("sigma/**/*.yml", recursive=True)

if not rules:
    print("WARNING: No Sigma rules found in sigma/ — add rules to get started.")
    sys.exit(0)

for path in rules:
    with open(path) as f:
        try:
            data = yaml.safe_load(f)
            if not isinstance(data, dict):
                errors.append(f"{path}: not a valid YAML mapping")
                continue
            for field in REQUIRED_FIELDS:
                if field not in data:
                    errors.append(f"{path}: missing required field '{field}'")
        except yaml.YAMLError as e:
            errors.append(f"{path}: YAML parse error: {e}")

if errors:
    print(f"\nFAILED — {len(errors)} error(s):\n")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)
else:
    print(f"OK — {len(rules)} rule(s) validated")
