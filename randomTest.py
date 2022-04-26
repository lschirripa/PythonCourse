import random

roll = random.randint(1,3)

guess = int(input("guess the dice\n"))

if roll == guess:
    print('CORRECT! computer number was ' + str(roll))
else:
    print("NOPE! computer number was " + str(roll))