#!/bin/bash

# Read lines from stdin and process them
while IFS= read -r line; do
    echo "$line"
done | python3 min_changes.py
