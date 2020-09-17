#stringChange.py
#Program that gets a string from a given string where all occurences of its
#first character have been changed to $ except the very first character


def main():

    str = input("Please type a word: ")
    char = str[0]
    str = str.replace(char,'$')
    
    
    print(char + str[1: ])
   

main()
    
