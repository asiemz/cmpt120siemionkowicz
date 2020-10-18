#syracuse.py




def main():

    num = int(input("Enter a starting value: "))

    sequence = syracuse(num)

    print(sequence)


def syracuse(x):

    result = [x]

    while x != 1:
        if x % 2 ==0:
            x = x//2 # JA

            result.append(x)

        else:

            x = 3 * x +1

            result.append(x)

    return result

main()
