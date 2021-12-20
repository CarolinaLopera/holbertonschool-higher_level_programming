#!/usr/bin/python3

'''Lists all states from a database'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}'".format(argv[4]))

    result = cur.fetchall()
    for i in result:
        print(i)
