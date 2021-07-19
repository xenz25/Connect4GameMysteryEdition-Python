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

class OPTIONS1():
    def __init__(self):
        self.gear_bottom_right = ROTATE(image.GEAR,(1336,610),1.5)
        self.gear_bottom = ROTATE(image.GEAR,(1030,740),-1.5)
        self.__counter1 = 0
        self.options_panelX = 400
        self.SOUND = False
        self.FULL_SCREEN = False
        self.FULL_SCREEN_DISABLED = False
        self.SOUND_DISABLED = False
        self.click_sound, self.click_full = 0,0
        self.BACK = False
        self.CURSOR_AVAILABLE = False
        self.STARTING = True
        self.ENDING = False
        self.soundX = 400
        self.fullX = 400
        self.played_once = 0
        self.GEAR_START = False

    def reset(self):
        self.gear_bottom_right = ROTATE(image.GEAR,(1336,610),1.5)
        self.gear_bottom = ROTATE(image.GEAR,(1030,740),-1.5)
        self.__counter1 = 0
        self.options_panelX = 400
        self.SOUND = False
        self.FULL_SCREEN = False
        self.FULL_SCREEN_DISABLED = False
        self.SOUND_DISABLED = False
        self.click_sound, self.click_full = 0,0
        self.BACK = False
        self.CURSOR_AVAILABLE = False
        self.STARTING = True
        self.ENDING = False
        self.soundX = 400
        self.fullX = 400
        self.played_once = 0
        self.GEAR_START = False

    def SHOW_OPTIONS_BLUR(self,n):
        image.OPTIONS_BLUR.set_alpha(n)
        BLIT(image.OPTIONS_BLUR,image.ORIGIN)

    def OPTIONS1_event_handler(self):
        if self.CURSOR_AVAILABLE:
            ##----------------------------------------------- checking mouse position
            if MOUSE_inside((1087,1219),(243,274)):
                self.SOUND = True
            else: self.SOUND = False

            if MOUSE_inside((1111,1192),(325,403)):
                self.FULL_SCREEN = True
            else: self.FULL_SCREEN = False

            if MOUSE_inside((0,965),(0,718)):
                self.BACK = True
            else: self.BACK = False
##------------------------------------------------- events
        for event in pg.event.get():
            if event.type == QUIT:
                scenes.create_scene('EXIT DIALOG')

            elif event.type == MOUSEBUTTONDOWN:
                click = get_MOUSECLICK()
                if click[0]:
                    if self.SOUND:
                        self.click_sound+=1
                        self.click_sound%=2
                        if self.click_sound == 1:
                            self.SOUND_DISABLED = True
                        else: self.SOUND_DISABLED = False; print(True)
                        sounds.toggle_mute('HOME')
                    elif self.FULL_SCREEN:
                        self.click_full+=1
                        self.click_full%=2
                        if self.click_full == 0:
                            self.FULL_SCREEN_DISABLED = True
                        else: self.FULL_SCREEN_DISABLED = False
                        game_window.toggle_fullscreen()
                    elif self.BACK:
                        self.CURSOR_AVAILABLE = False
                        self.GEAR_START = False
                        self.STARTING = False; self.ENDING = True
                '''elif click[2]:
                    self.start_OPTIONS1()'''
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.CURSOR_AVAILABLE = False
                    self.GEAR_START = False
                    self.STARTING = False; self.ENDING = True

    def start_OPTIONS1(self):
        self.reset()

        while scenes.scene == 'OPTIONS1':
            if self.__counter1 < 300:
                if self.STARTING:
                    self.__counter1 += 10
            self.SHOW_OPTIONS_BLUR(self.__counter1)

            if self.__counter1 == 300:
                self.GEAR_START= True
                if self.STARTING:
                    if sounds.GLOBAL_SOUND:
                        if self.played_once == 1: pass
                        else: sounds.MOVING_PANEL_SOUND(); self.played_once = 1
                    else: self.played_once = 1
                    if self.options_panelX > 0:
                        self.options_panelX -= 10
                    if self.soundX > 0:
                        self.soundX -= 10
                    if self.fullX > 0:
                        self.fullX -= 10
            if self.ENDING:
                if sounds.GLOBAL_SOUND:
                    if self.played_once == 1: sounds.MOVING_PANEL_SOUND(); self.played_once = 0
                    else: pass
                if self.options_panelX < 400:
                    self.options_panelX += 10
                else:
                    if scenes.get_previous_SCENE() == 'HOME' or scenes.get_previous_SCENE() == 'EXIT DIALOG': fade_out.start_fade_out(); scenes.create_scene('HOME'); game_window.MAIN_WINDOW.fill(BLACK)
                    else: fade_out.start_fade_out(); scenes.create_scene(scenes.get_previous_SCENE()); game_window.MAIN_WINDOW.fill(BLACK)
            if self.options_panelX == 0: self.CURSOR_AVAILABLE = True
            BLIT(image.OPTIONS_PANEL,(self.options_panelX,image.ORIGIN[1]))

            if self.SOUND:
                BLIT(image.SOUND_GLOW,image.ORIGIN)
            if self.FULL_SCREEN:
                BLIT(image.FULL_SCREEN_GLOW,image.ORIGIN)


            if sounds.get_sound_condition():
                if self.ENDING:
                    if self.soundX < 400:
                        self.soundX += 10
                BLIT(image.SOUND_NON_ACTIVE,(self.soundX,image.ORIGIN[1]))
            if game_window.get_screen_condition():
                if self.ENDING:
                    if self.fullX < 400:
                        self.fullX += 10
                BLIT(image.FULL_SCREEN_NON_ACTIVE,(self.fullX,image.ORIGIN[1]))


            if self.GEAR_START:
                self.gear_bottom_right.show_rotation()
                self.gear_bottom.show_rotation()

            image._SHADOW()

            if self.BACK:
                if self.CURSOR_AVAILABLE:
                    image._CURSOR_BACK()
            else:
                if self.CURSOR_AVAILABLE:
                    image._CURSOR_MAIN()

            self.OPTIONS1_event_handler()

            #print_current_mouse_position()

            UPDATE()


def main():
    pass
#GEAR POSITION 1: 176,63

options1 = OPTIONS1()

if __name__ == '__main__':
    scenes.scene = 'OPTIONS1'
    options1.start_OPTIONS1()
