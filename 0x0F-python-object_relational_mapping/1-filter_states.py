#!/usr/bin/python3
"""

This module selects and displays all states in the
database that their names start with N

"""


import MySQLdb
import sys


if __name__ != "__main__":
    exit()
argv = sys.argv
db = MySQLdb.connect(host="localhost", user=f"{argv[1]}",
                     passwd=f"{argv[2]}", db=f"{argv[3]}", port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
data = cur.fetchall()
for row in data:
    print(row)
