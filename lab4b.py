##############################
# LAB 4 Block B              #
# by Sean Radel      #
##############################

# A broken game of rock, paper, scissors.

# This program has many, many errors. Do not try to locate the errors
# before running the code. Run the code and use the error messages to debug.
# Most of the errors involve either adding or changing a single character.
# If you are writing entire lines of code, you are doing it the hard way.

###############################################################################
# BLOCK B
import random

cwins="Computer wins!"
pwins="Player Wins!"
choices = ["rock","paper","scissors"]
RUN= True
wlt=[0,0,0] # Win, loss, tie record

while RUN:
    print("-------------------------------------------")
    print("Rock [0], Paper [1], Scissors [2]")
    player_choice = int(input("Pick one: "))
    comp_choice = random.randint(0,2)  # Picks random num 0, 1, or 2

    if player_choice <= -1 or player_choice >= 3:
        print("Invalid Choice")
    else:
        print("Player chooses:   ",choices[player_choice])
        print("Computer chooses: ",choices[comp_choice])
        if player_choice == comp_choice:
            print("Tie")
            wlt[2]+=1
        elif player_choice==0:      # Player: Rock
            if comp_choice==1:      # Computer: Paper
                print(cwins)
                wlt[1]+=1
            else:                   # Computer: Scissors
                print(pwins)
                wlt[0]+=1
        elif player_choice==1:      # Player: Paper
            if comp_choice==0:      # Computer: Rock
                print(pwins)
                wlt[0]+=1
            else:                   # Computer: Scissors
                print(cwins)
                wlt[1]+=1
        elif player_choice==2:      # Player: Scissors
            if comp_choice==0:       # Computer: Rock
                print(cwins)
                wlt[0]+=1
            else:                   # Computer: Paper
                print(pwins)
                wlt[1]+=1

    print(wlt[0],"wins,",wlt[1],"losses,",wlt[2],"ties")
    print("-------------------------------------------")

    RUN = input("Play again? [y/n] ""=='y'")

print("Thanks for playing Rock, Paper, Scissors.")
