from tictactoe import TicTacToe
from connectFour import ConnectFour
from ai import get_best_move

def play_loop(game, depth):
    """
    The main gameplay loop for any game object passed into it.
    game: an instance of TicTacToe or ConnectFour.
    depth: how many moves ahead the AI should consider.
    """
    print("\nGame started!")
    game.print_board()
    
    while True:
        # User input handling
        try:
            move = int(input(f"\nYour turn {game.available_moves()}: "))
            if not game.make_move(move, "X"):
                print("Invalid move! Try again.")
                continue
        except (ValueError, IndexError):
            print("Please enter a valid number from the options.")
            continue

        if game.check_winner("X"):
            game.print_board()
            print("You won! You outsmarted the machine.")
            break
        
        if game.is_draw():
            game.print_board()
            print("It's a draw!")
            break

        # AI Turn
        print("AI is calculating...")
        ai_move = get_best_move(game, depth)
        game.make_move(ai_move, "O")
        game.print_board()

        if game.check_winner("O"):
            print("The AI won. Better luck next time!")
            break

def main():
    """
    Main menu to select the game and start the loop.
    """
    print("--- Python AI Games Collection ---")
    print("1: Tic Tac Toe (Solved game)")
    print("2: Connect Four (Strategic game)")
    choice = input("Select a game (1/2): ")

    if choice == "1":
        # Tic Tac Toe is small enough to calculate the full tree (9 moves)
        play_loop(TicTacToe(), 9)
    elif choice == "2":
        # Search depth 5 provides a strong opponent without long wait times
        play_loop(ConnectFour(), 5)
    else:
        print("Invalid choice. Please restart.")

if __name__ == "__main__":
    main()