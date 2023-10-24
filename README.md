# Unbeatable Tic-Tac-Toe Bot

This is a simple implementation of the classic Tic-Tac-Toe game in Python.

## Algorithms

In a standard minimax algorithm, all possible moves are explored to the terminal game state. For Tic-Tac-Toe, this would mean exploring all possible combinations, resulting in a branching factor of 9! (9 factorial), which is 362,880 combinations. However, by implementing the alpha-beta pruning technique, the algorithm intelligently prunes branches that do not affect the final decision. This significantly reduces the number of nodes that need to be evaluated, making the algorithm more efficient, especially for games with large state spaces like Tic-Tac-Toe. As a result, the algorithm can still guarantee the optimal outcome without having to explore all 9! combinations, making it an unbeatable Tic-Tac-Toe bot.

Lets take an example : Imagine a current state of tic-tac-toe have two possiblities Win or Draw, So by using alpha-beta pruning technique if one possibilities of the current state is win it won't check other possibilities for same state.

## Game Description

Tic-Tac-Toe is a two-player game where each player takes turns marking a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. If the grid is filled without any player achieving a winning pattern, the game is considered a draw.

## Requirements

- Python 3.x

## How to Run the Game

1. Make sure you have Python 3.x installed.
2. Clone the repository or download the script.
3. Run the script using a Python interpreter.

## Game Instructions

- Players can choose whether they want to start first or not.
- The game will display the board and prompt players for their moves.
- Players need to enter the coordinates for their moves in the format "row column".

## Credits

The game logic and code structure were implemented with the help of various online resources and tutorials.

## Contribution

Feel free to contribute and modify the code. Have fun playing!

