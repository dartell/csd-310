"""
    Title: outdoors_query_business.py
    Author: Group 2
    Date: 12 July 2022
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

#Do enough customers buy equipment to keep equipment sales?
#Displays Customer Purchase query query
cursor = db.cursor()
cursor.execute("SELECT count(*) as totalEquipment, count(purchaseDate) as totalPurchased FROM equipment")
purchaseColumns = cursor.fetchall()
print("-- DISPLAYING Purchase QUERY -- \n")
for purchaseColumns in purchaseColumns:
    print("Total Equipment: {}\n Total Purchased: {}\n".format(purchaseColumns[0], purchaseColumns[1]))


#So far, they have conducted treks in Africa, Asia, and Southern Europe.
#Is there anyone of those locations that has a downward trend in bookings?
#Booking Query
Africa = 0
Asia = 0
Southern_Europe = 0
cursor = db.cursor()
cursor.execute("SELECT bookings.booking_id, trips.trip_id, trips.location_id FROM bookings INNER JOIN trips ON bookings.trip_id=trips.trip_id")
bookingColumns = cursor.fetchall()
print("-- DISPLAYING Bookings QUERY -- \n")
for bookingColumns in bookingColumns:
    if bookingColumns[2] == 1:
        Africa += 1
    if bookingColumns[2] == 2:
        Asia += 1
    if bookingColumns[2] == 3:
        Southern_Europe += 1

print("Africa: " + str(Africa))
print("Asia: "  + str(Asia))
print("Southern Europe: " + str(Southern_Europe))
print("\n")

#Trend Query
cursor = db.cursor()
cursor.execute("SELECT locations.location_name,DATE(trips.startdate),COUNT(bookings.client_id) as bookingTotals \n" 
               "FROM trips \n" 
               "INNER JOIN bookings on trips.trip_id=bookings.trip_id \n"
               "INNER JOIN locations on trips.location_id=locations.location_id \n"
               "GROUP BY locations.location_name,trips.startdate \n"
               "ORDER by location_name,startdate")
trendColumns = cursor.fetchall()
print("-- DISPLAYING Trend QUERY -- \n")
for trendColumns in trendColumns:
    print("Location Name: {}\n Start Date: {}\n Booking Totals: {}\n".format(trendColumns[0],trendColumns[1],trendColumns[2]))

# They are a little concerned about the age of some of the inventory. Are there inventory items that are over five years old?
# Displays equipment age query
cursor = db.cursor()
cursor.execute("SELECT equipment_id AS old_ID_equipment, description, DATE(inventoryDate) AS inventoryDate \n"  
               "FROM equipment WHERE inventoryDate < now() - interval 5 year")
equipmentIdAgeColumns = cursor.fetchall()
print("-- DISPLAYING Equipment ID AGE QUERY -- \n")
print("EQUIPMENT OLDER THAN FIVE YEARS\n")
for equipmentIdAgeColumns in equipmentIdAgeColumns:
    print("Equipment ID: {}\n Description: {}\n Date: {}\n".format(equipmentIdAgeColumns[0],equipmentIdAgeColumns[1],equipmentIdAgeColumns[2]))

#Displays number of old inventory items (Greater than 5 years)
cursor = db.cursor()
cursor.execute("SELECT COUNT(equipment_id) As old_inventory FROM equipment WHERE inventoryDate < now() - interval 5 year")
inventoryAgeColumns = cursor.fetchall()
print("-- DISPLAYING Number of old equipment QUERY -- \n")
for inventoryAgeColumns in inventoryAgeColumns:
    print("Number of equipment older than 5 years: {}\n".format(inventoryAgeColumns[0]))




# db.close


# # Template for displaying SQL queries
# """cursor = db.cursor()
# cursor.execute(“SELECT f_name, l_name, email FROM employee”) -- selecting three fields
# employees = cursor.fetchall()
# for employee in employee:
# print(“First Name: {}\n Last Name:{}\n Email:{}\n”.format(employee[0], employee[1], employee[2])) -- three fields"""

# #Bookings
# locations.location_name,trips.startdate,count(bookings.client_id) as bookingTotals
# from trips
# INNER JOIN bookings on trips.trip_id=bookings.trip_id
# INNER JOIN locations on trips.location_id=locations.location_id
# GROUP BY locations.location_name,trips.startdate
# ORDER by location_name,startdate;