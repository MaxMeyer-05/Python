import config as config
from ai_modules.game_ai import get_best_move

def play_loop(game, depth):
    """
    General gameplay loop handling turns and terminal display logic.
    Args:
        game: An instance of the game class.
        depth: Search depth for the AI's minimax algorithm.
    """
    print(f"\n--- Starting {type(game).__name__} ---\n") # Using type(game).__name__ because the instance itself doesn't have a __name__ attribute

    game.print_board()
    
    while True:
        # --- Player Turn ---
        try:
            prompt = f"\nYour turn {game.available_moves()}: "
            move = int(input(prompt))
            if not game.make_move(move, config.USER):
                print("Invalid move! Try again.")
                continue
        except (ValueError, IndexError):
            print("Please enter a valid number.")
            continue

        # Check if Player won BEFORE printing the board
        if game.check_winner(config.USER):
            game.print_board()
            print("You won! You outsmarted the machine.")
            break
        
        if game.is_draw():
            game.print_board()
            print("It's a draw!")
            break

        # --- AI Turn ---
        print("AI is calculating...")
        ai_move = get_best_move(game, depth)

        game.make_move(ai_move, config.AI) # 'real_move=True' ensures the move is marked for visual highlighting
        
        # Check if AI won BEFORE printing the board
        if game.check_winner(config.AI):
            game.print_board()
            print("The AI won. Better luck next time!")
            break
            
        game.print_board()
