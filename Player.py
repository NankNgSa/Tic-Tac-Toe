
from Board import Board

class Player:
    global b
    b = [" " for i in range(9)]

    def __init__(self):
        self.player = "x"
        self.round = 0


    def play(self):
        while True:
            # Board.print_board(b)
            print("the round of the player " +self.player)

            # the player enter a number where he wants to mark
            print("enter a number between 1 & 9")
            # -1 because the index starts from 0 to 8
            move = int(input()) - 1

            # if the case is free
            if b[move] == " ":
                b[move] = self.player
                self.round += 1
            else:
                print("/!\ Choose another case...")
                # continue


def play(self, b):
        while True:
            Board.print_board(b)
            print("the round of the player " +self.player)

            # the player enter a number where he wants to mark
            print("enter a number between 1 & 9")
            # -1 because the index starts from 0 to 8
            move = int(input()) - 1

            # if the case is free
            if b[move] == " ":
                b[move] = self.player
                self.round += 1
            else:
                print("/!\ Choose another case...")
                continue

            if self.round == 9:
                print("Nobody've won...")
                break



















