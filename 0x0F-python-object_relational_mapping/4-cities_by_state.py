#!/usr/bin/python3

"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=a, passwd=b, db=c)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
