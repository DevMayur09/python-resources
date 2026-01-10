#!/bin/bash

# Check if number is provided
if [ -z "$1" ]; then
  echo "Usage: ./create_files.sh <number>"
  exit 1
fi

count=$1

for ((i=1; i<=count; i++)); do
  printf -v num "%02d" "$i"
  touch "${num}_solution.py"
done

echo "Created $count files successfully."
