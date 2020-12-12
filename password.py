password = input("What's the password?")
count = 3
while count > 0:
    guess = input("What's your guess?")
    if ( guess == password):
        print("You guessed it!")
        count = 0
    else:
        count = count - 1
        print("That aint it")
