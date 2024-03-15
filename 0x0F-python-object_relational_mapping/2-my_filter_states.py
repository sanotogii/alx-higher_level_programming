#!/usr/bin/python3

"""
 script that takes in an argument and displays all values
 in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=a, passwd=b, db=c)

    cursor = db.cursor()
    cmd = "SELECT * FROM states WHERE name = '{}'".format(state_name)
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
