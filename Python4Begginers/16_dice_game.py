import random

def rollDice():
    rand = random.randint(1,6) + random.randint(1,6)  
    return rand 


def main():

    name1 = input("enter your name\n")
    name2 = input("enter your name\n")

    value1 = rollDice()
    value2 = rollDice()
    print(value1,value2)

    if value1 > value2:
        print(name1, " wins with a total score of " + str(value1))
    elif value2 > value1    :
        print(name2, " wins with a total score of " + str(value2))
    else:
        print("tie!")

main()