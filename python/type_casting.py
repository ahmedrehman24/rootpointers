# Type Casting Example

user_input = input("Enter a number: ")

try:
    number = int(user_input)
    print("Integer:", number)
    print("Float:", float(number))
except ValueError:
    print("Invalid input! Please enter a valid number.")
