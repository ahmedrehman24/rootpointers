p = float(input("Principal: "))
r = float(input("Rate (%): ")) / 100
t = int(input("Years: "))

amount = p * (1 + r) ** t
print(f"Final Amount: {amount:.2f}")
