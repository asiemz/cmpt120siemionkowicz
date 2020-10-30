#craps.py


from random import randrange
def main():

    print("Welcome to Craps! In order to win you must roll either a 7 or 11, or you must roll something other than a 2, 3, or 12 twice")


    x = int(input("Enter the number of times you would like to play: "))

    wins = 0



    for i in range (x):

        r1 = int(randrange(1,13))

        if r1 == 7 or r1 == 11:
            wins = wins + 1
            print("You win!")
            

        elif r1 == 2 or r1 == 3 or r1 == 12:
                print("You lose!")
                

        else:
            r2 = int(randrange(1,13))

            if r2 == 7:
                print("You lose!")
            

            elif r2 == r1:
                    wins = wins + 1
                    print("You win!")
                    

            else:
                while r2 != r1 or r2 != 7:
                    r3 = int(randrange(1,13))

                    if r3 == 7 or r3 == r1:
                        wins = wins + 1
                        print("You win!")
                        

                    else:
                        print("You  lose")
                        break
                        


        probwin = (wins/x)*100
        print("Your winning probability is",probwin,"%.")   


main()
        


