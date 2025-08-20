#!/usr/bin/python3
for c in range(97, 123):
    if c == 101 or c == 113:  # skip 'e' and 'q'
        continue
    print("{:c}".format(c), end="")
