#!/usr/bin/python3
'''

Gets a particular variable from the header

'''


import urllib.request
import sys


argv = sys.argv
with urllib.request.urlopen(argv[1]) as response:
    headers = dict(response.headers)
    print(headers.get("X-Request-Id"))
