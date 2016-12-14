import numpy as np
import random


def create_board():
    return np.zeros((3, 3))


def place(board, player, position):
    board[position] = player


def possibilities_utility(pos):
    list = []
    for i in range(len(pos[0])):
        list.append((pos[0][i], pos[1][i]))
    return list


def possibilities(board):
    return possibilities_utility(np.where(board == 0))


def random_place(board, player):
    if board[1,1] == 0:
        board[1,1] == player
        return
    board[random.choice(possibilities(board))] = player


def row_win(board, player):
    for i in range(3):
        if np.all(board[i] == player):
            return True
    return False


def col_win(board, player):
    for i in range(3):
        if np.all(board[:, i] == player):
            return True
    return False


def diag_win(board, player):
    if board[1, 1] == player and ((board[0, 0] == player and board[2, 2] == player) or (board[2, 0] == player and board[0, 2] == player)):
        return True
    return False


def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            return player
    if np.all(board != 0):
        winner = -1
    return winner


def print_winner(winner):
    if winner == -1:
        print("The game is a draw.")
    elif winner == 1:
        print("Player one is the winner")
    elif winner == 2:
        print("Player two is the winner")


def play_strategic_game():
    board, winner = create_board(), 0
    i = np.random.randint(1, 3)
    print("Player " + str(i) + " Plays first.")
    print(board)
    board[1, 1] = i
    print(board)
    if i == 1:
        l = [2, 1]
    else:
        l = [1, 2]
    while winner == 0:
        for player in l:
            random_place(board, player)
            print(board)
            winner = evaluate(board)
            if winner != 0:
                break
    print_winner(winner)
    return winner


def player_choice(board, player):
    print(board)
    possible_locations = possibilities(board)
    print("The locations available are ", possible_locations)
    choice = (-1, -1)
    while choice not in possible_locations:
        try:
            choice = (int(input("Please enter the row.")), int(input("Please enter the column.")))
        except:
            print("Input is not entered correctly.")
            continue
    board[choice] = player


def play_with_computer():
    board = create_board()
    print("Player is number 1.\ncomputer is number 2.\n Let's choose who plays first.")
    i = np.random.randint(1, 3)
    print("Player "+str(i)+" Plays first.")
    if i==2:
        board[1, 1] = 2
    while evaluate(board) == 0:
        player_choice(board, 1)
        if evaluate(board) != 0:
            break
        print(board)
        random_place(board, 2)
    print(board)
    print_winner(evaluate(board))


def player_vs_player():
    board, i, winner = create_board(), np.random.randint(1, 3), 0
    print("Player " + str(i) + " Plays first.")
    if i == 2:
        l = [2, 1]
    else:
        l = [1, 2]
    while evaluate(board) == 0:
        for player in l:
            player_choice(board, player)
            if evaluate(board) != 0:
                break
    print(board)
    print_winner(evaluate(board))


def play_game():
    i = 0
    while i not in [1, 2, 3]:
        i = int(input("Please choose the mode for the game.\n 1 - Player vs Player \n 2 - Player vs Computer . \n 3 - Computer vs Computer."))
    if i == 3:
        play_strategic_game()
    elif i == 2:
        play_with_computer()
    else:
        player_vs_player()

play_game()
