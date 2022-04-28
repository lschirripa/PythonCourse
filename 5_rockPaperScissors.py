import random

roll = random.randint(1,3)

print("computer rolled number " + str(roll))

# if roll == 1:
#     computer_choice = 'scissors'
# elif roll == 2:
#     computer_choice = 'paper'
# else:
#     computer_choice = 'rock'

computer_choice = random.choice(["rock","paper","scissors"])

user_choice = input("Do you want - rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print('THIS IS A TIE bc computer choice was ' + computer_choice)
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('YOU WIN bc computer choice was ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('YOU WIN bc computer choice was ' + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('YOU WIN bc computer choice was ' + computer_choice)
else:
    print('YOU LOSE :( because computer choice was ' + computer_choice)
