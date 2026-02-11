from Games import config

class ConnectFour:
    """
    Logic and rendering for the Connect Four game.
    """
    def __init__(self):
        """
        Initializes an empty board and tracking variables.
        """
        self.rows, self.cols = 6, 7
        self.board = [[" " for _ in range(self.cols)] for _ in range(self.rows)]
        self.last_move = None

    def print_board(self):
        """
        Renders the grid with color support for highlights.
        """
        for r in range(self.rows):
            row_str = "|"
            for c in range(self.cols):
                cell = self.board[r][c]
                if self.last_move == (r, c) and cell != " ":
                    row_str += f" {config.RED}{cell}{config.RESET} |"
                else:
                    row_str += f" {cell} |"
            print(row_str)
        print("-" * 29)
        print("  " + "   ".join(map(str, range(self.cols))))

    def available_moves(self):
        """
        Returns a list of columns that are not yet full.
        """
        return [c for c in range(self.cols) if self.board[0][c] == " "]

    def make_move(self, col, player, real_move=True):
        """
        Places a move in the specified column.
        Args:
            col: Column index where the piece is to be placed.
            player: The player symbol (config.USER or config.AI).
            real_move: If True, tracks the move for visual highlighting.
        Returns:
            True if the move was successful, False otherwise.
        """
        if col < 0 or col >= self.cols or self.board[0][col] != " ":
            return False
        for r in range(self.rows - 1, -1, -1):
            if self.board[r][col] == " ":
                self.board[r][col] = player
                self.last_move = (r, col) # Store row and column
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
                self.last_move = None
                break

    def check_winner(self, p):
        """
        Searches for 4 in a row and saves coordinates to winning_line.
        Args:
            p: The player symbol to check for a win (config.USER or config.AI).
        Returns:
            True if player p has won, False otherwise.
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
        return not self.available_moves() and not self.check_winner(config.USER) and not self.check_winner(config.AI)