#!/usr/bin/python3
'''

Gets a particular variable from the header

'''


import urllib.request
import sys


if __name__ == "__main__":
    argv = sys.argv
    with urllib.request.urlopen(argv[1]) as response:
        headers = response.getheaders()
    for header in headers:
        if header[0] == "X-Request-Id":
            print(header[1])
