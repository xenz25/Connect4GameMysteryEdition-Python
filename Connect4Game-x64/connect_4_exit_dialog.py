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

class EXIT_DIALOG():
    def __init__(self):
        self.YES_GLOW = False
        self.NO_GLOW = False
        self.YES = False
        self.NO = False
        self.FADE = False
        self.FADE2 = True

    def show_yes_no(self):
        if self.YES_GLOW:
            image.SHOW_QUIT_DIALOG_YES_GLOW()

        if self.NO_GLOW:
            image.SHOW_QUIT_DIALOG_NO_GLOW()

    def __exit_dialog_event_handler(self):
        if MOUSE_inside((494,568),(386,418)): #YES
            self.YES = True
            self.YES_GLOW = True
        else:
            self.YES = False
            self.YES_GLOW = False

        if MOUSE_inside((725,800),(386,418)): #NO
            self.NO = True
            self.NO_GLOW = True
        else:
            self.NO = False
            self.NO_GLOW = False

        for event in pg.event.get():
            if event.type == QUIT:
                pass
            elif event.type == MOUSEBUTTONDOWN:
                click = CLICK()
                if click[0]:
                    if self.YES:
                        self.FADE = True
                    if self.NO:
                        fade_out.start_fade_out()
                        prev_scene = scenes.get_previous_SCENE()
                        scenes.create_scene(scenes.get_previous_SCENE())

    def start_EXIT_DIALOG(self):
        self.FADE2 = True
        while scenes.scene == 'EXIT DIALOG':
            if self.FADE2:
                fade_out.start_fade_out()
                self.FADE2 = False

            image.SHOW_EXIT_DIALOG()
            self.show_yes_no()
            self.__exit_dialog_event_handler()

            if self.FADE:
                fade_out.start_fade_out('QUIT')
                self.FADE = False

            image._CURSOR_MAIN()

            #print_current_mouse_position()

            UPDATE()

exit_dialog = EXIT_DIALOG()


if __name__ == '__main__':
    scenes.scene = 'EXIT DIALOG'
    exit_dialog = EXIT_DIALOG()
    exit_dialog.start_EXIT_DIALOG()

