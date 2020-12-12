def task2():
    A = 9
    B = 5
    C = 2
    D = 6
    E = 4
    print(A<10)
    print(1<B<9)
    print(C!=3 or 1)
    print(D<=A or C)
    print(E == (A-5))



#-10 <= 1                - TRUE
#True and 1 != 1        -FALSE
#False or 1 == 1        - TRUE
#9//2 == 4              - TRUE
#5%2 == 1               - TRUE
#bool(5) and bool("pig") - TRUE
#bool("") or bool(0.0)    -TRUE

task2()

def task3():
    # A output =
    #It is mild
    #B output =
    #You can ride the bus and bring a friend.
    #You could order a cheap lunch.
    #You could go see a movie.
    #but you probably can’t afford any popcorn
    #C
    userNum = float(input("Please inptut a number 1,10"))
    progNum = 8
    if userNum == progNum:
        print("You guessed my number!!")
    elif userNum > progNum:
        print("Your number is higher than my number!")
    else:
        print("Your number is less than my number!!!!!!")

task3()

def task4():
    i = 1
    userChar = ''
    while(i < 11):
        print(i)
        i = i + 1
    while(userChar != 'q'):
        userChar = input("enter a single character ")


task4()

def extraTask():
    lever = "up"
    dial = 1
    valve = "open"
    switch = False

    if lever == "up":
        print("The first door is closed")
    else:
        print("The first door is open")
    if valve == "open" and switch == False:
        print("The second door is open")
    else:
        print("The second door is closed")
    if dial < 9 and dial > 7:
        print("The third door is open")
    elif dial == 1:
        print("The third door is open")
    else:
        print("The third door is closed")
    if dial == 1 and switch != True:
        if lever == "down" or valve == "open":
            print("The fourth door is open")
        else:
            print("the fourth door is closed")
    else:
        print("The fourth door is closed")

extraTask()
        # correct Lever = "up", valve = "open",
        # switch = False, dial = 1
