from tictactoe import TicTacToe
from ai import get_ai_move

def play():
    game = TicTacToe()
    print("Willkommen bei Tic Tac Toe gegen die KI!")
    game.print_board()

    while True:
        user_move = int(input("Wähle ein Feld (0-8): "))
        if not game.make_move(user_move, "X"):
            print("Ungültiger Zug!")
            continue
        
        if game.check_winner("X"):
            game.print_board()
            print("Du hast gewonnen! (Unmöglich...)")
            break

        if game.is_draw():
            print("Unentschieden!")
            break

        print("\nKI überlegt...")
        ai_move = get_ai_move(game)
        game.make_move(ai_move, "O")
        game.print_board()

        if game.check_winner("O"):
            print("Die KI hat gewonnen!")
            break

if __name__ == "__main__":
    play()