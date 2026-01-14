#restaurant.py restaurant managemnent system
import sys
import os
import sqlite3
import datetime
import time

# List to store orders
listOfOrders = []
dosa = {
    "name": "Dosa",
    "price": 50,
    "type": "veg",
    "description": "A crispy South Indian dish made from fermented rice and lentil batter, served with chutney and sambar.",
    "cooking_time": "10 minutes"
}
idli = {
    "name": "Idli",
    "price": 30,
    "type": "veg",
    "description": "Soft and fluffy steamed rice cakes, typically served with chutney and sambar.",
    "cooking_time": "15 minutes",
}
vada = {
    "name": "Vada",
    "price": 40,
    "type": "veg",
    "description": "A savory doughnut-shaped snack made from lentils, deep-fried to a golden brown.",
    "cooking_time": "8 minutes",
}
samosa = {
    "name": "Samosa",
    "price": 20,
    "type": "veg",
    "description": "A crispy pastry filled with spiced potatoes and peas, deep-fried to perfection.",
    "cooking_time": "12 minutes",
}
listOfItems = []
class item:
    def __init__(self, food):
        self.name = food["name"]
        self.price = food["price"]
        self.type = food["type"]
        self.description = food["description"]
        self.cooking_time = food["cooking_time"]
    def __str__(self):
        return f"{self.name} - {self.price} - {self.type} - {self.description}"
def main():
    global listOfItems
    listOfItems.append(item(dosa))
    listOfItems.append(item(idli))
    listOfItems.append(item(vada))
    listOfItems.append(item(samosa))
    print("Welcome to the Restaurant Management System")
    print("Available items:")
    t = 0
    for i in listOfItems:
        print(f"{t+1}. {i}")
        t += 1
    print("To place an order, type 'order' followed by the item name.")
    print("To exit, type 'exit'.")
    
    while True:
        command = input("Enter command: ").strip().lower()
        if command == "exit":
            print("Thank you for using the Restaurant Management System!")
            break
        elif command == "view orders":
            view_orders()
        elif command.startswith("order "):
            item_name = command[6:].strip()
            no_order = int(input("How many orders do you want to place? "))
            if no_order <= 0:
                print("Invalid number of orders. Please try again.")
                continue
            found = False
            for i in listOfItems:
                if i.name.lower() == item_name.lower():
                    for _ in range(no_order):
                        print(f"Placing order for {i.name}...")
                        time.sleep(1)
                        listOfOrders.append(i)
                    print(f"Order placed for {i.name}.")
                    found = True
                    break
            if not found:
                print(f"Item '{item_name}' not found. Please try again.")
        else:
            print("Invalid command. Please try again.")
main()
def view_orders():
    if not listOfOrders:
        print("No orders placed yet.")
        return
    print("Current orders:")
    for order in listOfOrders:
        print(order)
    print(f"Total number of orders: {len(listOfOrders)}")