''' classes Player and Point '''

from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform
from class_menu import *
import os

class Point:
    ''' Class Point: each point object has posiition and pcture.
        And the point are drawing after the bike, just in the middle of it.'''
    def __init__(self, position, player_color, player_type):
        self.position = position
        self.pic = pygame.image.load(
            os.path.join("pics", "bike_" + str(player_type + 1) +
                         "_" + str(player_color) + "_l.png"))

    def draw(self, screen):
        screen.blit(self.pic, (int(self.position[0] - 4),
                               int(self.position[1] - 4)))

class Player:
    ''' Class Point: with position and trace, which is a list with all points
        from the current trace. Also player_type (1 or 2) and player_color.'''
    def __init__(self, position, player_color, player_type, speed):
        self.position = position
        self.trace = []
        self.max_trave_len = 81
        self.move = [0,0,0,0]
        self.player_color = player_color
        self.player_type = player_type
        self.alive = True
        self.speed = speed

        self.base_pic = pygame.image.load(
            os.path.join("pics", "bike_" + str(self.player_type + 1) +
                         "_" + str(self.player_color) + ".png"))
        self.image = self.base_pic
        self.back_pic = pygame.image.load(os.path.join("pics", "back.png"))
        ''' Using a base image for each bike, which is rotated when needed.
            The light on the field is also a pic, which moves with the bike.'''

    def add_point(self):
        ''' Adding points to the trace. '''
        temp_point = Point(vec2d(self.position[0], self.position[1]),
                           self.player_color, self.player_type)
        self.trace.append(temp_point)

    def update(self, other_player, width, height):
        for point in other_player.trace:
            if (self.position - point.position).length < 10:
                ''' Detects a crash. '''
                self.alive = False

        if len(self.trace) >= self.max_trave_len:
            self.trace = self.trace[1:]
            ''' Makes the trace to dissapear after time
                (actually this happens after length) '''
        self.add_point()

        if self.move[0]:
            self.position[0] += self.speed
            self.image = self.base_pic
        elif self.move[1]:
            self.position[0] -= self.speed
            self.image = pygame.transform.rotate(self.base_pic, 180)
        elif self.move[2]:
            self.position[1] -= self.speed
            self.image = pygame.transform.rotate(self.base_pic, 90)
        elif self.move[3]:
            self.position[1] += self.speed
            self.image = pygame.transform.rotate(self.base_pic, 270)
            ''' Moves the player and rotate their pictures accordingly.'''

        coord = [width, height]
        for dot in coord:
            ''' This makes the screen wraparound.'''
            if self.position[coord.index(dot)] < 0:
                self.position[coord.index(dot)] = dot
            if self.position[coord.index(dot)] > dot:
                self.position[coord.index(dot)] = 0

    def draw(self, screen):  
        if self.trace:
            previous_point = self.trace[-1]
            for point in self.trace:
                if not previous_point.position == point.position:
                    point.draw(screen)
                    screen.blit(self.back_pic,
                                (((point.position[0]//20) - 1) * 20,
                                 (((point.position[1]//20) - 1) * 20)))
                previous_point = point
        screen.blit(self.image, (int(self.position[0] - 9),
                                 int(self.position[1] - 9)))
