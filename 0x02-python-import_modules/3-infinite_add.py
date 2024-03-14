#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the result of the addition of all arguments."""
    from sys import argv
    arg_len = len(argv)
    arg_len -= 1
    sum = 0
    if arg_len == 0:
        print("{}".format(sum))
    elif arg_len > 0:
        for i in range(1, arg_len+1):
            sum += int(argv[i])
        print("{:d}".format(sum))
