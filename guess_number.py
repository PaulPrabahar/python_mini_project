'''to learn about condition and generation of random numbers'''
import random

user_range = input("at what range of numbers u need to play? ")

if user_range.isdigit():
    user_range = int(user_range)

    random_number = random.randint(0, user_range)
    tries = 0
    while True:
        tries += 1
        user_guess = input("enter the number you guessed.")

        if  user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess == random_number:
                print("You guessed it right")
                break
            elif user_guess > random_number:
                print("the guessed number is greater")
            else:
                print("the guessed number is lower")
        else:
            print("enter a valid number to guess.")

    print(f"total tries {tries}")

else:
    print("enter a valid number.")