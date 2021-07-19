#-------------------------------------------------------------------------------
# Name:        CONNECT 4 GAME
# Purpose:     PROJECT FOR GAME DEVELOPMENT IN OOP
#
# Author:      GROUP CATACUTAN, PASCUAL, LAURENT, VENERACION
#
# Created:     30/10/2019
# Copyright:   (c) XENON_XEIN_XENLY 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame as pg
from pygame.locals import *
from connect_4_images import * # BLIT, RECT, SCREEN
from connect_4_scene_switch import *
from _connect4_logic import *


class GAME_MODE():
    def __init__(self):
        self.gear_top_left = ROTATE(image.GEAR,(176,63),1.5)
        self.gear_top_right = ROTATE(image.GEAR,(1140,63),-1.5)
        self.__counter1 = 0
        self.fade_normal_glow = True
        self.fade_max_glow = False
        self.SINGLE_MATCH = False
        self.BEST_OF_4 = False
        self.COMPUTER = False
        self.black_surface = pg.Surface(game_window.MAIN_WINDOW.get_size())
        self.black_surface.set_alpha(50)
        self.__BACK_BUTTON = False
        self.switcher = 0

    def SHOW_GAMEMODE_BG_GLOW(self,n):
        image.GAME_MODE_BG_GLOW.set_alpha(n)
        BLIT(image.GAME_MODE_BG_GLOW,image.ORIGIN)

    def GAMEMODE_event_handler(self):
        if MOUSE_inside((406,539),(456,496)):
            self.SINGLE_MATCH = True
        else: self.SINGLE_MATCH = False

        if MOUSE_inside((595,715),(456,496)):
            self.BEST_OF_4 = True
        else: self.BEST_OF_4 = False

        if MOUSE_inside((773,888),(456,496)):
            self.COMPUTER = True
        else: self.COMPUTER = False

        if MOUSE_inside((1170,1256),(643,686)):
            self.__BACK_BUTTON = True
        else: self.__BACK_BUTTON = False

##--------------------------------- EVENT LOOP
        for event in pg.event.get():
            if event.type == QUIT:
                if scenes.get_previous_SCENE() != 'HOME':
                    scenes.create_scene('EXIT DIALOG')
            if event.type == MOUSEBUTTONDOWN:
                click = get_MOUSECLICK()
                if click[0]:
                    if self.SINGLE_MATCH:
                        logic.create_GAME_MODE('SINGLE MATCH')
                        scenes.create_scene('INGAME')
                        fade_out.start_fade_out()
                    elif self.BEST_OF_4:
                        logic.create_GAME_MODE('BEST OF 4')
                        scenes.create_scene('INGAME')
                        fade_out.start_fade_out()
                    elif self.COMPUTER:
                        scenes.create_scene('UNDER CONSTRUCTION')
                        fade_out.start_fade_out()
                    elif self.__BACK_BUTTON:
                        if scenes.get_previous_SCENE() == 'INGAME': pass
                        else:
                            scenes.create_scene('HOME')
                            fade_out.start_fade_out()

    def start_GAME_MODE(self):
        while scenes.scene == 'GAME MODE':
            BLIT(image.GAME_MODE_BG_NORMAL,image.ORIGIN)

            ##---------------------------------------- breathing fade
            if self.fade_normal_glow:
                if self.__counter1 < 300:
                    self.switcher = 0
                    self.fade_normal_glow = False
            elif self.fade_max_glow:
                if self.__counter1 < 0:
                    self.switcher = 0
                    self.fade_normal_glow = True
                    self.fade_max_glow = False

            if self.switcher == 0:
                self.__counter1+=10
                if self.__counter1 > 300:
                    self.switcher = 1
                    self.fade_max_glow = True
            elif self.switcher == 1:
                self.__counter1-=10

            self.SHOW_GAMEMODE_BG_GLOW(self.__counter1)

            self.gear_top_left.show_rotation()
            self.gear_top_right.show_rotation()
            image.SHOW_LIGHT_SHADE()

            if scenes.get_previous_SCENE() != 'INGAME':
                if scenes.get_previous_SCENE() != 'EXIT DIALOG':
                    BLIT(image.BACK_BUTTON,image.ORIGIN)

            if self.SINGLE_MATCH:
                BLIT(image.SINGLE_MATCH_GLOW,image.ORIGIN)
            if self.BEST_OF_4:
                BLIT(image.BEST_OF_4_GLOW,image.ORIGIN)
            if self.COMPUTER:
                BLIT(image.AI_GLOW,image.ORIGIN)
            if scenes.get_previous_SCENE() != 'INGAME':
                if scenes.get_previous_SCENE() != 'EXIT DIALOG':
                    if self.__BACK_BUTTON:
                        BLIT(image.BACK_BUTTON_GLOW,image.ORIGIN)


            image._CURSOR_MAIN()

            self.GAMEMODE_event_handler()

            #print_current_mouse_position()

            UPDATE()


def main():
    pass
#GEAR POSITION 1: 176,63

game_mode = GAME_MODE()

if __name__ == '__main__':
    scenes.scene = 'GAME MODE'
    game_mode.start_GAME_MODE()
