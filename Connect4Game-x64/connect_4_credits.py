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
from _connect4_sounds import *


class CREDITS_SCENE():
    def __init__(self):
        self.FLICKER_LIGHTS = Ticker(0.05)
        self.BACK = False
        self.BLUE_CURSOR = False
        self.SHOW_CURSOR_BACK = False
        self.counter = 0

        self.STEVEN_ACTIVE = False
        self.XEN_ACTIVE = False
        self.ELBERT_ACTIVE = False
        self.LAURENT_ACTIVE = False
        self.LOGO_ANIMATION_ACTIVE = False

        '''self.BOX = pg.image.load('BOX_GREEN.png')
        self.BOX_RECT = RECT(self.BOX)
        self.SCREEN_RECT = RECT(game_window.MAIN_WINDOW)
        self.CURRENT = (0,0)
        self.touched = False'''

        self.__FADE = False

    def cursor_toggle(self):
        if self.SHOW_CURSOR_BACK:
            image._CURSOR_BACK() #RED BACK CURSOR
        if self.BLUE_CURSOR:
            image._CURSOR_MAIN() #BLUE CURSOR


    def FLASHLIGHT_FLICK_I(self,num):
        if num == 0 or num == 3:
            image.LIGHT_FLICK()


    def SHOW_FADE_TO_CREDITS(self,n):
        image.CREDITS.set_alpha(n)
        BLIT(image.CREDITS,image.ORIGIN)


    def CREDITS_EVENT_HANDLER(self):
        mouse_pos = get_MOUSEPOS()

        if -1000 < mouse_pos[0] < 284:
            BACK = True
            self.BLUE_CURSOR = False
            self.SHOW_CURSOR_BACK = True
        else:
            self.SHOW_CURSOR_BACK = False
            self.BLUE_CURSOR = True
            BACK = False

        if MOUSE_inside((770,784),(337,359)):
            self.STEVEN_ACTIVE = True
        else: self.STEVEN_ACTIVE = False

        if MOUSE_inside((812,852),(306,326)):
            self.XEN_ACTIVE = True
        else: self.XEN_ACTIVE = False

        if MOUSE_inside((788,806),(378,397)):
            self.LAURENT_ACTIVE = True
        else: self.LAURENT_ACTIVE = False

        if MOUSE_inside((782,797),(411,434)):
            self.ELBERT_ACTIVE = True
        else: self.ELBERT_ACTIVE = False

        if MOUSE_inside((296,326),(233,267)):
            self.LOGO_ANIMATION_ACTIVE = True
        else: self.LOGO_ANIMATION_ACTIVE = False


        for event in pg.event.get():
            if event.type == QUIT:
                scenes.create_scene('EXIT DIALOG')
            elif event.type == KEYDOWN:
                if event.key == K_f: #---------------- f
                    game_window.toggle_fullscreen()
                elif event.key == K_m:
                    sounds.toggle_mute(scenes.scene)
            elif event.type == MOUSEBUTTONDOWN:
                '''if self.BOX_RECT.collidepoint(event.pos):
                    self.touched = True
                    pg.mouse.get_rel()'''
                click = CLICK()
                if click[0]:
                    if BACK:
                        sounds.fadeout_ALL()
                        self.__FADE = True
                        scenes.create_scene('HOME')
                        self.BACK = False
                    if self.STEVEN_ACTIVE:
                        self.__FADE = True
                        scenes.create_scene('STEVEN')
                    if self.XEN_ACTIVE:
                        self.__FADE = True
                        scenes.create_scene('XEN')
                    if self.LAURENT_ACTIVE:
                        self.__FADE = True
                        scenes.create_scene('LAURENT')
                    if self.ELBERT_ACTIVE:
                        self.__FADE = True
                        scenes.create_scene('ELBERT')
                    if self.LOGO_ANIMATION_ACTIVE:
                        scenes.create_scene('LOGO')
            '''elif event.type == MOUSEBUTTONUP:
                self.touched = False'''



    def start_CREDITS(self):
        self.counter = 0
        if sounds.GLOBAL_SOUND:
            if scenes.get_previous_SCENE() == 'EXIT DIALOG': pass
            else:
                if scenes.from_inside: pass
                elif scenes.from_outside:
                    sounds.fadeout_ALL()
                    sounds.CREDITS_SOUND()
        while scenes.scene == 'CREDITS':
            HIDE_CURSOR(False)

            if self.counter < 300:
                self.counter +=6
            self.SHOW_FADE_TO_CREDITS(self.counter)

            '''BLIT(self.BOX,self.CURRENT)
            if self.touched:
                self.BOX_RECT.move_ip(pg.mouse.get_rel())
                self.BOX_RECT.clamp_ip(self.SCREEN_RECT)
                self.CURRENT = self.BOX_RECT.topleft
                BLIT(self.BOX,self.BOX_RECT)'''

            if not scenes.from_inside:
                flashlight_time = self.FLICKER_LIGHTS.delay()
                self.FLASHLIGHT_FLICK_I(flashlight_time)

            self.cursor_toggle()

            self.CREDITS_EVENT_HANDLER()

            if self.__FADE:
                fade_out.start_fade_out()
                self.__FADE = False

            #print_current_mouse_position()

            UPDATE()




credits = CREDITS_SCENE()

if __name__ == '__main__':
    scenes.scene = 'CREDITS'
    credits = CREDITS_SCENE()
    credits.start_CREDITS()






