from Advance import AdTime, Clamp
from random import randint


class Game:
    """rock paper scissors."""
    def __init__(self):
        self.sTime = AdTime(0)
        self.itemList = {"rock": {"win": "scissors", "los": "paper"},
                         "paper": {"win": "rock", "los": "scissors"},
                         "scissors": {"win": "paper", "los": "rock"}}

    def TestInput(self, userInput_):
        """
        Takes in input and returns if it is in the accepted inputs list

        userInput_: string - the user input
        Return: bool - if it is in the accepted inputs
        """
        return userInput_ in self.itemList

    def PromptType(self, inputText_, errorText_):
        """
        Produces user input with the provided prompt and validates it, if it fails,
        it prints the provided error message and restarts the prompt

        inputText_: string - The message that the user is prompted with
        errorText_: string - The error message if the input is not valid to the test
        Return: string - The validated user input
        """
        while True:
            userInput = input(inputText_).lower()
            if self.TestInput(userInput) or userInput == "exit":
                return userInput
            print(errorText_)

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
            return f"{player_} and {bot_}?! Stalemate!"
        else:
            return "... what. Somehow, an error occurred?"

        return f"{win} beats {loss}! {who} WON!"

    def BotMove(self, min_ = 0, max_ = 1):
        return list(self.itemList.keys())[Clamp(randint(min_, max_), 0, len(self.itemList)-1)]

    def RollGame(self, playerInput_):
        """
        Plays out the game by making a random bot move, giving input, and printing the output

        playerInput_: string - the input provided by the player
        """
        botSelect = self.BotMove(0, len(self.itemList)-1)
        self.sTime.WaitUntil(0.8)
        print("-" * 30)
        self.sTime.WaitUntil(0.8)
        print("rock,")
        self.sTime.WaitUntil(0.7)
        print("paper,")
        self.sTime.WaitUntil(0.7)
        print("SCISSORS!")
        self.sTime.WaitUntil(0.7)
        print("...")
        self.sTime.WaitUntil(4)
        print(self.FindWin(botSelect, playerInput_))
        print("-" * 30)

    def Play(self):
        """
        The main game loop, run this to play the game!
        """
        chosenPiece = -1
        while True:
            chosenPiece = self.PromptType(f"Please enter one of these! {str(self.itemList.keys())} (or exit to leave!)"
                                          f"\n",
                                          f"Input was not on the list!\n "
                                          + f"Please choose one of these! {str(self.itemList.keys())}\n")
            if chosenPiece == "exit":
                print("Good Game!")
                exit()

            self.RollGame(chosenPiece)


if __name__ == '__main__':
    game = Game()
    game.Play()
