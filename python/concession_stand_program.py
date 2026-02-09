menu = {"popcorn": 5, "nachos": 6, "soda": 3}

choice = input("Choose item: ").lower()

if choice in menu:
    print(f"Price: ${menu[choice]}")
else:
    print("Item not available")
