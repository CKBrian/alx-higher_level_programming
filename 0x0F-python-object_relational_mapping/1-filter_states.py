#!/usr/bin/python3

""" Defines a module that  lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":

    usr = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", charset="utf8", user=usr,
                           passwd=password, db=db_name)

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE states.name LIKE 'N%'"
                   "ORDER BY states.id ASC")

    state_rows = cursor.fetchall()
    for state in state_rows:
        print("{}, '{}'".format(state_rows[0], state_rows[1]))

    cursor.close()
    conn.close()
