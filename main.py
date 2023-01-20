
import pygame
from pygame.locals import *
from GUI.Game_Button import Game_Button
from Game_utils.Point import Point
from Interface.IClick import IClick

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

def handle_mouse_click(clickables : [IClick]):
    left, middle, right = pygame.mouse.get_pressed()
    if left:
        for clickable_obj in clickables:
            p = Point(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
            if clickable_obj.is_clicked(p):
                clickable_obj.handle_click(p)


def main():
    buttons = [Game_Button('7',100, 100,Color(192,192,192), Color(0, 255, 255), Point(0,0)),
               Game_Button('8', 100, 100, Color(192,192,192), Color(0, 255, 255), Point(100, 100))]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
               handle_mouse_click(buttons)

        for button in buttons:
            button.draw(screen)

        clock.tick(30)
        pygame.display.flip()

main()
