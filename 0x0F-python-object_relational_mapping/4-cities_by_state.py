#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON states.id = cities.state_id \
        ORDER BY cities.id")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
