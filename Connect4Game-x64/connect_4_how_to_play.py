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

class HOW_TO_PLAY():
    def __init__(self):
        self.gear2 = image.GEAR
        self.gear2 = pg.transform.scale(self.gear2,(211,211))
        self.gear_bottom_right = ROTATE(image.GEAR,(1320,192),1.5)
        self.gear_bottom = ROTATE(self.gear2,(1320,458),-1.5)
        self.gear_top = ROTATE(image.GEAR,(0,0),2)
        self.__counter1 = 0
        self.options_panelX = 400
        self.WELCOME = True
        self.RULES = False
        self.GUIDES = False
        self.BACK = False

        self.WELCOME_GLOW = True
        self.RULES_GLOW = False
        self.GUIDES_GLOW = False
        self.BACK_GLOW = False

        self.BUTTON_LEFT = False
        self.BUTTON_RIGHT = False
        self.CURSOR_AVAILABLE = True
        self.what_scene_number = 0
        self.DISABLE_FALSING_welcome = True
        self.DISABLE_FALSING_rules = False
        self.DISABLE_FALSING_guides = False
        self.DISABLE_FALSING_back = False


    def reset(self):
        self.gear2 = image.GEAR
        self.gear2 = pg.transform.scale(self.gear2,(211,211))
        self.gear_bottom_right = ROTATE(image.GEAR,(1320,192),1.5)
        self.gear_bottom = ROTATE(self.gear2,(1320,458),-1.5)
        self.gear_top = ROTATE(image.GEAR,(0,0),2)
        self.__counter1 = 0
        self.options_panelX = 400
        self.WELCOME = True
        self.RULES = False
        self.GUIDES = False
        self.BACK = False

        self.WELCOME_GLOW = True
        self.RULES_GLOW = False
        self.GUIDES_GLOW = False
        self.BACK_GLOW = False

        self.BUTTON_LEFT = False
        self.BUTTON_RIGHT = False
        self.CURSOR_AVAILABLE = True
        self.what_scene_number = 0
        self.DISABLE_FALSING_welcome = True
        self.DISABLE_FALSING_rules = False
        self.DISABLE_FALSING_guides = False
        self.DISABLE_FALSING_back = False

    def false_all_GLOW(self):
        self.WELCOME_GLOW = False
        self.RULES_GLOW = False
        self.GUIDES_GLOW = False
        self.BACK_GLOW = False



    def WELCOME1(self,n):
        image.WELCOME.set_alpha(n)
        BLIT(image.WELCOME,image.ORIGIN)

    def RULE1(self,n):
        image.RULES1.set_alpha(n)
        BLIT(image.RULES1,image.ORIGIN)

    def RULE2(self,n):
        image.RULES2.set_alpha(n)
        BLIT(image.RULES2,image.ORIGIN)


    def BLUE_CURSOR(self,n):
        image.BLUE_CURSOR_GUIDE.set_alpha(n)
        BLIT(image.BLUE_CURSOR_GUIDE,image.ORIGIN)

    def BACK_CURSOR(self,n):
        image.BACK_GUIDE.set_alpha(n)
        BLIT(image.BACK_GUIDE,image.ORIGIN)

    def SM_GUIDE(self,n):
        image.SINGLE_MATCH.set_alpha(n)
        BLIT(image.SINGLE_MATCH,image.ORIGIN)

    def B4_MATCH(self,n):
        image.B4_MATCH.set_alpha(n)
        BLIT(image.B4_MATCH,image.ORIGIN)

    def AI_MATCH(self,n):
        image.AI_MATCH.set_alpha(n)
        BLIT(image.AI_MATCH,image.ORIGIN)

    def CHIP_GUIDE(self,n):
        image.CHIP_INFO.set_alpha(n)
        BLIT(image.CHIP_INFO,image.ORIGIN)

    def BOARD_GUIDE(self,n):
        image.BOARD_INFO.set_alpha(n)
        BLIT(image.BOARD_INFO,image.ORIGIN)

    def SWAP_GUIDE(self,n):
        image.SWAP_B_INFO.set_alpha(n)
        BLIT(image.SWAP_B_INFO,image.ORIGIN)

    def NEW_GUIDE(self,n):
        image.NEW_B_INFO.set_alpha(n)
        BLIT(image.NEW_B_INFO,image.ORIGIN)

    def OPTIONS_GUIDE(self,n):
        image.OPTIONS_B_INFO.set_alpha(n)
        BLIT(image.OPTIONS_B_INFO,image.ORIGIN)

    def DROP_GUIDE(self,n):
        image.DROP_GUIDE.set_alpha(n)
        BLIT(image.DROP_GUIDE,image.ORIGIN)

    def CLOCK_GUIDE(self,n):
        image.CLOCK_GUIDE.set_alpha(n)
        BLIT(image.CLOCK_GUIDE,image.ORIGIN)

    def SCORE_GUIDE(self,n):
        image.SCORE_GUIDE.set_alpha(n)
        BLIT(image.SCORE_GUIDE,image.ORIGIN)

    def TURN_GUIDE(self,n):
        image.TURN_GUIDE.set_alpha(n)
        BLIT(image.TURN_GUIDE,image.ORIGIN)


    def HOW_TO_PLAY_event_handler(self):
        if self.CURSOR_AVAILABLE:
            ##----------------------------------------------- checking mouse position
            if MOUSE_inside((51,229),(246,268)): #WELCOME BUTTON
                self.WELCOME = True
            else: self.WELCOME = False

            if MOUSE_inside((90,199),(331,353)): #RULES BUTTON
                self.RULES = True
            else: self.RULES = False

            if MOUSE_inside((75,203),(429,448)): #GUIDES BUTTON
                self.GUIDES = True
            else: self.GUIDES = False

            if MOUSE_inside((1184,1266),(642,662)): #BACK BUTTON
                self.BACK = True
            else: self.BACK = False

            if MOUSE_inside((384,439),(326,379)): #left button
                self.BUTTON_LEFT = True
            else: self.BUTTON_LEFT = False

            if MOUSE_inside((1115,1170),(326,379)): #right button
                self.BUTTON_RIGHT = True
            else: self.BUTTON_RIGHT = False
##------------------------------------------------- events
        for event in pg.event.get():
            if event.type == QUIT:
                pass
            elif event.type == MOUSEBUTTONDOWN:
                click = CLICK()
                if click[0]:
                    if self.WELCOME: ##------------------------------------- WELCOME
                        self.__counter1 = 0
                        self.what_scene_number = 0
                    if self.RULES: ##----------------------- RULES
                        if self.what_scene_number == 1: self.what_scene_number = 1
                        elif self.what_scene_number == 2: self.what_scene_number = 2
                        else: self.__counter1 = 0; self.what_scene_number = 1
                    if self.GUIDES: ##------------------------------------- GUIDES
                        if self.what_scene_number > 2: self.what_scene_number = self.what_scene_number
                        else: self.__counter1 = 0; self.what_scene_number = 3
                    if self.BACK: ##------------------------------------- BACK
                        fade_out.start_fade_out()
                        if scenes.from_home_access:
                            scenes.create_scene('HOME')
                        elif scenes.from_ingame_access:
                            scenes.create_scene('INGAME')
                    if self.BUTTON_LEFT:
                        self.__counter1 = 0
                        if self.what_scene_number == 0: pass
                        else: self.what_scene_number -=1
                    if self.BUTTON_RIGHT:
                        self.what_scene_number +=1
                        self.__counter1 = 0

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    scenes.create_scene('OPTIONS1')

    def start_HOW_TO_PLAY(self):
        self.reset()
        if scenes.get_previous_SCENE() == 'EXIT DIALOG' or scenes.get_previous_SCENE() == 'OPTIONS1': pass
        else:
            if sounds.GLOBAL_SOUND:
                sounds.fadeout_ALL(); sounds.HOW_TO_PLAY_SOUND()

        while scenes.scene == 'HOW TO PLAY':
            ##--------------------------------------- PAGE SWITCHING
            if self.what_scene_number == 0:
                self.false_all_GLOW()
                self.WELCOME_GLOW = True
            elif self.what_scene_number == 1 or self.what_scene_number == 2:
                self.false_all_GLOW()
                self.RULES_GLOW = True
            elif self.what_scene_number > 2:
                self.false_all_GLOW()
                self.GUIDES_GLOW = True

            if self.what_scene_number == 0:
                self.WELCOME1(self.__counter1)
            elif self.what_scene_number == 1:
                self.RULE1(self.__counter1)
            elif self.what_scene_number == 2:
                self.RULE2(self.__counter1)
            elif self.what_scene_number == 3:
                self.BLUE_CURSOR(self.__counter1)
            elif self.what_scene_number == 4:
                self.BACK_CURSOR(self.__counter1)
            elif self.what_scene_number == 5:
                self.SM_GUIDE(self.__counter1)
            elif self.what_scene_number == 6:
                self.B4_MATCH(self.__counter1)
            elif self.what_scene_number == 7:
                self.AI_MATCH(self.__counter1)
            elif self.what_scene_number == 8:
                self.CHIP_GUIDE(self.__counter1)
            elif self.what_scene_number == 9:
                self.BOARD_GUIDE(self.__counter1)
            elif self.what_scene_number == 10:
                self.SWAP_GUIDE(self.__counter1)
            elif self.what_scene_number == 11:
                self.NEW_GUIDE(self.__counter1)
            elif self.what_scene_number == 12:
                self.OPTIONS_GUIDE(self.__counter1)
            elif self.what_scene_number == 13:
                self.DROP_GUIDE(self.__counter1)
            elif self.what_scene_number == 14:
                self.CLOCK_GUIDE(self.__counter1)
            elif self.what_scene_number == 15:
                self.SCORE_GUIDE(self.__counter1)
            elif self.what_scene_number == 16:
                self.TURN_GUIDE(self.__counter1)
            else: self.what_scene_number = 16

            if self.__counter1<300:
                self.__counter1 += 50
            BLIT(image.HOW_TO_PLAY_TOP_BG,image.ORIGIN)

            if self.WELCOME_GLOW:
                BLIT(image.WELCOME_GLOW,image.ORIGIN)
            if self.RULES_GLOW:
                BLIT(image.RULE_GLOW,image.ORIGIN)
            if self.GUIDES_GLOW:
                BLIT(image.GUIDES_GLOW,image.ORIGIN)
            if self.BUTTON_LEFT:
                BLIT(image.BUTTON_LEFT_GLOW,image.ORIGIN)
            if self.BUTTON_RIGHT:
                BLIT(image.BUTTON_RIGHT_GLOW,image.ORIGIN)
            if self.BACK:
                BLIT(image.BACK_GLOW,image.ORIGIN)


            self.gear_bottom_right.show_rotation()
            self.gear_bottom.show_rotation()
            self.gear_top.show_rotation()

            image._SHADOW()
            image._CURSOR_MAIN()

            self.HOW_TO_PLAY_event_handler()

            #print_current_mouse_position()
            #print(self.what_scene_number)

            UPDATE()


how_to_play = HOW_TO_PLAY()

if __name__ == '__main__':
    scenes.scene = 'HOW TO PLAY'
    how_to_play.start_HOW_TO_PLAY()
