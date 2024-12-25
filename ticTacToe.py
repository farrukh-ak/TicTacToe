from random import randrange
from random import choice
global free_fields
global board

free_fields = []

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
positions = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}

def display_board(board):
    print("----- Tic Tac Toe -----")
    for i, nested_list in enumerate(board):
        print(" | ".join(map(str, nested_list)))  # Convert elements to string and join with " | "
        if i < len(board) - 1:  # Print horizontal line only between rows
            print("-" * 9)
    print("--------------------------")

def get_user_input():
    move = int(input("Enter your move (1-9):"))



def enter_move(board):
    while True:
        try:
            user_move = int(input("Enter your move (1-9): "))
            if user_move not in positions:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            x, y = positions[user_move]
            if (x, y) in free_fields:
                board[x][y] = 'O'
                print("Board after player's move:\n")
                display_board(board)
                break
            else:
                print("The move is already played. Please enter a valid move.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def make_list_of_free_fields(board):
    free_fields.clear()  # Clear the list at the start
    for i in range(3):
        for j in range(3):
            if board[i][j] != "X" and board[i][j] != "O":
                t = (i,j)
                free_fields.append(t)
    print("Playable fields after the move:", free_fields)
    return len(free_fields) > 0


def victory_for(board):
    # Checking rows for a win
    for i in range(3):
        if all('X' == j for j in board[i]):
            print("Computer Wins!")
            return True
        if all('O' == j for j in board[i]):
            print("Player Wins!!")
            return True

    # Checking columns for a win
    for i in range(3):
        col_elements = [board[j][i] for j in range(3)]
        if all(k == 'X' for k in col_elements):  # Ensure all elements are 'X'
            print("Computer Wins!")
            return True
        if all(k == 'O' for k in col_elements):  # Ensure all elements are 'O'
            print("Player Wins!!")
            return True

    n = len(board)

    # Main diagonal
    if all(board[i][i] == 'X' for i in range(n)):
        print("Computer Wins!")
        return True
    if all(board[i][i] == 'O' for i in range(n)):
        print("Player Wins!!")
        return True

    # Anti-diagonal
    if all(board[i][n - 1 - i] == 'X' for i in range(n)):
        print("Computer Wins!")
        return True
    if all(board[i][n - 1 - i] == 'O' for i in range(n)):
        print("Player Wins!!")
        return True
        
def draw_move(board):
    if board == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
        board[1][1] = 'X'
    else:
        x, y = choice(free_fields)    
        board[x][y] = 'X'
    print("Board after computer's move:\n")
    display_board(board)

        

display_board(board)

while make_list_of_free_fields(board):
    draw_move(board)
    if victory_for(board):
        break
    if not make_list_of_free_fields(board):
        print("Game Drawn! :\\")
        break
    enter_move(board)
    if victory_for(board):
        break
