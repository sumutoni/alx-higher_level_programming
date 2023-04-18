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
    command = """SELECT city_name FROM
                 (SELECT cities.name AS city_name, states.name AS state_name
                 FROM cities
                 INNER JOIN states ON cities.state_id = states.id)
                 AS citystate
                 WHERE state_name LIKE BINARY '{}'""".format(state)
    curs.execute(command)
    print(", ".join(city[0] for city in curs.fetchall()))
    curs.close()
    db.close()
