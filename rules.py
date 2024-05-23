'''
This is a file that contains the rules for playing chess.
'''

class GameCondition:
    '''
    This class represents the game condition of a chess game. It contains the chess board, move functions, and other game-related information.
    '''
    def __init__(self):
        '''
        Initialize the GameCondition object with the initial chess board setup.

        Returns:
        None
        '''
        self.board = [
            ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']]
        
        self.moveFunctions = {'p': self.getPawnMoves, 'r': self.getRookMoves, 'n': self.getKnightMoves, 'b': self.getBishopMoves, 'q': self.getQueenMoves, 'k': self.getKingMoves}
        self.whiteToMove = True
        self.moveHistory = []
        self.whiteKingPosition = (7, 4)
        self.blackKingPosition = (0, 4)
        self.checkMate = False
        self.staleMate = False
       
    def makeMove(self, move):
        '''
        Method to make a move on the chess board.

        Parameters:
        move (Move): An instance of the Move class representing the move to be made.

        Returns:
        None. The chess board is updated with the new move.

        Raises:
        IndexError: If when moving a pawn a new piece is not selected or the new piece is indicated incorrectly.

        Postconditions:
        - The piece at the start position of the move is removed from the board.
        - The piece at the end position of the move is placed on the board.
        - The move is added to the move history.
        - The 'whiteToMove' flag is updated based on whose turn it is.
        - If the move is a pawn promotion, the user is prompted to choose a new piece for the pawn.
        '''
        self.board[move.startRow][move.startCol] = '--'
        self.board[move.endRow][move.endCol] = move.startSquare
        self.moveHistory.append(move)
        self.whiteToMove = not self.whiteToMove

        if move.startSquare == 'wk':
            self.whiteKingPosition = (move.endRow, move.endCol)
        elif move.startSquare == 'bk':
            self.blackKingPosition = (move.endRow, move.endCol)

        if move.pawnPromotion:
            choice = input('Pawn promotion: q, r, b or n: ')
            self.board[move.endRow][move.endCol] = move.startSquare[0] + choice   

    def undoMove(self):
        """
        Method to undo the last move made on the chess board.

        Parameters:
        None.

        Returns:
        None. The chess board is updated with the previous state before the last move.

        Raises:
        UnboundLocalError: cannot access local variable 'move' where it is not associated with a value (if 'moveHistory' is empty).

        Postconditions:
        - The piece at the start position of the last move is restored on the board.
        - The piece at the end position of the last move is removed from the board.
        - The 'whiteToMove' flag is updated based on whose turn it was before the last move.
        - If the last move was a pawn promotion, the user is prompted to choose a new piece for the pawn.
        """
        if len(self.moveHistory)!= 0:
            move = self.moveHistory.pop()
            self.board[move.startRow][move.startCol] = move.startSquare
            self.board[move.endRow][move.endCol] = move.endSquare
            self.whiteToMove = not self.whiteToMove

        if move.startSquare == 'wk':
            self.whiteKingPosition = (move.startRow, move.startCol)
        elif move.startSquare == 'bk':
            self.blackKingPosition = (move.startRow, move.startCol)

    def getValidMoves(self):
        """
        Method to get a list of all possible moves for the current player.

        Returns:
        list: A list of all possible moves for the current player.

        This method first gets all possible moves for the current player using the 'getAllPossibleMoves' method.
        Then it iterates through the list of moves in reverse order. For each move, it makes the move on the chess board,
        checks if the current player is in check, and if so, removes the move from the list. Finally, it undoes the move,
        and continues with the next move in the list.

        If no valid moves are found, it checks if the current player is in checkmate or stalemate. If the current player is in checkmate,
        the 'checkMate' attribute is set to True. If the current player is in stalemate, the 'staleMate' attribute is set to True.

        If a valid move is found, the 'checkMate' and 'staleMate' attributes are set to False.

        The method returns the list of valid moves.
        """
        moves = self.getAllPossibleMoves()

        for i in range(len(moves) - 1, -1, -1):
            self.makeMove(moves[i])
            self.whiteToMove = not self.whiteToMove
            if self.threatOfCheck():
                moves.remove(moves[i])
            self.whiteToMove = not self.whiteToMove
            self.undoMove()

        if (len(moves) == 0):
            if self.threatOfCheck():
                self.checkMate = True
                if self.whiteToMove:
                    print('Black win!!!')
                else:
                    print('White win!!!')
            else:
                self.staleMate = True
                print('Stalemate!!!')
        else:
            self.checkMate = False
            self.staleMate = False

        return moves

    def threatOfCheck(self):
        """
        Method to check if the current player's king is under attack.

        Returns:
        bool: True if the current player's king is under attack, False otherwise.

        This method first determines whether the current player is white or black. If the current player is white,
        it checks if any of the black pieces are attacking the white king. If the current player is black,
        it checks if any of the white pieces are attacking the black king.

        The method uses the 'squareUnderAttack' method to determine if the current player's king is under attack.
        This method iterates through all the pieces on the board and checks if any of them are attacking the king.

        If the current player's king is under attack, the method returns True. Otherwise, it returns False.
        """
        if self.whiteToMove:
            return self.squareUnderAttack(self.whiteKingPosition[0], self.whiteKingPosition[1])
        else:
            return self.squareUnderAttack(self.blackKingPosition[0], self.blackKingPosition[1])

    def squareUnderAttack(self, row, col):
        """
        Method to check if the current player's king is under attack.

        Parameters:
        row (int): The row index of the square to check for attack.
        col (int): The column index of the square to check for attack.

        Returns:
        bool: True if the current player's king is under attack, False otherwise.

        Note:
        - This method iterates through all the pieces on the board and checks if any of them are attacking the specified square.
        - It does not check for pawn captures or en passant moves.
        """
        self.whiteToMove = not self.whiteToMove
        opponentMoves = self.getAllPossibleMoves()
        self.whiteToMove = not self.whiteToMove

        for move in opponentMoves:
            if move.endRow == row and move.endCol == col:
                return True
        return False

    def getAllPossibleMoves(self):
        '''
        Method to get a list of all possible moves for the current player.

        Returns:
        list: A list of all possible moves for the current player.

        Note:
        - This method don't check for en passant moves.
        - This method don't check for castling moves.
        '''
        moves = []

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                color = self.board[row][col][0]
                if (color == 'w' and self.whiteToMove) or (color == 'b' and not self.whiteToMove):
                    piece = self.board[row][col][1]
                    self.moveFunctions[piece](row, col, moves)
        return moves
    
    def getPawnMoves(self, row, col, moves):
        """
        Method to get all valid pawn moves for the current player.

        Parameters:
        row (int): The row index of the pawn on the chess board.
        col (int): The column index of the pawn on the chess board.
        moves (list): A list to store the valid pawn moves.

        Returns:
        None. The valid pawn moves are appended to the 'moves' list.

        Note:
        - This method checks for single and double pawn moves for white and black players.
        - It does not check for en passant moves.
        """
        if self.whiteToMove:
            if self.board[row - 1][col] == '--':
                moves.append(Move((row, col), (row - 1, col), self.board))
                if row == 6 and self.board[row - 2][col] == '--':
                    moves.append(Move((row, col), (row - 2, col), self.board))
            if col - 1 >= 0:
                if self.board[row - 1][col - 1][0] == 'b':
                    moves.append(Move((row, col), (row - 1, col - 1), self.board))
            if col + 1 <= 7:
                if self.board[row - 1][col + 1][0] == 'b':
                    moves.append(Move((row, col), (row - 1, col + 1), self.board))
        else:
            if self.board[row + 1][col] == '--':
                moves.append(Move((row, col), (row + 1, col), self.board))
                if row == 1 and self.board[row + 2][col] == '--':
                    moves.append(Move((row, col), (row + 2, col), self.board))
            if col - 1 >= 0:
                if self.board[row + 1][col - 1][0] == 'w':
                    moves.append(Move((row, col), (row + 1, col - 1), self.board))
            if col + 1 <= 7:
                if self.board[row + 1][col + 1][0] == 'w':
                    moves.append(Move((row, col), (row + 1, col + 1), self.board))

    def getRookMoves(self, row, col, moves):
        """
        Method to get all valid rook moves for the current player.

        Parameters:
        row (int): The row index of the rook on the chess board.
        col (int): The column index of the rook on the chess board.
        moves (list): A list to store the valid rook moves.

        Returns:
        None. The valid rook moves are appended to the 'moves' list.
        """
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        if self.whiteToMove:
            enemyColor = 'b'
        else:
            enemyColor = 'w'

        for direction in directions:
            for i in range(1, 8):
                endRow = row + i * direction[0]
                endCol = col + i * direction[1]
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endSquare = self.board[endRow][endCol]
                    if endSquare == '--':
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                    elif endSquare[0] == enemyColor:
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                        break
                    else:
                        break
                else:
                    break


    def getKnightMoves(self, row, col, moves):
        """
        Method to get all valid knight moves for the current player.

        Parameters:
        row (int): The row index of the knight on the chess board.
        col (int): The column index of the knight on the chess board.
        moves (list): A list to store the valid knight moves.

        Returns:
        None. The valid knight moves are appended to the 'moves' list.
        """
        directions = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2))

        if self.whiteToMove:
            enemyColor = 'b'
        else:
            enemyColor = 'w'

        for direction in directions:
            endRow = row + direction[0]
            endCol = col + direction[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endSquare = self.board[endRow][endCol]
                if endSquare == '--' or endSquare[0] == enemyColor:
                    moves.append(Move((row, col), (endRow, endCol), self.board))

    def getBishopMoves(self, row, col, moves):
        '''
        Method to get all valid bishop moves for the current player.

        Parameters:
        row (int): The row index of the bishop on the chess board.
        col (int): The column index of the bishop on the chess board.
        moves (list): A list to store the valid bishop moves.

        Returns:
        None. The valid bishop moves are appended to the 'moves' list.
        '''
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        if self.whiteToMove:
            enemyColor = 'b'
        else:
            enemyColor = 'w'

        for direction in directions:
            for i in range(1, 8):
                endRow = row + i * direction[0]
                endCol = col + i * direction[1]
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    endSquare = self.board[endRow][endCol]
                    if endSquare == '--':
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                    elif endSquare[0] == enemyColor:
                        moves.append(Move((row, col), (endRow, endCol), self.board))
                        break
                    else:
                        break
                else:
                    break

    def getQueenMoves(self, row, col, moves):
        '''
        Method to get all valid queen moves for the current player.

        Parameters:
        row (int): The row index of the queen on the chess board.
        col (int): The column index of the queen on the chess board.
        moves (list): A list to store the valid bishop moves.

        Returns:
        None. The valid queen moves are appended to the 'moves' list.
        '''
        self.getBishopMoves(row, col, moves)
        self.getRookMoves(row, col, moves)

    def getKingMoves(self, row, col, moves):
        '''
        Method to get all valid king moves for the current player.

        Parameters:
        row (int): The row index of the king on the chess board.
        col (int): The column index of the king on the chess board.
        moves (list): A list to store the valid bishop moves.

        Returns:
        None. The valid king moves are appended to the 'moves' list.

        Note:
        - This method don't check for castling moves.
        '''
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))

        if self.whiteToMove:
            allyColor = 'w'
        else:
            allyColor = 'b'

        for direction in directions:
            endRow = row + direction[0]
            endCol = col + direction[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                endSquare = self.board[endRow][endCol]
                if endSquare[0] != allyColor:
                    moves.append(Move((row, col), (endRow, endCol), self.board))


class Move:
    boardToRow = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    rowToBoard = {value: key for key, value in boardToRow.items()}
    boardToCol = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    colToBoard = {value: key for key, value in boardToCol.items()}

    def __init__(self, startMove, endMove, board):
        '''
        Initializes a new instance of the Move class with the specified start and end positions and board parameter.

        Parameters:
        startMove (tuple): A tuple containing the row and column indices of the start position of the move.
        endMove (tuple): A tuple containing the row and column indices of the end position of the move.
        board (list): A list representing the current state of the chess board.
        
        Returns:
        None. A new instance of the Move class is initialized with the specified parameters.
        '''
        self.startRow = startMove[0]
        self.startCol = startMove[1]
        self.endRow = endMove[0]
        self.endCol = endMove[1]
        self.startSquare = board[self.startRow][self.startCol]
        self.endSquare = board[self.endRow][self.endCol]
        
        self.pawnPromotion = False
        if (self.startSquare == 'wp' and self.endRow == 0) or (self.startSquare == 'bp' and self.endRow == 7):
            self.pawnPromotion = True

        self.moveID = str(self.startRow) + str(self.startCol) + str(self.endRow) + str(self.endCol)

    def __eq__(self, other):
        '''
        Compares the current instance of the Move class with another instance of the Move class, returning True if the two instances have the same start and end positions, and False otherwise.

        Parameters:
        other (Move): Another instance of the Move class to be compared with the current instance.

        Returns:
        bool: True if the two instances have the same start and end positions, and False otherwise.
        '''
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getNotation(self, startMove, endMove):
        '''
        Returns a string representing the notation of the move, in the format 'startSquare_endSquare'.

        Parameters:
        startMove (tuple): A tuple containing the row and column indices of the start position of the move.
        endMove (tuple): A tuple containing the row and column indices of the end position of the move.

        Returns:
        str: A string representing the notation of the move, in the format 'startSquare_endSquare'.
        '''
        move = self.getSquare(startMove[0], startMove[1]) + self.getSquare(endMove[0], endMove[1])
        return move

    def getSquare(self, row, col):
        '''
        Returns a string representing the square at the specified row and column, in the format 'a1' for the bottom-left square.

        Parameters:
        row (int): The row index of the square to be retrieved.
        col (int): The column index of the square to be retrieved.

        Returns:
        str: A string representing the square at the specified row and column, in the format 'a1' for the bottom-left square.
        '''
        square = self.colToBoard[col] + self.rowToBoard[row]
        return square

