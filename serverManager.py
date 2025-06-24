import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Users()")
cur.execute("CREATE TABLE IF NOT EXISTS Reservations(Name text, phone int(10), aadhar int(16), booking_time time, check_in_date date, check_out_date date, guest_count int)")
con.commit()

def authenticate():
    pass  #COMING SOON

def book_room(name,phone,aadhar,timeOfBooking,dateOfCheckIn,dateOfCheckOut,noOfGuests):
    query = f"INSERT INTO Reservations VALUES('{name}',{phone},{aadhar},'{timeOfBooking}','{dateOfCheckOut}','{dateOfCheckIn}',{noOfGuests})"

    cur.execute(query)
    con.commit()

def check_booking(aadhar):
    query = f"SELECT * FROM Reservations WHERE aadhar = {aadhar}"
    room_info = cur.execute(query)
    return cur.rowcount  #RETURNS NUMBER OF RESERVATIONS
    #OR USE the following to get full info
    #for info in room_info:
    #    print(info)  #RETURNS LIST OF INFO, FOLLOWING ORDER IN CREATE TABLE COMMAND

def cancel_booking(room_no,aadhar):
    query = f"DELETE FROM Reservation WHERE room_no = {room_no} AND aadhar = {aadhar}"
    cur.execute(query)
    con.commit()

def modify_booking():
    pass  #COMING SOON

if __name__ == "__main__":
    pass
