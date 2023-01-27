from pygame import Color, Surface
from pygame.math import Vector2

from GUI.Game_Button import Game_Button
from GUI.Game_line import GameLine
from Game_utils.Point import Point
from Interface.IClick import IClick
from Interface.IDraw import IDraw
import random

from Interface.IGameLogic import IGameLogic


class GameBoard(IDraw,IClick):
    BORDER=5#px

    def __init__(self, matrix_width, matrix_height: int , num_of_rows:int ,
                 num_of_cols : int, gameLogicService:IGameLogic):
        if matrix_width * matrix_height % 2 != 0: raise Exception("matrix_size must be odd number")
        self.matrix_width = matrix_width
        self.matrix_height = matrix_height
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols
        self.game_matrix:[] = []
        self.border_lines = []
        self.button_width = matrix_width/num_of_cols
        self.button_height = matrix_height/num_of_rows
        self.button_color  = Color(255, 153, 51)
        self.font_color = Color(255, 255, 255)
        self.create_game()
        self.generate_border_lines()
        self.__gameLogicService = gameLogicService


    def create_game(self):
        random_values = self.generate_randomize_game_values()
        values_idx = 0

        for row in range(self.num_of_rows):
            temp_buttons_arr = []
            for col in range(self.num_of_cols):
                temp_buttons_arr.append(self.create_gamebutton_object(str(random_values[values_idx]),col,row))
                values_idx = values_idx + 1
            self.game_matrix.append(temp_buttons_arr)



    def create_gamebutton_object(self,text_value : str ,col : int , row : int)->Game_Button:
        button = Game_Button(text_value,
                             self.button_width,
                             self.button_height,
                             self.button_color,
                             self.font_color,
                             self.calculate_button_coordinate(col,row))
        return button

    def generate_border_lines(self):
        for row in range(self.num_of_rows):
            # horizontal lines
            y = row * self.button_height
            startPoint = Vector2(0, y)
            endPoint = Vector2(self.matrix_width, y)
            self.border_lines.append(GameLine(GameBoard.BORDER,
                                              startPoint,
                                              endPoint))
        for col in range(self.num_of_cols):
            # vertecal  lines
            x = col * self.button_width
            startPoint = Vector2(x, 0)
            endPoint = Vector2(x, self.matrix_height)
            self.border_lines.append(GameLine(GameBoard.BORDER,
                                              startPoint,
                                              endPoint))

    def generate_randomize_game_values(self):
        size = self.num_of_rows*self.num_of_cols
        game_values = [i for i in range(int(size/2))]
        game_values.extend([i for i in range (int(size / 2))])
        random.shuffle(game_values)

        return game_values

    def calculate_button_coordinate(self,col,row):
        return Point(col*self.button_width,row*self.button_height)


    def draw(self,surface : Surface):
        for row in range(self.num_of_rows):
            for col in range(self.num_of_cols):
                self.game_matrix[row][col].draw(surface)
        for line in self.border_lines:
            line.draw(surface)

    def is_clicked(self,coordinate : Point):
        pass

    def handle_click(self,coordinate : Point):
        for row in range(self.num_of_rows):
            for col in range(self.num_of_cols):
                if self.game_matrix[row][col].is_clicked(coordinate):
                    self.game_matrix[row][col].handle_click(coordinate)
                    self.__gameLogicService.handle_click(self.game_matrix[row][col])
