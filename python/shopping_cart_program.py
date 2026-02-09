cart = {}
total = 0

while True:
    item = input("Item (q to quit): ")
    if item == "q":
        break
    price = float(input("Price: "))
    cart[item] = price
    total += price

print("Cart:", cart)
print("Total:", total)
