#!/usr/bin/python3
'''

Creates a POST request with urllib

'''


import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    argv = sys.argv
    url = argv[1]
    email = argv[2]
    params = {"email": email}
    data = urllib.parse.urlencode(params)
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
