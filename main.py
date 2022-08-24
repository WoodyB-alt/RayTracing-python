import pygame as pg 
import sys 
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
'''initalise pyame moduels 
create screen for rendering the set resolutions in an 
instance of the clock class framer 8
'''
class Game:
    def __init__(self):
       pg.init()
       self.screen = pg.display.set_mode(RES)
       self.clock = pg.time.Clock()
       self.delta_time = 1
       self.new_game()

 #new game method -- store map and call to new game method from the main applications constructor and raycasting method
    def new_game(self):
        self.map = map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)

    #update screen and display info about frames per second in win caption
    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    #at each iteration paint screen black + draw map
    def draw(self):
        self.screen.fill('black')
        #self.map.draw()
        #self.player.draw()

    #check events for closing the working window and for pressing the ESC key(for quitting game) called from main loop
    def check_events(self):
        for event in pg.event.get():
            if event == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    #run method that will store main game loop 
    #will call the update and draw methods
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()