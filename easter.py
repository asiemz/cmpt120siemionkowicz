#easter.py
#prints when easter falls on


def main():
    year = int(input("What year between 1982 and 2048: "))
  

    
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    easter = 22 + d + e

    if easter > 31:
        print("Easter is on April", easter-31, str(year))
    else:
        print("Easter is on March", easter, str(year))

main()
