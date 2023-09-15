#!/usr/bin/python3
'''

Gets all cities in a particular state from the hbtn_0e_4_usa

'''


import MySQLdb
import sys


if __name__ != "__main__":
    exit()
argv = sys.argv
db = MySQLdb.connect(
    host="localhost",
    user=argv[1],
    passwd=argv[2],
    db=argv[3]
)
cursor = db.cursor()
cursor.execute(
    "SELECT cities.name FROM cities INNER JOIN states ON " +
    "cities.state_id=states.id WHERE states.name=%(name)s", {"name": argv[4]}
)
data = list(cursor.fetchall())
data_string = ", ".join([city[0] for city in data])
print(data_string)
