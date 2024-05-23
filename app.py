import pygame as pg
import sys
import rules

# Constants
WIDTH, HEIGHT = 512, 512
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE
FRAMES = 5
GRAY = 153, 153, 153
WHITE = 255, 255, 255
IMAGES = {}


def loadImages():
    """
    Loads images of chess pieces.

    This function loads images of all chess pieces, such as pawns, rooks, knights, bishops,
    queens, and kings, in a dictionary where the keys are the piece names, and the values
    are the corresponding Pygame image objects.

    :return: None
    """
    pieces = ['bp', 'br', 'bn', 'bb', 'bq', 'bk', 'wp', 'wr', 'wn', 'wb', 'wq', 'wk']
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))


def GameCondition(screen, gc):
    drawBoard(screen)
    drawPieces(screen, gc.board)


def drawBoard(screen: pg.Surface):
    """
    Draws a chessboard on the provided Pygame display screen.

    This function takes a Pygame display screen object and draws a standard 8x8 chessboard
    with alternating black and white squares. The board is drawn to fit the dimensions of the screen.

    :param screen: pg.Surface
    :return: None
    """
    colors = [WHITE, GRAY]

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = colors[(row + col) % 2]
            pg.draw.rect(screen, color, pg.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Обновление экрана
    pg.display.update()


def drawPieces(screen, board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            piece = board[row][col]
            if piece != '--':
                pieceImage = IMAGES[piece]
                screen.blit(pieceImage, pg.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    pg.display.update()


def main():
    '''
    Main function of the chess game.
    '''
    pg.init()
    gc = rules.GameCondition()
    loadImages()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    reset = pg.time.Clock()
    selectedSquare = ()
    playerMove = []
    validMoves = gc.getValidMoves()
    moveMade = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos()
                row = location[1] // SQUARE_SIZE
                col = location[0] // SQUARE_SIZE
                if selectedSquare == (row, col):
                    selectedSquare = ()
                    playerMove = []
                else:
                    selectedSquare = (row, col)
                    playerMove.append(selectedSquare)
                if len(playerMove) == 2:
                    move = rules.Move(playerMove[0], playerMove[1], gc.board)
                    print(move.getNotation(playerMove[0], playerMove[1])) ########################
                    for i in range(len(validMoves)):
                        if move == validMoves[i]:
                            gc.makeMove(validMoves[i])
                            moveMade = True
                            selectedSquare = ()
                            playerMove = []
                    if not moveMade:
                        playerMove = [selectedSquare]

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    gc.undoMove()
                    moveMade = True

        if moveMade:
            validMoves = gc.getValidMoves()
            moveMade = False

        GameCondition(screen, gc)
        reset.tick(FRAMES)
        pg.display.flip()


if __name__ == "__main__":
    main()
