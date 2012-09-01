from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform

class Point:
    def __init__(self, pos, player_num):
        self.pos = pos
        if player_num:
            self.pic = pygame.image.load("red_line.png")
        else:
            self.pic = pygame.image.load("green_line.png")

    def draw(self, screen):
        screen.blit(self.pic, (int(self.pos[0] - 4), int(self.pos[1] - 4)))

class Player:
    def __init__(self, pos, player_type, speed):
        self.pos = pos
        self.path = []
        self.move = [0,0,0,0]
        self.player_type = player_type
        self.alive = True
        self.speed = speed
        if player_type:
            self.base_pic = pygame.image.load("red_player.png")
        else:
            self.base_pic = pygame.image.load("green_player.png")
        self.image = self.base_pic
        self.back_pic = pygame.image.load("back.png")

    def add_point(self):
        temp_point = Point(vec2d(self.pos[0], self.pos[1]), self.player_type)
        self.path.append(temp_point)

    def update(self, other_player, width, height):
        for point in other_player.path:
            if (self.pos - point.pos).length < 10:
                self.alive = False

        if len(self.path) == 81:
            self.path = self.path[1:]

        self.add_point()

        if self.move[0]:
            self.pos[0] += self.speed
            self.image = self.base_pic
        elif self.move[1]:
            self.pos[0] -= self.speed
            self.image = pygame.transform.rotate(self.base_pic, 180)
        elif self.move[2]:
            self.pos[1] -= self.speed
            self.image = pygame.transform.rotate(self.base_pic, 90)
        elif self.move[3]:
            self.pos[1] += self.speed
            self.image = pygame.transform.rotate(self.base_pic, 270)
            
        if self.pos[0] < 0:
            self.pos[0] = width
        if self.pos[0] > width:
            self.pos[0] = 0
        if self.pos[1] < 0:
            self.pos[1] = height
        if self.pos[1] > height:
            self.pos[1] = 0

    def draw(self, screen):  
        if self.path:
            previous_point = self.path[-1]
            for point in self.path:
                if not previous_point.pos == point.pos:
                    point.draw(screen)
                    screen.blit(self.back_pic, (((point.pos[0]//20) - 1) * 20,
                                                (((point.pos[1]//20) - 1) * 20)))
                previous_point = point
        screen.blit(self.image, (int(self.pos[0] - 9), int(self.pos[1] - 9)))


class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
        
        self.background = pygame.image.load("background.png")
        self.win = pygame.image.load("win.png")
		
        self.game_speed = 3
        self.player_one = Player(vec2d(100, 200), 0, self.game_speed)
        self.player_two = Player(vec2d(100, 300), 1, self.game_speed)
        
        
    def update(self):
        if self.player_one.alive and self.player_two.alive:
            self.player_one.update(self.player_two, self.w, self.h)
            self.player_two.update(self.player_one, self.w, self.h)
        
    def keyUp(self, key):
        if key == 100:
            self.player_one.move[0] = 0
        if key == 97:
            self.player_one.move[1] = 0
        if key == 119:
            self.player_one.move[2] = 0
        if key == 115:
            self.player_one.move[3] = 0
        if key == 275:
            self.player_two.move[0] = 0
        if key == 276:
            self.player_two.move[1] = 0
        if key == 273:
            self.player_two.move[2] = 0
        if key == 274:
            self.player_two.move[3] = 0
     
    def keyDown(self, key):
        if key == 100:
            self.player_one.move[0] = 1
        if key == 97:
            self.player_one.move[1] = 1
        if key == 119:
            self.player_one.move[2] = 1
        if key == 115:
            self.player_one.move[3] = 1
        if key == 275:
            self.player_two.move[0] = 1
        if key == 276:
            self.player_two.move[1] = 1
        if key == 273:
            self.player_two.move[2] = 1
        if key == 274:
            self.player_two.move[3] = 1
        
    def mouseUp(self, button, pos):
        if not self.player_one.alive or not self.player_two.alive:
            if (pos - vec2d(548, 355)).length < 18 and button == 1:
                self.game_speed += 1
                self.player_one = Player(vec2d(100, 200), 0, self.game_speed)
                self.player_two = Player(vec2d(100, 300), 1, self.game_speed)

        
    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.player_one.draw(self.screen)

        self.player_two.draw(self.screen)

        if not self.player_one.alive:
            self.screen.blit(self.win, (150, 130))
            pygame.draw.circle(self.screen, (200, 0, 0), (548, 355), 36, 3)
        elif not self.player_two.alive:
            self.screen.blit(self.win, (150, 130))
            pygame.draw.circle(self.screen, (0, 200, 0), (548, 355), 36, 3)

        
        
s = Starter()
s.mainLoop(40)
