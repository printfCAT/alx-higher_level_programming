#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    add = 0
    add = int(add)
    for i in range (1, length + 1):
        sys.argv[i] = int(sys.argv[i])
        add = add + sys.argv[i]
    print("{}".format(add))
