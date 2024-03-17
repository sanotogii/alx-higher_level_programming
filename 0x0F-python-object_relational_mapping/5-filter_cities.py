#!/usr/bin/python3

"""
This script filters the cities of a state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    d = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=a, passwd=b, db=c)

    cursor = db.cursor()
    cmd = "SELECT cities.name FROM cities JOIN states ON cities.state_id \
            = states.id WHERE states.name LIKE BINARY \
            %s ORDER BY cities.id ASC"
    cursor.execute(cmd, (d, ))

    rows = cursor.fetchall()
    for row in rows:
        print(row[0], end="")
        if row != rows[-1]:
            print(", ", end="")
    print()
    cursor.close()
    db.close()
