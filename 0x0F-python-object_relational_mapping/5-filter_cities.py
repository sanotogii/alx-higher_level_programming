#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM cities WHERE state_id = \
        (SELECT id FROM states WHERE name LIKE BINARY %s) \
        ORDER BY cities.id ASC", (argv[4], ))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
