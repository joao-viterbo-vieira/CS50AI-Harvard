"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X= sum(row.count(X) for row in board)
    count_O= sum(row.count(O) for row in board)
    
    if count_X == count_O:
        return X
    else:
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    plays = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                plays.add((i, j))
    
    return plays
            
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    player_turn = player(board)
    
    new = [row[:] for row in board]
    new[i][j] = player_turn 
    
    return new
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRows (board, X) or checkColumns (board, X) or checkDiagonals(board,X):
        return X

    elif checkRows (board, O) or checkColumns (board, O) or checkDiagonals(board,O) :
        return O

    else:
        return None
    
def checkRows(board, player):

    for row in board:
        if all(cell == player for cell in row):
            return True
    return False

def checkColumns(board, player):

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    return False

def checkDiagonals(board, player):

    if all(board[i][i] == player for i in range(3)):
        return True
    

    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def tie(board):
    for row in board:
        if EMPTY in row:
            return False
    
    # If there are no empty cells left, and there's no winner, it's a tie
    if winner(board) is None:
        return True
    
    return False

    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or tie(board):
        return True
    
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    player1 = player(board)

    if player1 == X:
        
        best_score = -math.inf
        best_action = None
        
        for action in actions(board):
            
            result_board = result(board, action)
            score = min_value(result_board)
            
            if score > best_score:
                best_score = score
                best_action = action
                
    else:
        best_score = math.inf
        best_action = None
        
        for action in actions(board):
            
            result_board = result(board, action)
            score = max_value(result_board)
            
            
            if score < best_score:
                best_score = score
                best_action = action

    return best_action

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v