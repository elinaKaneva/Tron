import unittest
from pygame import *
from pygamehelper import *
from pygame.locals import *
from vec2d import *
from math import e, pi, cos, sin, sqrt
from random import uniform
from class_menu import *
from class_player_point import *
import os

                    
class test_player(unittest.TestCase):
    
    def test_vec2d(self):
        testvec = vec2d(200,300)
        self.assertEqual(testvec[0], 200)
        self.assertEqual(testvec[1], 300)
    
    def test_init_player(self):
        player1 = Player(vec2d(100, 200), 1, 0, 3)
        player2 = Player(vec2d(100, 300), 1, 1, 3)
        self.assertEqual(player1.position[0], 100, "player 1 x is wrong")
        self.assertEqual(player1.position[1], 200, "player 1 y is wrong")
        self.assertEqual(player2.position[0], 100, "player 2 x is wrong")
        self.assertEqual(player2.position[1], 300, "player 2 y is wrong")

    def test_init_point(self):
        point1 = Point(vec2d(100, 200), 1, 0)
        point2 = Point(vec2d(100, 300), 1, 1)
        self.assertEqual(point1.position[0], 100, "point 1 x is wrong")
        self.assertEqual(point1.position[1], 200, "point 1 y is wrong")
        self.assertEqual(point2.position[0], 100, "point 2 x is wrong")
        self.assertEqual(point2.position[1], 300, "point 2 y is wrong")

    def test_add_point(self):
        point_new = Point(vec2d(100, 200), 1, 0)
        
        #self.assertEqual(point1.position[0], 100, "point 1 x is wrong")
        #self.assertEqual(point1.position[1], 200, "point 1 y is wrong")
        #self.assertEqual(point2.position[0], 100, "point 2 x is wrong")
        #self.assertEqual(point2.position[1], 300, "point 2 y is wrong")
        
'''
    def test_click_options_menu(self):
        s = Starter()
        s.menu.selected = 2
        m.click(s, position = vec2d(300, 400))
        self.assertEqual(m.selected == 2, m.screen == 2, "Options menu")

    def test_click_info_menu(self):
        m = Menu()
        self.selected = 2
        self.assertEqual(m.selected == 2, m.screen == 3, "Info menu")

    def test_click_new_game(self):
        m = Menu()
        m.selected = 1
        m.click()
        self.assertEqual(m.selected == 4, m.screen == 0, "New Game")
        
       
    def test_player_update(self):
        p1 = Player(vec2d(100, 200), 1, 0, 3)
        p2 = Player(vec2d(100, 300), 1, 1, 3)
        self.speed = 3
        p1.move[0] = 1
        p2.move[2] = 1
        self.assertEqual(p1.position[0], 100, "player 1 x is wrong")
        self.assertEqual(p1.position[1], 200, "player 1 y is wrong")
        self.assertEqual(p2.position[0], 100, "player 2 x is wrong")
        self.assertEqual(p2.position[1], 300, "player 2 y is wrong")
        #self.assertFalse(p2.alive, "test if player 1 is live")
        #self.assertFalse(p2.alive, "test if player 2 is live")
'''   
        
if __name__ == '__main__':
    unittest.main()
