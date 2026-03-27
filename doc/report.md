# Project Report

By a1e0xye 2026/3-2026/4

> [!NOTE]
> Status: In Progress.

---

## Program logic flow overview
![logicflow](/doc/img/prog-logic-flow.jpg)

---

## Variable/constant declaration and initialization

| Name | Type | Initial value | Notes |
| --- | --- | --- | --- |
| `turn` | variable | 0 [Ln 15]| Recorded which player's turn currently. The value will be 0 or 1, as the represent of player 1 or 2 |
| `empty_cell_indicator` | constant | (Customize value) [Ln 16]| When the cell on the board is empty, the board will show this value as it indicate a empty cell. |
| `player_1_indicator` | constant | (Customize value) [Ln 17] | The indicator for player 1. It will show on the board cell if the player selected the cell. It should be different from player 2. |
| `player_2_indicator` | constant | (Customize value) [Ln 18] | The indicator for player 2. It will show on the board cell if the player selected the cell. It should be different from player 1. 
| `board` | 2D List | Filled with `empty_cell_indicator` [Ln 20-25] | Stored all cell value.
| `num_row_column` | constant | (Customize value) [Ln 21] | The value determine the size of the board (if num_row_column = 15, then the board will have 15 rows and columns). The board size can be easily changed by change the value of this varibale.

### Initialization of 2D array
```python
board = []
num_row_column = 15 # Board Size
for i in range(num_row_column):
    board.append([])
    for r in range(num_row_column):
        board[i].append(empty_cell_indicator)
```

The for-loop add the `empty_cell_indicator` into all cell of the board, with the size of board. It will append row by row, and the value of `num_row_column` determine how many row and column will be added.