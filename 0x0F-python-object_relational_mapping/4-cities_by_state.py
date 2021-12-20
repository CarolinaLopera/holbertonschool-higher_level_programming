#!/usr/bin/python3

'''Lists all cities from a database'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities, states WHERE cities.state_id = states.id \
            ORDER BY cities.id ASC;")

    result = cur.fetchall()
    for i in result:
        print(i)
