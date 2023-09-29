#!/usr/bin/python3
'''

Gets error codes of a request using requests module

'''


import requests
import sys


if __name__ == "__main__":
    argv = sys.argv
    response = requests.get(argv[1])
    status = response.status_code
    if status >= 400:
        print(f"Error code: {status}")
    else:
        print(response.text)
