#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument_str = "argument"
    punctuation = ":"
    args_no = len(sys.argv)
    if args_no != 2:
        argument_str = "arguments"
    if args_no == 1:
        punctuation = "."
    print(f"{args_no - 1} {argument_str}{punctuation}")
    for i in range(1, args_no):
        print(f"{i}: {sys.argv[i]}")
