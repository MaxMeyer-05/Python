AI = 'O'
HUMAN = 'X'

board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
            print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
            if i < 6: print("--+---+--")

def check_winner(b, player):
    win_configs = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(b[s[0]] == b[s[1]] == b[s[2]] == player for s in win_configs)

def is_board_full(b):
    return ' ' not in b

def minimax(b, depth, is_maximizing):
    if check_winner(b, AI):
        return 1
    if check_winner(b, HUMAN):
        return -1
    if is_board_full(b):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if b[i] == ' ':
                b[i] = AI
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if b[i] == ' ':
                b[i] = HUMAN
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score
    
def best_move():
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()
    
    while True:
        human_move = int(input("Enter your move (1-9): ")) - 1
        if board[human_move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[human_move] = HUMAN
        print_board()
        
        if check_winner(board, HUMAN):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        
        ai_move = best_move()
        board[ai_move] = AI
        print("AI's move:")
        print_board()
        
        if check_winner(board, AI):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()