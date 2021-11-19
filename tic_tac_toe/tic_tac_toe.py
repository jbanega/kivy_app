from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    title = "Tic-Tac-Toe | The Game"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepOrange"
        return Builder.load_file("tic_tac_toe.kv")

    # Define who's turn it is
    turn = "X"

    # Keep track of win or lose
    winner = False

    # Keep track of winners and losers scores
    X_win = 0
    O_win = 0


    def get_btns(self):
        # List of buttons
        btns = [
            self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3,
            self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6,
            self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9
        ]
        return btns

    
    def no_winner(self):
        btns = self.get_btns()
        if (self.winner == False) and \
            (btns[0].disabled == True) and (btns[1].disabled == True) and (btns[2].disabled == True) and \
            (btns[3].disabled == True) and (btns[4].disabled == True) and (btns[5].disabled == True) and \
            (btns[6].disabled == True) and (btns[7].disabled == True) and (btns[8].disabled == True):
            self.root.ids.score.text = "It's a tie"


    def end_game(self, btn1, btn2, btn3):
        self.winner = True
        for btn in [btn1, btn2, btn3]:
            btn.color = "darkorange"

        # Disable the buttons
        self.disable_all_buttons()

        # Set label for winner
        self.root.ids.score.text = f"{btn1.text} Wins!"

        # Keep track of winners and losers scores
        if btn1.text == "X":
            self.X_win += 1
        else:
            self.O_win += 1
        self.root.ids.game.text = f"X wins: {self.X_win}  |  O wins: {self.O_win}"


    def disable_all_buttons(self):
        btns = self.get_btns()
        for btn in btns:
            btn.disabled = True


    def win(self):
        btns = self.get_btns()

        # Across
        for n in range(0, 9, 3):
            if (btns[n].text != "") and (btns[n].text == btns[n+1].text) and (btns[n+1].text == btns[n+2].text):
                self.end_game(btns[n], btns[n+1], btns[n+2])

        # Down
        for c in range(0, 3):
            if (btns[c].text != "") and (btns[c].text == btns[c+3].text) and (btns[c+3].text == btns[c+6].text):
                self.end_game(btns[c], btns[c+3], btns[c+6])

        # Diagonal Right-Down
        if (btns[0].text != "") and (btns[0].text == btns[4].text) and (btns[4].text == btns[8].text):
            self.end_game(btns[0], btns[4], btns[8])

        # Diagonal Left-Up
        if (btns[6].text != "") and (btns[6].text == btns[4].text) and (btns[4].text == btns[2].text):
            self.end_game(btns[6], btns[4], btns[2])

        # No winner
        self.no_winner()


    def presser(self, btn):
        if self.turn == "X":
            btn.text = self.turn
            btn.disabled = True
            self.root.ids.score.text = "O's turn!"
            self.turn = "O"
        else:
            btn.text = self.turn
            btn.disabled = True
            self.root.ids.score.text = "X's turn!"
            self.turn = "X"

        # Check to see if won
        self.win()
            

    def restart(self):
        # Restart who's turn it is
        self.turn = "X"
        self.root.ids.score.text = "X's turn!"

        # List of buttons
        btns = self.get_btns()

        for btn in btns:
            # Enabling the button
            btn.disabled = False
            # Clearing the text button
            btn.text = ""
            # Resetting bolor
            btn.color = "gray"

        # Resetting the winner variable
        self.winner = False


if __name__ == "__main__":
    MainApp().run()