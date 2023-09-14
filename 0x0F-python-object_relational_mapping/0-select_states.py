#!/usr/bin/python3
"""

This module selects and displays all states in the
database

"""
import MySQLdb
import sys


argv = sys.argv
db = MySQLdb.connect(host="localhost", user=f"{argv[1]}", passwd=f"{argv[2]}", db=f"{argv[3]}", port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
data = cur.fetchall()
for row in data:
    print(row)
