#shuffle.py

from random import randrange



def shuffle (myList):
    newList = []
    for i in range(len(myList)):
        itemToMove = randrange(0, len(myList))
        newList.append(myList[itemToMove])
        myList.pop(itemToMove)
    return newList

print (shuffle([]))
