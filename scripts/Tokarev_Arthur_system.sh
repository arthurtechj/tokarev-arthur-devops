
#!/bin/bash

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INFO_FILE="$PROJECT_DIR/Tokarev_Arthur_info.txt"

echo "=============================="
echo "Student Information"
echo "=============================="

if [ -f "$INFO_FILE" ]; then
    cat "$INFO_FILE"
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi

echo
echo "=============================="
echo "System Information"
echo "=============================="

echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -s)"

echo "Disk Usage:"
df -h /

echo "Memory Usage:"
free -h
