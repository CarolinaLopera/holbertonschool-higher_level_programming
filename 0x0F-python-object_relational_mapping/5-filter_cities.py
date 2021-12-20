#!/usr/bin/python3
  
'''Lists all cities from a state'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name='{}' \
            ORDER BY cities.id ASC;".format(argv[4]))

    result = []
    for i in cur.fetchall():
        result.append(i[0])

    print(', '.join(result))
