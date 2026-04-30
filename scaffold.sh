#!/bin/bash
# Run from inside your cloned detection-rules repo:
#   git clone git@github.com:YOUR-USERNAME/detection-rules.git
#   cd detection-rules && bash scaffold.sh

set -e
echo "Scaffolding detection-rules..."

mkdir -p .github/workflows
mkdir -p scripts
mkdir -p sigma/initial-access
mkdir -p sigma/execution
mkdir -p sigma/persistence
mkdir -p sigma/privilege-escalation
mkdir -p sigma/defense-evasion
mkdir -p sigma/discovery
mkdir -p sigma/lateral-movement
mkdir -p sigma/command-and-control
mkdir -p yara
mkdir -p converted

# gitkeep empty folders so git tracks them
for dir in sigma/initial-access sigma/execution sigma/persistence \
           sigma/privilege-escalation sigma/defense-evasion sigma/discovery \
           sigma/lateral-movement sigma/command-and-control yara converted; do
  touch "$dir/.gitkeep"
done

echo "Done."
echo ""
echo "Next: git add . && git commit -m 'Scaffold detection-rules repo' && git push"
