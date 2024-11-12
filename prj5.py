##rock paper scissors 
import random

options= ("rock", "paper", "scissors")


running  = True

while running:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("enter a choice [rock, paper, scissors]: ").lower()
    print(f"player: {player}")
    print(f"computer : {computer}")
    if player == computer:
        print("its a tie!")
    elif player == "rock" and computer == "scissors":
        print("you won")
    elif player == "paper" and computer == "rock":
        print("you won")
    elif player == "scissors" and computer == "paper":
        print("you won")
    else:
        print("you lose")
    if not input("wanna play again?(y/n): ").lower() == "y":
        running = False

print("thanks for playing")