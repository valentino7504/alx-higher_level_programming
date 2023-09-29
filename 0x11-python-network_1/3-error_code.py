#!/usr/bin/python3
'''

Returns the error code if any from HTTP request

'''


import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    argv = sys.argv
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
