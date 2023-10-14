'''
this is a description of this project and bla-bla-bla...
'''

class GameCondition:
    def __init__(self):
        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['..', '..', '..', '..', '..', '..', '..', '..'],
            ['..', '..', '..', '..', '..', '..', '..', '..'],
            ['..', '..', '..', '..', '..', '..', '..', '..'],
            ['..', '..', '..', '..', '..', '..', '..', '..'],
            ['pp', 'pp', 'pp', 'pp', 'pp', 'pp', 'pp', 'pp'],
            ['pR', 'pN', 'pB', 'pQ', 'pK', 'pB', 'pN', 'pR']
        ]

        self.whiteToMove = True

class ChessFigure():
    def __init__(self):
        self.color = "EMPTY"


