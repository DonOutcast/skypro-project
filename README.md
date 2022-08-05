# Simple Tic-Tac-Toe

## Part 1
### Description
Tic-tac-toe is a game known all over the world. Each country may have its own version of the name, sometimes the rules are different, but the essence of the game remains the same. Below are the main rules that may be familiar to you since childhood.

Tic-tac-toe is played by two players on a 3x3 grid. One of the players is 'X', and the other player is 'O'. X plays first, then O takes the next turn, and so on.

The players write 'X' and 'O' on a 3x3 field.

The first player that puts 3 X's or 3 O's in a straight line (including diagonals) wins the game.

### Objectives
Your first task in this project is to print the game grid in the console output. Use what you've learned about the print() function to print three lines, each containing three characters (X's and O's) to represent a game of tic-tac-toe where all fields of the grid have been filled in.

### Example
The example below shows how your output might look:

X O X
O X O
X X O 
 Report a typo

## Part 2 The user is the gamemaster
### Description
Our program should be able to display the grid at all stages of the game. Now we're going to write a program that allows the user to enter a string representing the game state and correctly prints the 3x3 game grid based on this input. We'll also add some boundaries around the game grid.

### Objectives
In this stage, you will write a program that:

Reads a string of 9 symbols from the input and displays them to the user in a 3x3 grid. The grid can contain only X, O and _ symbols.
Outputs a line of dashes --------- above and below the grid, adds a pipe | symbol to the beginning and end of each line of the grid, and adds a space between all characters in the grid.
### Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

- Example 1:

> O_OXXO_XX
---------
| O _ O |
| X X O |
| _ X X |
---------
- Example 2:

> OXO__X_OX
---------
| O X O |
| _ _ X |
| _ O X |
---------
- Example 3:

> _XO__X___
---------
| _ X O |
| _ _ X |
| _ _ _ |
---------

## Part 3 What's up on the field?
### Description
In this stage, we're going to analyze the game state to determine if either player has already won the game or it is still ongoing, if the game is a draw, or if the user has entered an impossible game state (two winners, or with one player having made too many moves).

### Objectives
In this stage, your program should:

Take a string entered by the user and print the game grid as in the previous stage.
Analyze the game state and print the result. Possible states:
Game not finished when neither side has three in a row but the grid still has empty cells.
Draw when no side has a three in a row and the grid has no empty cells.
X wins when the grid has three X's in a row (including diagonals).
O wins when the grid has three O's in a row (including diagonals).
Impossible when the grid has three X's in a row as well as three O's in a row, or there are a lot more X's than O's or vice versa (the difference should be 1 or 0; if the difference is 2 or more, then the game state is impossible).
In this stage, we will assume that either X or O can start the game.

You can choose whether to use a space or underscore _ to print empty cells.

### Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

- Example 1:

> XXXOO__O_
---------
| X X X |
| O O _ |
| _ O _ |
---------
X wins
- Example 2:

> XOXOXOXXO
---------
| X O X |
| O X O |
| X X O |
---------
X wins
- Example 3:

> XOOOXOXXO
---------
| X O O |
| O X O |
| X X O |
---------
O wins
- Example 4:

> XOXOOXXXO
---------
| X O X |
| O O X |
| X X O |
---------
Draw
- Example 5:

> XO_OOX_X_
---------
| X O   |
| O O X |
|   X   |
---------
Game not finished
- Example 6:

> XO_XO_XOX
---------
| X O _ |
| X O _ |
| X O X |
---------
Impossible
- Example 7:

> _O_X__X_X
---------
|   O   |
| X     |
| X   X |
---------
Impossible
- Example 8:

> _OOOO_X_X
---------
|   O O |
| O O   |
| X   X |
---------
Impossible