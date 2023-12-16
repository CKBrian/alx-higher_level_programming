#!/usr/bin/python3

"""
Defines a module that  takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys


if __name__ == "__main__":

    usr, password, db_name = sys.argv[1:4]

    conn = MySQLdb.connect(host="localhost", charset="utf8", user=usr,
                           passwd=password, db=db_name)

    cursor = conn.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities " \
            "LEFT JOIN states ON state_id = states.id"
    cursor.execute(query)

    city_rows = cursor.fetchall()
    for city in city_rows:
        print("({}, '{}', '{}')".format(city[0], city[1], city[2]))

    cursor.close()
    conn.close()
