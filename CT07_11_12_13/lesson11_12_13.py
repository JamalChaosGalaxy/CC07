
def initialise_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        board.append(row) 
    return board

     
def print_board(board):
    print("\nBoard Layout: ")
    cell_number = 1
    for row in board:
        for cell in row:
            if cell != ' ':
                print(" " + str(cell) + " ", end="")
            else:
                print(" " + str(cell_number) + " ", end="")
            if cell_number % 3 != 0:
                print("|", end="")
            cell_number += 1
        if cell_number <= 9:
            print("\n----------")
    print("\n")    
        
def get_player_move(board):
    move_input = input("Pick a number from 1 to 9: ")
    if move_input.isdigit():
        if int(move_input) >= 0 and int(move_input) <=9:
            move = int(move_input) - 1
            row = move // 3
            col = move % 3
            if board[row][col] == " ":
                board[row][col] = 'X'
            else:
                print("Space is already taken")
        else:
            print("Invalid error. Please enter a value between 1-9.")
    else:
        print("Invalid input. Please put in a number from 1 to 9")

board = initialise_board()

def check_win():
    win_conditions = [
        # Horizontal
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Vetical
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonal
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
        
    ]
    for condition in win_conditions:
        if condition[0] == condition[1] == condition[2] and condition[0] != ' ':
            return True
    return False
board = initialise_board()
while True:
    print_board(board)
    get_player_move(board)


