#Pig Game
import random

val = random.randint(1, 6)

player1_total = 0
player2_total = 0

turn = 1
max_score = 20

while True:
    choice = input("[Player {}] Enter 'r' to roll or 'h' to hold: ".format(turn))
    if choice == 'r':
        print("Player {} rolled:".format(turn), val ," Player{} score is:".format(turn),)
        val = random.randint(1, 6)
        if val != 1:
            if turn == 1:
                player1_total += val
            else:
                player2_total += val

        else:
            print('Player {} loses turn'.format(turn))
            if turn == 1:
                player1_total = 0
                turn = 2
            else:
                player2_total = 0
                turn = 1
    else:
        print('Player{} holds'.format(turn))
        if turn == 1:
            turn = 2
        else:
            turn = 1

#check if someone wins the game
    if player1_total >= max_score or player2_total >= max_score:
      break

if player1_total >= max_score:
    print('Player 1 wins!!!')
else:
    print('Player 2 wins!!!')

'''
print("You rolled:", val ," Your score:", player1_total)
while player1_total < 20 and player2_total < 20:
    choice = input("Enter 'r' to roll or 'h' to hold: ")
    if choice == 'r':
        val = random.randint(1, 6)
        if val != 1:
            player1_total += val
            print("You rolled:", val ," Your score:", player1_total)
        if val == 1:
            player1_total = 0
            switch = input("Player2 press 'r' or 'h' to hold: ")
        if choice == 'h':
            switch = input("Player2 press 'r' or 'h' to hold: ")
'''