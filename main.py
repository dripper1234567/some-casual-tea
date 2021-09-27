from Advance import AdTime
from random import randint


sTime = AdTime(0)
itemList = {"rock": {"win": "scissors", "los": "paper"},
            "paper": {"win": "rock", "los": "scissors"},
            "scissors": {"win": "paper", "los": "rock"}}


def TestInput(userInput_):
    return userInput_ in itemList


def PromptType(inputText_, errorText_):
    while True:
        userInput = input(inputText_).lower()
        if TestInput(userInput):
            return userInput
        print(errorText_)


def FindWin(bot_, player_):
    win = ""
    loss = "| || || |_"
    who = ""

    if itemList[bot_]["win"] == player_:
        win = bot_
        loss = player_
        who = "I"
    elif itemList[bot_]["los"] == player_:
        win = player_
        loss = bot_
        who = "YOU"
    else:
        print(f"{player_} and {bot_}?! Stalemate!")
        return

    print(f"{win} beats {loss}! {who} WON!")
    print("-"*30)


def RollGame(playerInput_):
    botSelect = list(itemList.keys())[randint(0, len(itemList))]
    sTime.WaitUntil(0.8)
    print("-"*30)
    sTime.WaitUntil(0.8)
    print("rock,")
    sTime.WaitUntil(0.7)
    print("paper,")
    sTime.WaitUntil(0.7)
    print("SCISSORS!")
    sTime.WaitUntil(0.7)
    print("...")
    sTime.WaitUntil(4)
    FindWin(botSelect, playerInput_)


def main():
    chosenPiece = -1
    while True:
        chosenPiece = PromptType(f"Please enter one of these! {str(itemList.keys())}\n", f"Input was not on the list!\n "
                                 + f"Please choose one of these! {str(itemList.keys())}\n")
        RollGame(chosenPiece)


if __name__ == '__main__':
    main()
