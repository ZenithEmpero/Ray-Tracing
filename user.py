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

    def draw(self):
        self.mouse_pos = pg.mouse.get_pos()

        # Calculate the direction and distance to the mouse position
        self.direction = [self.mouse_pos[0] - self.pos[0], self.mouse_pos[1] - self.pos[1]]
        self.distance = m.sqrt(self.direction[0] ** 2 + self.direction[1] ** 2)

        # Normalize the direction vector
        self.direction[0] /= self.distance + 0.0001
        self.direction[1] /= self.distance + 0.0001

        # Calculate the end position of the line
        self.end = (self.pos[0] + self.direction[0] * 20, self.pos[1] + self.direction[1] * 20)
        self.end2 = (self.pos[0] + self.direction[0] * user_ray_length, self.pos[1] + self.direction[1] * user_ray_length)

        #Kuhaon ang mga position sa multi rays stored in self.rays_pos
        self.multiple_rays()

        self.ray_cast()
        #pg.draw.line(self.window.window, (255, 0, 0), (self.pos[0], self.pos[1]), (self.end[0], self.end[1]), width=10)

    def multiple_rays(self):
        self.rays_pos = []
        center_angle = m.atan2(self.mouse_pos[1] - self.pos[1], self.mouse_pos[0] - self.pos[0])
        for i in range(num_rays):
            # Calculate the angle of the ray relative to the center angle
            angle = center_angle + (i - num_rays / 2) * cone_angle / num_rays

            # Calculate the direction of the ray
            direction = [math.cos(angle), math.sin(angle)]

            # Calculate the end point of the ray
            end_point = (self.pos[0] + direction[0] * user_ray_length, self.pos[1] + direction[1] * user_ray_length)
            self.rays_pos.append(end_point)



    def ray_cast(self):
        for a in self.rays_pos:
            self.num_of_intersections = 0
            for i in self.walls:
                self.points = []
                
                x1 = self.pos[0]
                x2 = a[0]
                x3 = i[0]
                x4 = i[2]
                y1 = self.pos[1]
                y2 = a[1]
                y3 = i[1]
                y4 = i[3]

                x1, y1, x2, y2, x3, y3, x4, y4 = x3, y3, x4, y4, x1, y1, x2, y2

                self.t_num = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4))
                self.u_num = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2))
                self.den = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
                if self.den == 0:
                    return
                self.t = (self.t_num / self.den)    
                self.u = self.u_num / self.den
                self.point = (x1 + self.t * (x2 - x1)), (y1 + self.t * (y2 - y1)) 
                if (0 < self.t) and (self.t < 1) and (1 > self.u > 0):
                    #print(f'T: [{self.t}] U: [{self.u}] Bool: [TRUE] VALUES: X1[{x1}] X3[{x3}] Y3[{y3}] Y4[{y4}] Y1[{y1}] X4[{x4}]')
                    self.points.append(self.point)
                    self.num_of_intersections += 1

                else:
                    #print(f'T: [{self.t_num}] U: [{self.u}] Bool: [FALSE] VALUES: X1[{x1}] X3[{x3}] Y3[{y3}] Y4[{y4}] Y1[{y1}] X4[{x4}]')
                    self.num_of_intersections += 0
                if self.num_of_intersections > 0:
                    self.draw_ray()
                else:
                    pg.draw.line(self.window.window, 'green', self.pos, a, 2)
                
    def draw_ray(self):
        for i in self.rays_pos:
            if len(self.points) > 0:
                x = self.check_nearest_point()
                pg.draw.line(self.window.window, (255, 255, 0), self.pos, x, 2)
                #pg.draw.circle(self.window.window, (255, 255, 0), x, 5)
    
    def check_nearest_point(self):
        point_dis = {}
        if len(self.points) > 0:
            for i in self.points:
                x1 = self.pos[0]
                y1 = self.pos[1]
                x2 = i[0]
                y2 = i[1]

                dif = (abs(x1 - x2), abs(y1 - y2))
                pyth = m.sqrt((dif[0])**2 + (dif[1]**2))
                point_dis[pyth] = (x2, y2)
            point_dis = sorted(point_dis.items())
            x = point_dis[0][1]
            return x
