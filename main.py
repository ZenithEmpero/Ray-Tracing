import pygame as pg, time as t
from settings import *
from wall import *
from user import *

class Window:

    def __init__(self, ws):
        pg.init()
        self.win_size = (ws[0], ws[1])
        self.clock = pg.time.Clock()
        self.walls = [(400, 100, 400, 400),
                      (200, 30, 40, 400)]
        self.new_display()

    def new_display(self):
        self.window = pg.display.set_mode(self.win_size)
        self.wall = Wall(self, self.walls)
        self.user = User(user_pos, self)

    def update(self):
        pg.display.update()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'POS: {pg.mouse.get_pos()}      FPS: {round(self.clock.get_fps(), 2)}')

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                pg.quit()

    def draw(self):
        self.window.fill((6, 87, 201))
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