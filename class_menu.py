from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform

class Menu:
    def __init__(self):
        self.main_menu = pygame.image.load("main_menu.png")
        self.button_glow = pygame.image.load("button_glow.png")
        self.button_info_glow = pygame.image.load("button_info_glow.png")

        self.options_menu = pygame.image.load("options_menu.png")
        self.options_back_liquid = pygame.image.load("options_back_liquid.png")
        self.options_liquid = pygame.image.load("options_liquid.png")

        self.info_menu = pygame.image.load("info_menu.png")

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

    def click(self, game, button, position):
        self.check_selected(position)
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
            if self.selected == 201 and self.speed < 9:
                self.speed += 1
            elif self.selected == 202 and self.speed > 0:
                self.speed -= 1
                
            elif self.selected == 211:
                if self.player_one_bike == 3:
                    self.player_one_bike = 0
                self.player_one_bike += 1
                self.load_pics()
            elif self.selected == 212:
                if self.player_one_bike == 1:
                    self.player_one_bike = 4
                self.player_one_bike -= 1
                self.load_pics()
                
            elif self.selected == 221:
                if self.player_two_bike == 3:
                    self.player_two_bike = 0
                self.player_two_bike += 1
                self.load_pics()
            elif self.selected == 222:
                if self.player_two_bike == 1:
                    self.player_two_bike = 4
                self.player_two_bike -= 1
                self.load_pics()
                
            elif self.selected == 200:
                self.screen = 1
                self.selected = 0
                game.player_colors = [self.player_one_bike, self.player_two_bike]
                game.game_speed = 3 + self.speed
                game.init_players()
                
        elif self.screen == 3:
            if self.selected == 300:
                self.screen = 1
                self.selected = 0

    def check_selected(self, position):
        self.selected = 0
        x = position[0]
        y = position[1]
        all_buttons = [1, 2, 3, 4, 211, 212, 221, 222, 201, 202, 200, 300]     
        x_scr1 = [[120, 341], [160, 381], [200, 421], [670, 741]]
        x_scr2 = [[74, 110], [219, 255], [540, 576], [683, 719], [380, 416], [380, 416], [300, 525]]
        x_scr3 = [300, 525]
        y_scr1 = [[280, 341], [380, 441], [480, 541], [480, 541]]
        y_scr2 = [[204, 240], [204, 240], [204, 240], [204, 240], [223, 259], [367, 403], [513, 572]]
        y_scr3 = [513, 572]

        if self.screen == 1:
            for which in range(len(x_scr1)):
                if x in range(x_scr1[which][0], x_scr1[which][1]) and y in range(y_scr1[which][0], y_scr1[which][1]):
                    self.selected = all_buttons[which]
        elif self.screen == 2:
            for which in range(len(x_scr2)):
                if x in range(x_scr2[which][0], x_scr2[which][1]) and y in range(y_scr2[which][0], y_scr2[which][1]):
                    self.selected = all_buttons[4:][which]
        elif self.screen == 3:
            if x in range(x_scr3[0], x_scr3[1]) and y in range(y_scr3[0],y_scr3[1]):
                self.selected = all_buttons[11]

    def draw(self, screen):
        if self.screen == 1:
            screen.blit(self.main_menu, (0, 0))
            if self.selected in [1, 2, 3]:
                screen.blit(self.button_glow, (103 + self.selected * 40, 180 + self.selected * 100))
            elif self.selected == 4:
                screen.blit(self.button_info_glow, (677, 480))
                
        elif self.screen == 2:
            screen.blit(self.options_back_liquid, (334, 193))
            screen.blit(self.options_liquid, (333, 416 - self.speed * 25))
            screen.blit(self.options_menu, (0, 0))
            screen.blit(self.player_one_pic, (157, 210))
            screen.blit(self.player_two_pic, (622, 210))

            if self.selected == 200:
                screen.blit(self.button_glow, (323, 513))
                
        elif self.screen == 3:
            screen.blit(self.info_menu, (0, 0))
            if self.selected == 300:
                screen.blit(self.button_glow, (323, 513))
