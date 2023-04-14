#!/usr/bin/python3
"""Script to print all states matching passed argument"""

import sys
import MySQLdb as mdb


if __name__ == "__main__":
    db = mdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    state = sys.argv[4]
    curs.execute("""SELECT * FROM states WHERE name = %s
                 ORDER BY id ASC""", (state,))
    for st in curs.fetchall():
        print(st)
    curs.close()
    db.close()
