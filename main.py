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

## Check Win (V1) (NEED TO IMPROVE: 判断算法 尝试使用方向连续数判断)
def check_win(board, turn):
    # Define current player indicator
    if turn == 0:
        player_indicator = "X"
    else:
        player_indicator = "O"
    # Check if the player has won
    for i in range(num_row_column):
        for r in range(num_row_column):
            if board[i][r] == player_indicator:
                # Horizontal Direction
                if i + 4 < num_row_column:
                    if board[i+1][r] == player_indicator and board[i+2][r] == player_indicator and board[i+3][r] == player_indicator and board[i+4][r] == player_indicator:
                        return True
                # Vertical Direction
                if r + 4 < num_row_column:
                    if board[i][r+1] == player_indicator and board[i][r+2] == player_indicator and board[i][r+3] == player_indicator and board[i][r+4] == player_indicator:
                        return True
    return False

## Check Win (V2)
def check_win_v2(board, row, col, indicator):
    directions = [
        (0, 1),   # Horizontal
        (1, 0),   # Vertical
        (1, 1),   # Right-down diagonal
        (1, -1)   # Left-down diagonal
    ]
    for dr, dc in directions:
        count = 1  # Initial count

        # Positive
        r, c = row + dr, col + dc
        while 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == indicator:
            count += 1
            r += dr
            c += dc
        # Negative
        r, c = row - dr, col - dc
        while 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == indicator:
            count += 1
            r -= dr
            c -= dc

        # Satisfy win condition: 5 in a row (or more)
        if count >= 5:
            return True

    return False

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

    # Check win
    if turn == 0:
        if check_win_v2(board, selected_row - 1, selected_column - 1, "X"):
            board_print(board)
            print("Player 1 wins!")
            break
    else:
        if check_win_v2(board, selected_row - 1, selected_column - 1, "O"):
            board_print(board)
            print("Player 2 wins!")
            break
    
    turn = 1 - turn # Player round switch