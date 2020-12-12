#Sean Radel
#Lab 5 task 3, Functions

def myPrint(printer):
    print(printer)
def multiply(operand, operator):
    results = operand * operator
    return results
def isNegative(negator):
    if negator < 0:
        return True
    else:
        return False
def getInt():
    number = int(input("Gimme and int"))
    return number
