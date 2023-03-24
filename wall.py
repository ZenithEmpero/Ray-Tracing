import pygame as pg
from settings import * 

class Wall:
    def __init__(self, window, walls):
        self.walls = walls
        self.window = window

    def draw(self):
        for i in self.walls:
            pg.draw.line(self.window.window, (255, 255, 255), (i[0], i[1]), (i[2], i[3]))
        
    