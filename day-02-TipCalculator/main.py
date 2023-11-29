print("Welcome to the tip calculator.")
total_amount = float(input("What was the total bill? $"))
tip_rate = int(input("What percentage tip would you like to give? 10,12 or 15? "))
people = int(input("How many people to split the bill? "))
final_amount = total_amount * (100 + tip_rate) / 100
individual_amount = round(final_amount / people, 2)
print(f"Each person should pay: ${individual_amount:.2f}")
