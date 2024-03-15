#!/usr/bin/python3

"""
Write a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=a, passwd=b, db=c)

    cursor = db.cursor()
    cmd = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
