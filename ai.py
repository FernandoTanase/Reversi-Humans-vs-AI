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
    def max_value(board, player, depth):
        # Base cases
        if depth == 0:  # Reached maximum depth
            return utility(board, player)
        
        valid_moves = []
        for row in range(len(board)):
            for col in range(len(board)):
                if is_valid_move(row, col, board, player):
                    valid_moves.append((row, col))
        
        if not valid_moves:  # No valid moves left
            return utility(board, player)
            
        max_score = float('-inf')
        for row, col in valid_moves:
            # Create a copy of the board
            new_board = [row[:] for row in board]
            new_board[row][col] = player
            change_pieces(row, col, new_board, player)
            
            # Recursive call with opponent's turn and decreased depth
            opponent = "white" if player == "black" else "black"
            score = min_value(new_board, opponent, depth - 1)
            max_score = max(max_score, score)
        
        return max_score

    def min_value(board, player, depth):
        # Base cases
        if depth == 0:
            return utility(board, original_player)  # Evaluate from original player's perspective
            
        valid_moves = []
        for row in range(len(board)):
            for col in range(len(board)):
                if is_valid_move(row, col, board, player):
                    valid_moves.append((row, col))
        
        if not valid_moves:
            return utility(board, original_player)
            
        min_score = float('inf')
        for row, col in valid_moves:
            new_board = [row[:] for row in board]
            new_board[row][col] = player
            change_pieces(row, col, new_board, player)
            
            opponent = "white" if player == "black" else "black"
            score = max_value(new_board, opponent, depth - 1)
            min_score = min(min_score, score)
            
        return min_score

    # Start of minimax_ai function
    original_player = player
    best_score = float('-inf')
    best_move = None
    
    # Find all valid moves
    valid_moves = []
    for row in range(len(board)):
        for col in range(len(board)):
            if is_valid_move(row, col, board, player):
                valid_moves.append((row, col))
    
    # Try each move and find the best one
    for row, col in valid_moves:
        new_board = [row[:] for row in board]
        new_board[row][col] = player
        change_pieces(row, col, new_board, player)
        
        opponent = "white" if player == "black" else "black"
        score = min_value(new_board, opponent, depth - 1)
        
        if score > best_score:
            best_score = score
            best_move = (row, col)
    
    return best_move

def alpha_beta_ai(board, player, depth):
    # Your code here
    pass