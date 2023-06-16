#!/usr/bin/python3
""" Lists all states starting with N from the database hbtn_0e_0_usa. """


import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ main function """
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM states\
                 WHERE name LIKE 'N%' ORDER BY states.id ASC")
    results = curs.fetchall()
    for row in results:
        print(row)
