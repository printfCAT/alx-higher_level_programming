#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM states")
    results = curs.fetchall()
    for row in results:
        print(row)
