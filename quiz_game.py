'''this program to learn conditional and user prompts to create a quizee game.'''

to_start = input("shall we start! ")
answer = ""
score = 0
if to_start.lower() == "yes":
    answer = input("what usa stands for? ")
    if answer.lower() == "united states of america":
        print("correct.")
        score += 1
    else:
        print("incorrect")

    answer = input("what currency used in usa? ")   
    if answer.lower() == "doller":
        print("correct.")
        score += 1
    else:
        print("incorrect")  

    answer = input("where is the capital of usa? ")   
    if answer.lower() == "washington dc":
            print("correct.")
            score += 1
    else:
            print("incorrect")

    print(f"your score is {score}")
else:
    quit()
