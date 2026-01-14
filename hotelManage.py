#hotel managemnt imports
########################################        IMPORTING SOME STUFF            ##############################################################
import os
import sys
import math 
import datetime
import time
import sqlite3 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
###################################                  ROOM PROPERTIES HERE                    #####################################################
economy_room ={
    "room_type": "Economy",
    "price": 100,
    "amenities": ["Television"],
    "capacity": 2,  
    "bed_type": "Queen Size",
    "room_size": "200 sq ft",
}
suite_room ={
    "room_type": "Suite",
    "price": 200,
    "amenities": ["Television", "Air Conditioning", "Mini Bar","freebie"],
    "capacity": 4,
    "bed_type": "King Size",
    "room_size": "400 sq ft",
}
deluxe_room ={
    "room_type": "Deluxe",
    "price": 150,
    "amenities": ["Television", "Air Conditioning", "Mini Bar"],
    "capacity": 3,
    "bed_type": "King Size",
    "room_size": "300 sq ft",
}
deluxeRoomAvailable = 20 
suiteRoomAvailable = 10
ecRoomAvailable = 30        
# Room lists
economyRoomList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
deluxeRoomList = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
suiteRoomList = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

######################################          ESTABLISH SQL CONNECTION                 #######################################
connection = sqlite3.connect('hotel_management.db')
cursor = connection.cursor()

########************************** id IS A integer is a random number between 1000 and 9999 geerated unique to a room .....

#######################################             CREATING TABLES IN DB            ############################################################

createTableCommand = """CREATE TABLE IF NOT EXISTS
bookings (id INTEGER PRIMARY KEY, room_type TEXT, room_number INTEGER, customer_name TEXT, phone_no REAL, aadhar_no REAL, check_in_time TEXT, check_in_date TEXT, check_out_date TEXT, no_of_guests INTEGER, total_amount REAL)"""
cursor.execute(createTableCommand)
connection.commit()
#create a table for reservation over here 
createReserveCommand = """ CREATE TABLE IF NOT EXISTS
reservation(id INTEGER PRIMARY KEY, room_type TEXT, room_number INTEGER, customer_name TEXT, phone_no REAL, aadhar_no REAL, check_in_time TEXT, check_in_date TEXT)"""
cursor.execute(createReserveCommand)
connection.commit()

#########################################                LIST OF SQL QUERIES          ##########################################################

def add_booking(id, room_type, room_number, customer_name, phone_no, aadhar_no, check_in_time, check_in_date, check_out_date, no_of_guests, total_amount):
    cursor.execute("INSERT INTO bookings (id, room_type, room_number, customer_name, phone_no, aadhar_no, check_in_time, check_in_date, check_out_date, no_of_guests, total_amount) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (id, room_type, room_number, customer_name, phone_no, aadhar_no, check_in_time, check_in_date, check_out_date, no_of_guests, total_amount))
    connection.commit()
def add_reservation(id, room_type, room_number, customer_name, phone_no, aadhar_no, check_in_time, check_in_date):
    cursor.execute("INSERT INTO reservation (id, room_type, room_number, customer_name, phone_no, aadhar_no, check_in_time, check_in_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (id, room_type, room_number, customer_name, phone_no, aadhar_no, check_in_time, check_in_date))
    connection.commit()
def view_bookings():
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return rows
def view_all():
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    cursor.execute("SELECT * FROM reservation")
    liu = cursor.fetchall()
    return list(rows + liu)
def view_bookings_by_room_type(room_type):
    cursor.execute("SELECT * FROM bookings WHERE room_type = ?", (room_type,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
def view_reservation_by_room_type(room_type):
    cursor.execute("SELECT * FROM reservation WHERE room_type = ?", (room_type,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
def check_out_booking_byRoomNo(room_number):
    cursor.execute("DELETE FROM bookings WHERE room_number = ?", (room_number,))
    connection.commit()
def cancel_reservation_byRoomNo(room_number):
    cursor.execute("DELETE FROM reservation WHERE room_number = ?", (room_number,))
    connection.commit()
def check_out_booking_byId(id):
    cursor.execute("DELETE FROM bookings WHERE id = ?", (id,))
    connection.commit()
def cancel_reservation_byId(id):
    cursor.execute("DELETE FROM reservation WHERE id = ?", (id,))
    connection.commit()
def returnValueByRoomNo(room_number):
    cursor.execute("SELECT * FROM bookings WHERE room_number = ?", (room_number,))
    row = cursor.fetchone()
    if row:
        return row
    else:
        return None
def returnValueById(id):
    cursor.execute("SELECT * FROM bookings WHERE id = ?", (id,))
    row = cursor.fetchone()
    if row:
        return row
    else:
        return None   
def getSomethingByRoomNo(room_number, column_name):
    cursor.execute(f"SELECT {column_name} FROM bookings WHERE room_number = ?", (room_number,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        return None
def getSomethingById(id, column_name):
    cursor.execute(f"SELECT {column_name} FROM bookings WHERE id = ?", (id,))
    row = cursor.fetchone()
    try:
        if row is None:
            print("No person found with that ID.")
            return None
        if row:
            return row[0]
        else:
            return None
    except IndexError:
        print(f"Column '{column_name}' does not exist in the bookings table.")
        return None
    except sqlite3.OperationalError as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        print("Query called")
def modifySomethingById(id, column_name, newValue):
    try:
        cursor.execute(f"UPDATE bookings SET {column_name} = ? WHERE id = ?",(newValue, id,))
        connection.commit()
    except Exception as e:
        print(f"an error occured as: {e}")
        return None
    finally:
        print("function called")
def getSomethingByRoomNo_R(room_number, column_name):
    cursor.execute(f"SELECT {column_name} FROM reservation WHERE room_number = ?", (room_number,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        return None
def getSomethingById_R(id, column_name):
    cursor.execute(f"SELECT {column_name} FROM reservation WHERE id = ?", (id,))
    row = cursor.fetchone()
    try:
        if row is None:
            print("No person found with that ID.")
            return None
        if row:
            return row[0]
        else:
            return None
    except IndexError:
        print(f"Column '{column_name}' does not exist in the bookings table.")
        return None
    except sqlite3.OperationalError as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        print("Query called")
def modifySomethingById_R(id, column_name, newValue):
    try:
        cursor.execute(f"UPDATE reservation SET {column_name} = ? WHERE id = ?",(newValue, id,))
        connection.commit()
    except Exception as e:
        print(f"an error occured as: {e}")
        return None
    finally:
        print("function called")
def pushIdsList(db_name):
    roomIds = []
    cursor.execute(f"SELECT room_id FROM {db_name}")
    rows = cursor.fetchall()

    for row in rows:
        roomIds.append(int(row[0]))
def pushSomethingIntoList(db_name, column_name): 
    r_list = []
    cursor.execute(f"SELECT {column_name} FROM {db_name}")
    rows = cursor.fetchall()
    for row in rows:
        r_list.append(row[0])
    return r_list
def pushSomethingIntoListRName(db_name, column_name, room_name): 
    r_list = []
    cursor.execute(f"SELECT {column_name} FROM {db_name} WHERE room_type = ?",(room_name,))
    rows = cursor.fetchall()
    for row in rows:
        r_list.append(row[0])
    return r_list
def refreshEconomyRoomList(db_name, fname):
    Eroom_nos = []
    Eroom_nos = pushSomethingIntoListRName(db_name, 'room_number', 'Economy')
    liveList = []
    liveList = list(set(fname) - (set(fname) & set(Eroom_nos)))
    return liveList
def refreshSuiteRoomList(db_name, fname):
    Eroom_nos = pushSomethingIntoListRName(db_name, 'room_number', 'Suite')
    Eroom_nos = [int(x) for x in Eroom_nos]
    liveList = []
    liveList = list(set(fname) - (set(fname) & set(Eroom_nos)))
    return liveList
def refreshDeluxeRoomList(db_name, fname):
    Eroom_nos = []
    Eroom_nos = pushSomethingIntoListRName(db_name, 'room_number', 'Deluxe')
    liveList = []
    liveList = list(set(fname) - (set(fname) & set(Eroom_nos)))
    return liveList

############################################                VARIABLES USED IN LIVE TRACKING...........
liveDeluxeList = refreshDeluxeRoomList('reservation', deluxeRoomList)
liveDeluxeList2 = refreshDeluxeRoomList('bookings', liveDeluxeList)     #use tis a

liveSuiteList = refreshSuiteRoomList('reservation', suiteRoomList)
liveSuiteList2 = refreshSuiteRoomList('bookings', liveSuiteList)        ###USE THIS 

liveEconomyList = refreshEconomyRoomList('reservation', economyRoomList)
liveEconomyList2 = refreshEconomyRoomList('bookings', liveEconomyList)     #USE THIS

##########################################################        SAMPLE USAGE        ########################################################
#view_bookings()

#query = getSomethingById(7889, "room_type")
#print(f"Query result: {query}")

#modifySomethingById(7889, "room_type", "Deluxe")
#add_reservation(8456, "Suite", 45, "bamsay", 7878787878, 565656565666, "1:34", "28/09/25")
#add_reservation(7476, "Deluxe", 65, "kmsay", 7876787878, 565690565666, "1:34", "28/09/25")
#modifySomethingById(3456, 'room_number', 55)
#modifySomethingById(3476, 'room_number', 35)
#modifySomethingById(7889, 'room_number', 35)
#x = pushSomethingIntoList("reservation", "id")
#print(x)
#room_ids = pushSomethingIntoListRName('reservation', 'room_number', 'Suite')
#x = list(set(suiteRoomList) - (set(suiteRoomList) & set(room_ids)))
#print(x)

#print(room_ids) #prints a list of requested items from db table for usage



