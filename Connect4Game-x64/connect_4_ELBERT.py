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


class ELBERT():
    def __init__(self):
        self.BACK = False
        self.BLUE_CURSOR = False
        self.SHOW_CURSOR_BACK = False
        self.__FADE = False
        self.counter = 0

    def cursor_toggle(self):
        if self.SHOW_CURSOR_BACK:
            image._CURSOR_BACK() #RED BACK CURSOR
        if self.BLUE_CURSOR:
            image._CURSOR_MAIN() #BLUE CURSOR

    def SHOW_FADE_TO_ELBERT(self,n):
        image.ELBERT.set_alpha(n)
        BLIT(image.ELBERT,image.ORIGIN)


    def elbert_event_handler(self):
        mouse_pos = get_MOUSEPOS()
        if -1000 < mouse_pos[0] < 284:
            self.BACK = True
            self.BLUE_CURSOR = False
            self.SHOW_CURSOR_BACK = True
        else:
            self.SHOW_CURSOR_BACK = False
            self.BLUE_CURSOR = True
            BACK = False

        for event in pg.event.get():
            if event.type == QUIT:
                scenes.create_scene('EXIT DIALOG')
            elif event.type == KEYDOWN:
                if event.key == K_f: #---------------- f
                    game_window.toggle_fullscreen()
                elif event.key == K_m:
                    sounds.toggle_mute('CREDITS')
            elif event.type == MOUSEBUTTONDOWN:
                click = CLICK()
                if click[0]:
                    if self.BACK:
                        scenes.from_outside = False
                        self.__FADE = True
                        scenes.from_inside = True
                        scenes.create_scene('CREDITS')
                        self.BACK = False

    def start_ELBERT(self):
        self.counter = 0
        while scenes.scene == 'ELBERT':
            if self.counter < 300:
                self.counter +=6
            self.SHOW_FADE_TO_ELBERT(self.counter)

            self.elbert_event_handler()
            self.cursor_toggle()

            if self.__FADE:
                fade_out.start_fade_out()
                self.__FADE = False

            UPDATE()

elbert = ELBERT()

if __name__ == '__main__':
    scenes.scene = 'ELBERT'
    elbert = ELBERT()
    elbert.start_ELBERT()