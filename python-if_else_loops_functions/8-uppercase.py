#!/usr/bin/python3


def uppercase(str):
    result = []
    for ch in str:
        code = ord(ch)
        if 97 <= code <= 122:  # 'a'..'z'
            code -= 32         # convert to 'A'..'Z'
        result.append(chr(code))
    print("{}".format("".join(result)))
