#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    n = len(argv) - 1

    if n == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(n, "" if n == 1 else "s"))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
