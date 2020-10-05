#dayNum.py
#program that accepts a date as month/day/year, verifies that it is a valid date, and then calculates the corresponding day number.



def main():

    month,day,year = input("Enter date in format (mm/dd/yyyy)").split('/')

    month = int(month)
    day = int(day)
    year = int(year)

    dayNum = 31*(month-1) + day
    
    if month > 2:
        dayNum -= (4*month + 23)//10
    if (year % 4 == 0 or year % 100 == 0) and not(year % 400 == 0) and month > 2:
        dayNum += 1

    print("The day number is", dayNum)

main()


