weight = float(input("Enter weight: "))
unit = input("Kilograms or Pounds (k/p): ")

if unit == "k":
    print(weight * 2.205, "lbs")
elif unit == "p":
    print(weight / 2.205, "kg")
