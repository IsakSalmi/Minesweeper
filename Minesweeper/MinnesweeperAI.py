import random
import Minesweeper.Config as Config


class AI:
    def __init__(self):
        self.r = None
        self.c = None
        self.firstClick = True


    def BestMove(self,gs):
        board = gs.GetBoard()
        if self.firstClick:
            self.r = random.randint(0,Config.DEMANTION-1)
            self.c = random.randint(0,Config.DEMANTION-1)
            self.firstClick = False
            return (self.r,self.c)
        return (1,1)