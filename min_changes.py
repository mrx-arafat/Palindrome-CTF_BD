# min_changes.py
import sys

def min_changes_to_palindrome(s):
    changes = 0
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            changes += 1
    return changes

for line in sys.stdin:
    s = line.strip().split(':')[-1]
    if s:
        print(min_changes_to_palindrome(s))
