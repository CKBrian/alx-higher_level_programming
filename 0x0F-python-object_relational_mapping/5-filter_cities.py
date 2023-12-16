#!/usr/bin/python3

"""
Defines a module that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa

"""
import MySQLdb
import sys


if __name__ == "__main__":

    usr, password, db_name, state_name = sys.argv[1:5]

    conn = MySQLdb.connect(host="localhost", charset="utf8", user=usr,
                           passwd=password, db=db_name)

    cursor = conn.cursor()
    query = "SELECT cities.name FROM cities " \
            "LEFT JOIN states ON state_id = states.id " \
            "WHERE states.name = %s COLLATE utf8_bin " \
            "ORDER BY cities.id ASC "
    cursor.execute(query, (state_name, ))

    city_rows = cursor.fetchall()
    names = [city[0] for city in city_rows]
    names = ", ".join(names)
    print("{}".format(names))

    cursor.close()
    conn.close()
