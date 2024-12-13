import random
while True:
    # Prompt the user for their choice
    user_choice = input("R, P, or S? ")
    user_choice = user_choice.upper()

    # Possible choices for the AI
    possible_choices = ["R", "P", "S"]

    # Randomly pick the AI's choice
    ai_choice = random.choice(possible_choices)

    # Output the AI's choice
    print(f"AI chose: {ai_choice}")

    # Determine the result based on the user's and AI's choices
    if user_choice == ai_choice:
        print("Draw")

    elif user_choice == "R" and ai_choice == "S":
        print("User wins by rock")

    elif user_choice == "S" and ai_choice == "P":
        print("User wins by scissors")

    elif user_choice == "P" and ai_choice == "R":
        print("User wins by paper")

    elif user_choice == "P" and ai_choice == "S":
        print("AI wins by scissors")

    elif user_choice == "S" and ai_choice == "R":
        print("AI wins by rock")

    elif user_choice == "R" and ai_choice == "P":
        print("AI wins by paper")
