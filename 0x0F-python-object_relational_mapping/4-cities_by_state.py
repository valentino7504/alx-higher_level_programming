#!/usr/bin/python3
'''

Lists all cities in hbtn_0e_4_usa

'''


import MySQLdb
import sys


if __name__ == "__main__":
    argv = sys.argv
    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306
    )
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities INNER" +
        " JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC"
    )
    data = cur.fetchall()
    for row in data:
        print(row)
