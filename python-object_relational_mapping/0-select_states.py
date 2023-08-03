#!/usr/bin/python3
""" lsscript that lists all states from a database """
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("Usage: script_name, username, password, db")

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        for row in cur.fetchall():
            print(row)

    conn.close()
