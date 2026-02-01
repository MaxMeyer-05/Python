import config

from difflib import get_close_matches
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
            if not game.make_move(move, config.USER):
                print("Invalid move! Try again.")
                continue
        except (ValueError, IndexError):
            print("Please enter a valid number from the options.")
            continue

        if game.check_winner(config.USER):
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
        game.make_move(ai_move, config.AI)
        game.print_board()

        if game.check_winner(config.AI):
            print("The AI won. Better luck next time!")
            break

def main():
    """
    Main menu to select the game and start the loop.
    """
    print("\n\n--- Universal AI Interface ---")
    print("Available: Tic Tac Toe, Connect Four, Math Solver")
    
    apps = {
        "tic tac toe": lambda: play_loop(TicTacToe(), 9),
        "connect four": lambda: play_loop(ConnectFour(), 5)
    }

    user_choice = input("\nWhat's on your mind? \n\n").lower()
    
    # Fuzzy matching for robustness
    matches = get_close_matches(user_choice, list(apps.keys()), n=1, cutoff=0.4)

    if matches:
        selected_app = matches[0]
        print(f"--- Launching {selected_app.upper()} ---")
        apps[selected_app]()
    else:
        print("Sorry, I don't know how to do that yet.")

if __name__ == "__main__":
    main()