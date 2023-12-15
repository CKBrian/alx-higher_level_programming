#!/usr/bin/python3
"""
 defines a module that lists all states from the database hbtn_0e_0_usa and
 Uses the module MySQLdb (import MySQLdb) to connect to  MySQL
 server on localhost at port 3306
 """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # creates connection to the mySQL server
    conn = MySQLdb.connect(user=username, host="localhost",
                           passwd=password, db=db_name, charset="utf8")

    cursor = conn.cursor()  # cursor object to execute queries

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")  # SQL query

    states_rows = cursor.fetchall()  # fetches the table rows

    for state in states_rows:
        print("({}, '{}')".format(state[0], state[1]))

    cursor.close()
    conn.close()
