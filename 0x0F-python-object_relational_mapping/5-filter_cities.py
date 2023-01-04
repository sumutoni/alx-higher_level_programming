#!/usr/bin/python3
""" Import all cities from database"""

import MySQLdb as mdb
import sys

if __name__ == "__main__":
    db = mdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("""SELECT name FROM cities LEFT JOIN
                 (SELECT id As s_id WHERE name = %s) ON
                 s_id = state_id ORDER BY id ASC;""", (sys.argv[4],))
    for city in curs.fetchall():
        print(city)
    curs.close()
    db.close()
