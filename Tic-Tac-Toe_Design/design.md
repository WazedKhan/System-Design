# Low Level Design of Tic Tac Toe | System Design

Soruce: [GeeksforGeeks](https://www.geeksforgeeks.org/low-level-design-of-tic-tac-toe-system-design/?utm_source=mailer&utm_medium=marketing&utm_campaign=system_design)

In classic games, few are as universally recognized and enjoyed as Tic Tac Toe. Despite its apparent simplicity, this game engages players of all ages in a battle of wits and strategy. In this article, we delve into the intricacies of designing a low-level structure for Tic Tac Toe that captures the essence of the game and highlights the underlying complexities.

### Important Topics for Low Level Design of Tic Tac Toe

- The Essence of Tic Tac Toe
- Rules of the game
- Representing the Game Board
- Player Turns and Moves
- Validating Moves
- Determining the Winner
- Tying It All Together
- Complete Tic Tac Toe implementation
- Conclusion

### The Essence of Tic Tac Toe

Tic Tac Toe, known colloquially as "Xs and Os," is a two-player game typically played on a 3x3 grid. The objective is simple: be the first to form a horizontal, vertical, or diagonal line of three of your marks (either "X" or "O"). The elegance of the game lies in its deceptive complexity, while the rules are straightforward, devising an unbeatable strategy demands a keen understanding of the game's dynamics.

### Rules of the game

Firstly let's understand the rules of the game:

- Setup: The game is played on a 3 * 3 grid. One player uses 'X' another player uses 'O' and each player takes turns making their moves.
- Winner: The game is won by the player placing his or her symbol in a row, column, or diagonal. The first player to get three symbols in a row wins the game. When the player reaches this, the game ends immediately.
- Draw: If all the grid cells are filled and no player has three symbols in a row, the game will be a tie or a draw.
- Illegal Moves: A player cannot place his or her symbol on a tile occupied by an opponent's symbol or their own symbol. The move must be made to an empty cell.

### Representing the Game Board

At the heart of every game lies the game board. In our low-level design for Tic Tac Toe, we choose a 2D array or matrix to represent the board. Each cell of the array can take three possible values: empty, "X," or "O." This array forms the canvas upon which players will make their moves.
`board = [[' ' for i in range(3)] for j in range(3)]`

### Player Turns and Moves

In any game, managing player turns is crucial. We can represent the players using simple integers – player 1 and player 2. Their moves are translated to row and column indices on the game board.

```python
current_player = 1
row = 1
column = 2board[row][column] = "X" if current_player == 1 else "O"
```

### Validating Moves

Ensuring that players adhere to the rules is paramount. The low-level design includes a move validation process, verifying that the chosen cell is empty and within the bounds of the board.

```python
def is_valid_move(row, column):
    return 0 <= row <= 3 and 0 <= column <=3 and board[row][column] == ' '
```

###### example usage of is_valid_move

```python
if is_valid_move(1, 2):
    # perform move
else:
    print("Invalid move. Please choose an empty cell within the board.")
```

### Determining the Winner

The climax of any Tic Tac Toe game is the declaration of a winner. Our low-level design accommodates a function to check for victory conditions after each move.

```python
def check_winner(player):
    # Check rows, columns, and diagonals for three marks in a row
    # Return True if the player wins, False otherwise
```

###### Example usage

```python
if check_winner(1):
    print("Player 1 wins!")
elif check_winner(2):
    print("Player 2 wins!")
```
