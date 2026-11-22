'''create a rock paper scissor game using list'''
import random

options = ["rock", "paper", "scissor"]
your_score = 0
computer_score = 0


while True:
    random_number = random.randint(0, 2)
    user_selection = input("enter your choice or q to exit: ")
    computer_choice = options[random_number]
    if user_selection == "q":
        break

    if user_selection not in options:
        print("kindly enter rock, paper or scissor:")
        continue

    if user_selection == computer_choice:
        print("you both select same so its draw.")
        continue

    if user_selection == "rock" and computer_choice == "scissor":
        your_score += 1
        print(f"computer choice is {computer_choice} you win")
    elif user_selection == "paper" and computer_choice == "rock":
        your_score += 1
        print(f"computer choice is {computer_choice} you win")
    elif user_selection == "scissor" and computer_choice == "paper":
        your_score += 1
        print(f"computer choice is {computer_choice} you win")
    else:
        computer_score += 1
        print(f"computer choice is {computer_choice} computer wins")

print(f"your score is {your_score}")
print(f"computer score is {computer_score}")
print("thanks for playing")

    
    