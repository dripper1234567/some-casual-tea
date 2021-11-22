from Advance import AdTime, Clamp
from random import randint
from breezypythongui import EasyFrame
from threading import Timer
import time


class Game(EasyFrame):
    """rock paper scissors."""

    def __init__(self, windowWidth, windowHeight):

        # __ Initialise game logic __
        self.sTime = AdTime(0)
        self.itemList = {"rock": {"win": "scissors", "los": "paper"},
                         "paper": {"win": "rock", "los": "scissors"},
                         "scissors": {"win": "paper", "los": "rock"}}
        self.isRunning = True

        # __ Initialise Display logic __
        EasyFrame.__init__(self, title="RPS!", width=windowWidth, height=windowHeight)

        self.messageLbl = self.addLabel(text=f"Please pick a move!", row=0, column=0, sticky="NEWS")
        self.buttons = [
            self.addButton(text=list(self.itemList.keys())[count], row=count+1, column=0,
                           command=self.AddMakeAction(list(self.itemList.keys())[count]), sticky="NEWS")
            for count in range(len(self.itemList))]
        self.isRunning = False

        self.mainloop()

    def AddMakeAction(self, key):

        def MakeAction():
            if not self.isRunning:
                self.RollGame(key)

        return MakeAction


    def DeclareWinner(self, win, loss, who, isStalemate = False):
        if isStalemate:
            return "A stalemate has occurred!"
        else:
            return f"{win} beats {loss}! {who} win!"


    def FindWin(self, bot_, player_):
        """
        Tests the users input and the bots input against each other, determines the winner/ if its a stalemate and
        returns the final text

        bot_: string - The bot provided input
        player_: string - The players given input
        Return: string - the game result text
        """
        win = ""
        loss = "| || || |_"
        who = ""

        if self.itemList[bot_]["win"] == player_:
            win = bot_
            loss = player_
            who = "I"
        elif self.itemList[bot_]["los"] == player_:
            win = player_
            loss = bot_
            who = "YOU"
        elif bot_ == player_:
            return self.DeclareWinner(win, loss, who, True)

        return self.DeclareWinner(win, loss, who)


    def BotMove(self, min_=0, max_=1):
        return list(self.itemList.keys())[Clamp(randint(min_, max_), 0, len(self.itemList) - 1)]

    def SetLabel(self, text):
        self.messageLbl["text"] = text

    def RollGame(self, playerInput_):
        """
        Plays out the game by making a random bot move, giving input, and printing the output

        playerInput_: string - the input provided by the player
        """
        if not self.isRunning:
            self.isRunning = True
            botSelect = self.BotMove(0, len(self.itemList) - 1)
            # time.sleep(0.7) fixing small time bug <-- this is no longer needed.
            self.SetLabel("rock")
            Timer(0.7, self.SetLabel, ["paper"]).start()
            Timer(1.4, self.SetLabel, ["scissors"]).start()
            Timer(2.1, self.SetLabel, [self.FindWin(botSelect, playerInput_) + "\n play again?"]).start()

            self.isRunning = False


if __name__ == '__main__':
    game = Game(250, 500)