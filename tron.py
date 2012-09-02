''' Main Game '''

from pygame import *
from pygamehelper import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform
from class_menu import *
from class_player_point import *
import os


class Starter(PygameHelper):
    ''' This is the main class which does all the work.
        It has some base methods, which are defined in pygamehelper.
        pygamehelper is not written by me,
        but I found it really useful and perfectly made for
        my purpouses with this game.
        And I use it to use pygame easier. :)

        This is in short how it works:
        1] Fisrt is the __init__ method, of course.
        2] Secondly all event are detected, this inclused:
            - keyUp
            - keyDown
            - mouseUp
            - mouseMotion
            Their names are pretty clear by themselves.
        3] Aftter that comes the update method.
        4] And finally, when we have all event and current condition of all
            obejcts, variables and so on, comes the draw method.
        And this loop can be called needed times per second,
        so indeed it is awesome. 
    '''
    def __init__(self):
        self.w, self.h = 800, 600
        self.game_speed = 3
        self.max_speed = 9
        self.player_colors = [1, 1]
        self.p1keys = [100, 97, 119, 115]
        self.p2keys = [275, 276, 273, 274]
        ''' These two list above hold the controlers's codes:
              W             ^
           A  S  D   and  < v >
        '''
        white = (255,255,255)
        green = (68, 255, 0)
        yellow = (194, 255, 0)
        blue = (67, 124, 227)
        red = (255, 0, 0)
        pink = (255, 0, 127)
        purple = (212, 0, 255)        
        self.p1colors = [green, yellow, blue]
        self.p2colors = [red, pink, purple]
        self.win_cicle_center = (548, 355)
        
        PygameHelper.__init__(self, size=(self.w, self.h), fill=(white))
        self.background = pygame.image.load(os.path.join("pics",
                                                         "background.png"))
        self.win = pygame.image.load(os.path.join("pics", "win.png"))
        self.menu = Menu()
        
        
    def init_players(self):
        ''' Creating two new players. '''
        self.player_one = Player(vec2d(100, 200),
                                 self.player_colors[0], 0, self.game_speed)
        self.player_two = Player(vec2d(100, 300),
                                 self.player_colors[1], 1, self.game_speed)
        
    def update(self):
        ''' "Moving" both players in the field if we're in the game
            and they's are still alive. '''
        if not self.menu.screen:
            ''' This check defines if we are in game and not in the menu. '''
            if self.player_one.alive and self.player_two.alive:
                ''' The players will be updated, if they're alive. '''
                self.player_one.update(self.player_two, self.w, self.h)
                self.player_two.update(self.player_one, self.w, self.h)
        
    def keyUp(self, key):
        ''' Detect if a key is not pressed anymore,
            so players can stop moving. '''
        if not self.menu.screen:
            if key in self.p1keys:
                self.player_one.move[self.p1keys.index(key)] = 0
            if key in self.p2keys:
                self.player_two.move[self.p2keys.index(key)] = 0
     
    def keyDown(self, key):
        ''' Detect if a key is pressed, so players can move. '''
        if not self.menu.screen:
            if key in self.p1keys:
                self.player_one.move[self.p1keys.index(key)] = 1
            if key in self.p2keys:
                self.player_two.move[self.p2keys.index(key)] = 1
            if key == 8:
                ''' This is Backspace button and it brings us back
                    to the main menu if we're playing.'''
                self.menu.screen = 1

        
    def mouseUp(self, button, position):
        if not self.menu.screen:
            if not (self.player_one.alive and self.player_two.alive):
                ''' If one of the players is dead, this part detects
                    if it is clicked on the Window logo and if so:
                    creates two new players and rises the speed with one.'''
                if (position - vec2d(
                    self.win_cicle_center)).length < 18 and button == 1:
                    if self.game_speed < self.max_speed:
                        self.game_speed += 1
                    self.player_one = Player(vec2d(100, 200),
                                             self.player_colors[0], 0,
                                             self.game_speed)
                    self.player_two = Player(vec2d(100, 300),
                                             self.player_colors[1], 1,
                                             self.game_speed)
        else:
            self.menu.click(self, button, position)

    def mouseMotion(self, buttons, position, rel):
        ''' mouseMotion is used for the buttons in the menu only.
            If the mouse is over a button, it "lights" in green.
            check_selected checks if we're over a button in the menu.'''
        self.menu.check_selected(position)

        
    def draw(self):
        if not self.menu.screen:
            self.screen.blit(self.background, (0, 0))
            self.player_one.draw(self.screen)
            self.player_two.draw(self.screen)

            live = ['one', 'two']
            for motor in live:
                ''' Draws the win image and circles the Windows logo
                    with the color of the winner. '''
                if not eval("self.player_" + motor + ".alive"):
                    self.screen.blit(self.win, (150, 130))
                    if live.index(motor):
                        pygame.draw.circle(self.screen,
                                   self.p1colors[self.player_colors[0] - 1],
                                   self.win_cicle_center, 36, 3)
                    else:
                        pygame.draw.circle(self.screen,
                                   self.p2colors[self.player_colors[1] - 1],
                                   self.win_cicle_center, 36, 3)
        else:
            self.menu.draw(self.screen)
        
s = Starter()
s.mainLoop(40)
''' A new Starter object is created each time, when we start the game.
    And it is updated 40 times per second.
'''
