#speed.py
#indicates if speed is legal and how much fine costs




def main():
    speed = int(input("What is the speed of the car? "))
    if speed <= 90:
        print("Car is not speeding")
    else:
        print("Car is speeding")
        fine = 5 *(speed - 90) + 50 + 200
        print("The fine is",fine,"dollars")



main()

    






