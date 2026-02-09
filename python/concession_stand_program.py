menu = {"popcorn": 5, "soda": 3}

choice = input("What would you like? ")
if choice in menu:
    print("Price:", menu[choice])
