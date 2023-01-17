import pygame as p
import Minesweeper.Config as Config


BOARD_HIGHT = Config.BOARD_HIGHT
BOARD_WIDTH = Config.BOARD_WIDTH
MAX_FPS = Config.MAX_FPS

def StartGame():
    Screen = p.display.set_mode((BOARD_WIDTH,BOARD_HIGHT))
    Clock = p.time.Clock()
    Screen.fill(p.Color('Black'))
    start = True
    while start:
        for e in p.event.get():
            if e.type == p.QUIT:
                start = False
        Clock.tick(MAX_FPS)
        p.display.flip()
