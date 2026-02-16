import math
import config as config

from games.tictactoe import TicTacToe
from games.connect_four import ConnectFour

def minimax(game, depth, alpha, beta, is_maximizing):
    """
    Minimax algorithm with Alpha-Beta pruning to find the best move.
    Args:
        game: An instance of the game class.
        depth: Current depth in the game tree.
        alpha: Best score for maximizing player.
        beta: Best score for minimizing player.
        is_maximizing: Boolean indicating if the current layer is maximizing or minimizing.
    Returns:
        The evaluated score for the current game state.
    """
    # Base cases: return scores for terminal states
    if game.check_winner(config.AI): return 1000 + depth
    if game.check_winner(config.USER): return -1000 - depth
    if game.is_draw() or depth == 0: return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in game.available_moves():
            # simulate move without updating visual highlights
            game.make_move(move, config.AI, real_move=False)
            evaluation = minimax(game, depth - 1, alpha, beta, False)
            game.undo_move(move)
            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha: break
        return max_eval
    else:
        min_eval = math.inf
        for move in game.available_moves():
            game.make_move(move, config.USER, real_move=False)
            evaluation = minimax(game, depth - 1, alpha, beta, True)
            game.undo_move(move)
            min_eval = min(min_eval, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha: break
        return min_eval

def get_best_move(game, depth):
    """
    Iterates through all possible moves and picks the one with the highest score.
    Args:
        game: An instance of the game class.
        depth: Search depth for the minimax algorithm.
    Returns:
        The best move for the AI.
    """
    best_score = -math.inf
    move = None
    for m in game.available_moves():
        game.make_move(m, config.AI, real_move=False)
        score = minimax(game, depth, -math.inf, math.inf, False)
        game.undo_move(m)
        if score > best_score:
            best_score = score
            move = m
    return move