#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    arg = sys.arg[1]
    for x in range(1, arg):
        if arg == 0:
            print("0 arguments.")
        elif arg == 1:
            print("1 argument:")
            print(sys.argv)
        else:
            print("{} arguments:".format(arg))
            print(sys.argv)
