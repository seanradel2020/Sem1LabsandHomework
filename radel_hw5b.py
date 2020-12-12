#Sean Radel
#October 19, 2020
#HW5B

def palindromer(palinString):
    if isAlreadyAPalindrome(palinString) == False:
        #start with the string
        #take every letter but the last
        #place it in reverse order on the back end of the string
        newPalindrome = palinString
        palinHelpTemp = palinString[0:len(palinString)-1]
        palinHelpTemp = palinHelpTemp[::-1]
        newPalindrome = newPalindrome + palinHelpTemp
        return newPalindrome #return the new palindrome
    else:
        return palinString #return the existing palindome


def isAlreadyAPalindrome(palinString):
    boolIsAPalindrome = palinString == palinString[::-1] #check to see if string is the same forward as backwards
    return boolIsAPalindrome

def maine():
    palinString = input("Enter a string to be palindromized: ") #get string to palindromize
    print(palindromer(palinString))
maine()
