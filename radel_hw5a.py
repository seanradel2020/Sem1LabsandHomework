#Sean Radel
#October 19, 2020
#HW5A
import random
def main():
    #<Name>:<verb> <direct object> <adverbphrase>

    #Initialize lists
    names = ["Hulk", "Spock", "Daenerys", "Aaron Burr", "The Cowardly Lion",
    "Cinderella", "Black Panther", "Merida", "Uhura", "Freya","Frodo"]
    verbs = ["Serving","Leading","Building","Creating", "Putting", "Fighting",
     "Taking","Cleaning up","Protecting","Smashing", "Working", "Incinerating"]
    dObjects = ["the future", "our community", "jobs", "education", "corruption",
      "action", "families", "change", "progress", "government", "results", "our enemies"]
    adPhrases = ["with integrity", "for you", "first", "safe", "for the future",
     "for a change", "for Maine", "with experience", "with vision"]
    sloganCount = -1
    while sloganCount < 0: #ensure a positive number
        sloganCount = int(input("How many slogans would you like? Please enter a positive nu,ber")) #Ask user for the amount of slogans they want


    for i in range(sloganCount): #Initialize loop, will run the loop however many times the user specified
        print(names[random.randint(0,len(names)-1)] + ": "+ #Print out a random name or verb... etc from each list in the desired format
        verbs[random.randint(0,len(verbs)-1)] + " " +
        dObjects[random.randint(0,len(dObjects)-1)] + " "
        + adPhrases[random.randint(0,len(adPhrases)-1)])

main() #call the main function
