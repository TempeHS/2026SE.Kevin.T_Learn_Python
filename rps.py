import random

choices = ["rock", "paper", "scissors"]
score = [0, 0]

def player_choice():
    while True:
        choice = input("Choice? ")
        if choice in choices:
            return choice
        else:
            print("invalid choice")

def random_choice():
    return random.choice(choices)

def winner(p1, p2):
    if p1 == p2:
        return "Draw"
    elif p1 == "rock" and p2 == "scissors" or p1 == "paper" and p2 == "rock" or p1 == "scissors" and p2 == "paper": #cooked
        score[0] += 1
        print(score[0], "to", score[1])
        return "You win"
    else:
        score[1] += 1
        print(score[0], "to", score[1])
        return "You lose"

def main_game():
    name = input("Name? ")
    for i in range(3):
        computer = "rock" #random_choice()
        player = player_choice()
        print(name, "picks", player)
        print("Computer picks", computer)
        print(winner(player, computer))
    if score[0] > score[1]:
        print(name, "wins the game!!!")
    elif score[0] < score[1]:
        print("computer wins the game!!!")
    else:
        print("its a draw!!!")

main_game()