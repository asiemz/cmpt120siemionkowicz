#dayNum.py
#program that accepts a date as month/day/year, verifies that it is a valid date, and then calculates the corresponding day number.



def main():

    print("Enter date in format (mm/dd/yyyy)")

    month = float(input("What is the month? "))
    day = float(input("What is the day? "))
    year = float(input("What is the year? "))


    dayNum = 31*(month-1) + day
    
    if month > 2:
        dayNum = (4(month) + 23)//10

    elif year % 4 ==0 and year % 100 ==0 and month >= 2 and day > 29:
        dayNum = ((4(month) + 23)//10 )+1

    else:
        dayNum = 31*(month-1)+day

    print("The day number is", dayNum)

main()


