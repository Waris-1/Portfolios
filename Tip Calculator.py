print("Welcome to the tip calculator")
bill = float(input("What was your total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people should split the bill? "))

tip_total = tip / 100
tipamount = bill * tip_total
total_bill = bill + tipamount
per_person = total_bill / people
final = round(per_person, 2)



print(f"Each person should pay: ${final}")

