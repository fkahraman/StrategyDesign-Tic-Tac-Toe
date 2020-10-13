#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""


from context import app

#   #   #           Kullanıcı işlemleri burada tanımlanabilir           #   #   #
if __name__ == '__main__':

    while(True):
        app()
        while(True):
            new_game = input("\nYeni oyun oynamak ister misiniz ? E/H --> ")
            new_game = new_game.upper()

            if (new_game == 'E'):
                break

            elif (new_game == 'H'):
                break

            else:
                pass

        if new_game == 'H':
            break

        else:
            pass
