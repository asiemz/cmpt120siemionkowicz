# dice.py

# program that performs a simulation to estimate the probability of
# rolling five of a kind in a single roll of five six-sided dice.


from random import randrange


def main():
    print("This program estimates the probability of rolling five of a kind in one roll of five 6-sided dice")

    x = int(input("How many times should we roll? "))

    wins = 0

    for i in range(x):

        roll1 = randrange(1, 7)
        roll2 = randrange(1, 7)
        roll3 = randrange(1, 7)
        roll4 = randrange(1, 7)
        roll5 = randrange(1, 7)

        if roll1 == roll2 and roll1 == roll3 and roll1 == roll4 and roll1 == roll5:
            wins += 1
            #print("You have won")

        #else:
            #print("unsuccessful")

    print("Probability ", wins / x)
main()
