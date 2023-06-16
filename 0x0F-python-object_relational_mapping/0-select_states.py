#!/usr/bin/python3
import MySQLdb
from sys import argv
db = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])
curs = db.cursor()
curs.execute("SELECT * FROM states ORDER BY states.id ASC")
results = curs.fetchall()
for row in results:
    print(row)
curs.close()
db.close()
