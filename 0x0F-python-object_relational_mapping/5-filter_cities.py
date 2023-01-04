#!/usr/bin/python3
""" Import all cities from database"""

import MySQLdb as mdb
import sys

if __name__ == "__main__":
    db = mdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("""SELECT name FROM cities WHERE state_id IN
                 (SELECT states.id As s_id FROM states
                 WHERE states.name = %s) ORDER BY id
                 ASC;""", (sys.argv[4],))
    for city in curs.fetchall():
        for c in city:
            print(c, end='')
        print(',')
    curs.close()
    db.close()
