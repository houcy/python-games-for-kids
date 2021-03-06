from .CONFIGS import *
import pygame


class Cube:
    def __init__(self, surface, pos, color=SNAKE_COLOR, dir=(1, 0)):
        self.surface = surface
        self.pos = pos
        self.color = color
        self.dir = dir

    def move(self, dir):
        self.dir = dir

        # is reached boundaries
        isMove = True
        if dir[0] == -1 and self.pos[0] <= 0:
            isMove = False
            self.pos = (NROWS - 1, self.pos[1])
        if dir[0] == 1 and self.pos[0] >= NROWS - 1:
            isMove = False
            self.pos = (0, self.pos[1])
        if dir[1] == 1 and self.pos[1] >= NCOLS - 1:
            isMove = False
            self.pos = (self.pos[0], 0)
        if dir[1] == -1 and self.pos[1] <= 0:
            isMove = False
            self.pos = (self.pos[0], NCOLS - 1)
        if isMove:
            self.pos = (self.pos[0]+dir[0],self.pos[1]+dir[1])

    def draw(self,isEyes=False):
        pygame.draw.rect(self.surface,self.color,
                         (self.pos[0] * GRID_DX + 1,
                          self.pos[1] * GRID_DY + 1,
                          GRID_DX - 1,
                          GRID_DY - 1))
        if isEyes:
            centrex = GRID_DX // 2
            centrey = GRID_DY // 2
            radius = 3
            x0 = self.pos[0] * GRID_DX + centrex
            y0 = self.pos[1] * GRID_DY + centrey
            if self.dir[0]!=0:
                circle1 = (x0 + centrex/2*self.dir[0], y0 - centrey/2)
                circle2 = (x0 + centrex/2*self.dir[0], y0 + centrey/2)
            else:
                circle1 = (x0 - centrex/2, y0 + centrey/2*self.dir[1])
                circle2 = (x0 + centrex/2, y0 + centrey/2*self.dir[1])
            pygame.draw.circle(self.surface, EYE_COLOR, circle1, radius)
            pygame.draw.circle(self.surface, EYE_COLOR, circle2, radius)
