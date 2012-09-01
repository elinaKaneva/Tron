from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform

class Menu:
    def __init__(self):
        self.main_menu = pygame.image.load("menu_1.png")
        self.main_menu_light = pygame.image.load("glow.png")
        self.main_menu_light_small = pygame.image.load("info_glow.png")

        self.options_menu = pygame.image.load("menu_options.png")
        self.options_menu_back = pygame.image.load("options_back_liquid.png")
        self.options_menu_liquid = pygame.image.load("options_liquid.png")

        self.info_menu = pygame.image.load("menu_info.png")

        self.screen = 1
        self.selected = 0
        self.speed = 0
        self.player_one_bike = 1
        self.player_two_bike = 1
        self.load_pics()

    def load_pics(self):
        self.player_one_pic = pygame.image.load("bike_1_" + str(self.player_one_bike) + ".png")
        self.player_one_pic = pygame.transform.rotate(self.player_one_pic, 90)
        self.player_two_pic = pygame.image.load("bike_2_" + str(self.player_two_bike) + ".png")
        self.player_two_pic = pygame.transform.rotate(self.player_two_pic, 90)

    def click(self, game, button, pos):
        self.check_selected(pos)
        if self.screen == 1:
            if self.selected == 1:
                game.init_players()
                self.screen = 0
            elif self.selected == 2:
                self.screen = 2
                self.selected = 0
            elif self.selected == 3:
                game.running = False
            elif self.selected == 4:
                self.screen = 3
                self.selected = 0
        elif self.screen == 2:
            if self.selected == 31 and self.speed < 9:
                self.speed += 1
            elif self.selected == 32 and self.speed > 0:
                self.speed -= 1
                
            elif self.selected == 11:
                if self.player_one_bike == 3:
                    self.player_one_bike = 0
                self.player_one_bike += 1
                self.load_pics()
                
            elif self.selected == 12:
                if self.player_one_bike == 1:
                    self.player_one_bike = 4
                self.player_one_bike -= 1
                self.load_pics()
                
            elif self.selected == 21:
                if self.player_two_bike == 3:
                    self.player_two_bike = 0
                self.player_two_bike += 1
                self.load_pics()
            elif self.selected == 22:
                if self.player_two_bike == 1:
                    self.player_two_bike = 4
                self.player_two_bike -= 1
                self.load_pics()
            elif self.selected == 5:
                self.screen = 1
                self.selected = 0
                game.player_colors = [self.player_one_bike, self.player_two_bike]
                game.game_speed = 3 + self.speed
                game.init_players()
        elif self.screen == 3:
            if self.selected == 1:
                self.screen = 1
                self.selected = 0

    def check_selected(self, pos):
        self.selected = 0
        if self.screen == 1:
            if pos[0] in range(120, 341) and pos[1] in range(280, 341):
                self.selected = 1
            elif pos[0] in range(160, 381) and pos[1] in range(380, 441):
                self.selected = 2
            elif pos[0] in range(200, 421) and pos[1] in range(480, 541):
                self.selected = 3
            elif pos[0] in range(670, 741) and pos[1] in range(480, 541):
                self.selected = 4
                
        elif self.screen == 2:
            if pos[0] in range(74, 110) and pos[1] in range(204, 240):
                self.selected = 11
            elif pos[0] in range(219, 255) and pos[1] in range(204, 240):
                self.selected = 12
            elif pos[0] in range(540, 576) and pos[1] in range(204, 240):
                self.selected = 21
            elif pos[0] in range(683, 719) and pos[1] in range(204, 240):
                self.selected = 22
            elif pos[0] in range(380, 416) and pos[1] in range(223, 259):
                self.selected = 31
            elif pos[0] in range(380, 416) and pos[1] in range(367, 403):
                self.selected = 32
            elif pos[0] in range(300, 525) and pos[1] in range(513, 572):
                self.selected = 5
                
        elif self.screen == 3:
            if pos[0] in range(300, 525) and pos[1] in range(513, 572):
                self.selected = 1
                
    def draw(self, screen):
        if self.screen == 1:
            screen.blit(self.main_menu, (0, 0))
            if self.selected in [1, 2, 3]:
                screen.blit(self.main_menu_light, (103 + self.selected * 40, 180 + self.selected * 100))
            if self.selected == 4:
                screen.blit(self.main_menu_light_small, (677, 480))
        elif self.screen == 2:
            screen.blit(self.options_menu_back, (334, 193))
            screen.blit(self.options_menu_liquid, (333, 416 - self.speed * 25))
            screen.blit(self.options_menu, (0, 0))
            screen.blit(self.player_one_pic, (157, 210))
            screen.blit(self.player_two_pic, (622, 210))

            if self.selected == 5:
                screen.blit(self.main_menu_light, (323, 513))
        elif self.screen == 3:
            screen.blit(self.info_menu, (0, 0))
            if self.selected == 1:
                screen.blit(self.main_menu_light, (323, 513))
            

class Point:
    def __init__(self, pos, player_color, player_type):
        self.pos = pos
        self.pic = pygame.image.load("bike_" + str(player_type + 1) + "_" + str(player_color) + "_l.png")

    def draw(self, screen):
        screen.blit(self.pic, (int(self.pos[0] - 4), int(self.pos[1] - 4)))

class Player:
    def __init__(self, pos, player_color, player_type, speed):
        self.pos = pos
        self.path = []
        self.move = [0,0,0,0]
        self.player_color = player_color
        self.player_type = player_type
        self.alive = True
        self.speed = speed

        self.base_pic = self.player_one_pic = pygame.image.load("bike_" + str(self.player_type + 1) + "_" + str(self.player_color) + ".png")

        self.image = self.base_pic
        self.back_pic = pygame.image.load("back.png")

    def add_point(self):
        temp_point = Point(vec2d(self.pos[0], self.pos[1]), self.player_color, self.player_type)
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

        coord = [width, height]
        for x in coord:
            if self.pos[coord.index(x)] < 0:
                self.pos[coord.index(x)] = x
            if self.pos[coord.index(x)] > x:
                self.pos[coord.index(x)] = 0

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

        self.keysP1 = [100, 97, 119, 115]
        self.keysP2 = [275, 276, 273, 274]

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
            if key in self.keysP1:
                self.player_one.move[self.keysP1.index(key)] = 0
            if key in self.keysP2:
                self.player_two.move[self.keysP2.index(key)] = 0
     
    def keyDown(self, key):
        if not self.menu.screen:
            if key in self.keysP1:
                self.player_one.move[self.keysP1.index(key)] = 1
            if key in self.keysP2:
                self.player_two.move[self.keysP2.index(key)] = 1
            if key == 112:
                self.menu.screen = 1

        
    def mouseUp(self, button, pos):
        if not self.menu.screen:
            if not self.player_one.alive or not self.player_two.alive:
                if (pos - vec2d(548, 355)).length < 18 and button == 1:
                    self.game_speed += 1
                    self.player_one = Player(vec2d(100, 200), self.player_colors[0], 0, self.game_speed)
                    self.player_two = Player(vec2d(100, 300), self.player_colors[1], 1, self.game_speed)
        else:
            self.menu.click(self, button, pos)

    def mouseMotion(self, buttons, pos, rel):
        self.menu.check_selected(pos)

        
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
