#hotel managemnt imports

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
ecRoomAvailable = 30        #while repeated ananlysis use len(economyRoomList) instead of this variable
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
# Room lists
economyRoomList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
deluxeRoomList = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
suiteRoomList = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
