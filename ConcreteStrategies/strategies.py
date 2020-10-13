#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

#   #   #           Tahta oyunları için base class          #   #   #
class Board:

    def __init__(self):

        self.up_left = " "
        self.up_mid = " "
        self.up_right = " "

        self.middle_left = " "
        self.middle_mid = " "
        self.middle_right = " "

        self.down_left = " "
        self.down_mid = " "
        self.down_right = " "

        self.board = ""

        self.moves = []

        self.currentPlayer = 'x'

    def setBoard(self):
        pass

    def move(self):
        pass

    def checkArea(self, location):
        pass

    def setMove(self):
        pass

    def changePlayer(self):
        pass

    def whoWin(self):
        pass

    def showBoard(self):
        print(self.board)

    def run(self):

        while not self.whoWin():
            self.move()
            self.setMove()
            self.setBoard()
            self.showBoard()
        print(self.whoWin()[1])

#   #   #           X-O-X oyunu için abc class           #   #   #
class tic_tac_toe(Board):

    def changePlayer(self):
        if self.currentPlayer == 'x':
            self.currentPlayer = 'o'

        else:
            self.currentPlayer = 'x'

    def move(self):

        error_message = "Lütfen 1-9 arası bir konum seçiniz."

        move = 0

        while not move:
            try:
                move = int(input("\nHamleniz(1-9): "))

                if not 0 < move < 10:
                    move = 0
                    print(error_message)
                    continue

                check = self.checkArea(move)

                if check == True:
                    self.moves.append(move)

                else:
                    move = 0
                    print(check)


            except:
                print(error_message)

    def checkArea(self, location):
        if not location in self.moves:
            self.moves.append(location)
            return True

        else:
            return "Lütfen boş bir alan seçiniz!\n{}".format(self.board)

    def setMove(self):
        if self.moves[-1] == 1:
            self.down_left = self.currentPlayer
            self.changePlayer()

        elif self.moves[-1] == 2:
            self.down_mid = self.currentPlayer
            self.changePlayer()

        elif self.moves[-1] == 3:
            self.down_right = self.currentPlayer
            self.changePlayer()

        elif self.moves[-1] == 4:
            self.middle_left = self.currentPlayer
            self.changePlayer()

        elif self.moves[-1] == 5:
            self.middle_mid = self.currentPlayer
            self.changePlayer()

        elif self.moves[-1] == 6:
            self.middle_right = self.currentPlayer
            self.changePlayer()

        elif self.moves[-1] == 7:
            self.up_left = self.currentPlayer
            self.changePlayer()

        elif self.moves[-1] == 8:
            self.up_mid = self.currentPlayer
            self.changePlayer()

        else:
            self.up_right = self.currentPlayer
            self.changePlayer()

    def setBoard(self):

        self.board = "{} | {} | {}\n{} | {} | {}\n{} | {} | {}".format(self.up_left, self.up_mid, self.up_right,
                                                                 self.middle_left, self.middle_mid,
                                                                 self.middle_right,
                                                                 self.down_left, self.down_mid, self.down_right)

    def whoWin(self):

        message_win = "'{}' oyuncusu kazandı!".format(self.currentPlayer)
        draw_message = "Berabere!"

        if self.up_left == self.up_mid == self.up_right != " ":
            self.changePlayer()
            return True, message_win

        elif self.middle_left == self.middle_mid == self.middle_right != " ":
            self.changePlayer()
            return True, message_win

        elif self.down_left == self.down_mid == self.down_right != " ":
            self.changePlayer()
            return True, message_win

        elif self.up_left == self.middle_left == self.down_left != " ":
            self.changePlayer()
            return True, message_win

        elif self.up_mid == self.middle_mid == self.down_mid != " ":
            self.changePlayer()
            return True, message_win

        elif self.up_right == self.middle_right == self.down_right != " ":
            self.changePlayer()
            return True, message_win

        elif self.up_left == self.middle_mid == self.down_right != " ":
            self.changePlayer()
            return True, message_win

        elif self.up_right == self.middle_mid == self.down_left != " ":
            self.changePlayer()
            return True, message_win

        else:
            if len(self.moves) == 9:
                return True, draw_message
            else:
                return False

#   #   #           Çalışacak olan strateji fonksiyonu          #   #   #
def play_tic_tac_toe(self):
    theGame = tic_tac_toe()
    theGame.run()