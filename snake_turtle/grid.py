import pygame

from .CONFIGS import *


class Grid:
    def __init__(self,win,size,step):
        self.win = win
        self.size = size
        self.step = step

    def draw(self):
        self.win.fill(BACKGROUND_COLOR)
        x = 0
        y = 0
        for ix in range(self.size[0]+1):
            pygame.draw.line(self.win, GRID_COLOR, (x, 0), (x, DISPLAY_WIDTH))
            x += self.step[0]
        for iy in range(self.size[1]+1):
            pygame.draw.line(self.win, GRID_COLOR, (0, y), (DISPLAY_HEIGHT, y))
            y += self.step[1]
