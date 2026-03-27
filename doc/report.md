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

---

## External Library 

Library can help us archive specific function, it can (make the code easy simple, strc more clear). Library can be easily install to computer by `pip install`, and `import` to the code. 

In this project, the following library is used.

### tabulate
> https://github.com/astanin/python-tabulate

`tabulate` is a python3 library that help output a formatted tabular data, provide a clear table. In this project, we make the game baord into a 2D array, by using this library, we can print the data in the 2D array in a clear way. 

Following function provided by the library is used
| Function Name | Used line |
| --- | --- |
| tabulate | Ln 41 |

#### `tabulate()`

This function takes a list of lists or another tabular data type as the first argument, and outputs a nicely formatted plain-text table.

It can be used by `tabulate(table,headers,tablefmt,stralign,numalign)`.

The table format can be customize by changing the value in `tablefmt`,`stralign`, `numalign`.


### termcolor
> https://github.com/termcolor/termcolor

`termcolor` can help us output in terminal with color, instead of plain text with no color. It will defintely enhance the user experience compared to original, especially for terminals in white & black.

Following function provided by the library is used
| Function Name | Used Line |
| --- | --- |
| cprint | Ln 94,95,97,98,106,116,127,129,136,142,149 |


#### `cprint()`

This function output the message with text colors, text highlights.

It can be used by `cprint(message,textcolors,texthighlights)`

Example: `cprint("Hello, World!", "green", "on_red")`

---

If the library is imported unsuccessfully, the program will occur a (run-time error). So at the start of the code, a `try-except` is used. 

```python
try:
    from tabulate import tabulate
    from termcolor import colored, cprint
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        "Missing dependency. Please follow instructions from README.md"
    ) from e
```

The `try` block lets us test a block of code for errors. When there is error, the `except` block lets us handle the error. In this project, this help us to show a notice message to user when the program unsuccessfully import library.

---