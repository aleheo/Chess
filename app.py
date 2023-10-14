import pygame
import sys
import rules

pygame.init()

# Constants
WIDTH, HEIGHT = 512, 512
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH / BOARD_SIZE
BLACK = 0, 0, 0
WHITE = 255, 255, 255
IMAGES = {}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Шахматы')

def loadImages():
    pieces = ['bp', 'bR', 'bN', 'bB', 'bQ', 'bK', 'pp', 'pR', 'pN', 'pB', 'pQ', 'pK']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

def main():
    gc = rules.GameCondition()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Очистка экрана
        screen.fill(WHITE)

        # Рисование шахматной доски
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(screen, BLACK, (col * WIDTH / 8, row * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))

        # Обновление экрана
        pygame.display.update()


if __name__ == "__main__":
    main()
