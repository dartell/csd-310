"""Darius Dinkins 7/10/2023 Assignment 8.2
Inserts, updates, and deletes records from a table using a python script

"""

import mysql.connector
from mysql.connector import errorcode

#variable for database connection
config = {
    "user": "root",
    "password": "35RUBcirarby$$$",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}
#Connects to the database
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

#Variables to use cursor method
cursor = db.cursor()
cursor2 = db.cursor()

#function that displays results of database changes.  Uses two arguments
def show_films(cursor, title):
# method to execute an inner join on all tables;
# iterate over the dataset and output the results to the terminal window.

# inner join query
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
    films = cursor.fetchall()
    # get the results from the cursor object
    print("\n -- {} --".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0],film[1],film[2]))

# Displays The purge movie insert.  Inserts the purge movie into database
show_films(cursor, "DISPLAYING FILMS")
cursor2.execute("INSERT INTO film (film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES(4,'The Purge', 2013, 85, 'James DeMonaco', 3, 1)")
db.commit()
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

#Displays the update to change Alien to the horror genre 
cursor2.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")
db.commit()
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

#Displays the deletion of the gladiator move record
cursor2.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
db.commit()
show_films(cursor, "DISPLAYING FILMS AFTER DELETE- Removed Gladiator")