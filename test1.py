def draw_board(board):
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("     |     |")


def get_move(player, board):
    while True:
        move = input(f"Player {player}, enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == " ":
            return int(move)-1
        else:
            print("Invalid move. Try again.")


def check_win(board):
    win_patterns = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != " ":
            return board[pattern[0]]
    return None


def play_game():
    board = [" "] * 9
    player = "X"
    draw_board(board)
    while True:
        move = get_move(player, board)
        board[move] = player
        draw_board(board)
        winner = check_win(board)
        if winner:
            print(f)
