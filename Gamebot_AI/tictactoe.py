import config

class TicTacToe:
    """
    Logic and rendering for the Tic-Tac-Toe game.
    """
    def __init__(self):
        """
        Initializes an empty board and tracking variables.
        """
        self.board = [" " for _ in range(9)]
        self.last_move = None

    def print_board(self):
        """
        Prints the board with colored highlights for AI moves and winning lines.                
        """
        for i in range(0, 9, 3):
            row_display = []
            for j in range(3):
                idx = i + j
                cell = self.board[idx]
                # If this cell was the last move, wrap it in red tags
                if idx == self.last_move and cell != " ":
                    row_display.append(f"{config.RED}{cell}{config.RESET}")
                else:
                    row_display.append(cell)
            
            print(f" {row_display[0]} | {row_display[1]} | {row_display[2]} ")
            if i < 6: print("---+---+---")

    def available_moves(self):
        """
        Returns a list of indices (0-8) that are currently empty.
        """
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, position, player, real_move=True):
        """
        Places a move and optionally tracks it for visual highlighting.
        Args:
            position: Board index (0-8) where the move is to be placed.
            player: The player symbol (config.USER or config.AI).
            real_move: If True, tracks the move for visual highlighting.
        Returns:
            True if the move was successful, False otherwise.
        """
        if self.board[position] == " ":
            self.board[position] = player
            self.last_move = position # Track the move
            return True
        return False

    def undo_move(self, position):
        """
        Removes a move from the board.
        Used by the AI to simulate games.
        """
        self.board[position] = " "
        self.last_move = None

    def check_winner(self, p):
        """
        Checks if player p has won and stores the winning line.
        Args:
            p: The player symbol to check for a win (config.USER or config.AI).
        Returns:
            True if player p has won, False otherwise.
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
        return " " not in self.board and not self.check_winner(config.USER) and not self.check_winner(config.AI)