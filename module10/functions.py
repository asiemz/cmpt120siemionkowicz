#functions.py

def count(myList,x):
    ctr = 0
    for elem in myList:
        if x == elem:
            ctr+=1
    return ctr

def isin(myList,x):

    is_in = False
    for elem in myList:
        if x == elem:
            is_in = True
            break
    return is_in

def index(myList,x):
    for i in range(len(myList)):
        if myList[i] == x:
            return i


def reverse(myList):
    return myList[-1:-1]


    
