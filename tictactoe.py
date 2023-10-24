import math
import random

def print_board(board):
    print(" ")
    for i in range(3):
        print(" " + " | ".join(board[i]))
        if i < 2:
            print("---|---|---")
    print(" ")

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([cell != " " for row in board for cell in row])

def evaluate(board):
    if check_win(board, 'O'):
        return 1
    elif check_win(board, 'X'):
        return -1
    else:
        return 0

def minimax(board, depth, alpha, beta, is_maximizing):
    score = evaluate(board)
    if score == 1 or score == -1 or check_draw(board):
        return score

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'O'
                    best_score = max(best_score, minimax(board, depth + 1, alpha, beta, False))
                    board[i][j] = " "
                    alpha = max(alpha, best_score)
                    if alpha >= beta:  # Pruning condition for the maximizing player
                        break
            if alpha >= beta:  # Pruning condition for the maximizing player
                break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'X'
                    best_score = min(best_score, minimax(board, depth + 1, alpha, beta, True))
                    board[i][j] = " "
                    beta = min(beta, best_score)
                    if beta <= alpha:  # Pruning condition for the minimizing player
                        break
            if beta <= alpha:  # Pruning condition for the maximizing player
                break
        return best_score


def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)
    alpha = -math.inf
    beta = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'O'
                move_score = minimax(board, 0, alpha, beta, False)
                board[i][j] = " "
                if move_score >= best_score:
                    best_score = move_score
                    best_move = (i, j)
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Let's play Tic-Tac-Toe!")
    z = input("Do you want to start Y/N : ")
    if z.lower() != 'y':
        while True:
            ai_x = random.randint(0, 2)
            ai_y = random.randint(0, 2)
            if board[ai_x][ai_y] == " ":
                board[ai_x][ai_y] = 'O' 
                break
        print("AI starts!")
        print_board(board)

    while True:
        x, y = map(int, input("Enter coordinates for X (row column): ").strip().split())
        board[x][y] = 'X'
        print_board(board)
        if check_win(board, 'X'):
            print("You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        print("AI is making a move...")

        ai_x, ai_y = find_best_move(board)
        board[ai_x][ai_y] = 'O'
        print_board(board)
        if check_win(board, 'O'):
            print("You lose!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == '__main__':
    main()
