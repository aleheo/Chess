'''
this is a description of this project and bla-bla-bla...
'''


class GameCondition:
    def __init__(self):
        self.board = [
            ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']
        ]
        self.move_variations = {'p': self.getPawnMoves, 'r': self.getRookMoves, 'n': self.getKnightMoves,
                               'b': self.getBishopMoves, 'q': self.getQueenMoves, 'k': self.getKingMoves}
        self.white_to_move = True
        self.move_history = []

    def makeMove(self, move):
        """

        :param move:
        :return: None
        """
        self.board[move.start_row][move.start_col] = None
        self.board[move.end_row][move.end_col] = move.start_square
        self.move_history.append(move)
        self.white_to_move = not self.white_to_move

    def undoMove(self):
        if len(self.move_history) != 0:
            move = self.move_history.pop()
            self.board[move.start_row][move.start_col] = move.start_square
            self.board[move.end_row][move.end_col] = move.end_square


    def getAcceptableMove(self):
        return self.getAllPossibleMoves()

    def getAllPossibleMoves(self):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                turn = self.board[row][col][0]
                if (turn == 'w' and self.white_to_move) or (turn == 'b' and not self.white_to_move):
                    piece = self.board[row][col][1]
                    self.move_variations[piece](row, col, moves)

        return moves

    def getPawnMoves(self, row, col, moves):
        if self.white_to_move:
            if self.board[row - 1][col] is None:
                moves.append(Move((row, col), (row - 1, col), self.board))
                if row == 6 and self.board[row - 2][col] is None:
                    moves.append(Move((row, col), (row - 2, col), self.board))
            if col - 1 >= 0:
                if self.board[row - 1][col - 1][0] == 'b':
                    moves.append(Move((row, col), (row - 1, col - 1), self.board))
            if col + 1 <= 7:
                if self.board[row - 1][col + 1][0] == 'b':
                    moves.append(Move((row, col), (row - 1, col + 1), self.board))

        else:
            pass

    def getRookMoves(self, row, col, moves):
        pass

    def getKnightMoves(self, row, col, moves):
        pass

    def getBishopMoves(self, row, col, moves):
        pass

    def getQueenMoves(self, row, col, moves):
        pass

    def getKingMoves(self, row, col, moves):
        pass


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
        self.moveID = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col
        print(self.moveID)

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getNotation(self, start_move, end_move):
        """

        :param start_move:
        :param end_move:
        :return:
        """
        move = self.getSquare(start_move[0], start_move[1]) + self.getSquare(end_move[0], end_move[1])
        return move

    def getSquare(self, row, col):
        """

        :param row:
        :param col:
        :return:
        """
        square = self.col_to_board[col] + self.row_to_board[row]
        return square

    # def hasPiece(self):
    #     """
    #
    #     :return:
    #     """
    #     return self.start_square is not None
