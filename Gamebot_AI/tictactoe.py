class TicTacToe:
    """
    Represents a Tic-Tac-Toe game on a 3x3 grid.
    The board is represented as a 1D list of 9 strings.
    """
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.rows, self.cols = 3, 3 # Required for AI compatibility

    def print_board(self):
        """
        Displays the current state of the board to the console.
        """
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6: print("---+---+---")

    def available_moves(self):
        """
        Returns a list of indices (0-8) that are currently empty.
        """
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, position, player):
        """
        Places a player's symbol on the board.
        Returns True if successful, False if the spot was taken.
        """
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False

    def undo_move(self, position):
        """
        Removes a move from the board.
        Used by the AI to simulate games.
        """
        self.board[position] = " "

    def check_winner(self, p):
        """
        Checks if the given player (p) has 3 in a row.
        Includes horizontal, vertical, and diagonal checks.
        """
        win_configs = [
            (0,1,2), (3,4,5), (6,7,8), # Rows
            (0,3,6), (1,4,7), (2,5,8), # Columns
            (0,4,8), (2,4,6)           # Diagonals
        ]
        return any(all(self.board[i] == p for i in config) for config in win_configs)

    def is_draw(self):
        """
        Returns True if the board is full and no one has won.
        """
        return " " not in self.board and not self.check_winner("X") and not self.check_winner("O")