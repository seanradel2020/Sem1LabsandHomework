#Sean radel
#Homework 6b
#*I did not collaborate with any other students*

def bubbleSort(listOfNums): #this program uses sort of a bubble sort, I did not invent the bubble sort, but i took inspiration from it

    sorted = False
    while sorted == False:
        for k in range(len(listOfNums)-1):
            if listOfNums[k]>listOfNums[k+1]: #if out of order
                buffer = listOfNums[k] #use a buffer to swap around
                listOfNums[k] = listOfNums[k+1] #swap
                listOfNums[k+1] = buffer#reassign to finish swap

            if(all(listOfNums[i] <= listOfNums[i+1] for i in range(len(listOfNums)-1))): # checks to see if all are sorted :).
            #uses the all function, learned from here https://beginnersbook.com/2019/03/python-all-function/#:~:text=Python%20all%20%28%29%20function%20accepts%20an%20iterable%20object,is%20empty%20then%20also%20this%20function%20returns%20true.
                sorted = True

    return listOfNums



def main():
    listOfNums = [] # list
    newListItem = input("Enter a number, or \"stop\" to break out ") #add firsrt num
    listOfNums.append(newListItem)
    count = 0
    while listOfNums[len(listOfNums)-1] != "stop": # while not stop

        newListItem = input("Enter a number, or \"stop\" to break out ")
        listOfNums.append(newListItem) #add to list
        count = count + 1

    listOfNums.remove("stop")

    sorted = bubbleSort(listOfNums)
    print("Heres your sorted list!")
    for i in range(count):# print sorted list
        print(sorted[i])

main()
