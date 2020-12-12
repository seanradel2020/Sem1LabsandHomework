#Sean Radel
#October 20 2020
#HW5C
#Notes
#first to ten points
#Both players turn over a card
#(spades > hearts > diamonds > clubs)
#Don't keep track of cards, pull from a list of all cards in a deck.
#multiple of the same card can be drawn - both players lose a point at tie
# if player a draws 4 of clubs they lose all their points
#if player a draws 7 of any suit, they get a point, b loses all their points
import random

def main():
    #Initialize deck
#Sort by hirearchy of card
#whichever player draws the higher number will win, because of how the cards are indexed
    cardsIndex = ["2 of clubs ","2 of diamonds ","2 of hearts "," 2 of spades ","3 of clubs ","3 of diamonds ","3 of hearts "
    ,"3 of spades ","4 of clubs ","4 of diamonds ","4 of hearts ","4 of spades ","5 of clubs ","5 of diamonds "
    ,"5 of hearts "," 5 of spades ","6 of clubs ","6 of diamonds ","6 of hearts "," 6 of spades ","7 of clubs ","7 of diamonds ","7 of hearts ",
    "7 of spades ","8 of clubs ","8 of diamonds ","8 of hearts "," 8 of spades ","9 of clubs ","9 of diamonds ","9 of hearts ","9 of spades ",
    "10 of clubs ","10 of diamonds ","10 of hearts ","10 of spades ","jack of clubs ","jack of diamonds ","jack of hearts ","jack of spades ",
    "queen of clubs ","queen of diamonds ","queen of hearts ","queen of spades ","king of clubs ","king of diamonds ","king of hearts ",
    "king of spades ","ace of clubs ","ace of diamonds ","ace of hearts ","ace of spades ",]
    player1Score = 0
    player2Score = 0
    while (player1Score < 10 and player2Score < 10): #While someone doesnt have a winning score
        player1Draw = random.randint(0,len(cardsIndex)-1) #Draw cards
        player2Draw = random.randint(0,len(cardsIndex)-1)
        print("Player 1 draws the: " + cardsIndex[player1Draw]) #Print the drawn card
        print("Player 2 draws the: " + cardsIndex[player2Draw])
        #Check to see if the cards meet any of the specified conditions of the game (the rules)
        if player1Draw > player2Draw:
            print("Player 1 wins this round")
            player1Score = player1Score + 1
        if player2Draw > player1Draw:
            print("Player 2 wins this round")
            player2Score = player2Score + 1
        if player1Draw == player2Draw:
            player1Score = player1Score - 1
            player2Score = player2Score - 1
            print("Tie, both players lose a point")
        if player1Draw == 8:
            print("four of clubs, player 1, you lose all your points")
            player1Score = 0
        if player2Draw == 8:
            print("four of clubs, player 2, you lose all your points")
            player2Score = 0
        if (player1Draw == 21) or (player1Draw == 22) or (player1Draw == 23) or (player1Draw == 24):
            print("7, player 2 you lose all your points, player 1 you gain a point")
            player2Score = 0
            player1Score = player1Score + 1
        if(player2Draw == 21) or (player2Draw == 22) or (player2Draw == 23) or (player2Draw == 24):
            print("7, player 1 you lose all your points, player 2 you gain a point")
            player1Score = 0
            player2Score = player2Score + 1
        report = ("Score: Player 1, {}; Player 2, {}" ) #report the score string
        print(report.format(player1Score,player2Score)) #print the formatted report
        print()

main()
