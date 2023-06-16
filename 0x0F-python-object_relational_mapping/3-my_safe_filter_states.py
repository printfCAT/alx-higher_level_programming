#!/usr/bin/python3
"""
    Lists all states matching the terminal input
    from the database hbtn_0e_0_usa.
 """


import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ main function """
    username = argv[1]
    password = argv[2]
    database = argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)
    curs = db.cursor()
    name = argv[4]
    curs.execute("SELECT * FROM states WHERE BINARY name='{}'\
                 ORDER BY states.id ASC".format(name))
    results = curs.fetchall()
    for row in results:
        print(row)
