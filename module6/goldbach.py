#goldbach.py





#input

def main():

  



    number = int(input("Enter an even number: "))

    fx = number//2 + 1
    fy = number//2 - 1

    if number%2==0:
        while fx%2==0 and fy%2==0:
            fx = fx+1
            fy = fy-1
        print(fx, fy)

    else:
        print("This is not an even number")

main()


    



    
