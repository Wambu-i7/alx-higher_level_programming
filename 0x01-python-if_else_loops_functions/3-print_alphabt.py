#!/usr/bin/python3
start_alph = ord('a')
end_alph = ord('z')
for alphabets in range(start_alph, end_alph + 1):
    char = chr(alphabets)
    if char not in ['q', 'e']:
        print("{}".format(char), end='')
