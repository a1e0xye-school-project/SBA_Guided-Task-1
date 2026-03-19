# Dependencies
try:
    from tabulate import tabulate  # type: ignore
    from termcolor import colored, cprint  # type: ignore
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        "Missing dependency. Please follow instructions from README.md"
    ) from e

# Varaiable
turn = 0
empty_cell_indicator = " "
player_1_indicator = "●"
player_2_indicator = "○"

board = []
num_row_column = 15 # Board Size
for i in range(num_row_column):
    board.append([])
    for r in range(num_row_column):
        board[i].append(empty_cell_indicator)

# Function
## Board Print
def board_print(board):
    headers = [" "]
    for i in range(1, num_row_column + 1):
        headers.append(str(i))

    rows = []
    for i in range(num_row_column):
        row = [str(i + 1)]
        for cell in board[i]:
            row.append(cell)
        rows.append(row)
    print(
        tabulate(
            rows,
            headers=headers,
            tablefmt="rounded_grid",
            stralign="center",
            numalign="center",
        )
    )
    print()

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
    print("\033c", end="") # Clean console (ANSI Escape Codes)
    
    # Player turn Noti
    if turn == 0:
        cprint("Player 1 turn \n", "green", attrs=["bold"])
        print("Your piece is: ", player_1_indicator)
    else:
        cprint("Player 2 turn \n", "red", attrs=["bold"])
        print("Your piece is: ", player_2_indicator)
    board_print(board)

    # Player input & Data validation
    while True:
        while True:
            selected_row = input("Enter the row: ")
            selected_column = input("Enter the column: ")
            if selected_row == '' or selected_column == '':   # Input nothing
                print("Invalid, Please enter agian")
            else:
                selected_column = int(selected_column)
                selected_row = int(selected_row)
                break

        if selected_row > 0 and selected_row <= num_row_column and selected_column > 0 and selected_column <= num_row_column:  # Data validation - within the board size
            if board[selected_row - 1][selected_column - 1] == empty_cell_indicator:   # Data validation - EMPTY CELL 
                if turn == 0:
                    board[selected_row - 1][selected_column - 1] = player_1_indicator
                else:
                    board[selected_row - 1][selected_column - 1] = player_2_indicator
                break  # Exit inner loop - input valid & finish replacing the cell
            else:
                print("This cell is already occupied") # Repeat loop - Input valid & Cell occupied
        else:
            print("Invalid input") # Repeat loop - Input invalid

    # Check win
    if turn == 0:
        if check_win_v2(board, selected_row - 1, selected_column - 1, player_1_indicator):
            print("\033c", end="")
            board_print(board)
            print("Player 1 wins!")
            break    # Exit main loop - Game end
    else:
        if check_win_v2(board, selected_row - 1, selected_column - 1, player_2_indicator):
            print("\033c", end="")
            board_print(board)
            print("Player 2 wins!")
            break    # Exit main loop - Game end
    
    turn = 1 - turn # Player round switch