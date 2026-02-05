# env.


# Varaiable
turn = 0

board = []
num_row_column = 15
for i in range(num_row_column):
    board.append([])
    for r in range(num_row_column):
        board[i].append("  ")

# Function
## Board Print
def board_print(board):
    for i in range(num_row_column):
        print(i, end="  ")
    print()
    for i in range(num_row_column):
        print(i+1,end="  ")
        for r in range(num_row_column):
            print(board[i][r], end="  ")
        print()

board_print(board)