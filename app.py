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
    pieces = ['bp', 'br', 'bn', 'bb', 'bq', 'bk', 'wp', 'wr', 'wn', 'wb', 'wq', 'wk']
    for piece in pieces:
        IMAGES[piece] = pg.transform.scale(pg.image.load("images/" + piece + ".png"),
                                           (SQUARE_SIZE, SQUARE_SIZE))


def GameCondition(screen, gc):
    drawBoard(screen)
    drawPieces(screen, gc.board)


def drawBoard(screen):
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
            if piece:
                piece_image = IMAGES[piece]
                screen.blit(piece_image, pg.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    pg.display.update()


def main():
    pg.init()
    gc = rules.GameCondition()
    loadImages()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    reset = pg.time.Clock()
    selected_square = ()
    player_move = ()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos()
                selected_square = (location[1] // SQUARE_SIZE, location[0] // SQUARE_SIZE)
                player_move.append(selected_square)
                print(selected_square)
            elif event.type == pg.MOUSEBUTTONUP:
                location = pg.mouse.get_pos()
                if selected_square == (location[1] // SQUARE_SIZE, location[0] // SQUARE_SIZE):
                    selected_square = ()
                    player_move = []
                else:
                    player_move.append(selected_square)

                print(player_move)
        GameCondition(screen, gc)
        reset.tick(FRAMES)
        pg.display.flip()


if __name__ == "__main__":
    main()
