#!/usr/bin/python3
"""Script to print all states starting with 'N'"""

import sys
import MySQLdb as mdb


if __name__ == "__main__":
    db = mdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'
                 ORDER BY id ASC;""")
    for state in curs.fetchall():
        print(state)
    curs.close()
    db.close()
