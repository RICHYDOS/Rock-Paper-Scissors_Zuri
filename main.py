import random

options = ["R", "P", "S"]

while True:
    user_input = input("Input R for Rock P for Paper S for Scissors")

    if user_input.upper() not in options:
        print("Invalid Input")
        continue

    cpu = random.choice(options)
    print(f"Player {user_input.upper()} : CPU {cpu}")
    
    if user_input.upper() == cpu:
        print("It's a Tie")
        continue
    elif (user_input.upper() == "R") and (cpu == "S"):
        print("Player Wins")
        break
    elif (user_input.upper() == "P") and (cpu == "R"):
        print("Player Wins")
        break
    elif (user_input.upper() == "S") and (cpu == "P"):
        print("Player Wins")
        break
    else:
        print("CPU Wins")
        break
