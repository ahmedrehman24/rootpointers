age = int(input("Age: "))
has_id = input("Have ID? (y/n): ").lower() == "y"

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
