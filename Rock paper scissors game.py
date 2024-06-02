import random
user = 0
computer = 0
while True:
    choices = ["rock","paper","scissors"]
    inp = input("Enter your choice (rock,paper,scissors)\nPress E to exit:" )
    inp=inp.lower()
    if (inp=="E" or inp=="e"):
        print("------------------------------------------------------------------------------------------------------------")
        print("Your score:",user,"\tComputer's score:",computer)
        print("------------------------------------------------------------------------------------------------------------")
        if (computer==user):
            printf("It's a tie.")
        elif (computer > user):
            print("Computer wins.")
            print("------------------------------------------------------------------------------------------------------------")
        else:
            print("You win.")
            print("------------------------------------------------------------------------------------------------------------")
        break
    else:
        ch = random.choice(choices)
        print("Your choice:",inp,"\nComputer's choice:",ch)
        if (inp==ch):
            print("It's a tie.")
        elif((inp=="rock" and ch=="paper")or(inp=="paper" and ch=="scissors")or(inp=="scissors" and ch=="rock")):
            print("Computer wins.")
            computer += 1
        else:
            print("You win.")
            user += 1
