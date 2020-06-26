import random
lst=['s','p','sc']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t Stone,Paper,Scissor Game\n \n")
print("s for stone\np for paper \nsc for scissor \n")
name=input('enter the yout name:')
while no_of_chance<chance:
    inp = input('enter the your choice:')
    ran= random.choice(lst)

    if inp == ran:
        print("Tie Both 0 point to each \n ")

    if inp=='s'and ran=='p':
        computer_point=computer_point+1;
        print(f"your guess {inp} and computer guess is {ran} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif inp=='s'and ran=='sc':
        human_point=human_point+1;
        print(f"your guess {inp} and computer guess is {ran} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif inp=='p'and ran=='sc':
        computer_point = computer_point + 1;
        print(f"your guess {inp} and computer guess is {ran} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif inp=='p'and ran=='s':
        human_point = human_point + 1;
        print(f"your guess {inp} and computer guess is {ran} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif inp=='sc'and ran=='s':
        computer_point = computer_point + 1;
        print(f"your guess {inp} and computer guess is {ran} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif inp=='sc'and ran=='p':
        human_point = human_point + 1;
        print(f"your guess {inp} and computer guess is {ran} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    else:
        print("pls enter the valid input \n")
    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point > human_point:
    print("Computer wins and you loose")

if computer_point < human_point:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")







