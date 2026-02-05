# env.


# Varaiable
turn = 0
empty_cell_indicator = "*"

board = []
num_row_column = 15 # Board Size
for i in range(num_row_column):
    board.append([])
    for r in range(num_row_column):
        board[i].append(empty_cell_indicator)

# Function
## Board Print
def board_print(board):
    for i in range(num_row_column):
        print(i, end=" ")
    print()
    for i in range(num_row_column):
        print(i+1,end=" ")
        for r in range(num_row_column):
            print(board[i][r], end=" ")
        print()



# Main 
while True:
    board_print(board)
    if turn == 0:
        print("Player 1 turn")
    else:
        print("Player 2 turn")
    while True:
        selected_row = int(input("Enter the row: "))
        selected_column = int(input("Enter the column: "))
        if selected_row > 0 and selected_row <= num_row_column and selected_column > 0 and selected_column <= num_row_column:  # Data validation - within the board size
            if board[selected_row - 1][selected_column - 1] == empty_cell_indicator:
                if turn == 0:
                    board[selected_row - 1][selected_column - 1] = "X"
                else:
                    board[selected_row - 1][selected_column - 1] = "O"
                break  # Exit inner loop - input valid & finish replacing the cell
            else:
                print("This cell is already occupied") # Repeat loop - Input valid & Cell occupied
        else:
            print("Invalid input") # Repeat loop - Input invalid
    turn = 1 - turn # Player round switch