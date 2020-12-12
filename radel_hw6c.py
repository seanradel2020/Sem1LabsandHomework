#Sean radel
#Homework 6c
#*I did not collaborate with any other students*

import random
#fullDeck = []
#discardPile = []

def buildADeck(): #Build the deck
    suits = [" of Spades"," of Clubs"," of Diamonds", " of Hearts"]
    fullDeck = []
    for i in range(4): #I use two loops here, to save me the time of writing all of the cards out
        for j in range(14):
            fullDeck.append(str(j)+suits[i]) #Deck gets filled all the way up

    return fullDeck #Returns a full deck


def printADeck(aDeck): #Takes in any deck
    for i in range(len(aDeck)-1): #Prints the deck
        print(aDeck[i])



def shuffleADeck(Deck): #uses the random shuffle method to shuffle whatever deck is passed
    shuffledDeck = random.shuffle(Deck)

def drawAndDiscard(fullDeck,howManyDrawn): #Draw and discard wizard
    discardPile = [] #Create a discard pile
    for i in range(howManyDrawn):
        drawn = fullDeck[random.randint(0,len(fullDeck)-1)] #randomly draw a card
        fullDeck.remove(drawn) #Remove the drawn card from the deck
        keep = input("Your drew a: "+ drawn + ". K for keep, D for discard")
        if keep.lower() == "k": #either keep the card and putit on the bottom of the deck, or discard it
            fullDeck.append(drawn)
        else:
            discardPile.append(drawn)

    return fullDeck, discardPile #return both lists

def main():

    wizard = input("Would you like to,\n 'a' build a new deck, \n 'b' print a deck, \n 'c' shuffle a deck, \n or 'd' draw and discard from  a deck ")

    while wizard.lower() != "quit": #Loop through so you can perform any function at any time as many times as your heart desires

        if wizard.lower() == 'a':
            fullDeck = buildADeck()

        if wizard.lower() == 'b':
            temp = input("A. to print your full deck, B. to print your discard pile ")
            if temp.lower() == "a":
                printADeck(fullDeck)
            if temp.lower() == "b":
                printADeck(discardPile)


        if wizard.lower() == 'c':
            temp = input("A. to shuffle your full deck, B. to shuffle your discard pile ")
            if temp.lower() == "a":
                shuffleADeck(fullDeck)
            if temp.lower() == "b":
                shuffleADeck(discardPile)

        if wizard.lower() == 'd':
            howManyDrawn = int(input("How many cards would you like to draw? "))
            fullDeck, discardPile = drawAndDiscard(fullDeck,howManyDrawn)




        wizard = input("Would you like to, \n 'a' build a new deck, \n 'b' print a deck, \n 'c' shuffle a deck, \n or 'd' draw and discard from  a deck \n quit to end program ")
main()
#I hope you enjoyed this code, I was very happy with how it came out, I think it is very functional and efficient
