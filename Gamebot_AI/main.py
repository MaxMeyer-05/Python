import config

from difflib import get_close_matches
from tictactoe import TicTacToe
from connectFour import ConnectFour
from ai import get_best_move

def play_loop(game, depth):
    """
    General gameplay loop handling turns and terminal display logic.
    Args:
        game: An instance of the game class.
        depth: Search depth for the AI's minimax algorithm.
    """
    print("\nGame started!")
    game.print_board()
    
    while True:
        # User Turn
        try:
            prompt = f"\nYour turn {game.available_moves()}: "
            move = int(input(prompt))
            if not game.make_move(move, config.USER):
                print("Invalid move! Try again.")
                continue
        except (ValueError, IndexError):
            print("Please enter a valid number.")
            continue

        # Check user win BEFORE printing
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
        
        # Check AI win BEFORE printing
        if game.check_winner(config.AI):
            game.print_board()
            print("The AI won. Better luck next time!")
            break
            
        game.print_board()

def main():
    """
    Entry point with fuzzy matching for game selection.
    """
    print("\n--- Universal AI Interface ---")
    print("Available games: Tic Tac Toe, Connect Four")
    
    apps = {
        "tic tac toe": lambda: play_loop(TicTacToe(), 9),
        "connect four": lambda: play_loop(ConnectFour(), 5)
    }

    user_choice = input("\nWhat would you like to play?\n\n").lower()
    matches = get_close_matches(user_choice, list(apps.keys()), n=1, cutoff=0.4)

    if matches:
        selected = matches[0]
        print(f"--- Launching {selected.upper()} ---")
        apps[selected]()
    else:
        print("Sorry, game not recognized.")

if __name__ == "__main__":
    main()