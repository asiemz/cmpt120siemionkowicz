#fibonacci

#read the value of n in the sequence if n<3
#for i in the sequence (3)

#i = (i-1) + (i-2)
#print number


def main():
    n = int(input("enter the number of terms for the sequence: "))
    if n==1:
        print("The Fibonacci sequence is 1")
    elif n==2:
        print("The Fibonacci sequence is 1,1")
    else:
        print("The Fibonacci sequence is 1,1, ")
        num1=1
        num2=1
        for i in range(2,n):
            num = num1 + num2
            print(","+ str(num), end="")
            num2 = num1
            num1 = num

main()
            
