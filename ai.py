import random
def is_valid_move(row, col, board, player):
    if board[row][col] is not None:
        return False

    opponent = "black" if player == "white" else "white"
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for d_row, d_col in directions:
        r, c = row + d_row, col + d_col
        if not (0 <= r < len(board) and 0 <= c < len(board)) or board[r][c] != opponent:
            continue

        r += d_row
        c += d_col
        while 0 <= r < len(board) and 0 <= c < len(board):
            if board[r][c] is None:
                break
            if board[r][c] == player:
                return True
            r += d_row
            c += d_col

    return False


def change_pieces(row, col, board, player):
    opponent = "black" if player == "white" else "white"
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for d_row, d_col in directions:
        r, c = row + d_row, col + d_col
        if not (0 <= r < len(board) and 0 <= c < len(board)) or board[r][c] != opponent:
            continue

        r += d_row
        c += d_col
        while 0 <= r < len(board) and 0 <= c < len(board):
            if board[r][c] is None:
                break
            if board[r][c] == player:
                r, c = row + d_row, col + d_col
                while board[r][c] == opponent:
                    board[r][c] = player
                    r += d_row
                    c += d_col
                break
            r += d_row
            c += d_col




def random_ai(board, player):
    valid_moves = []
    for row in range(len(board)):
        for col in range(len(board)):
            if is_valid_move(row, col, board, player):
                valid_moves.append((row, col))

    if not valid_moves:
        return None

    return random.choice(valid_moves)

def utility(board, player):
    """
    Evaluate the board position for the given player.
    Returns a numeric score where higher is better for the player.
    """
    opponent = "white" if player == "black" else "black"
    
    # Count pieces
    player_count = sum(row.count(player) for row in board)
    opponent_count = sum(row.count(opponent) for row in board)
    
    # Corner control (corners are valuable)
    corners = [(0,0), (0,7), (7,0), (7,7)]
    player_corners = sum(1 for r,c in corners if board[r][c] == player)
    opponent_corners = sum(1 for r,c in corners if board[r][c] == opponent)
    
    # Mobility (number of valid moves)
    player_moves = sum(1 for r in range(8) for c in range(8) 
                      if is_valid_move(r, c, board, player))
    opponent_moves = sum(1 for r in range(8) for c in range(8) 
                        if is_valid_move(r, c, board, opponent))
    
    # Calculate weighted score
    score = (player_count - opponent_count) * 1.0 + \
            (player_corners - opponent_corners) * 25.0 + \
            (player_moves - opponent_moves) * 5.0
            
    return score

def greedy_ai(board, player):
    valid_moves = []
    for row in range(len(board)):
        for col in range(len(board)):
            if is_valid_move(row, col, board, player):
                score = utility(board, player)
                valid_moves.append((row, col, score))
    return max(valid_moves, key=lambda x: x[2])[:2]

def minimax_ai(board, player, depth):
    # Your code here
    pass

def alpha_beta_ai(board, player, depth):
    # Your code here
    pass