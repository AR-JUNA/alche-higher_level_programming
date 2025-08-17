def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            result += "{}".format(chr(ord(c) - 32))
        else:
            result += "{}".format(c)
    print(result)
