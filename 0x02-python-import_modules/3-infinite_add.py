#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum_of_args = 0
    for i in range(1, len(sys.argv)):
        sum_of_args += int(sys.argv[i])
    print(sum_of_args)
