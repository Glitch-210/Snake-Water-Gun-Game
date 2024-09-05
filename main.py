import random

'''
    1 = snake
    2 = water
    0 = gun

'''

computer = random.choice([2,1,0])
user = input("Enter your choice: ")
dict = {"s":1,"w":2,"g":0}
revdict = {1:"Snake",2:"Water",0:"Gun"}

you = dict[user]

print(f"You chose {revdict[you]}\nComputer chose {revdict[computer]}")

if(computer == you):
    print("Draw")

else:
    if(computer == 2 and you == 1):
        print("You win")
    elif(computer == 2 and you == 0):
        print("You Lose!")
    elif(computer == 1 and you == 2):
        print("You Lose!")
    elif(computer == 1 and you == 0):
        print("You win")
    elif(computer == 0 and you == 2):
        print("You lose")
    elif(computer == 0 and you == 1):
        print("You win")

    else:
        print("Something went wrong!")