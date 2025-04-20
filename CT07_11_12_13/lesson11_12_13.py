def initialise_board():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        board.append(row)
    return board
        
def print_board(board):
    print("/n Board Layout: ")
    cell_number = 1
    for row in board:
        for cell in row:
            if cell != " ":
                print(" " + str(cell) + " ", end="")

print(initialise_board())
print_board(bo)


