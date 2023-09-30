#!/usr/bin/python3
"""

makes a POST request and gets json response

"""


import requests
import sys


if __name__ == "__main__":
    argv = sys.argv
    q = "" if len(argv) == 1 else argv[1]
    params = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=params)
    try:
        data = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if data == {}:
            print("No result")
        else:
            print(f"[{data.get('id')}] {data.get('name')}")
