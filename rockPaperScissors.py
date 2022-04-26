computer_choice = 'scissors'
user_choice = input("Do you want - rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print('THIS IS A TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('YOU WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('YOU WIN')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('YOU WIN')
else:
    print('YOU LOSE :(')
