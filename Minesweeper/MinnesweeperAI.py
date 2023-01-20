import random
import Minesweeper.Config as Config


class AI:
    def __init__(self) -> None:
        r = None
        c = None


    def BestMove(self,gs):
        self.r = random.randint(0,Config.DEMANTION-1)
        self.c = random.randint(0,Config.DEMANTION-1)
        return (self.r,self.c)