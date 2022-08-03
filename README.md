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