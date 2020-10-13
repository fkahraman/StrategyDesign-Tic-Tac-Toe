#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

import types
from ConcreteStrategies.strategies import play_tic_tac_toe

#   #   #           Bağlam sınıfı           #   #   #
class Game:

    def __init__(self, strategy = None):

        if strategy is not None:
            self.execute = types.MethodType(strategy, self) #-Kullanıcı tanımlı sınıf örneklerinin yöntemlerinin türü.-#

    def execute(self):
        pass

#   #   #           Çalışacak olan strateji algoritmaları buraya yazılacak          #   #   #
def run_strategy():

    strategy = Game(play_tic_tac_toe)
    strategy.execute()

def app():
    run_strategy()