import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
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
        deluxeLabelButton = QPushButton(f"Deluxe Room {14}", self) #remember to change this to the actual number of rooms available
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
        suiteLabelButton = QPushButton(f"Suite Room {14}", self) #remember to change this to the actual number of rooms available
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
        ecoLabelButton = QPushButton(f"econome Room {14}", self) #remember to change this to the actual number of rooms available
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
        buttonR.clicked.connect(self.cancelBooking)  # Connect button click to a function
        buttonR.show()
        buttonV = QPushButton("View bookings", self)
        buttonV.setGeometry(650, 650, 300, 50)  
        buttonV.setStyleSheet("background-color: #f0ec00; color: #000000; font-weight: bold;")
        buttonV.clicked.connect(self.cancelBooking)  # Connect button click to a function
        buttonV.show()
        buttonS = QPushButton("Modify bookings", self)
        buttonS.setGeometry(950, 650, 300, 50)  
        buttonS.setStyleSheet("background-color: #f0ec00; color: #000000; font-weight: bold;")
        buttonS.clicked.connect(self.cancelBooking)  # Connect button click to a function
        buttonS.show()
        buttonA = QPushButton("ROOM SERVICEs", self)
        buttonA.setGeometry(850, 550, 400, 75)  
        buttonA.setStyleSheet("background-color: #f55a00; color: #000000; font-weight: bold; font-size: 20px; border: 2px solid #000000;")
        buttonA.clicked.connect(self.cancelBooking)  # Connect button click to a function
        buttonA.show()
        labelI2 =  QLabel(self)
        labelI2.setPixmap(QPixmap("Dubai.jpg").scaled(800, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        labelI2.setGeometry(850, 150, 800, 500)
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
    def resererveRoom(self):
        pass    # # Here  you would implement the functionality for reserving a room
    def viewBookings(self):
        pass    # # Here you would implement the functionality for viewing bookings
    def modifyBookings(self):
        pass    # # Here you would implement the functionality for modifying bookings
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
        pass #implement here use "type" variable to determine the type of room booked
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
            # Here you would implement the logic to cancel the booking
            QMessageBox.information(self, "Success", f"Booking with ID {booking_id} has been canceled.")
            print(f"Booking with ID {booking_id} has been canceled.")
            #run a script to remove the booking from the database
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Please enter a valid Booking ID/ROOM NUMBER.") 



def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Set the application style
    window = WelcomeWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
