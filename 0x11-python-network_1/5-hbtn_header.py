#!/usr/bin/python3
'''

Gets headers of a request using requests module

'''


import requests
import sys


if __name__ == "__main__":
    argv = sys.argv
    response = requests.get(argv[1])
    print(response.headers.get("X-Request-Id"))
