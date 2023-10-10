print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lower_names = combined_names.lower()
f = lower_names.count ("f")
i = lower_names.count ("i")
r = lower_names.count ("r")
s = lower_names.count ("s")
first_digit = f + i + r + s

l = lower_names.count ("l")
o = lower_names.count ("o")
v = lower_names.count ("v")
e = lower_names.count ("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
