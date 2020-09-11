import math    #makes math library available

def main():
    print("This program will help you evaluate surface area and volume of a sphere given a radius.")
    print()
    r = eval(input("Please enter the radius of the sphere: "))
    pi = 3.14159
    area = 4*pi*(r**2)

    volume = (4/3)*pi*(r**3)

    print("The surface area of the sphere is", area)
    print("The volume of the sphere is", volume)

main()
