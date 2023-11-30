#!/usr/bin/python3
for c in reversed(range(ord('a'), ord('z') + 1)):
    print("{}".format(chr(c) if c % 2 == 0 else chr(c + ord('A')
        - ord('a'))), end='')
print()
