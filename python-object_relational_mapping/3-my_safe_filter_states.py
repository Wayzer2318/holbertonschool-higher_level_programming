#!/usr/bin/python3
"""
displays all values in
table where name matche argument
"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306, 
            user=sys.argv[1],               
            passwd=sys.argv[2],
            db=sys.argv[3])

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM states  ORDER BY id ASC")
        for row in cur.fetchall():
            if row[1] == sys.argv[4]:
                print(row)

    conn.close()
