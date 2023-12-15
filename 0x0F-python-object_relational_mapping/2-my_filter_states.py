#!/usr/bin/python3

"""
Defines a module that  takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys


if __name__ == "__main__":

    usr, password, db_name, state_name = sys.argv[1:5]

    conn = MySQLdb.connect(host="localhost", charset="utf8", user=usr,
                           passwd=password, db=db_name)

    cursor = conn.cursor()
    query = "SELECT * FROM states WHERE name = '{}'" \
            "COLLATE utf8_bin ORDER BY states.id ASC".format(state_name)
    cursor.execute(query)

    state_rows = cursor.fetchall()
    for state in state_rows:
        print("({}, '{}')".format(state[0], state[1]))

    cursor.close()
    conn.close()
