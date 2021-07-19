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

class LOGO():
    def __init__(self):
        self.__counter,self.__counter2,self.__counter3,self.__counter4, \
        self.__counter5, self.__counter6, self.__counter7, self.__counter8 = 0,0,0,0,0,0,0,300
        self.BLACK_SURFACE = pg.Surface(game_window.MAIN_WINDOW.get_size())
        self.BLACK_SURFACE.fill((0,0,0))
        #self.FADE_NOW_TO_LOGO = False
        self.FADE_NOW_TO_WARNING = True
        #self.FADE_NOW_TO_PRODUCTIONS = False
        self.CONNECT_4_illum = Ticker(0.2)
        self.FADE = False
        self.CLICK_ACTIVATED = False
        self.switcher = 0
        self.fade_normal_glow = True
        self.fade_max_glow = False
        self.cursor_pos = (0,0)
        self.fade1, self.fade2, self.fade3, self.fade4 = True,True,True,True

    def reset(self):
        self.__counter,self.__counter2,self.__counter3,self.__counter4, \
        self.__counter5, self.__counter6, self.__counter7, self.__counter8 = 0,0,0,0,0,0,0,300
        self.BLACK_SURFACE = pg.Surface(game_window.MAIN_WINDOW.get_size())
        self.BLACK_SURFACE.fill((0,0,0))
        #self.FADE_NOW_TO_LOGO = False
        self.FADE_NOW_TO_WARNING = True
        #self.FADE_NOW_TO_PRODUCTIONS = False
        self.CONNECT_4_illum = Ticker(0.2)
        self.FADE = False
        self.CLICK_ACTIVATED = False
        self.switcher = 0
        self.fade_normal_glow = True
        self.fade_max_glow = False
        self.cursor_pos = (0,0)
        self.fade1, self.fade2, self.fade3, self.fade4 = True,True,True,True


    def CONNECT_GLOW_I(self,num):
        if num == None:
            pass
        else:
            image.SHOW_LOGO_GLOW()

    def false_all_previous_fading(self):
        self.fade1, self.fade2, self.fade3, self.fade4 = False,False,False,False

    def SHOW_ACTUAL_LOGO(self,n):
        image.FULL_LOGO.set_alpha(n)
        BLIT(image.FULL_LOGO,image.ORIGIN)

    def SHOW_WARNING(self,n):
        image.WARNING.set_alpha(n)
        BLIT(image.WARNING,image.ORIGIN)

    def SHOW_PRODUCTIONS(self,n):
        image.PRODUCTIONS.set_alpha(n)
        BLIT(image.PRODUCTIONS,image.ORIGIN)

    def SHOW_LOGO_BLUR(self,n):
        image.LOGO_BLUR.set_alpha(n)
        BLIT(image.LOGO_BLUR,image.ORIGIN)

    def SHOW_BLACK_FADING_SURFACE(self,n):
        self.BLACK_SURFACE.set_alpha(n)
        BLIT(self.BLACK_SURFACE,image.ORIGIN)

    def SHOW_LOGO_MAX_BRIGHT(self,n):
        image.FULL_LOGO_MAX_BRIGHT.set_alpha(n)
        BLIT(image.FULL_LOGO_MAX_BRIGHT,image.ORIGIN)

    def __fade_in_logo(self,n):
        image.LOGO.set_alpha(n)
        BLIT(image.LOGO,image.ORIGIN)

    def logo_event_handler(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if self.CLICK_ACTIVATED:
                    if scenes.get_previous_SCENE() == 'CREDITS':
                        scenes.from_outside = True
                        scene_to_make = 'CREDITS'
                    else: scene_to_make = 'HOME'
                    if self.CLICK_ACTIVATED:
                        self.FADE = True
                        scenes.create_scene(scene_to_make)
            elif event.type == MOUSEBUTTONDOWN:
                if self.CLICK_ACTIVATED:
                    click = CLICK()
                    if click[0]:
                        if scenes.get_previous_SCENE() == 'CREDITS':
                            scenes.from_outside = True
                            scene_to_make = 'CREDITS'
                        else: scene_to_make = 'HOME'
                        if self.CLICK_ACTIVATED:
                            self.FADE = True
                            scenes.create_scene(scene_to_make)


    def start_logo_animation(self):
        self.reset()
        BLIT(self.BLACK_SURFACE,image.ORIGIN)
        sounds.fadeout_ALL()
        sounds.FADE_WOOSH()
        sounds.play_next(sounds.OPENING,-1)
        while scenes.scene == 'LOGO':
            #self.FADE_NOW_TO_WARNING:
                #image.WARNING()
            ##---------------------------- show the fading of warning
            if self.FADE_NOW_TO_WARNING:
                self.__counter3+=3
                self.SHOW_WARNING(self.__counter3)

            ##---------------------------- show black surface first to cover previous
            if self.fade1:
                if self.__counter3 > 300:
                    self.FADE_NOW_TO_WARNING = False
                    self.__counter5 += 6
                    self.SHOW_BLACK_FADING_SURFACE(self.__counter5)
                    ##---------------------------- show the fading of productions
                    if self.__counter5 > 300:
                        self.__counter4+=3
                        self.SHOW_PRODUCTIONS(self.__counter4)

            ##---------------------------- show black surface first to cover previous
            if self.fade2:
                if self.__counter4 > 300:
                    self.__counter6 += 6
                    self.SHOW_BLACK_FADING_SURFACE(self.__counter6)

            ##---------------------------- show the fading initial image
            if self.fade4:
                if self.__counter6 > 300:
                    self.__counter6 = 301
                    self.__counter+=4
                    self.__fade_in_logo(self.__counter)
                    ##------------------------------------------------------ manage the blinking effect
                    #connect_title_time = self.CONNECT_4_illum.delay()
                    #self.CONNECT_GLOW_I(connect_title_time)

            ##---------------------------- show the second image after a second of blinking
            if self.__counter > 300:
                self.false_all_previous_fading()
                self.__counter2 += 3
                self.SHOW_ACTUAL_LOGO(self.__counter2)
                if self.__counter2 > 300:
                    ##---------------------------------------- breathing fade
                    if self.fade_normal_glow:
                        if self.__counter7 < 300:
                            self.switcher = 0
                            self.fade_normal_glow = False
                    elif self.fade_max_glow:
                        if self.__counter7 < 0:
                            self.switcher = 0
                            self.fade_normal_glow = True
                            self.fade_max_glow = False
                    if self.switcher == 0:
                        self.__counter7+=8
                        if self.__counter7 > 300:
                            self.switcher = 1
                            self.fade_max_glow = True
                    elif self.switcher == 1:
                        self.__counter7-=8
                    self.SHOW_LOGO_MAX_BRIGHT(self.__counter7)
                    ##-----------------------------------------
                    self.CLICK_ACTIVATED = True



            self.logo_event_handler()

            if self.FADE:
                fade_out.start_fade_out()
                self.FADE = False

            UPDATE()

logo = LOGO()

if __name__ == '__main__':
    scenes.scene = 'LOGO'
    logo.start_logo_animation()

