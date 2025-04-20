def initialise_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        board.append(row)
    return board
        
def print_board(board):
    print("/nBoard Layout: ")
    cell_number = 1
    for row in board:
        for cell in row:
            if cell != " ":
                print(" " + str(cell) + " ", end="")
            else:
                print(" " + str(cell_number) + " ", end="")
            if cell_number % 3 != 0:
                print("|", ends="")
            cell_number += 1

print(initialise_board())
print_board(board)


