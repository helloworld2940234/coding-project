import random
user_choice = input ("R,P,or S? ")
possible_choices = ["R","P","S"]

ai_choice = random.choice(possible_choices)
if user_choice == "R" and ai_choice == "P":
    print ("ai wins by paper")
if user_choice == "P" and ai_choice == "R":
    print ("user wins by paper")
if user_choice == ai_choice:
    print ("Draw")