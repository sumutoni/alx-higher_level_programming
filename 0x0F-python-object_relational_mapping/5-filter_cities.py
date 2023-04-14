#!/usr/bin/python3
"""
Script to print all cities of state based on
state name passed as argument
"""

import sys
import MySQLdb as mdb


if __name__ == "__main__":
    db = mdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    state = sys.argv[4]
    command = """SELECT cities.name FROM cities
                 INNER JOIN states ON cities.state_id = states.id
                 WHERE states.name LIKE BINARY '{}'
                 ORDER BY cities.id ASC""".format(state)
    curs.execute(command)
    for city in curs.fetchall():
        print(city)
    curs.close()
    db.close()
