"""
    Title: show_tables.py
    Author: Group 2
    Date: 8 July 2022
    Description: Outdoors Database show tables script.
"""

import mysql.connector
from mysql.connector import errorcode

#variable to has sql connection info
config = {
    "user": "outdoors_user",
    "password": "nature",
    "host": "127.0.0.1",
    "database": "outdoors",
    "raise_on_warnings": True
}
#connects to the database
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

#finally:
#    db.close()

#Displays Guide query
cursor = db.cursor()
cursor.execute("SHOW tables;")
tableColumns = cursor.fetchall()
print("-- DISPLAYING Guide RECORDS -- \n")
for tableColumns in tableColumns:
    print("Tables_in_outdoors: {}\n".format(tableColumns[0]))

