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

    