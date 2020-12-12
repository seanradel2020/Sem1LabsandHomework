#Sean radel
#Homework 6 a
#*I did not collaborate with anyone else. All work is mine.*

def longRun(listOfThings):

#Return how long, and what element

# my algorithm
#Counter = 0
# While index x == next index x
#tempcounter +=1
#if tempcounter >Counter
#  counter = tempcounter
#runElement = index x
    counter = 0
    runElement = listOfThings[0]
    tempcounter = 1
    for i in range(len(listOfThings)-1):

        #print(i)
        if listOfThings[i-1] != listOfThings[i]:
            tempcounter = 1


        if listOfThings[i-1] == listOfThings[i]:
            tempcounter = tempcounter + 1
                #print("while works")
            if tempcounter >= counter:
                runElement = listOfThings[i]
                counter = tempcounter



    reportString = "Longest run was: " + str(counter) + " and the run element was: " + str(runElement)
    return reportString


def main():
    listOfThings = ["-1"]
    while listOfThings[len(listOfThings)-1] != "stop":

        newListItem = input("Enter a number, or \"stop\" to break out")
        listOfThings.append(newListItem)


    report = longRun(listOfThings)

    print(report)

main()
