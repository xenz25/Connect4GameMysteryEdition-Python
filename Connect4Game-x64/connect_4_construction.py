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


class UNDER_CONSTRUCTION():
    def __init__(self):
        self.BACK = False
        self.BLUE_CURSOR = False
        self.SHOW_CURSOR_BACK = False

    def UNDER_EVENT_HANDLER(self):
        mouse_pos = get_MOUSEPOS()

        if -1000 < mouse_pos[0] < 284:
            BACK = True
            self.BLUE_CURSOR = False
            self.SHOW_CURSOR_BACK = True
        else:
            self.SHOW_CURSOR_BACK = False
            self.BLUE_CURSOR = True
            BACK = False

        for event in pg.event.get():
            if event.type == QUIT:
                scenes.create_scene('EXIT DIALOG')
            if event.type == KEYDOWN:
                if event.key == K_f: #---------------- f
                    game_window.toggle_fullscreen()
            elif event.type == MOUSEBUTTONDOWN:
                click = CLICK()
                if click[0]:
                    if BACK:
                        scenes.create_scene(scenes.get_previous_SCENE())
                        self.BACK = False

    def start_UNDER_CONSTRUCTION(self):
        while scenes.scene == 'UNDER CONSTRUCTION':
            HIDE_CURSOR(False)
            mouse_pos = get_MOUSEPOS()
            image._UNDER_CONSTRUCTION()

            if self.SHOW_CURSOR_BACK:
                image._CURSOR_BACK() #RED BACK CURSOR
            if self.BLUE_CURSOR:
                image._CURSOR_MAIN() #BLUE CURSOR

            self.UNDER_EVENT_HANDLER()
            UPDATE()


if __name__ == '__main__':
    scenes.scene = 'UNDER CONSTRUCTION'
    under_construction = UNDER_CONSTRUCTION()
    under_construction.start_UNDER_CONSTRUCTION()