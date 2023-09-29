#!/usr/bin/python3
'''

using the requests module to retrieve a page

'''


import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    content = response.text
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
