#!/usr/bin/python3
"""
Script to print all states matching passed argument
and make sure it is safe from SQL injection
"""

import sys
import MySQLdb as mdb


if __name__ == "__main__":
    db = mdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    command = """SELECT cities.id, cities.name, states.name FROM cities
                 INNER JOIN states ON cities.state_id = states.id
                 ORDER BY cities.id ASC"""
    curs.execute(command)
    for city in curs.fetchall():
        print(city)
    curs.close()
    db.close()
