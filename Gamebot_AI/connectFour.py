class ConnectFour:
    """
    Represents a Connect Four game on a 6x7 grid.
    Uses a 2D list to represent rows and columns.
    """
    def __init__(self):
        self.rows, self.cols = 6, 7
        self.board = [[" " for _ in range(self.cols)] for _ in range(self.rows)]

    def print_board(self):
        """
        Prints the grid with column indices at the bottom.
        Displays the current state of the board to the console.
        """
        for row in self.board:
            print("| " + " | ".join(row) + " |")
        print("-" * 29)
        print("  " + "   ".join(map(str, range(self.cols))))

    def available_moves(self):
        """
        Returns a list of columns that are not yet full.
        """
        return [c for c in range(self.cols) if self.board[0][c] == " "]

    def make_move(self, col, player):
        """
        Places the piece in the lowest available row of a column.
        Returns True if successful, False if the column is full.
        """
        if col < 0 or col >= self.cols or self.board[0][col] != " ":
            return False
        for r in range(self.rows - 1, -1, -1):
            if self.board[r][col] == " ":
                self.board[r][col] = player
                return True
        return False

    def undo_move(self, col):
        """
        Removes the top-most piece from the specified column.
        Used by the AI to simulate games.
        """
        for r in range(self.rows):
            if self.board[r][col] != " ":
                self.board[r][col] = " "
                break

    def check_winner(self, p):
        """
        Checks for 4 connected pieces of player 'p' in all directions.
        """
        # Horizontal
        for r in range(self.rows):
            for c in range(self.cols - 3):
                if all(self.board[r][c+i] == p for i in range(4)): return True
        # Vertical
        for r in range(self.rows - 3):
            for c in range(self.cols):
                if all(self.board[r+i][c] == p for i in range(4)): return True
        # Diagonal (standard and mirrored)
        for r in range(self.rows - 3):
            for c in range(self.cols - 3):
                if all(self.board[r+i][c+i] == p for i in range(4)): return True
                if all(self.board[r+3-i][c+i] == p for i in range(4)): return True
        return False

    def is_draw(self):
        """
        Checks if there are no moves left and no winner.
        """
        return not self.available_moves() and not self.check_winner("X") and not self.check_winner("O")