temp = float(input("Enter temperature: "))
unit = input("Celsius or Fahrenheit (c/f): ")

if unit == "c":
    print((temp * 9/5) + 32)
elif unit == "f":
    print((temp - 32) * 5/9)
