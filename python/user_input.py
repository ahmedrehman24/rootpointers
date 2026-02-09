while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number.")

name = input("Enter your name: ").strip().title()
print(f"Welcome {name}, age {age}")
