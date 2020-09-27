#toNumbers.py
#changes entries in a list into numbers




'''def toNumbers(strList):
    n = ['1','2','3']
    newList = str.replace(strList,n)
    strList = newList
    print(strList)'''

def toNumbers(strList):
    numbers = []
    for elem in strList:
        numbers.append(int(elem))
    return numbers

toNumbers("red")
    
