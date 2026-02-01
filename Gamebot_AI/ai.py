import math

def minimax(game, is_maximizing):
    if game.check_winner("O"): return 1
    if game.check_winner("X"): return -1
    if game.is_draw(): return 0

    if is_maximizing:
        best_score = -math.inf
        for move in game.available_moves():
            game.board[move] = "O"
            score = minimax(game, False)
            game.board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in game.available_moves():
            game.board[move] = "X"
            score = minimax(game, True)
            game.board[move] = " "
            best_score = min(score, best_score)
        return best_score

def get_ai_move(game):
    best_score = -math.inf
    move = None
    for i in game.available_moves():
        game.board[i] = "O"
        score = minimax(game, False)
        game.board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    return move