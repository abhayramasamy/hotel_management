############################################            IMPORTING SOME STUFF.....       ####################################################
import sys
import os
import random
import math
from hotelManage import view_all, add_reservation, cancel_reservation_byId, cancel_reservation_byRoomNo, add_booking, view_bookings, economyRoomList, deluxeRoomList, suiteRoomList, economy_room, deluxe_room, suite_room, view_bookings_by_room_type, check_out_booking_byId, check_out_booking_byRoomNo, modifySomethingById,liveDeluxeList2, liveEconomyList2, liveSuiteList2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

##################          WE NEED TO FIX THE NUMBER PROBLEM DO IT @ NIGHT !!!!!!!!
########################################              SOME VARIABLES                       ################################################
deluxeRoomAvailable = 20  # Number of Deluxe rooms available
suiteRoomAvailable = 10    # Number of Suite rooms available
ecRoomAvailable = 30       # Number of Economy rooms available

########################################            MANAGAING WINDOWS OF THE APP             #############################################################
class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign In ")
        self.setWindowIcon(QIcon("logo.jpg")) 
        self.setStyleSheet("background-color: #1d7ccf; font-family: 'Trebuchet MS'; color: #f7fbff; font-size: 16px;")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        central_widget.setStyleSheet("""
        QWidget {
            background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 #1d7ccf, stop:1 #f5ed00
            );
        }
        """)
        layout = QVBoxLayout()

        self.label = QLabel("hello welcome to \r\n          \r\n ROCK CREEK HOTELS", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Trebuchet MS", 24, QFont.Bold))
        self.label.setStyleSheet("background-color: none; font-family: 'Arial'; color: #f7fbff; font-size: 35px;")
        self.label.setGeometry(50, 50, 500, 300)  # Adjusted size for better visibility
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)

      
        
        self.label.show()  # Show the label
        self.button = QPushButton("SIGN IN", self)
        self.button.setGeometry(200, 400, 250, 10)  
        self.button.setStyleSheet("""
                                  background-color: #03fc4e;
                                   color: #ebebeb; 
                                  font-weight: bold;
                                  border: 2px solid #000000;
                                  font-size: 20px;
                                  """)
        self.button.clicked.connect(self.signIN)
        self.button.show()

        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.setAlignment(Qt.AlignCenter)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def signIN(self):
        signin_input = QInputDialog.getText(self, "Sign In", "Enter your username:")
        if signin_input[1]:
            username = signin_input[0]
            self.label.setText(f"Welcome, {username}!") 
        psw_input = QInputDialog.getText(self, "Sign In", "Enter your password:", QLineEdit.Password)
        if psw_input[1]:
            password = psw_input[0]
            if password == "abc":
                QMessageBox.information(self, "Success", f"Welcome, {username}!")
                print(f"Username: {username} has successfully signed in.")
                self.main_window = mainWindow()
                self.main_window.show()
                self.close()
                #here rite scripts  
            else:
                QMessageBox.warning(self, "Error", "Incorrect password. Please try again.")
                self.label.setText(f"umm... {username} \r\n Incorrect password. Please try again.")  
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROCKhotels - Hotel Management System")
        self.setGeometry(100, 100, 900, 900)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.initUI()
        self.setWindowIcon(QIcon("logo.jpg"))

    def initUI(self):
        central_widget = QWidget()
        central_widget.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 #1d7ccf, stop:1 #f5ed00
            );
            }
        """)
        self.setCentralWidget(central_widget)
        topLabel = QLabel(" (c) ROCK CREEK HOTELS pvt limited      centre: madipakkam       location: chennai       phone: xxxxxxxxx", self)
        topLabel.setStyleSheet("""
                               background-color: #40d6ed;
                        color: #333333;
                               font-family: 'Trebuchet MS';
                               font-size: 15px;""")
        topLabel.setAlignment(Qt.AlignCenter)
        topLabel.setGeometry(0, 0, 1370, 30)
        topLabel.show()
        labelI =  QLabel(self)
        labelI.setPixmap(QPixmap("logo.jpg").scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        labelI.setGeometry(50, 50, 200, 200)
        labelI.show()
        label = QLabel("ROCK CREEK HOTELS \r\n   \r\n WHAT WOULD YOU LIKE TO DO TODAY?", self) 
        label.setStyleSheet("""
                            color: #333333;
                            font-family: 'Trebuchet MS';
                            font-size: 35px;
                            font-weight: bold;
                            background-color: none;
                            """)
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(400, 100, 650, 150)
        label.show()
        deluxeLabelButton = QPushButton(f"Deluxe Room {len(liveDeluxeList2)}", self) #remember to change this to the actual number of rooms available
        deluxeLabelButton.setStyleSheet("""
                                  color: #000000;
                                 font-family: 'Trebuchet MS';
                                 font-size: 25px;
                                    font-weight: bold;
                                  background-color: #005af5;
                                  border: 2px solid #000000;
                                  """)

        deluxeLabelButton.setGeometry(100, 300, 450, 100)
        deluxeLabelButton.show()
        deluxeLabelButton.clicked.connect(self.deluxeRoom)
        suiteLabelButton = QPushButton(f"Suite Room {len(liveSuiteList2)}", self) #remember to change this to the actual number of rooms available
        suiteLabelButton.setStyleSheet("""
                                  color: #000000;
                                 font-family: 'Trebuchet MS';
                                 font-size: 25px;
                                    font-weight: bold;
                                  background-color: #00f535;
                                  border: 2px solid #000000;
                                  """)

        suiteLabelButton.setGeometry(100, 410, 450, 100)
        suiteLabelButton.show()
        suiteLabelButton.clicked.connect(self.suiteRoom)
        ecoLabelButton = QPushButton(f"economy Room {len(liveEconomyList2)}", self) #remember to change this to the actual number of rooms available
        ecoLabelButton.setStyleSheet("""
                                  color: #000000; 
                                 font-family: 'Trebuchet MS';
                                 font-size: 25px;
                                font-weight: bold;
                                  background-color: #f50039;
                                  border: 2px solid #000000;
                                  """)

        ecoLabelButton.setGeometry(100, 515, 450, 100)
        ecoLabelButton.show()
        ecoLabelButton.clicked.connect(self.ecoRoom)
        buttonC = QPushButton("Cancel booking", self)
        buttonC.setGeometry(50, 650, 300, 50)  
        buttonC.setStyleSheet("background-color: #f0ec00; color: #000000; font-weight: bold;")
        buttonC.clicked.connect(self.cancelBooking)  # Connect button click to a function
        buttonC.show()
        buttonR = QPushButton("Reserve booking", self)
        buttonR.setGeometry(350, 650, 300, 50)  
        buttonR.setStyleSheet("background-color: #f0ec00; color: #000000; font-weight: bold;")
        buttonR.clicked.connect(self.resererveRoom)  # Connect button click to a function
        buttonR.show()
        buttonV = QPushButton("View bookings", self)
        buttonV.setGeometry(650, 650, 300, 50)  
        buttonV.setStyleSheet("background-color: #f0ec00; color: #000000; font-weight: bold;")
        buttonV.clicked.connect(self.viewBookings)  # Connect button click to a function
        buttonV.show()
        buttonS = QPushButton("Modify bookings", self)
        buttonS.setGeometry(950, 650, 300, 50)  
        buttonS.setStyleSheet("background-color: #f0ec00; color: #000000; font-weight: bold;")
        buttonS.clicked.connect(self.modifyBookings)  # Connect button click to a function
        buttonS.show()
        buttonA = QPushButton("CHECK OUT", self)
        buttonA.setGeometry(850, 550, 400, 75)  
        buttonA.setStyleSheet("background-color: #f55a00; color: #000000; font-weight: bold; font-size: 20px; border: 2px solid #000000;")
        buttonA.clicked.connect(self.checkOut)  # Connect button click to a function
        buttonA.show()
        labelI2 =  QLabel(self)
        labelI2.setPixmap(QPixmap("Dubai.jpg").scaled(800, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        labelI2.setGeometry(850, 150, 100, 100)
        labelI2.setStyleSheet("background-color: none;")
        labelI2.show()
    def suiteRoom(self):
        self.booking_window = bookingWindow("Suite")
        self.booking_window.show()
    def deluxeRoom(self):
        self.booking_window = bookingWindow("Deluxe")
        self.booking_window.show()
    def ecoRoom(self):
        self.booking_window = bookingWindow("Economy")
        self.booking_window.show()
    def cancelBooking(self):
        self.cancel_booking_window = cancelBookingWindow()
        self.cancel_booking_window.show()
    def checkOut(self):
        booking_id, ok = QInputDialog.getText(self, "Check Out", "Enter Booking ID/ROOM NUMBER:")
    
        if ok and booking_id:
            # Here you would implement the logic to check out the room
            if len(booking_id) == 0:
                QMessageBox.warning(self, "Error", "Please enter a valid Booking ID/ROOM NUMBER.")
                return
            if not booking_id.isdigit():
                QMessageBox.warning(self, "Error", "Booking ID/ROOM NUMBER must be a number.")
                return
            booking_id = int(booking_id)
            if len(booking_id) == 4:
                try:
                    check_out_booking_byId(booking_id)  # Assuming booking_id is the room number
                    QMessageBox.information(self, "Success", f"Checked out successfully for Booking ID: {booking_id} \n at current time {QTime.currentTime().toString('HH:mm')} \n at current date {QDate.currentDate().toString('dd/MM/yyyy')}")
                    print(f"Checked out successfully for Booking ID: {booking_id} at current time {QTime.currentTime().toString('HH:mm')}")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"An error occurred while checking out: {str(e)}")
                    print(f"An error occurred while checking out: {str(e)}")
                finally:
                    print("Check out process completed.")
            elif len(booking_id) == 2:
                try:
                    check_out_booking_byRoomNo(booking_id)  # Assuming booking_id is the room number
                    QMessageBox.information(self, "Success", f"Checked out successfully for Room Number: {booking_id} \n at current time {QTime.currentTime().toString('HH:mm')} \n at current date {QDate.currentDate().toString('dd/MM/yyyy')}")
                    print(f"Checked out successfully for Room Number: {booking_id} at current time {QTime.currentTime().toString('HH:mm')}")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"An error occurred while checking out: {str(e)}")
                    print(f"An error occurred while checking out: {str(e)}")
                finally:
                    print("Check out process completed.")
            else:
                QMessageBox.warning(self, "Error", "Booking ID/ROOM NUMBER must be 2 or 4 digits long.")
                print("Booking ID/ROOM NUMBER must be 2 or 4 digits long.")
    def resererveRoom(self):
        self.resererveRoom = BookReservationWindow()
        self.resererveRoom.show()
    def viewBookings(self):
        self.viewBook = ViewBookingsWindow()
        self.viewBook.show()
    def modifyBookings(self):
        self.modify_window = ModifyBookingWindow()
        self.modify_window.show()
    def roomService(self):
        pass    # # Here you would implement the functionality for room service management
class bookingWindow(QMainWindow):
    def __init__(self, type):
        super().__init__()

        self.type = type
        self.setWindowIcon(QIcon("logo.jpg"))
        self.setWindowTitle("Booking Window")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("logo.jpg"))
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 #1d7ccf, stop:1 #f5ed00
            );
            }
        """)

        main_layout = QVBoxLayout(self.central_widget)

        #set layout for the booking window
        self.booking_central_widget = QWidget()
        self.layout = QVBoxLayout(self.booking_central_widget)
        #self.setLayout(layout)
        # Create a scroll area to hold the booking form
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.booking_central_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setGeometry(850, 500, 1300, 1000)
        scroll_area.setStyleSheet("background-color: none;")
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        main_layout.addWidget(scroll_area)
        self.setCentralWidget(self.central_widget)
        #self.setLayout(layout)
        self.setGeometry(100, 100, 800, 800)
       # self.setStyleSheet("background-color: none; font-family: 'Trebuchet MS'; color: #000000; font-size: 16px;")
        self.initUI()

    def initUI(self):
        #set a scroll area for the booking window
        opactity_effect = QGraphicsOpacityEffect()
        opactity_effect.setOpacity(0.5)


        # Initialize the UI components for booking
        
        #layout2 = QVBoxLayout(self.central_widget)
        #self.central_widget.setLayout(layout2)
        #label = QLabel(f"ROCK CREEK HOTELS \r\n {self.type} Booking kiosk form ", self) 
        #label.setStyleSheet("""
      #                      color: #333333;
       #                     font-family: 'Trebuchet MS';
        #                    font-size: 35px;
       #                     font-weight: bold;
       #                     background-color: none;
       #                     opacity: 0.5;
       #                     """)
       # label.setAlignment(Qt.AlignCenter)
       # label.setGeometry(400, 100, 650, 150)
       # label.show()
        topLabel = QLabel(" (c) ROCK CREEK HOTELS pvt limited      centre: madipakkam       location: chennai       phone: xxxxxxxxx", self)
        topLabel.setStyleSheet("""
                               background-color: #40d6ed;
                        color: #333333;
                               font-family: 'Trebuchet MS';
                               font-size: 15px;""")
        topLabel.setAlignment(Qt.AlignCenter)
        topLabel.setGeometry(0, 0, 1370, 30)
        topLabel.show()
        labelI =  QLabel(self)
        labelI.setPixmap(QPixmap("logo.jpg").scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        labelI.setGeometry(50, 600, 200, 200)
        labelI.setStyleSheet("background-color: none;")
        labelI.setGraphicsEffect(opactity_effect)  # Apply opacity effect
        labelI.show()
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter your name")
        self.name_input.setStyleSheet("font-size: 20px; padding: 10px;")
        self.name_input.setGeometry(50, 200, 700, 50)
        self.name_input.show()
        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Enter your phone number")
        self.phone_input.setStyleSheet("font-size: 20px; padding: 10px;")
        self.phone_input.setGeometry(50, 300, 700, 50)
        self.phone_input.show()
        self.aadhar_input = QLineEdit(self)
        self.aadhar_input.setPlaceholderText("Enter your Aadhar number")
        self.aadhar_input.setStyleSheet("font-size: 20px; padding: 10px;")
        self.aadhar_input.setGeometry(50, 400, 700, 50)
        self.aadhar_input.show()
        self.checkin_time_input = QTimeEdit(self)
        #self.checkin_time_input.setPlaceholderText("Select checkin time")
        self.checkin_time_input.setMinimumTime(QTime(0, 0))
        self.checkin_time_input.setDisplayFormat("HH:mm")
        self.checkin_time_input.setStyleSheet("font-size: 20px; padding: 10px;")
        self.checkin_time_input.setGeometry(50, 500, 700, 50)
        self.checkin_time_input.setTime(QTime.currentTime())
        self.checkin_time_input.show()
        self.checkin_input = QDateEdit(self)
        #self.checkin_input.setPlaceholderText("Select checkin date")
        self.checkin_input.setMinimumDate(QDate.currentDate())
        self.checkin_input.setDisplayFormat("dd/MM/yyyy")
        self.checkin_input.setCalendarPopup(True)
        self.checkin_input.setStyleSheet("font-size: 20px; padding: 10px;")
        self.checkin_input.setGeometry(150, 600, 700, 50)
        self.checkin_input.setDate(QDate.currentDate())
        self.checkin_input.show()
        self.checkout_input = QDateEdit(self)
        #self.checkout_input.setPlaceholderText("Select checkout date")
        self.checkout_input.setMinimumDate(QDate.currentDate().addDays(1))
        self.checkout_input.setDisplayFormat("dd/MM/yyyy")
        self.checkout_input.setCalendarPopup(True)
        self.checkout_input.setStyleSheet("font-size: 20px; padding: 10px;")
        self.checkout_input.setGeometry(50, 700, 700, 50)
        self.checkout_input.setDate(QDate.currentDate().addDays(5))
        self.checkout_input.show()
        self.no_of_guests_input = QSpinBox(self)
        #self.no_of_guests_input.setPlaceholderText("Select number of guests")
        self.no_of_guests_input.setSuffix(" guests")
        self.no_of_guests_input.setSingleStep(1)
        self.no_of_guests_input.setRange(1, 10)
        self.no_of_guests_input.setValue(1)
        self.no_of_guests_input.setStyleSheet("font-size: 20px; padding: 10px;")
        self.no_of_guests_input.setGeometry(50, 800, 700, 50)
        self.no_of_guests_input.show()
        self.book_button = QPushButton(f" {self.type} Rooms Book Now", self)
        self.book_button.setStyleSheet("""
            background-color: #034fce;
                        color: #ffffff;
            font-weight: bold;
             font-size: 20px;
           padding: 10px;
             border-radius: 5px;
             border: 2px solid #000000;   
                                       """)
        
        self.book_button.setGeometry(50, 900, 700, 50)
        self.book_button.clicked.connect(self.bookRoom)
        self.book_button.show()
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.phone_input)
        self.layout.addWidget(self.aadhar_input)
        self.layout.addWidget(self.checkin_time_input)
        self.layout.addWidget(self.checkin_input)
        self.layout.addWidget(self.checkout_input)
        self.layout.addWidget(self.no_of_guests_input)
        self.layout.addWidget(self.book_button)



    def bookRoom(self):
        global deluxeRoomAvailable, suiteRoomAvailable, ecRoomAvailable
        global economyRoomList, deluxeRoomList, suiteRoomList
        #obtain random booking id:
        booking_id = random.randint(1000, 9999)
        room_type = self.type
        name = self.name_input.text()
        phone = self.phone_input.text()
        aadhar = self.aadhar_input.text()
        checkin_time = self.checkin_time_input.time().toString("HH:mm")
        checkin_date = self.checkin_input.date().toString("dd/MM/yyyy")
        checkout_date = self.checkout_input.date().toString("dd/MM/yyyy")
        no_of_guests = self.no_of_guests_input.value()
        price = 100 # Set a default price, you can modify this based on room type
        if self.type == "Economy":
            if ecRoomAvailable > 0:
                room_number = economyRoomList.pop(0)
                ecRoomAvailable -= 1
                price = economy_room["price"]
            else:
                QMessageBox.warning(self, "Error", "No Economy rooms available.")
                return
        elif self.type == "Deluxe":
            if deluxeRoomAvailable > 0:
                room_number = deluxeRoomList.pop(0)
                deluxeRoomAvailable -= 1
                price = deluxe_room["price"]
            else:
                QMessageBox.warning(self, "Error", "No Deluxe rooms available.")
                return
        elif self.type == "Suite":
            if suiteRoomAvailable > 0:
                room_number = suiteRoomList.pop(0)
                suiteRoomAvailable -= 1
                price = suite_room["price"]
            else:
                QMessageBox.warning(self, "Error", "No Suite rooms available.")
                return
        else:
            QMessageBox.warning(self, "Error", "Invalid room type selected.")
            self.close()  # Close the booking window if room type is invalid    
            return

         #implement here use "type" variable to determine the type of room booked
        total_amount = price * no_of_guests  # Calculate total amount based on room type and number of guests
        try:
            add_booking(booking_id, room_type, room_number, name, phone, aadhar, checkin_time, checkin_date, checkout_date, no_of_guests, total_amount)
            QMessageBox.information(self, "Success", f"Booking successful!\nBooking ID: {booking_id}\nRoom Type: {room_type}\nRoom Number: {room_number}\nTotal Amount: ₹{total_amount}")
            print(f"Booking successful!\nBooking ID: {booking_id}\nRoom Type: {room_type}\nRoom Number: {room_number}\nTotal Amount: ₹{total_amount}")
            self.close()  # Close the booking window after successful booking
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while booking the room: {str(e)}")
            print(f"An error occurred while booking the room: {str(e)}")
class ModifyBookingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modify Booking")
        self.setGeometry(100, 100, 800, 400)
        self.setWindowIcon(QIcon("logo.jpg"))
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1d7ccf, stop:1 #f5ed00
                );
            }
        """)
        self.setCentralWidget(self.central_widget)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self.central_widget)

        topLabel = QLabel("Modify Booking Details", self)
        topLabel.setStyleSheet("""
            color: #333333;
            font-family: 'Trebuchet MS';
            font-size: 28px;
            font-weight: bold;
            background-color: none;
        """)
        topLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(topLabel)

        self.booking_id_input = QLineEdit(self)
        self.booking_id_input.setPlaceholderText("Enter Booking ID")
        self.booking_id_input.setStyleSheet("font-size: 20px; padding: 10px;background-color: #ffffff;color: #000000;")
        layout.addWidget(self.booking_id_input)

        self.field_combo = QComboBox(self)
        self.field_combo.setStyleSheet("font-size: 20px; padding: 10px; background-color: #ffffff;color: #000000;")
        # Add fields you allow to edit
        self.field_combo.addItems([
            "name", "phone", "aadhar", "checkin_time", "checkin_date",
            "checkout_date", "no_of_guests", "room_number"
        ])
        layout.addWidget(self.field_combo)

        self.new_value_input = QLineEdit(self)
        self.new_value_input.setPlaceholderText("Enter new value")
        self.new_value_input.setStyleSheet("font-size: 20px; padding: 10px; background-color: #ffffff;color: #000000;")
        layout.addWidget(self.new_value_input)

        self.done_button = QPushButton("Done", self)
        self.done_button.setStyleSheet("""
            background-color: #034fce;
            color: #ffffff;
            font-weight: bold;
            font-size: 22px;
            padding: 10px;
            border-radius: 5px;
            border: 2px solid #000000;
        """)
        self.done_button.setFixedWidth(200)
        self.done_button.clicked.connect(self.modifyBooking)
        # Center the button
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.done_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)

    def modifyBooking(self):
        booking_id = self.booking_id_input.text().strip()
        field = self.field_combo.currentText()
        new_value = self.new_value_input.text().strip()
        if not booking_id or not new_value:
            QMessageBox.warning(self, "Error", "Please fill all fields.")
            return
        try:
            modifySomethingById(int(booking_id), field, new_value)
            QMessageBox.information(self, "Success", f"{field} updated for Booking ID {booking_id}.")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to modify booking: {str(e)}")
class cancelBookingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cancel Booking")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("logo.jpg"))
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        central_widget.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 #1d7ccf, stop:1 #f5ed00
            );
            }
        """)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        label = QLabel("Cancel Booking", self)

        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Trebuchet MS", 24, QFont.Bold))
        label.setStyleSheet("color: #333333; font-size: 35px;")
        label.setGeometry(50, 50, 700, 100)  # Adjusted size for better visibility
        label.setWordWrap(True)
        layout.addWidget(label)

        # Add form elements for canceling a booking here
        self.booking_id_input = QLineEdit(self)
        self.booking_id_input.setPlaceholderText("Enter Booking ID/ROOM NUMBER")
        self.booking_id_input.setStyleSheet("background: #ffffff;color: #000000;font-size: 20px; padding: 10px;")
        self.booking_id_input.setGeometry(50, 200, 700, 50)
        layout.addWidget(self.booking_id_input)
        self.booking_id_input.show()
        self.roomtype_input = QLineEdit(self)
        self.roomtype_input.setPlaceholderText("Enter room type (e.g., Deluxe, Suite, Economy)")
        self.roomtype_input.setStyleSheet("background: #ffffff;color: #000000;font-size: 20px; padding: 10px;")
        self.roomtype_input.setGeometry(50, 300, 700, 50)
        layout.addWidget(self.roomtype_input)
        self.roomtype_input.show()
        self.cancel_button = QPushButton("Cancel Booking", self)
        self.cancel_button.setGeometry(50, 400, 700, 50)
        self.cancel_button.setStyleSheet("""
            background-color: #f55a00; 
            color: #ffffff;
            font-weight: bold;
            font-size: 20px;
            padding: 10px;
            border-radius: 5px;
            border: 2px solid #000000;                            
                                         """)
        self.cancel_button.clicked.connect(self.cancelBooking)
        self.cancel_button.show()
        layout.addWidget(self.cancel_button)
        self.setLayout(layout)
        self.setGeometry(100, 100, 500, 300)
                                         

    def cancelBooking(self):
        booking_id = self.booking_id_input.text()
        if booking_id:
            cancel_reservation_byId(booking_id)
            # Here you would implement the logic to cancel the booking
            QMessageBox.information(self, "Success", f"Reservation with ID {booking_id} has been canceled.")
            print(f"Booking with ID {booking_id} has been canceled.")
            #run a script to remove the booking from the database
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Please enter a valid Booking ID/ROOM NUMBER.") 
class BookReservationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Book Reservation")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("logo.jpg"))
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1d7ccf, stop:1 #f5ed00
                );
            }
        """)
        self.setCentralWidget(self.central_widget)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self.central_widget)

        topLabel = QLabel("Book Reservation", self)
        topLabel.setStyleSheet("""
            color: #333333;
            font-family: 'Trebuchet MS';
            font-size: 28px;
            font-weight: bold;
            background-color: #40d6ed;
        """)
        topLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(topLabel)

        self.id_input = QLineEdit(self)
        self.id_input.setPlaceholderText("Enter Reservation ID")
        self.id_input.setStyleSheet("font-size: 20px; padding: 10px; background-color: #ffffff; color: #000000;")
        layout.addWidget(self.id_input)

        self.room_type_combo = QComboBox(self)
        self.room_type_combo.setStyleSheet("font-size: 20px; padding: 10px; background-color: #ffffff; color: #000000;")
        self.room_type_combo.addItems(["Economy", "Deluxe", "Suite"])
        layout.addWidget(self.room_type_combo)

        self.room_number_input = QLineEdit(self)
        self.room_number_input.setPlaceholderText("Enter Room Number")
        self.room_number_input.setStyleSheet("font-size: 20px; padding: 10px; background-color: #ffffff; color: #000000;")
        layout.addWidget(self.room_number_input)

        self.customer_name_input = QLineEdit(self)
        self.customer_name_input.setPlaceholderText("Enter Customer Name")
        self.customer_name_input.setStyleSheet("font-size: 20px; padding: 10px; background-color: #ffffff; color: #000000;")
        layout.addWidget(self.customer_name_input)

        self.phone_no_input = QLineEdit(self)
        self.phone_no_input.setPlaceholderText("Enter Phone Number")
        self.phone_no_input.setStyleSheet("font-size: 20px; padding: 10px; background-color: #ffffff; color: #000000;")
        layout.addWidget(self.phone_no_input)

        self.aadhar_no_input = QLineEdit(self)
        self.aadhar_no_input.setPlaceholderText("Enter Aadhar Number")
        self.aadhar_no_input.setStyleSheet("font-size: 20px; padding: 10px; background-color: #ffffff; color: #000000;")
        layout.addWidget(self.aadhar_no_input)

        self.check_in_time_input = QTimeEdit(self)
        self.check_in_time_input.setMinimumTime(QTime(0, 0))
        self.check_in_time_input.setDisplayFormat("HH:mm")
        self.check_in_time_input.setStyleSheet("font-size: 20px; padding: 10px; background-color: #ffffff; color: #000000;")
        self.check_in_time_input.setTime(QTime.currentTime())
        layout.addWidget(self.check_in_time_input)

        self.check_in_date_input = QDateEdit(self)
        self.check_in_date_input.setMinimumDate(QDate.currentDate())
        self.check_in_date_input.setDisplayFormat("dd/MM/yyyy")
        self.check_in_date_input.setCalendarPopup(True)
        self.check_in_date_input.setStyleSheet("font-size: 20px; padding: 10px; background-color: #ffffff; color: #000000;")
        self.check_in_date_input.setDate(QDate.currentDate())
        layout.addWidget(self.check_in_date_input)

        self.book_button = QPushButton("Book Reservation", self)
        self.book_button.setStyleSheet("""
            background-color: #034fce;
            color: #ffffff;
            font-weight: bold;
            font-size: 22px;
            padding: 10px;
            border-radius: 5px;
            border: 2px solid #000000;
        """)
        self.book_button.setFixedWidth(250)
        self.book_button.clicked.connect(self.bookReservation)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.book_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)

    def bookReservation(self):
        try:
            id_val = int(self.id_input.text().strip())
            room_type = self.room_type_combo.currentText()
            room_number = int(self.room_number_input.text().strip())
            customer_name = self.customer_name_input.text().strip()
            phone_no = self.phone_no_input.text().strip()
            aadhar_no = self.aadhar_no_input.text().strip()
            check_in_time = self.check_in_time_input.time().toString("HH:mm")
            check_in_date = self.check_in_date_input.date().toString("dd/MM/yyyy")

            if not all([id_val, room_type, room_number, customer_name, phone_no, aadhar_no, check_in_time, check_in_date]):
                QMessageBox.warning(self, "Error", "Please fill all fields.")
                return

            add_reservation(id_val, room_type, room_number, customer_name, phone_no, aadhar_no, check_in_time, check_in_date)
            QMessageBox.information(self, "Success", f"Reservation booked!\nID: {id_val}\nRoom: {room_type} {room_number}\nCustomer: {customer_name}")
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to book reservation: {str(e)}")
class ViewBookingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("View Bookings")
        self.setGeometry(100, 100, 1200, 600)
        self.setWindowIcon(QIcon("logo.jpg"))
        self.central_widget = QWidget()
        self.central_widget.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1d7ccf, stop:1 #f5ed00
                );
            }
        """)
        self.setCentralWidget(self.central_widget)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self.central_widget)

        topLabel = QLabel("All Bookings / Reservations", self)
        topLabel.setStyleSheet("""
            color: #333333;
            font-family: 'Trebuchet MS';
            font-size: 28px;
            font-weight: bold;
            background-color: #40d6ed;
        """)
        topLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(topLabel)

        # Table setup
        self.table = QTableWidget(self)
        self.table.setStyleSheet("""
            QTableWidget {
                font-size: 18px;
                background-color: #ffffff;
                color: #000000;
                border: 2px solid #000000;
            }
            QHeaderView::section {
                background-color: #034fce;
                color: #ffffff;
                font-weight: bold;
                font-size: 20px;
            }
        """)
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "ID", "Room Type", "Room No", "Name", "Phone", "Aadhar", "Check-in Time", "Check-in Date"
        ])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.loadBookings()
        layout.addWidget(self.table)

    def loadBookings(self):
        # Use your view_bookings() function to get all bookings
        try:
            bookings = view_all()  # Should return a list of tuples/lists
            self.table.setRowCount(len(bookings))
            for row_idx, booking in enumerate(bookings):
                for col_idx, value in enumerate(booking[:8]):  # Only first 8 fields
                    item = QTableWidgetItem(str(value))
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    self.table.setItem(row_idx, col_idx, item)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not load bookings: {str(e)}")

# To open this window, add to your mainWindow:

###########################################         CALLING START                       #################################################
def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Set the application style
    window = WelcomeWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()          ###     WILL WORK ONLY IF THIS FILE IS RUN AS THE NATIVE MAIN FILE..............