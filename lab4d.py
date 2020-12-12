##############################
# LAB 4 Block C              #
# by Sean Radel      #
##############################


##############################################################################
#
# This piece of code should ask the user which character they want to print
# and how many times they want to print it. The program will then print the
# character that many times on its own line. If the user types 'n' or 'N',
# for the question asking whether they want to print more, then the program
# should stop. Example:

# Which character do you want to print? A
# How many times do you want to print it? 8
# AAAAAAAA
# Do you want to print more letters? n

run = "y"
while run != "N" or run == "n":
    char = input("Which character do you want to print? ")
    num = int(input("How many times do you want to print it? "))
    for i in range(1,num):
        print(char,end="")
    print()

    run = input("Do you want to print more letters? ")
