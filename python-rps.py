# setup a rock paper scissors game with a computer opponent, and a wins, losses, and ties counter

# import random as we will need it to make the computer's choice
import random

print("Welcome to Rock, Paper, Scissors!")

wins = 0
losses = 0
ties = 0

playing = True

while playing:
    print("Wins: " + str(wins))
    print("Losses: " + str(losses))
    print("Ties: " + str(ties))

    user_choice = input("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit: ")

    print('Your choice: ' + user_choice)

    # check if user wants to quit
    if user_choice == 'q':
        playing = False
        print("Thanks for playing!")
        continue

    computer_choice = random.choice(['r', 'p', 's'])

    print('Computer choice: ' + computer_choice)

    if user_choice == 'r' and computer_choice == 'r':
        print("Tie!")
        ties += 1
    elif user_choice == 'r' and computer_choice == 'p':
        print("You lose!")
        losses += 1
    elif user_choice == 'r' and computer_choice == 's':
        print("You win!")
        wins += 1
    elif user_choice == 'p' and computer_choice == 'r':
        print("You win!")
        wins += 1
    elif user_choice == 'p' and computer_choice == 'p':
        print("Tie!")
        ties += 1
    elif user_choice == 'p' and computer_choice == 's':
        print("You lose!")
        losses += 1
    elif user_choice == 's' and computer_choice == 'r':
        print("You lose!")
        losses += 1
    elif user_choice == 's' and computer_choice == 'p':
        print("You win!")
        wins += 1
    elif user_choice == 's' and computer_choice == 's':
        print("Tie!")
        ties += 1
    else:
        print("Invalid input. Please try again.")