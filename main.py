
import pygame
from pygame.locals import *

from GUI.GameBoard import GameBoard
from GUI.Game_Button import Game_Button
from Game_utils.Point import Point
from Interface.IClick import IClick

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

def handle_mouse_click(game_board):
    left, middle, right = pygame.mouse.get_pressed()
    if left:
        game_board.handle_click(Point(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))


def main():

    board = GameBoard(600,600,6,6)

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
