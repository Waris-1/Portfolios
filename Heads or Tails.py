import random

tails = 0
heads = 1

random_int = random.randint(tails, heads)

if random_int == tails:
    print("tails")
else:
    print("heads")



