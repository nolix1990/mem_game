from datetime import datetime

import pygame
from pygame.color import Color
from pygame.rect import Rect
from pygame.surface import Surface

from Game_utils.Point import Point
from IDraw import IDraw
from IClick import IClick

class Game_Button(IDraw,IClick):

    def __init__(self,value,width,height,button_color : Color,coordinate : Point):
        self.value = value
        self.width = width
        self.height = height
        self.button_color = button_color
        self.coordinate = coordinate
        self.flliped = False
        self.rect = Rect(self.coordinate.x,self.coordinate.y, width, height)
        self.font = pygame.font.SysFont("Comic Sans MS", 50)
        self.title = self.font.render(str(self.value), False, (0, 255, 255))
        self.last_click_time = datetime.now()

    def draw(self,surface : Surface):
        pygame.draw.rect(surface , self.button_color , self.rect)
        if self.get_is_flliped():
            centerTitle = self.title.get_rect(center=(self.width / 2 + self.coordinate.x , self.height/2 + self.coordinate.y))
            surface.blit(self.title,centerTitle)

    def is_clicked(self, coordinate: Point):
        return ( coordinate.x >= self.rect.left and coordinate.x <= self.rect.right) and\
               (coordinate.y >= self.rect.top and coordinate.y <= self.rect.bottom)

    def get_is_flliped(self):
        if self.flliped:
            timeout = datetime.now() - self.last_click_time
            if timeout.seconds > 1:
                self.fllip()
                self.last_click_time = datetime.now()
        return self.flliped

    def handle_click(self, coordinate: Point):
        self.fllip()

    def fllip(self):
        self.flliped = not self.flliped