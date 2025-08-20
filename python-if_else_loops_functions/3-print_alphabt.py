#!/usr/bin/python3
<<<<<<< HEAD
for c in range(97, 123):
    if c == 101 or c == 113:  # skip 'e' and 'q'
        continue
    print("{:c}".format(c), end="")
=======
for i in range(97, 123):
    if i != 101 and i != 113:  # skip 'e' (101) and 'q' (113)
        print("{}".format(chr(i)), end="")
>>>>>>> Add script to print lowercase alphabet without q and e
