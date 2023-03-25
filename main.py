import pygame as pg, time as t, random as r
from settings import *
from wall import *
from user import *

class Window:

    def __init__(self, ws):
        pg.init()
        self.win_size = (ws[0], ws[1])
        self.clock = pg.time.Clock()
        self.walls = [(self.crwp()),
                      (self.crwp()),
                       (self.crwp()),
                      (self.crwp()),
                      (self.crwp()),
                      (self.crwp())]
        self.new_display()

    def crwp(self): # CREATE RANDOM WALL POSITION
        x = r.randint(0, win_size[0]), r.randint(0, win_size[1]), r.randint(0, win_size[0]), r.randint(0, win_size[1])
        return x

    def new_display(self):
        self.window = pg.display.set_mode(self.win_size, flags=pg.RESIZABLE)
        self.wall = Wall(self, self.walls)
        self.user = User(user_pos, self)

    def update(self):
        pg.display.update()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'POS: {pg.mouse.get_pos()}      FPS: {round(self.clock.get_fps(), 2)}   {self.user.if_hit_wall}')

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                pg.quit()

    def draw(self):
        self.window.fill((23, 2, 117))
        self.wall.draw()
        self.user.draw()

    def run(self):
        while True:
            self.update()
            self.draw()
            self.check_events()

if __name__ == '__main__':
    window = Window(win_size)
    window.run()