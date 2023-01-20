from pygame import Color
from GUI.Game_Button import Game_Button
from Game_utils.Point import Point
import random


class GameBoard:

    def __init__(self, matrix_width, matrix_height: int):
        if matrix_width * matrix_height % 2 != 0: raise Exception("matrix_size must be odd number")
        self.matrix_width = matrix_width
        self.matrix_height = matrix_height
        #self.create_game()
        self.game_matrix = []

    # def create_game(self):
    #     generate_randomize_game_values()
    #     for x in range(self.matrix_width):
    #             self.game_matrix[x] = [y for y in range(self.matrix_height)]



    def create_gamebutton_object(self,y:int)->Game_Button:
        button = Game_Button('7',100, 100,Color(192,192,192), Color(0, 255, 255), Point(0,0))

    def generate_randomize_game_values(self):
        size = self.matrix_height*self.matrix_width
        game_values = [i for i in range(int(size/2))]
        game_values.extend([i for i in range (int(size / 2))])
        random.shuffle(game_values)
        return game_values

