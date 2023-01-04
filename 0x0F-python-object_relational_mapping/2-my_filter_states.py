#!/usr/bin/python3
""" Import all states from database"""

import MySQLdb as mdb
import sys

if __name__ == "__main__":
    db = mdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("""SELECT * FROM states WHERE
                 name = {} ORDER BY id ASC;""".format(sys.argv[4]))
    for state in curs.fetchall():
        print(state)
    curs.close()
    db.close()
