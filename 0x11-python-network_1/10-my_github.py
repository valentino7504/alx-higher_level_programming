#!/usr/bin/python3
"""

gets data about an authorised github user

"""


import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    headers = {
        "Authorization": f"token {password}"
    }
    response = requests.get(f"https://api.github.com/user", headers=headers)
    print(response.json().get("id"))
