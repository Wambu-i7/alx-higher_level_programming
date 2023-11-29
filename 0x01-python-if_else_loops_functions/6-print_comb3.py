#!/usr/bin/python3
combo = []
for tens in range(10):
    for ones in range(tens + 1, 10):
        combo.append("{:d}{:d}".format(tens, ones))
result = ", ".join(combo)
print(result)
