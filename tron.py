from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform
from class_menu import *
from class_player_point import *
import os

class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
        
        #self.background = pygame.image.load("pics\background.png")
        self.background = pygame.image.load(os.path.join("pics", "background.png"))
        self.win = pygame.image.load(os.path.join("pics", "win.png"))

        self.p1keys = [100, 97, 119, 115]
        self.p2keys = [275, 276, 273, 274]

        self.menu = Menu()
        self.player_colors = [1, 1]
        
        self.game_speed = 3
        
    def init_players(self):
        self.player_one = Player(vec2d(100, 200), self.player_colors[0], 0, self.game_speed)
        self.player_two = Player(vec2d(100, 300), self.player_colors[1], 1, self.game_speed)      
        
    def update(self):
        if not self.menu.screen:
            if self.player_one.alive and self.player_two.alive:
                self.player_one.update(self.player_two, self.w, self.h)
                self.player_two.update(self.player_one, self.w, self.h)
        
    def keyUp(self, key):
        if not self.menu.screen:
            if key in self.p1keys:
                self.player_one.move[self.p1keys.index(key)] = 0
            if key in self.p2keys:
                self.player_two.move[self.p2keys.index(key)] = 0
     
    def keyDown(self, key):
        if not self.menu.screen:
            if key in self.p1keys:
                self.player_one.move[self.p1keys.index(key)] = 1
            if key in self.p2keys:
                self.player_two.move[self.p2keys.index(key)] = 1
            if key == 112:
                self.menu.screen = 1

        
    def mouseUp(self, button, position):
        if not self.menu.screen:
            if not self.player_one.alive or not self.player_two.alive:
                if (position - vec2d(548, 355)).length < 18 and button == 1:
                    self.game_speed += 1
                    self.player_one = Player(vec2d(100, 200), self.player_colors[0], 0, self.game_speed)
                    self.player_two = Player(vec2d(100, 300), self.player_colors[1], 1, self.game_speed)
        else:
            self.menu.click(self, button, position)

    def mouseMotion(self, buttons, position, rel):
        self.menu.check_selected(position)

        
    def draw(self):
        if not self.menu.screen:
            self.screen.blit(self.background, (0, 0))

            self.player_one.draw(self.screen)

            self.player_two.draw(self.screen)

            if not self.player_one.alive:
                self.screen.blit(self.win, (150, 130))
                pygame.draw.circle(self.screen, (200, 0, 0), (548, 355), 36, 3)
            elif not self.player_two.alive:
                self.screen.blit(self.win, (150, 130))
                pygame.draw.circle(self.screen, (0, 200, 0), (548, 355), 36, 3)
        else:
            self.menu.draw(self.screen)
        
s = Starter()
s.mainLoop(40)
