#Darius Dinkins; 7/6/2023; Assignment 7.2
#Connects to movie database and displays 4 queries.

import mysql.connector
from mysql.connector import errorcode

#variable to has sql connection info
config = {
    "user": "root",
    "password": "35RUBcirarby$$$",
    "host": "127.0.0.1",
    "database": "movies",
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

#Displays Studio query
cursor = db.cursor()
cursor.execute("SELECT studio_id, studio_name FROM studio;")
studioColumns = cursor.fetchall()
print("-- DISPLAYING Studio RECORDS -- \n")
for studioColumns in studioColumns:
    print("Studio ID: {}\n Studio Name: {}\n".format(studioColumns[0], studioColumns[1]))

#Displays genre query
cursor = db.cursor()
cursor.execute("SELECT genre_id, genre_name FROM genre;")
genreColumns = cursor.fetchall()
print("-- DISPLAYING Genre RECORDS -- \n")
for genreColumns in genreColumns:
    print("Genre ID: {}\n Genre name: {}\n".format(genreColumns[0], genreColumns[1]))

#Displays films with runtimes less than two hours query
cursor = db.cursor()
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime<120;")
runColumns = cursor.fetchall()
print("-- DISPLAYING Short Film RECORDS -- \n")
for runColumns in runColumns:
    print("Film: {}\n Run Time: {}\n".format(runColumns[0], runColumns[1]))

#Displays Director query in order
cursor = db.cursor()
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director ASC;")
directorColumns = cursor.fetchall()
print("-- DISPLAYING Director RECORDS in Order -- \n")
for directorColumns in directorColumns:
    print("Film: {}\n Director: {}\n".format(directorColumns[0], directorColumns[1]))

db.close
# Template for displaying SQL queries
"""cursor = db.cursor()
cursor.execute(“SELECT f_name, l_name, email FROM employee”) -- selecting three fields
employees = cursor.fetchall()
for employee in employee:
print(“First Name: {}\n Last Name:{}\n Email:{}\n”.format(employee[0], employee[1], employee[2])) -- three fields"""