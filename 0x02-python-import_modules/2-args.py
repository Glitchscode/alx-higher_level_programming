#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the number of and the list of its arguments."""
    import sys
    arg_len = len(sys.argv)
    arg_len -= 1
    if arg_len == 0:
        print("{} arguments.".format(arg_len))
    elif arg_len == 1:
        print("{} argument:".format(arg_len))
        for i in range(1, arg_len+1):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments:".format(arg_len))
        for i in range(1, arg_len+1):
            print("{}: {}".format(i, sys.argv[i]))
