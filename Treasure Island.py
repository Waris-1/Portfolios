print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

question1 = input("You're at a pathway. Where do you want to go? Type left or right: ")

if question1.lower() == "right":
    print("You got killed by a lion. Game over")
    exit()
elif question1.lower() == "left":
    question2 = input("You come across a river, do you want to take the boat or wait: ")
    
    if question2.lower() == "boat":
        print("You successfully made it across the river")
    elif question2.lower() == "wait":
        print("The crocodiles have caught up to you. Game over")
        exit()
    else:
        print("You must choose between 'boat' or 'wait'")
        exit()

    question3 = input("What weapon do you want to pick to fight the bear? gun, cue, sword: ")

    if question3.lower() == "gun":
        print("You have killed the bear and made it to the end of the forest. You win!")
    elif question3.lower() == "cue":
        print("Your snooker cue broke and the bear has killed you")
    elif question3.lower() == "sword":
        print("You were close to killing the bear but he killed you before you could")
    else:
        print("You must choose between 'gun', 'cue', or 'sword'")
else:
    print("You must choose between 'right' or 'left'")





