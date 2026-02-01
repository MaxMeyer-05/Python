class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6: print("--+---+--")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, position, player):
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False

    def check_winner(self, player):
        win_configs = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        return any(self.board[s[0]] == self.board[s[1]] == self.board[s[2]] == player for s in win_configs)

    def is_draw(self):
        return " " not in self.board and not self.check_winner("X") and not self.check_winner("O")