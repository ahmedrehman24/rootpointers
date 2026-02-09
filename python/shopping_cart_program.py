cart = []
total = 0

while True:
    item = input("Enter item (q to quit): ")
    if item == "q":
        break
    price = float(input("Enter price: "))
    cart.append(item)
    total += price

print("Items:", cart)
print("Total:", total)
