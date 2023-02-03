from time import sleep

from GUI.Game_Button import Game_Button
from Game_utils.Point import Point
from Interface.IGameLogic import IGameLogic


class GameLogic(IGameLogic):
    def __init__(self,window_height,window_width):
        self.maxClieckedButtons = 2
        self.clickedButtons = []
        self.game_size = window_width*window_height
        self.num_of_flipped_buttons = 0
        self.game_end = False

    def handle_click(self, button:Game_Button):
        self.clickedButtons.append(button)

        if len(self.clickedButtons) > 2:
            if (not self.clickedButtons[0].flliped and not self.clickedButtons[1].flliped):
                self.clickedButtons = [button]
            else:
                self.clickedButtons.pop()
                button.hide()

        elif len(self.clickedButtons) == 2:
            self.handle_if_same(self.clickedButtons[0], self.clickedButtons[1])

        elif len(self.clickedButtons) == 1 and not self.clickedButtons[0].flliped:
            self.clickedButtons[0].hide()
            self.clickedButtons = []




    def handle_if_same(self,button:Game_Button,button2:Game_Button)->bool:
        if button.is_equal(button2) == True and button.flliped and button2.flliped:
            button.finish()
            button2.finish()
            self.num_of_flipped_buttons = self.num_of_flipped_buttons + 2
            self.check_game_finished()
            self.clickedButtons = []
        elif (not button.flliped and not button2.flliped):
            self.clickedButtons = []

        

    def check_game_finished(self):
        if self.num_of_flipped_buttons == self.game_size:
            self.game_end = True
