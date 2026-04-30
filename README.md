# Detection Rules

![Validate Detection Rules](../../actions/workflows/validate-detections.yml/badge.svg)


> Sigma and YARA detection rules. 


---

### Sigma Rules

| Tactic | Folder | Examples |
|--------|--------|----------|
| Initial Access | `sigma/initial-access/` | Phishing, drive-by compromise |
| Execution | `sigma/execution/` | PowerShell, scripting engines |
| Persistence | `sigma/persistence/` | Registry run keys, scheduled tasks |
| Privilege Escalation | `sigma/privilege-escalation/` | Process injection, exploitation |
| Defense Evasion | `sigma/defense-evasion/` | Disabling defenses, clearing logs |
| Discovery | `sigma/discovery/` | System enumeration, network scanning |
| Lateral Movement | `sigma/lateral-movement/` | SMB, Pass-the-Hash, admin shares |
| Command & Control | `sigma/command-and-control/` | DNS tunneling, C2 beacons |

### YARA Rules

| Folder | What's in it |
|--------|-------------|
| `yara/` | File-based malware detection rules |
