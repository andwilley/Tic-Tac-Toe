from string import ascii_lowercase
# Tic Tac Toe

# Convert user input to board indexes.
STRING_TO_ROW = {
    'a': 0,
    'b': 1,
    'c': 2,
}
STRING_TO_COL = {
    '1': 0,
    '2': 1,
    '3': 2,
}

# Create a 3x3 list of blank spaces.
def new_board(dim):
    return [[None]*dim for _ in range(dim)]

# Print the current board to the terminal.
def print_board(board):
    print(("\n" + f"{'+'.join(['-'] * len(board))}" + "\n").join(map(
        lambda row: "|".join(map(
            lambda x: " " if not x else x,
            row)),
        board)))

def get_player_from_turn(turn):
    return 'X' if turn % 2 == 0 else 'O'

def parse_move(cli_input):
    cli_input = cli_input.strip()
    if len(cli_input) != 2 or cli_input[0] not in STRING_TO_ROW or cli_input[1] not in STRING_TO_COL:
        raise IOError("fuck off")
    return STRING_TO_ROW[cli_input[0]], STRING_TO_COL[cli_input[1]]

# Make sure the space is not already taken.
def square_is_open(move, board):
    return not board[move[0]][move[1]]

def update_board(board, move, player):
    board[move[0]][move[1]] = player
    return board

def check_rows(board):
    for row in board:
        if row[0] and len(set(row)) == 1:
            print('row', row[0])
            return row[0]
    return None

def check_diagonals(board):
    left_to_right_vals = set()
    right_to_left_vals = set()
    for col, row in enumerate(board):
        left_to_right_vals.add(row[col])
        right_to_left_vals.add(row[len(row) - 1 - col])
    if board[0][0] and len(left_to_right_vals) == 1:
        return left_to_right_vals.pop()
    if board[0][-1] and len(right_to_left_vals) == 1:
        return right_to_left_vals.pop()
    return None

# Assumes a square board.
def get_winner(board):
    # Check the rows for a winner.
    maybe_winner = check_rows(board)
    if maybe_winner:
        return maybe_winner
    # Check the columns for a winner.
    transposed_board = map(list, zip(*board))
    maybe_winner = check_rows(transposed_board)
    if maybe_winner:
        return maybe_winner
    # Check the diagonals for a winner.
    return check_diagonals(board)

# Get a valid move recursively.
def get_valid_move(player, board):
    print(f"{player}'s turn!")
    cli_input = input("Enter your move: ")
    print()
    move = None
    try:
        move = parse_move(cli_input)
    except:
        print("That's not a space on this board, try again!")
        return get_valid_move(player, board)

    if square_is_open(move, board):
        return move
    else:
        print("That space is already taken, try again!")
        return get_valid_move(player, board)

# Main loop.
def run():
    turn = 0
    winner = None
    board = new_board(5)
    player = 'X'

    print('Welcome to Tic Tac Toe!')
    print("Enter a1 - c3 to choose a space (a1 = top left corner)")
    print()

    print_board(board)

    while not winner and turn < 9:
        print()
        player = get_player_from_turn(turn)
        move = get_valid_move(player, board)
        board = update_board(board, move, player)
        print_board(board)
        winner = get_winner(board)
        turn += 1

    if winner:
        print()
        print(f'Player {winner} wins! Game over!')
    else:
        print()
        print("Cat's game! Game Over!")

if __name__ == "__main__":
    run()
