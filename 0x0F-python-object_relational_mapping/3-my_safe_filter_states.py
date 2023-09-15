#!/usr/bin/python3
"""

This module selects and displays the
state the user wants

"""


import MySQLdb
import sys


if __name__ == "__main__":
    argv = sys.argv
    db = MySQLdb.connect(host="localhost", user=f"{argv[1]}",
                         passwd=f"{argv[2]}", db=f"{argv[3]}", port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE " +
                "BINARY %(name)s ORDER BY id ASC;",
                {"name": argv[4]})
    data = cur.fetchall()
    for row in data:
        print(row)
