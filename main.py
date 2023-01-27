
import pygame
from pygame.locals import *

from GUI.GameBoard import GameBoard
from GameLogic import GameLogic
from Game_utils.Point import Point

pygame.init()
ScreenWidthpx = 1000
ScreenHieghpx = 1000
screen = pygame.display.set_mode((ScreenWidthpx, ScreenHieghpx))
clock = pygame.time.Clock()

def handle_mouse_click(game_board):
    left, middle, right = pygame.mouse.get_pressed()
    if left:
        game_board.handle_click(Point(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))


def main():
    gameLogicService = GameLogic()
    board = GameBoard(ScreenWidthpx,ScreenHieghpx,4,4, gameLogicService)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(board)

        board.draw(screen)

        clock.tick(30)
        pygame.display.flip()

main()
