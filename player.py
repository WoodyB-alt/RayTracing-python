from settings import *
import pygame as pg
import math 

''' create player class that in which the attributes will take instance of game, 
x and y coordinates of the player in the angle of his direction'''

class Player:
    def __init__(self, game):
        self.game = game 
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

 #writing movement- calculaed by movements by taking coordinated and using dx and dy using sin and cos to calculate the movment of play in a direction
 #if we wannt movment speed to be indpendent of the frame rate we need the delta time value for each frame
 #the delta time value is the amount of time that has passed since the last frame
    def movement(self): 
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0 
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin 
        if keys[pg.K_s]: 
            dx += - speed_cos 
            dy += - speed_sin
        if keys[pg.K_a]: 
            dx += speed_sin
            dy += - speed_cos
        if keys[pg.K_d]: 
            dx += - speed_sin 
            dy +=  speed_cos
        
        #apply received increments to the corrisponding coordinated of the player 
        #will remain to the controls of the players direction this is done via 
        #pressing the left and right keys while angle value will remain within 2p
        #tau = 2*pi
        self.check_wall_collision(dx, dy)
        
        if keys[pg.K_LEFT]: 
            self.angle -= PLAER_ROT_SPEED * self.game.delta_time 
        if keys[pg.K_RIGHT]:
            self.angle += PLAER_ROT_SPEED * self.game.delta_time 
        self.angle %= math.tau

 #method to check if player collides with walls via checking the coordinates 
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

 #use above method in collision chekc method to check if the checked coordinated hit walls
 #done by using the dx and dy incrments in turn to check new coordinates and onyl allow movments when there is no wall
    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

 # test method for drawing player on a plane 
 #draw player direction of movment as a line and player will be in form of circle 
 #add to main file and import player file
    def draw(self):
        #pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
        # (self.x * 100 + WIDTH * math.cos(self.angle),
        # self.y * 100 + WIDTH * math. sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)
 
 #call movement method through the update method 
    def update(self):
        self.movement()
 
 #make two properties, the first returning the players coordinates
 #the second interger coordinates to know which tile of the map were on 
     
    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)