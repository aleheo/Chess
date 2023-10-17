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

class ChessFigure:
    def __init__(self):
        self.color = "EMPTY"


class Move:
    def __init__(self, player_move):
        start_row = player_move[0][0]
        start_col = player_move[0][1]
        end_row = player_move[1][0]
        end_col = player_move[1][1]