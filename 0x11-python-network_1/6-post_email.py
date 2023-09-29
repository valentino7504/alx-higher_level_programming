#!/usr/bin/python3
'''

using requests module to make a post request

'''


import requests
import sys


if __name__ == "__main__":
    argv = sys.argv
    url = argv[1]
    email = argv[2]
    params = {"email": email}
    response = requests.post(url, data=params)
    print(response.text)
