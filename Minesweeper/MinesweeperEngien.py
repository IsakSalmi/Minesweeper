import Minesweeper.Config as Config

class MinesweeperEngien:
    def __init__(self):
        self.GameBoard = [['-','-','-','-','-','-','-','-','-'],
                        ['-','-','-','-','-','-','-','-','-'],
                        ['-','-','-','-','-','-','-','-','-'],
                        ['-','-','-','-','-','-','-','-','-'],
                        ['-','-','-','-','-','-','-','-','-'],
                        ['-','-','-','-','-','-','-','-','-'],
                        ['-','-','-','-','-','-','-','-','-'],
                        ['-','-','-','-','-','-','-','-','-'],
                        ['-','-','-','-','-','-','-','-','-']]
        self.DisplayBoard = self.GameBoard
        self.Minse = Config.MINNES
        self.GameStatus = True
    
    def GetBoard(self):
        return self.DisplayBoard
    
    def SelectSQ(self, r, c):
        if self.GameBoard == '*':
            self.GameBoard = False
            self.DisplayBoard[r][c] = '*'
        else:
            self.DisplayBoard[r][c] = ' '

        
    def flagSQ(self, r, c):
        self.DisplayBoard[r][c] = 'F'
    
    
    
    
        


