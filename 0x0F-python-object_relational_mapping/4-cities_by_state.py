#!/usr/bin/python3
""" Import all cities from database"""

import MySQLdb as mdb
import sys

if __name__ == "__main__":
    db = mdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("""SELECT cities.id, cities.name, states.name FROM cities
                 LEFT JOIN states ON state_id = states.id ORDER BY id ASC;""")
    for city in curs.fetchall():
        print(city)
    curs.close()
    db.close()
