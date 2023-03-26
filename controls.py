import pygame as pg
from settings import *

class Controls:

    def __init__(self, speed):
        self.speed = speed
        pass

    def movement(self):
        events = pg.key.get_pressed()
        if events[pg.K_w]:
            user_pos[1] += -self.speed
        if events[pg.K_s]:
            user_pos[1] += self.speed
        if events[pg.K_d]:
            user_pos[0] += self.speed
        if events[pg.K_a]:
            user_pos[0] += -self.speed