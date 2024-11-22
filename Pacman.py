"""
    Author: Zak Groenewold
    Date: 11/20/2024
    CSCI310
    Pacman game utilizing multithreading
    Credit: 
        Some Code used from https://medium.com/dataflair/create-pacman-game-using-python-7dcedbbe74f1
"""

import pygame
import sys
import random

# Initialize pygame library
pygame.init()

# Settings for the game window
SCREEN_WIDTH = 560
SCREEN_HEIGHT = 620
CELL_SIZE = 20
FPS = 10

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

font = pygame.font.SysFont('Arial', 18)

board = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#o####.#####.##.#####.####o#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "######.##### ## #####.######",
    "######.##          ##.######",
    "######.## ###--### ##.######",
    "######.## #      # ##.######",
    "       ## #      # ##       ",
    "######.## #      # ##.######",
    "######.## ######## ##.######",
    "######.##          ##.######",
    "######.## ######## ##.######",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#o..##................##..o#",
    "###.##.##.########.##.##.###",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################"
]

# TODO Load images for ghosts and Pac-Man

pacman_image = pygame.image.load('./assets/Pacman.png')

"""ghost_images = [
    pygame.image.load(),
    pygame.image.load(),
    pygame.image.load(),
    pygame.image.load()
]
"""
pacman_sprite = pygame.transform.scale(screen, (CELL_SIZE, CELL_SIZE))
'''for i in range (len(ghost_images)):
    ghost_images[i] = pygame.transform.scale(CELL_SIZE,CELL_SIZE)
    '''
def draw_board():
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell == '#':
                pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == '.':
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE // 2, y* CELL_SIZE + CELL_SIZE // 2), 3)
            elif cell == 'o':
                pygame.draw.circle(screen, WHITE, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), 7)
                