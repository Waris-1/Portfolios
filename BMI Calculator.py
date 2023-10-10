height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

result = (weight / (height * height))
if result < 18.5:
    print("Your BMI is " + str(round(result)) + ", you are underweight.")
elif result < 25:
    print("Your BMI is " + str(round(result)) + ", you have a normal weight.")
elif result < 30:
    print("Your BMI is " + str(round(result)) + ", you are slightly overweight.")
elif result < 35:
    print("Your BMI is " + str(round(result))  + ", you are obese.")
else:
    print("Your BMI is " + str(round(result)) + " , you are clinically obese.")

