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

pg.init()


class HOME_SCENE():
    def __init__(self,start_this_again = False):

        self.HOME_OVER = False
        #--------------------------------------------------------- HOME GLOBALS
        self.play_glow = False
        self.options_glow = False
        self.extras_glow = False
        self.exit_glow = False
        self.how_to_play_glow = False
        self.FADE_TO_PLAY = False

        self.PLAY = False
        self.EXIT = False
        self.EXTRAS = False
        self.OPTIONS = False
        self.HOW_TO_PLAY = False
        self.CREDITS = False
        self.CREDITS_IS_AVAILABLE = False

        self.BALLOON_STARTING_POSY = window_scale[1]+10
        self.balloon_y_position = self.BALLOON_STARTING_POSY

        '''self.PLAY_BN = NEW_XY_WH((449,327),(638,369))
        self.OPTIONS_BN = NEW_XY_WH((438,405),(628,455))
        self.EXTRAS_BN= NEW_XY_WH((470,489),(660,529))
        self.HOW_BN = NEW_XY_WH((183,381),(227,571))
        self.EXIT_BN = NEW_XY_WH((702,521),(892,567))'''

        self.HOME_WAS_QUIT = start_this_again
        self.arrow_illum = Ticker(0.1)
        self.light_flick = Ticker(0.9)
        self.connect_4_illum = Ticker(1)

    def FALSE_ALL(self):
        self.PLAY = False
        self.EXIT = False
        self.EXTRAS = False
        self.BACK_FROM_EXTRAS = False
        self.OPTIONS = False
        self.HOW_TO_PLAY = False
        self.CREDITS = False
        self.CREDITS_IS_AVAILABLE = False
        self.EVERYTHING_IS_AVAILABLE = False

    def HOME_ARROW_I(self,num):
        if num == 0 or num == 3:
            image.ARROW_G()

    def LIGHT_FLICK_I(self,num):
        if num == 0 or num == 3:
            image.LIGHT_FLICK()

    def CONNECT_TITLE_I(self,num):
        if num == 0 or num == 3:
            image.CONNECT_4_GLOW()

    def BALLOON_ANIMATION(self,y):
        if y < 0:
            self.CREDITS_IS_AVAILABLE = True
            self.EVERYTHING_IS_AVAILABLE = True
            y = 0
        image.SHOW_BALLOON(y)


    def HOME_Event_Handler(self):
        if self.EVERYTHING_IS_AVAILABLE:
            if self.CREDITS_IS_AVAILABLE:
                if MOUSE_inside((1058,1131),(296,393)):
                    self.CREDITS = True
                else: self.CREDITS = False

            ##------------------------------------------------------------------- HOME BUTTONS
            if MOUSE_inside((449,638),(327,369)): #play
                self.PLAY = True
                self.play_glow = True
            else: self.PLAY = False

            if MOUSE_inside((436,628),(405,455)): #options
                self.OPTIONS = True
                self.options_glow = True
            else: self.OPTIONS = False

            if MOUSE_inside((470,660),(489,529)): #extras
                self.EXTRAS = True
                self.extras_glow = True
            else: self.EXTRAS = False

            if MOUSE_inside((702,892),(521,567)): #exit
                self.EXIT = True
                self.exit_glow = True
            else: self.EXIT = False

            if MOUSE_inside((183,227),(381,571)): #how to play
                self.HOW_TO_PLAY = True
                self.how_to_play_glow = True
            else: self.HOW_TO_PLAY = False

        for event in pg.event.get():
            if event.type == QUIT:
                scenes.create_scene('EXIT DIALOG')
            if event.type == KEYDOWN:
                if event.key == K_f: #---------------- f
                    game_window.toggle_fullscreen()
                elif event.key == K_m:
                    sounds.toggle_mute(scenes.scene)
            if event.type == MOUSEBUTTONDOWN:
                click = CLICK()
                if click[0] :
                    if self.EXIT:
                        scenes.create_scene('EXIT DIALOG')
                    if self.PLAY:
                        self.FADE_TO_PLAY = True
                        scenes.create_scene('GAME MODE')
                    if self.EXTRAS:
                        scenes.create_scene('UNDER CONSTRUCTION')
                    if self.HOW_TO_PLAY:
                        if scenes.HOW_TO_PLAY_IS_SELECTED: pass
                        else:
                            scenes.HOW_TO_PLAY_IS_SELECTED = True
                            scenes.from_ingame_access = False
                            scenes.from_home_access = True
                        fade_out.start_fade_out()
                        scenes.create_scene('HOW TO PLAY')
                    if self.CREDITS:
                        scenes.from_outside = True
                        scenes.from_inside = False
                        scenes.create_scene('CREDITS')
                    if self.OPTIONS:
                        scenes.create_scene('OPTIONS1')


    def HOME(self):
        image.HOME_BRICKBG()
        if scenes.HOW_TO_PLAY_IS_SELECTED == False:
            image.ARROW_G(); image.HOW_TO_PLAY_G()
        #----------------------------------------------- flicker functions
        arrow_time = self.arrow_illum.delay()
        self.HOME_ARROW_I(arrow_time)

        light_time = self.light_flick.delay()
        self.LIGHT_FLICK_I(light_time)

        connect_title_time = self.connect_4_illum.delay()
        self.CONNECT_TITLE_I(connect_title_time)

        if self.EVERYTHING_IS_AVAILABLE:
    #--------------------------------------- BUTTON GLOW EFFECTS
            if self.play_glow:
                image.PLAY_G()
            self.play_glow = False

            if self.options_glow:
                image.OPTIONS_G()
            self.options_glow = False

            if self.extras_glow:
                image.EXTRAS_G()
            self.extras_glow = False

            if self.how_to_play_glow:
                image.HOW_TO_PLAY_G()
            self.how_to_play_glow = False

            if self.exit_glow:
                image.EXIT_G()
            self.exit_glow = False

#---------------------------------------------------------- BALLOON ANIMATION
        self.BALLOON_ANIMATION(self.balloon_y_position)
        self.balloon_y_position -= 5


    def start_HOME(self):
        self.FALSE_ALL()
        if sounds.GLOBAL_SOUND:
            if scenes.get_previous_SCENE() == 'LOGO' or scenes.get_previous_SCENE() == 'EXIT DIALOG' \
            or scenes.get_previous_SCENE() == 'GAME MODE' or scenes.get_previous_SCENE() == 'OPTIONS1'\
            or scenes.get_previous_SCENE() == 'HOW TO PLAY': pass
            else:
                sounds.fadeout_ALL()
                sounds.OPENING_SOUND()
        while scenes.scene == 'HOME':
            self.HOME()
            self.HOME_Event_Handler()

            if self.FADE_TO_PLAY:
                fade_out.start_fade_out()
                self.FADE_TO_PLAY = False

            if self.EVERYTHING_IS_AVAILABLE:
                image._CURSOR_MAIN()

            UPDATE()


if __name__ == '__main__':
    scenes.scene = 'HOME'
    home = HOME_SCENE()
    home.start_HOME()

