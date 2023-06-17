#!/usr/bin/python3
"""
    Lists all cities from the given argument from the database
    hbtn_0e_0_usa.
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ main function """
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    curs = db.cursor()
    curs.execute("SELECT cities.name, states.name FROM states\
                 JOIN cities ON cities.state_id = states.id\
                 ORDER BY cities.id ASC")
    results = curs.fetchall()
    city_list = []
    for row in results:
        if row[1] == argv[4] and row[0] not in city_list:
            city_list.append(row[0])

    unique_cities = ', '.join(city_list)
    print(unique_cities)
