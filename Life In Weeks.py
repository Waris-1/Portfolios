# Calculates how long you have left untill you hit 90 years old
age = input("What is your current age? ")
agenum=int(age)

years_limit = 90-agenum
days = years_limit*365
weeks = years_limit*52
months = years_limit*12





print(f"You have {days} days, {weeks} weeks, and {months} months left.")

