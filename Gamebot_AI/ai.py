import math

def minimax(game, depth, alpha, beta, is_maximizing):
    """
    Core AI algorithm. 
    depth: how many moves to look ahead.
    alpha/beta: bounds for pruning to speed up calculation.
    is_maximizing: True if it's the AI's turn to maximize score.
    """
    # Base cases: Check for terminal states (win/loss/draw)
    if game.check_winner("O"): return 1000 + depth
    if game.check_winner("X"): return -1000 - depth
    if game.is_draw() or depth == 0: return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in game.available_moves():
            game.make_move(move, "O")
            evaluation = minimax(game, depth - 1, alpha, beta, False)
            game.undo_move(move) # Backtrack
            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha: break # Prune the branch
        return max_eval
    else:
        min_eval = math.inf
        for move in game.available_moves():
            game.make_move(move, "X")
            evaluation = minimax(game, depth - 1, alpha, beta, True)
            game.undo_move(move) # Backtrack
            min_eval = min(min_eval, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha: break # Prune the branch
        return min_eval

def get_best_move(game, depth):
    """
    Iterates through all possible moves and picks the one with the highest minimax score.
    game: an instance of TicTacToe or ConnectFour.
    depth: how many moves ahead the AI should consider.
    """
    best_score = -math.inf
    move = None
    for m in game.available_moves():
        game.make_move(m, "O")
        score = minimax(game, depth, -math.inf, math.inf, False)
        game.undo_move(m)
        if score > best_score:
            best_score = score
            move = m
    return move