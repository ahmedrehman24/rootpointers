weight = float(input("Enter weight: "))
unit = input("Convert to (kg/lb): ").lower()

if unit == "kg":
    print(f"{weight / 2.205:.2f} kg")
elif unit == "lb":
    print(f"{weight * 2.205:.2f} lb")
else:
    print("Invalid unit")
