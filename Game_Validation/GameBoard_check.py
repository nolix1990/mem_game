from GUI.GameBoard import GameBoard
import numpy as np

class GameBoard_check:

    def __init__(self,width = 4,heigth = 4):
        self.width = width
        self.heigth = heigth
        self.board = GameBoard(width,heigth)
        self.size = width*heigth

    def generate_randomize_game_values_test_all_values_appears_twice(self):
        mat = self.board.generate_randomize_game_values()

        counter_arr = [0]*int(self.size/2)
        for idx in range(self.size): counter_arr[mat[idx]] += 1


        for val in counter_arr:
            if val != 2 : raise Exception("all the values must appear twice")

    def generate_randomize_game_values_test_randomization_between_itreations(self):
        vec = np.array(self.board.generate_randomize_game_values())

        for i in range(5):
            vec2 = np.array(self.board.generate_randomize_game_values())
            res = vec2 - vec
            if np.all(res == 0) == True : raise Exception(f"randomizatio doesnt work ,res -> {res}")



if __name__ == '__main__':
    #GameBoard_check().generate_randomize_game_values_test_all_values_appears_twice()
    GameBoard_check().generate_randomize_game_values_test_randomization_between_itreations()