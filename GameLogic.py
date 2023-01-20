from GUI.Game_Button import Game_Button


class GameLogic:

    def check_if_same(self,button:Game_Button,button2:Game_Button)->bool:
        if button.is_equal(button2) == True:
            #delte
            self.game_finished()

        

    def game_finished(self):
        pass