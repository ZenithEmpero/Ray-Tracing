import pygame as pg
import math as m
from settings import *


class User:
    def __init__(self, pos, window):
        self.window = window
        self.walls = self.window.walls
        self.pos = pos
        self.if_hit_wall = None
        self.point = None
        self.x = pos[0]
        self.y = pos[1]

    def draw(self):
        self.mouse_pos = pg.mouse.get_pos()

        # Calculate the direction and distance to the mouse position
        self.direction = [self.mouse_pos[0] - self.pos[0], self.mouse_pos[1] - self.pos[1]]
        self.distance = m.sqrt(self.direction[0] ** 2 + self.direction[1] ** 2)

        # Normalize the direction vector
        self.direction[0] /= self.distance + 0.0001
        self.direction[1] /= self.distance + 0.0001

        # Calculate the end position of the line
        self.end = (self.pos[0] + self.direction[0] * user_size, self.pos[1] + self.direction[1] * user_size)
        self.end2 = (self.pos[0] + self.direction[0] * 1000, self.pos[1] + self.direction[1] * 1000)
        
        self.if_hit_wall = self.ray_cast()
        pg.draw.line(self.window.window, (255, 0, 0), (self.pos[0], self.pos[1]), (self.end[0], self.end[1]), width=10)

    def ray_cast(self):

        for i in self.walls:
            x1 = self.pos[0]
            x2 = self.end2[0]
            x3 = i[0]
            x4 = i[2]
            y1 = self.pos[1]
            y2 = self.end2[1]
            y3 = i[1]
            y4 = i[3]

            x1, y1, x2, y2, x3, y3, x4, y4 = x3, y3, x4, y4, x1, y1, x2, y2

            pg.draw.circle(self.window.window, 'black', (x1, y1), 5)
            pg.draw.circle(self.window.window, 'black', (x2, y2), 5)
            pg.draw.circle(self.window.window, 'black', (x3, y3), 5)
            pg.draw.circle(self.window.window, 'black', (x4, y4), 5)

            self.t_num = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4))
            self.u_num = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2))
            self.den = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
            if self.den == 0:
                return
            self.t = (self.t_num / self.den)    
            self.u = self.u_num / self.den
            #self.u_num = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3))

            if (0 < self.t) and (self.t < 1) and (self.u > 0):
                print(f'T: [{self.t}] U: [{self.u}] Bool: [TRUE] VALUES: X1[{x1}] X3[{x3}] Y3[{y3}] Y4[{y4}] Y1[{y1}] X4[{x4}]')
                self.point = (x1 + self.t * (x2 - x1)), (y1 + self.t * (y2 - y1))
                #return True

            else:
                print(f'T: [{self.t_num}] U: [{self.u}] Bool: [FALSE] VALUES: X1[{x1}] X3[{x3}] Y3[{y3}] Y4[{y4}] Y1[{y1}] X4[{x4}]')
                self.point = None
                #return False
            
            if self.point != None:
                pg.draw.line(self.window.window, (255, 255, 255), self.pos, self.point)
                pg.draw.circle(self.window.window, (255, 255, 0), (self.point), 5)
                

