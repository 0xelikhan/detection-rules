# detection-rules

![Validate Detection Rules](../../actions/workflows/validate-detections.yml/badge.svg)
![Rules](https://img.shields.io/badge/Sigma_Rules-15%2B-blue?style=flat-square)
![MITRE](https://img.shields.io/badge/MITRE_ATT%26CK-8_Tactics-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Backends](https://img.shields.io/badge/Converts_to-Elastic_%7C_Splunk-navy?style=flat-square)

> Sigma and YARA detection rules mapped to MITRE ATT&CK.  
> Every rule is automatically validated and converted to Elastic and Splunk formats on every push via GitHub Actions.

---

## How the pipeline works

```
Write Sigma rule (.yml)
        ↓
git push → GitHub Actions triggers
        ↓
validate_rules.py — checks required fields + valid YAML
        ↓
sigma convert → Elastic (Lucene) + Splunk SPL
        ↓
✓ Green checkmark — rule is production-ready
```

This is Detection-as-Code. Same workflow used in production detection engineering teams — no broken rules reach `main`.

---

## Coverage

| Tactic | Rules | MITRE IDs |
|--------|-------|-----------|
| Initial Access | | T1566.001 |
| Execution | | T1059.001, T1059.003 |
| Persistence | | T1547.001, T1053.005 |
| Privilege Escalation | | T1055, T1068 |
| Defense Evasion | | T1562.001, T1070.001 |
| Discovery | | T1082, T1083 |
| Lateral Movement | | T1021.002, T1550.002 |
| Command and Control | | T1071.004 |

---

## Structure

```
detection-rules/
├── .github/
│   └── workflows/
│       └── validate-detections.yml
├── sigma/
│   ├── initial-access/
│   ├── execution/
│   ├── persistence/
│   ├── privilege-escalation/
│   ├── defense-evasion/
│   ├── discovery/
│   ├── lateral-movement/
│   └── command-and-control/
├── yara/
├── converted/
└── scripts/
    └── validate_rules.py
```

---

## Rule format

```yaml
title: PowerShell Encoded Command Execution
status: experimental
description: >
  Detects PowerShell launched with an encoded command flag.
  Common in malware loaders and post-exploitation frameworks.
logsource:
  product: windows
  category: process_creation
detection:
  selection:
    Image|endswith: '\powershell.exe'
    CommandLine|contains:
      - '-EncodedCommand'
      - '-enc '
  condition: selection
falsepositives:
  - Legitimate admin scripts using encoded commands
level: high
tags:
  - attack.execution
  - attack.t1059.001
```

---

## Lab context

Rules are tested against a live Proxmox-based SOC lab — Wazuh SIEM with Sysmon on Windows endpoints and auditd on Linux. Attack scenarios from Atomic Red Team and MITRE CALDERA verify each rule fires before it gets committed.

**Related repos:**
[homelab](https://github.com/YOUR-USERNAME/homelab) · [cloud](https://github.com/YOUR-USERNAME/cloud) · [scripts](https://github.com/YOUR-USERNAME/scripts)

---

## License

MIT — see [LICENSE](LICENSE). Use freely with attribution.
