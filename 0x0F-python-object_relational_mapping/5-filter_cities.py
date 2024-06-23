#!/usr/bin/python3
"""a script that takes in the name of a state as an argument and lists all
   cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    match = sys.argv[4]
    cur.execute("""SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name LIKE %s""", (match, ))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
