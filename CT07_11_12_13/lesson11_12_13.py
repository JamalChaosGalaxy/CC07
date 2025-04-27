
def initialise_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        board.append(row)
    return board
print(initialise_board)        
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
    move = int(move_input) - 1
    row = move // 3
    col = move % 3
    board[[row][col]] = 'X'

print_board(initialise_board())
board = initialise_board
get_player_move(board)
print_board(board)

