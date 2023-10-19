'''
this is a description of this project and bla-bla-bla...
'''

class GameCondition:
    def __init__(self):
        self.board = [
            ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']
        ]
        self.whiteToMove = True
        self.move_history = []

    def makeMove(self, move):
        self.board[move.start_row][move.start_col] = None
        self.board[move.end_row][move.end_col] = move.start_square
        self.whiteToMove = not self.whiteToMove


class Move:
    board_to_row = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    row_to_board = {value: key for key, value in board_to_row.items()}
    board_to_col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    col_to_board = {value: key for key, value in board_to_col.items()}

    def __init__(self, start_move, end_move, board):
        self.start_row = start_move[0]
        self.start_col = start_move[1]
        self.end_row = end_move[0]
        self.end_col = end_move[1]
        self.start_square = board[self.start_row][self.start_col]
        self.end_square = board[self.end_row][self.end_col]

    def getNotation(self, start_move, end_move):
        move = self.getSquare(start_move[0], start_move[1]) + self.getSquare(end_move[0], end_move[1])
        return move

    def getSquare(self, row, col):
        square = self.col_to_board[col] + self.row_to_board[row]
        return square

    def hasPiece(self):
        return self.start_square is not None
