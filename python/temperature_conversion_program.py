temp = float(input("Temperature: "))
unit = input("Convert to (c/f): ").lower()

if unit == "c":
    result = (temp - 32) * 5/9
elif unit == "f":
    result = (temp * 9/5) + 32
else:
    result = None

if result is not None:
    print(f"{result:.2f}")
