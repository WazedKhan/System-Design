class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = 1

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == " "

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = "X" if self.current_player == 1 else "O"
            # switch player
            self.current_player = 1 if self.current_player == 2 else 2
            return True
        return False

    def check_winner(self):
        for i in range(3):
            # check row wise wins
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            # check column wise wins
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        # check diagonal wins
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        # check diagonal wins
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False


# Main game loop
if __name__ == "__main__":
    game = TicTacToe()

    while not game.is_board_full() and not game.check_winner():
        game.print_board()
        try:
            row, col = map(int, input("Enter row and col: ").split())
        except ValueError:
            print("Invalid input! Please enter two integers with space in between ex: 0 1")
            continue
        if game.make_move(row, col):
            if game.check_winner():
                print("Player", game.current_player, "wins!")
                break
        else:
            print("Invalid move!")
