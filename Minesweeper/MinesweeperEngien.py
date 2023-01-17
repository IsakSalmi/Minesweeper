import Minesweeper.Config as Config
import random

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


        self.DisplayBoard = [['-','-','-','-','-','-','-','-','-'],
                            ['-','-','-','-','-','-','-','-','-'],
                            ['-','-','-','-','-','-','-','-','-'],
                            ['-','-','-','-','-','-','-','-','-'],
                            ['-','-','-','-','-','-','-','-','-'],
                            ['-','-','-','-','-','-','-','-','-'],
                            ['-','-','-','-','-','-','-','-','-'],
                            ['-','-','-','-','-','-','-','-','-'],
                            ['-','-','-','-','-','-','-','-','-']]
        self.Minse = Config.MINES
        self.GameStatus = True
    
    def GetBoard(self):
        return self.DisplayBoard
    
    def SelectSQ(self, sr, sc):
        if self.GameBoard[sr][sc] == '-':
            self.DisplayBoard[sr][sc] = '0'
        elif self.GameBoard[sr][sc] != '*':
            self.DisplayBoard[sr][sc] = self.GameBoard[sr][sc]
        else:
            self.GameBoard[sr][sc] == '*'
            self.GameStatus = False
        
        if self.GameStatus:
            directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
            AvSQ = []
            AvSQ.append((sr,sc))
            while len(AvSQ) != 0:
                r = AvSQ[0][0]
                c = AvSQ[0][1]
                print(r,c)
                for d in directions:
                    endRow = r + d[0]
                    endCol = c + d[1]
                    if endRow >= 0 and endRow < Config.DEMANTION and endCol >= 0 and endCol < Config.DEMANTION:
                        if self.GameBoard[endRow][endCol] == '-':
                            AvSQ.append((endRow,endCol))
                            self.GameBoard[endRow][endCol] = '0'
                            self.DisplayBoard[endRow][endCol] = '0'
                        elif self.GameBoard[endRow][endCol] != '*':
                            self.DisplayBoard[endRow][endCol] = self.GameBoard[endRow][endCol]
                AvSQ.pop(0)
        
                
            

    def createBoard(self,sr,sc):
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        Mines = 0
        while Mines < 10:
            r = random.randint(0,Config.DEMANTION-1)
            c = random.randint(0,Config.DEMANTION-1)
            if  (r != sr) and (c != sc) and self.GameBoard[r][c] != '*':
                self.GameBoard[r][c] = '*'
                for d in directions:
                    endRow = r + d[0]
                    endCol = c + d[1]
                    if endRow >= 0 and endRow < Config.DEMANTION and endCol >= 0 and endCol < Config.DEMANTION:
                        if self.GameBoard[endRow][endCol] == '-':
                            self.GameBoard[endRow][endCol] = '1'
                        elif self.GameBoard[endRow][endCol] == '*':
                            pass
                        else:
                            temp = self.GameBoard[endRow][endCol]
                            temp = int(temp)
                            temp += 1
                            temp = str(temp)
                            self.GameBoard[endRow][endCol] = temp
                Mines += 1

    def PrintGameboard(self):
        for r in range(Config.DEMANTION):
            print(self.GameBoard[r])

    def flagSQ(self, r, c):
        self.DisplayBoard[r][c] = 'F'
    
    
    
    
        


