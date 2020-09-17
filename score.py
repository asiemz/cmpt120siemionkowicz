#score.py
#accepts quiz score as input
#outputs grade letter

def main():

    grade = ['F','F','D','C','B','A']
    
    n = int(input("Please enter the quiz score (0-5): "))

    print("Your grade is", grade[n])


main()
