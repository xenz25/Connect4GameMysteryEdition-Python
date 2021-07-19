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
from _connect4_logic import * # WINNER, POSTIONS DROP
from connect_4_images import * # BLIT, RECT, SCREEN, SOUNDS
from time import strftime
from connect_4_scene_switch import *
from connect_4_options2 import *

pg.init()

image = IMAGES() #CLASS IMAGES

IN_GAME_OVER = False
#------------------------------- INGAME GLOBALS
CURSOR_RED = False
CURSOR_YELLOW = False
MAIN_CURSOR = True


VELOCITY = 10

TURN_NUMBER = 0
GAME_STARTED = False

_I_BOARD = False
_I_BOARD2 = False
MULTIPLIER1 = 1
MULTIPLIER2 = 1
MULTIPLIER3 = 1
MULTIPLIER4 = 1
MULTIPLIER5 = 1

puppet = False
elephantleft = False
elephantright = False
hover_count = 0
MOVEx = 0
MOVEy = 0

DROP = False

SQUARE_SIZE = int(image.BOARDRECT.width/7)/2
BOX_SIZE = int(image.BOARDRECT.width/7)
DROP_SPEED = int(BOX_SIZE/2)


#---------------------


class INGAME_HELPER():
    def __init__(self):
        self.SHOW_WELCOME = True
        self.FALSE_OTHER = True
        self.show_winner_info = False
        self.P1_SCORE = logic.get_CURRENT_SCORE(1)
        self.P2_SCORE = logic.get_CURRENT_SCORE(2)
        ##---------------------- P1
        self.P1_score_0 = False
        self.P1_score_1 = False
        self.P1_score_2 = False
        self.P1_score_3 = False
        self.P1_score_4 = False
        self.ENABLE_INGAME_MOUSE = True
        self.ENABLE_WIN_MOUSE = False

        ##---------------------- P2
        self.P2_score_0 = False
        self.P2_score_1 = False
        self.P2_score_2 = False
        self.P2_score_3 = False
        self.P2_score_4 = False

        self.P1_GLOW_NOW = True
        self.P2_GLOW_NOW = False
        self.P1_CHIP_YELLOW = False

        self.P1_COLOR = image.RED_C1
        self.P2_COLOR = image.YELLOW_C1
        self.swapper = 0

        self.PLAYER_ONE_SHOW_CHIP = False
        self.PLAYER_TWO_SHOW_CHIP = False
        self.SHOW_CHIP = False
        self.THEY_SWAP = False

    def init_B4(self):
        self.P1_SCORE = logic.get_CURRENT_SCORE(1)

        if self.P1_SCORE == 0: self.P1_score_0 = True
        else: self.P1_score_0 = False
        if self.P1_SCORE == 1: self.P1_score_1 = True
        else: self.P1_score_1 = False
        if self.P1_SCORE == 2: self.P1_score_2 = True
        else: self.P1_score_2 = False
        if self.P1_SCORE == 3: self.P1_score_3 = True
        else: self.P1_score_3 = False
        if self.P1_SCORE == 4: self.P1_score_4 = True
        else: self.P1_score_4 = False

        self.P2_SCORE = logic.get_CURRENT_SCORE(2)

        if self.P2_SCORE == 0: self.P2_score_0 = True
        else: self.P2_score_0 = False
        if self.P2_SCORE == 1: self.P2_score_1 = True
        else: self.P2_score_1 = False
        if self.P2_SCORE == 2: self.P2_score_2 = True
        else: self.P2_score_2 = False
        if self.P2_SCORE == 3: self.P2_score_3 = True
        else: self.P2_score_3 = False
        if self.P2_SCORE == 4: self.P2_score_4 = True
        else: self.P2_score_4 = False

    def _reset(self):
        self.SHOW_WELCOME = True
        self.FALSE_OTHER = True
        self.show_winner_info = False
        self.P1_SCORE = logic.get_CURRENT_SCORE(1)
        self.P2_SCORE = logic.get_CURRENT_SCORE(2)
        ##---------------------- P1
        self.P1_score_0 = False
        self.P1_score_1 = False
        self.P1_score_2 = False
        self.P1_score_3 = False
        self.P1_score_4 = False
        self.ENABLE_INGAME_MOUSE = True
        self.ENABLE_WIN_MOUSE = False

        ##---------------------- P2
        self.P2_score_0 = False
        self.P2_score_1 = False
        self.P2_score_2 = False
        self.P2_score_3 = False
        self.P2_score_4 = False

        self.P1_GLOW_NOW = True
        self.P2_GLOW_NOW = False
        self.P1_CHIP_YELLOW = False

        self.P1_COLOR = image.RED_C1
        self.P2_COLOR = image.YELLOW_C1
        self.swapper = 0

        self.PLAYER_ONE_SHOW_CHIP = False
        self.PLAYER_TWO_SHOW_CHIP = False
        self.SHOW_CHIP = False

    def DISABLE_INGAME_MOUSE(self):
        global SHOW_CHIP
        self.SHOW_CHIP = False
        self.show_winner_info = True
        self.ENABLE_INGAME_MOUSE = False

    def FALSE_OTHER_INFOS(self):
        self.SHOW_WELCOME = False
        self.FALSE_OTHER = False

ingame_helper = INGAME_HELPER()

class WINNER():
    def __init__(self):
        self.show_winner_one = False
        self.show_winner_two = False
        self.show_tie = False
        self.new_glow = False
        self.quit_glow = False
        self.show_next_round_glow = False
        self.winner_exiting = False

    def show_winner(self,number):
        if number == 0:
            self.show_tie = True
        elif number == 1:
            self.show_winner_one = True
        elif number == 2:
            self.show_winner_two = True
        ingame_helper.ENABLE_WIN_MOUSE = True

    def winner_event_handler(self):
        if logic.get_GAME_MODE() == 'SINGLE MATCH':
            if MOUSE_inside((616,686),(400,419)):
                self.new_glow = True
            else: self.new_glow = False
        if logic.get_GAME_CONDITION() == 'NEXT ROUND':
            if logic.get_GAME_MODE() == 'BEST OF 4' and (logic.get_CURRENT_SCORE(logic.get_B4_winner()) < 4):
                if MOUSE_inside((545,758),(400,419)):
                    self.show_next_round_glow = True
                else: self.show_next_round_glow = False
                if MOUSE_inside((614, 684), (452, 472)):
                    self.quit_glow = True
                else:
                    self.quit_glow = False

        elif logic.get_GAME_CONDITION() == 'GAME TIED':
            if MOUSE_inside((545,758),(400,419)):
                self.show_next_round_glow = True
            else: self.show_next_round_glow = False
            if MOUSE_inside((614, 684), (452, 472)):
                self.quit_glow = True
            else:
                self.quit_glow = False
        if logic.get_GAME_CONDITION() == 'TIE':
            if MOUSE_inside((614, 684), (452, 472)):
                self.quit_glow = True
            else:
                self.quit_glow = False

        if logic.get_CURRENT_SCORE(logic.get_B4_winner()) == 4:
                if MOUSE_inside((616,686),(400,419)):
                    self.new_glow = True
                else: self.new_glow = False

        if logic.get_GAME_MODE() == 'SINGLE MATCH' and logic.tell_WINNER()[1]:
            if MOUSE_inside((614,684),(452,472)):
                self.quit_glow = True
            else: self.quit_glow = False

        for event in pg.event.get():
            if event.type == MOUSEBUTTONDOWN:
                click = CLICK('option 1')
                if click[0]:
                    if self.new_glow:
                        self.winner_exiting = True
                        logic.reset_LOGIC()
                        fade_out.start_fade_out(); scenes.create_scene("GAME MODE")
                        self.new_glow = False
                    if self.quit_glow:
                        logic.reset_LOGIC()
                        self.winner_exiting = True
                        fade_out.start_fade_out(); scenes.create_scene("HOME")
                    if self.show_next_round_glow:
                        self.winner_exiting = True
                        logic.GAME_MODE = 'BEST OF 4'
                        logic.reset_B4_match()
                        fade_out.start_fade_out(); start_INGAME()


    def reset_winner(self):
        self.show_winner_one = False
        self.show_winner_two = False
        self.show_tie = False
        self.new_glow = False
        self.quit_glow = False
        self.new_glow = False
        self.show_next_round_glow = False

win = WINNER()

class INGAME_BOOLEANS():
    def __init__(self):
        self.game_mode_0 = True # single match
        self.game_mode_1 = False # best of 4
        self.executed = 0 # check game mode once

    def reset(self):
        self.game_mode_0 = True # single match
        self.game_mode_1 = False # best of 4
        self.executed = 0 # check game mode once

ingame_bool = INGAME_BOOLEANS()

#=================================== EVENT FUNCTIONS
def SWAP():
    #print(ingame_helper.swapper)
    if ingame_helper.swapper == 2:
        ingame_helper.swapper = 0
    if ingame_helper.swapper%2 == 0:
        ingame_helper.P1_CHIP_YELLOW = True
        ingame_helper.THEY_SWAP = True
        ingame_helper.P1_COLOR = image.YELLOW_C1
        ingame_helper.P2_COLOR = image.RED_C1
    else:
        ingame_helper.P1_CHIP_YELLOW = False
        ingame_helper.THEY_SWAP = False
        ingame_helper.P1_COLOR = image.RED_C1
        ingame_helper.P2_COLOR = image.YELLOW_C1
    ingame_helper.swapper += 1

def disable_swap():
    global GAME_STARTED
    GAME_STARTED = True

def identify_POSITIONDROP(posx):
    x = image.BOARDRECT.left
    offset = 0
    div = int(image.BOARDRECT.width/7)

    if  x+offset < posx < x+div-offset:
        return 0
    elif x+div+offset < posx < x+div*2-offset:
        return 1
    elif x+div*2+offset < posx < x+div*3-offset:
        return 2
    elif x+div*3+offset < posx < x+div*4-offset:
        return 3
    elif x+div*4+offset < posx < x+div*5-offset:
        return 4
    elif x+div*5+offset < posx < x+div*6-offset:
        return 5
    elif x+div*6+offset < posx < x+div*7-offset:
        return 6

def BULB_I(num):
    if num == 0 or num == 3:
        image.L_BULB()



#=================================== EVENT FUNCTIONS

#------------------------- CLOCK GLOBALS
TELL = 0
makeZERO = False
#-------------------------
##==================================================== COMPUTER BASED CLOCK
def combased_clock():
    XOFFSET = 72
    YOFFSET = 145

    global TELL, makeZERO
    H = strftime('%H')
    M = strftime('%M')
    S = strftime('%S')
    if (H == '00' or H == '12') and TELL == 0 and M == '00':
        sounds.MINUTE_BEEP12()
        TELL += 1
    if M == '01': makeZERO = True
    if makeZERO:
        TELL = 0
        makeZERO = False

    fonttype = pg.font.Font('fonts\omnes-semibold-webfont.ttf',20)

    HOURS = fonttype.render(H, True, BLACK)
    HOURSRECT = RECT(HOURS)
    HOURSRECT.center = (int(window_scale[0]/2)-XOFFSET+2,YOFFSET)
    BLIT(HOURS,HOURSRECT)

    MINS = fonttype.render(M, True, BLACK)
    MINSRECT = RECT(MINS)
    MINSRECT.center = (int(window_scale[0]/2),YOFFSET)
    BLIT(MINS, MINSRECT)

    SEC = fonttype.render(S, True, BLACK)
    SECRECT = RECT(SEC)
    SECRECT.center = (int(window_scale[0]/2)+XOFFSET+2,YOFFSET)
    BLIT(SEC,SECRECT)

##============================================================================================================= PUPPET SHOWS
def PUPPET_SHOWS():
    global elephantleft, elephantright,puppet,MOVEx
    if elephantleft:
        if MOVEx == int(window_scale[0]/2):
            elephantright = True
            elephantleft = False
        else:
            MOVEx -= VELOCITY
            image._ELEPHANT_L(MOVEx,MOVEy)

    if elephantright:
        MOVEx += VELOCITY
        image._ELEPHANT_R(MOVEx,MOVEy)
        if MOVEx > window_scale[0]:
            MOVEx = -400
            elephantright = False

    if puppet:
        MOVEx += VELOCITY
        image._CIRCUS_MAN(MOVEx,MOVEy)
        if MOVEx > window_scale[0]:
            MOVEx = -400
            puppet = False
#===================================================== PUPPET SHOWS

##=============================================================================================================== CHIP DROP ANIMATION
class DRAW_CHIPS():
    def __init__(self):
        self.piece = image.RED_C1
        self.square_size = int(image.BOARDRECT.width/7)/2

    def _R_00(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_01(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_02(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*2+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_03(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*3+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_04(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*4+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_05(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*5+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_06(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*6+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)
##============================================
    def _R_10(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_11(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_12(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*2+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_13(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*3+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_14(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*4+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_15(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*5+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_16(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*6+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)
##======================================================================================
    def _R_20(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_21(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_22(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*2+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_23(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*3+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_24(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*4+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_25(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*5+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_26(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*6+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)
##======================================================================================
    def _R_30(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_31(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_32(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*2+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_33(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*3+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_34(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*4+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_35(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*5+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_36(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*6+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)
##======================================================================================
    def _R_40(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_41(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_42(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*2+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_43(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*3+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_44(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*4+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_45(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*5+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_46(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*6+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)
##======================================================================================
    def _R_50(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_51(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_52(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*2+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_53(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*3+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_54(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*4+SQUARE_SIZE+4),i)
        BLIT(color,piecerect)

    def _R_55(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*5+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)

    def _R_56(self,i, piecerect,color):
        piecerect.center = (int(image.BOARDRECT.topleft[0]+BOX_SIZE*6+SQUARE_SIZE+3),i)
        BLIT(color,piecerect)


DRAW = DRAW_CHIPS()
#------------- FOR RED
a_R00 = False
a_R01 = False
a_R02 = False
a_R03 = False
a_R04 = False
a_R05 = False
a_R06 = False
#-------------
a_R10 = False
a_R11 = False
a_R12 = False
a_R13 = False
a_R14 = False
a_R15 = False
a_R16 = False
#-------------
a_R20 = False
a_R21 = False
a_R22 = False
a_R23 = False
a_R24 = False
a_R25 = False
a_R26 = False
#-------------
a_R30 = False
a_R31 = False
a_R32 = False
a_R33 = False
a_R34 = False
a_R35 = False
a_R36 = False
#-------------
a_R40 = False
a_R41 = False
a_R42 = False
a_R43 = False
a_R44 = False
a_R45 = False
a_R46 = False
#-------------
a_R50 = False
a_R51 = False
a_R52 = False
a_R53 = False
a_R54 = False
a_R55 = False
a_R56 = False
#------------- FOR YELLOW
a_Y00 = False
a_Y01 = False
a_Y02 = False
a_Y03 = False
a_Y04 = False
a_Y05 = False
a_Y06 = False
#-------------
a_Y10 = False
a_Y11 = False
a_Y12 = False
a_Y13 = False
a_Y14 = False
a_Y15 = False
a_Y16 = False
#-------------
a_Y20 = False
a_Y21 = False
a_Y22 = False
a_Y23 = False
a_Y24 = False
a_Y25 = False
a_Y26 = False
#-------------
a_Y30 = False
a_Y31 = False
a_Y32 = False
a_Y33 = False
a_Y34 = False
a_Y35 = False
a_Y36 = False
#-------------
a_Y40 = False
a_Y41 = False
a_Y42 = False
a_Y43 = False
a_Y44 = False
a_Y45 = False
a_Y46 = False
#-------------
a_Y50 = False
a_Y51 = False
a_Y52 = False
a_Y53 = False
a_Y54 = False
a_Y55 = False
a_Y56 = False

#==================================== FOR RED
R_00 = image.BOARDRECT.topleft[1]-34
R_01 = image.BOARDRECT.topleft[1]-34
R_02 = image.BOARDRECT.topleft[1]-34
R_03 = image.BOARDRECT.topleft[1]-34
R_04 = image.BOARDRECT.topleft[1]-34
R_05 = image.BOARDRECT.topleft[1]-34
R_06 = image.BOARDRECT.topleft[1]-34
#====================================
R_10 = image.BOARDRECT.topleft[1]-34
R_11 = image.BOARDRECT.topleft[1]-34
R_12 = image.BOARDRECT.topleft[1]-34
R_13 = image.BOARDRECT.topleft[1]-34
R_14 = image.BOARDRECT.topleft[1]-34
R_15 = image.BOARDRECT.topleft[1]-34
R_16 = image.BOARDRECT.topleft[1]-34
#====================================
R_20 = image.BOARDRECT.topleft[1]-34
R_21 = image.BOARDRECT.topleft[1]-34
R_22 = image.BOARDRECT.topleft[1]-34
R_23 = image.BOARDRECT.topleft[1]-34
R_24 = image.BOARDRECT.topleft[1]-34
R_25 = image.BOARDRECT.topleft[1]-34
R_26 = image.BOARDRECT.topleft[1]-34
#====================================
R_30 = image.BOARDRECT.topleft[1]-34
R_31 = image.BOARDRECT.topleft[1]-34
R_32 = image.BOARDRECT.topleft[1]-34
R_33 = image.BOARDRECT.topleft[1]-34
R_34 = image.BOARDRECT.topleft[1]-34
R_35 = image.BOARDRECT.topleft[1]-34
R_36 = image.BOARDRECT.topleft[1]-34
#====================================
R_40 = image.BOARDRECT.topleft[1]-34
R_41 = image.BOARDRECT.topleft[1]-34
R_42 = image.BOARDRECT.topleft[1]-34
R_43 = image.BOARDRECT.topleft[1]-34
R_44 = image.BOARDRECT.topleft[1]-34
R_45 = image.BOARDRECT.topleft[1]-34
R_46 = image.BOARDRECT.topleft[1]-34
#====================================
R_50 = image.BOARDRECT.topleft[1]-34
R_51 = image.BOARDRECT.topleft[1]-34
R_52 = image.BOARDRECT.topleft[1]-34
R_53 = image.BOARDRECT.topleft[1]-34
R_54 = image.BOARDRECT.topleft[1]-34
R_55 = image.BOARDRECT.topleft[1]-34
R_56 = image.BOARDRECT.topleft[1]-34
#==================================== FOR YELLOW
Y_00 = image.BOARDRECT.topleft[1]-34
Y_01 = image.BOARDRECT.topleft[1]-34
Y_02 = image.BOARDRECT.topleft[1]-34
Y_03 = image.BOARDRECT.topleft[1]-34
Y_04 = image.BOARDRECT.topleft[1]-34
Y_05 = image.BOARDRECT.topleft[1]-34
Y_06 = image.BOARDRECT.topleft[1]-34
#====================================
Y_10 = image.BOARDRECT.topleft[1]-34
Y_11 = image.BOARDRECT.topleft[1]-34
Y_12 = image.BOARDRECT.topleft[1]-34
Y_13 = image.BOARDRECT.topleft[1]-34
Y_14 = image.BOARDRECT.topleft[1]-34
Y_15 = image.BOARDRECT.topleft[1]-34
Y_16 = image.BOARDRECT.topleft[1]-34
#====================================
Y_20 = image.BOARDRECT.topleft[1]-34
Y_21 = image.BOARDRECT.topleft[1]-34
Y_22 = image.BOARDRECT.topleft[1]-34
Y_23 = image.BOARDRECT.topleft[1]-34
Y_24 = image.BOARDRECT.topleft[1]-34
Y_25 = image.BOARDRECT.topleft[1]-34
Y_26 = image.BOARDRECT.topleft[1]-34
#====================================
Y_30 = image.BOARDRECT.topleft[1]-34
Y_31 = image.BOARDRECT.topleft[1]-34
Y_32 = image.BOARDRECT.topleft[1]-34
Y_33 = image.BOARDRECT.topleft[1]-34
Y_34 = image.BOARDRECT.topleft[1]-34
Y_35 = image.BOARDRECT.topleft[1]-34
Y_36 = image.BOARDRECT.topleft[1]-34
#====================================
Y_40 = image.BOARDRECT.topleft[1]-34
Y_41 = image.BOARDRECT.topleft[1]-34
Y_42 = image.BOARDRECT.topleft[1]-34
Y_43 = image.BOARDRECT.topleft[1]-34
Y_44 = image.BOARDRECT.topleft[1]-34
Y_45 = image.BOARDRECT.topleft[1]-34
Y_46 = image.BOARDRECT.topleft[1]-34
#====================================
Y_50 = image.BOARDRECT.topleft[1]-34
Y_51 = image.BOARDRECT.topleft[1]-34
Y_52 = image.BOARDRECT.topleft[1]-34
Y_53 = image.BOARDRECT.topleft[1]-34
Y_54 = image.BOARDRECT.topleft[1]-34
Y_55 = image.BOARDRECT.topleft[1]-34
Y_56 = image.BOARDRECT.topleft[1]-34

def NEW():
    global GAME_STARTED
    if logic.FROM_SAVES: logic.create_board_from_SAVE()
    else:
        logic.create_new_board()
        GAME_STARTED = False
        ingame_helper.THEY_SWAP = False
        ingame_helper.swapper = 0
    #--------------------------------------------------------- RED
    global a_R00, a_R01, a_R02, a_R03, a_R04, a_R05, a_R06
    global a_R10, a_R11, a_R12, a_R13, a_R14, a_R15, a_R16
    global a_R20, a_R21, a_R22, a_R23, a_R24, a_R25, a_R26
    global a_R30, a_R31, a_R32, a_R33, a_R34, a_R35, a_R36
    global a_R40, a_R41, a_R42, a_R43, a_R44, a_R45, a_R46
    global a_R50, a_R51, a_R52, a_R53, a_R54, a_R55, a_R56
    #--------------------------------------------------------- YELLOW
    global a_Y00, a_Y01, a_Y02, a_Y03, a_Y04, a_Y05, a_Y06
    global a_Y10, a_Y11, a_Y12, a_Y13, a_Y14, a_Y15, a_Y16
    global a_Y20, a_Y21, a_Y22, a_Y23, a_Y24, a_Y25, a_Y26
    global a_Y30, a_Y31, a_Y32, a_Y33, a_Y34, a_Y35, a_Y36
    global a_Y40, a_Y41, a_Y42, a_Y43, a_Y44, a_Y45, a_Y46
    global a_Y50, a_Y51, a_Y52, a_Y53, a_Y54, a_Y55, a_Y56
    #----------------------------------------------------------------- FOR RED
    global R_00, R_01, R_02, R_03, R_04, R_05, R_06
    global R_10, R_11, R_12, R_13, R_14, R_15, R_16
    global R_20, R_21, R_22, R_23, R_24, R_25, R_26
    global R_30, R_31, R_32, R_33, R_34, R_35, R_36
    global R_40, R_41, R_42, R_43, R_44, R_45, R_46
    global R_50, R_51, R_52, R_53, R_54, R_55, R_56
    #----------------------------------------------------------------- FOR YELLOW
    global Y_00, Y_01, Y_02, Y_03, Y_04, Y_05, Y_06
    global Y_10, Y_11, Y_12, Y_13, Y_14, Y_15, Y_16
    global Y_20, Y_21, Y_22, Y_23, Y_24, Y_25, Y_26
    global Y_30, Y_31, Y_32, Y_33, Y_34, Y_35, Y_36
    global Y_40, Y_41, Y_42, Y_43, Y_44, Y_45, Y_46
    global Y_50, Y_51, Y_52, Y_53, Y_54, Y_55, Y_56
    #------------- FOR RED
    a_R00 = False
    a_R01 = False
    a_R02 = False
    a_R03 = False
    a_R04 = False
    a_R05 = False
    a_R06 = False
    #-------------
    a_R10 = False
    a_R11 = False
    a_R12 = False
    a_R13 = False
    a_R14 = False
    a_R15 = False
    a_R16 = False
    #-------------
    a_R20 = False
    a_R21 = False
    a_R22 = False
    a_R23 = False
    a_R24 = False
    a_R25 = False
    a_R26 = False
    #-------------
    a_R30 = False
    a_R31 = False
    a_R32 = False
    a_R33 = False
    a_R34 = False
    a_R35 = False
    a_R36 = False
    #-------------
    a_R40 = False
    a_R41 = False
    a_R42 = False
    a_R43 = False
    a_R44 = False
    a_R45 = False
    a_R46 = False
    #-------------
    a_R50 = False
    a_R51 = False
    a_R52 = False
    a_R53 = False
    a_R54 = False
    a_R55 = False
    a_R56 = False
    #------------- FOR YELLOW
    a_Y00 = False
    a_Y01 = False
    a_Y02 = False
    a_Y03 = False
    a_Y04 = False
    a_Y05 = False
    a_Y06 = False
    #-------------
    a_Y10 = False
    a_Y11 = False
    a_Y12 = False
    a_Y13 = False
    a_Y14 = False
    a_Y15 = False
    a_Y16 = False
    #-------------
    a_Y20 = False
    a_Y21 = False
    a_Y22 = False
    a_Y23 = False
    a_Y24 = False
    a_Y25 = False
    a_Y26 = False
    #-------------
    a_Y30 = False
    a_Y31 = False
    a_Y32 = False
    a_Y33 = False
    a_Y34 = False
    a_Y35 = False
    a_Y36 = False
    #-------------
    a_Y40 = False
    a_Y41 = False
    a_Y42 = False
    a_Y43 = False
    a_Y44 = False
    a_Y45 = False
    a_Y46 = False
    #-------------
    a_Y50 = False
    a_Y51 = False
    a_Y52 = False
    a_Y53 = False
    a_Y54 = False
    a_Y55 = False
    a_Y56 = False

    #==================================== FOR RED
    R_00 = image.BOARDRECT.topleft[1]-34
    R_01 = image.BOARDRECT.topleft[1]-34
    R_02 = image.BOARDRECT.topleft[1]-34
    R_03 = image.BOARDRECT.topleft[1]-34
    R_04 = image.BOARDRECT.topleft[1]-34
    R_05 = image.BOARDRECT.topleft[1]-34
    R_06 = image.BOARDRECT.topleft[1]-34
    #====================================
    R_10 = image.BOARDRECT.topleft[1]-34
    R_11 = image.BOARDRECT.topleft[1]-34
    R_12 = image.BOARDRECT.topleft[1]-34
    R_13 = image.BOARDRECT.topleft[1]-34
    R_14 = image.BOARDRECT.topleft[1]-34
    R_15 = image.BOARDRECT.topleft[1]-34
    R_16 = image.BOARDRECT.topleft[1]-34
    #====================================
    R_20 = image.BOARDRECT.topleft[1]-34
    R_21 = image.BOARDRECT.topleft[1]-34
    R_22 = image.BOARDRECT.topleft[1]-34
    R_23 = image.BOARDRECT.topleft[1]-34
    R_24 = image.BOARDRECT.topleft[1]-34
    R_25 = image.BOARDRECT.topleft[1]-34
    R_26 = image.BOARDRECT.topleft[1]-34
    #====================================
    R_30 = image.BOARDRECT.topleft[1]-34
    R_31 = image.BOARDRECT.topleft[1]-34
    R_32 = image.BOARDRECT.topleft[1]-34
    R_33 = image.BOARDRECT.topleft[1]-34
    R_34 = image.BOARDRECT.topleft[1]-34
    R_35 = image.BOARDRECT.topleft[1]-34
    R_36 = image.BOARDRECT.topleft[1]-34
    #====================================
    R_40 = image.BOARDRECT.topleft[1]-34
    R_41 = image.BOARDRECT.topleft[1]-34
    R_42 = image.BOARDRECT.topleft[1]-34
    R_43 = image.BOARDRECT.topleft[1]-34
    R_44 = image.BOARDRECT.topleft[1]-34
    R_45 = image.BOARDRECT.topleft[1]-34
    R_46 = image.BOARDRECT.topleft[1]-34
    #====================================
    R_50 = image.BOARDRECT.topleft[1]-34
    R_51 = image.BOARDRECT.topleft[1]-34
    R_52 = image.BOARDRECT.topleft[1]-34
    R_53 = image.BOARDRECT.topleft[1]-34
    R_54 = image.BOARDRECT.topleft[1]-34
    R_55 = image.BOARDRECT.topleft[1]-34
    R_56 = image.BOARDRECT.topleft[1]-34
    #==================================== FOR YELLOW
    Y_00 = image.BOARDRECT.topleft[1]-34
    Y_01 = image.BOARDRECT.topleft[1]-34
    Y_02 = image.BOARDRECT.topleft[1]-34
    Y_03 = image.BOARDRECT.topleft[1]-34
    Y_04 = image.BOARDRECT.topleft[1]-34
    Y_05 = image.BOARDRECT.topleft[1]-34
    Y_06 = image.BOARDRECT.topleft[1]-34
    #====================================
    Y_10 = image.BOARDRECT.topleft[1]-34
    Y_11 = image.BOARDRECT.topleft[1]-34
    Y_12 = image.BOARDRECT.topleft[1]-34
    Y_13 = image.BOARDRECT.topleft[1]-34
    Y_14 = image.BOARDRECT.topleft[1]-34
    Y_15 = image.BOARDRECT.topleft[1]-34
    Y_16 = image.BOARDRECT.topleft[1]-34
    #====================================
    Y_20 = image.BOARDRECT.topleft[1]-34
    Y_21 = image.BOARDRECT.topleft[1]-34
    Y_22 = image.BOARDRECT.topleft[1]-34
    Y_23 = image.BOARDRECT.topleft[1]-34
    Y_24 = image.BOARDRECT.topleft[1]-34
    Y_25 = image.BOARDRECT.topleft[1]-34
    Y_26 = image.BOARDRECT.topleft[1]-34
    #====================================
    Y_30 = image.BOARDRECT.topleft[1]-34
    Y_31 = image.BOARDRECT.topleft[1]-34
    Y_32 = image.BOARDRECT.topleft[1]-34
    Y_33 = image.BOARDRECT.topleft[1]-34
    Y_34 = image.BOARDRECT.topleft[1]-34
    Y_35 = image.BOARDRECT.topleft[1]-34
    Y_36 = image.BOARDRECT.topleft[1]-34
    #====================================
    Y_40 = image.BOARDRECT.topleft[1]-34
    Y_41 = image.BOARDRECT.topleft[1]-34
    Y_42 = image.BOARDRECT.topleft[1]-34
    Y_43 = image.BOARDRECT.topleft[1]-34
    Y_44 = image.BOARDRECT.topleft[1]-34
    Y_45 = image.BOARDRECT.topleft[1]-34
    Y_46 = image.BOARDRECT.topleft[1]-34
    #====================================
    Y_50 = image.BOARDRECT.topleft[1]-34
    Y_51 = image.BOARDRECT.topleft[1]-34
    Y_52 = image.BOARDRECT.topleft[1]-34
    Y_53 = image.BOARDRECT.topleft[1]-34
    Y_54 = image.BOARDRECT.topleft[1]-34
    Y_55 = image.BOARDRECT.topleft[1]-34
    Y_56 = image.BOARDRECT.topleft[1]-34



CLOCK_GLOW = False
TITLE_GLOW = False
SWAP_GLOW, NEW_GLOW, OPTION_GLOW = False, False, False
CHIP_RECT = RECT(image.RED_C1)
BOARD_BOUNDS = False

def INGAME_Event_Handler():
    global puppet, elephantleft, MOVEx, MOVEy, _I_BOARD, DROP, hover_count, _I_BOARD2, TURN_NUMBER, CLOCK_GLOW, TITLE_GLOW, SWAP_GLOW, NEW_GLOW, OPTION_GLOW
    global MULTIPLIER1, MULTIPLIER2, MULTIPLIER3, MULTIPLIER4, MULTIPLIER5
    global BOARD_BOUNDS
#----------------------------------------------------------------- FOR RED
    global a_R00, a_R01, a_R02, a_R03, a_R04, a_R05, a_R06
    global a_R10, a_R11, a_R12, a_R13, a_R14, a_R15, a_R16
    global a_R20, a_R21, a_R22, a_R23, a_R24, a_R25, a_R26
    global a_R30, a_R31, a_R32, a_R33, a_R34, a_R35, a_R36
    global a_R40, a_R41, a_R42, a_R43, a_R44, a_R45, a_R46
    global a_R50, a_R51, a_R52, a_R53, a_R54, a_R55, a_R56
#----------------------------------------------------------------- FOR YELLOW
    global a_Y00, a_Y01, a_Y02, a_Y03, a_Y04, a_Y05, a_Y06
    global a_Y10, a_Y11, a_Y12, a_Y13, a_Y14, a_Y15, a_Y16
    global a_Y20, a_Y21, a_Y22, a_Y23, a_Y24, a_Y25, a_Y26
    global a_Y30, a_Y31, a_Y32, a_Y33, a_Y34, a_Y35, a_Y36
    global a_Y40, a_Y41, a_Y42, a_Y43, a_Y44, a_Y45, a_Y46
    global a_Y50, a_Y51, a_Y52, a_Y53, a_Y54, a_Y55, a_Y56

    if ingame_helper.ENABLE_INGAME_MOUSE:
        mouse_pos = get_MOUSEPOS()

        if image.TITLERECT.left < mouse_pos[0] < image.TITLERECT.right and image.TITLERECT.top < mouse_pos[1] < image.TITLERECT.bottom:
            TITLE_GLOW = True
        else: TITLE_GLOW = False
        if image.BOARDRECT.left+int(image.RED_C1RECT.width/2)-2 < mouse_pos[0] < image.BOARDRECT.right-int(image.RED_C1RECT.width/2)+2 and image.BOARDRECT.top-SQUARE_SIZE*2 < mouse_pos[1] < image.BOARDRECT.top-int(image.RED_C1RECT.width/2)+2:
            #DISPLAY CURRENT CHIP COLOR
            DROP = True
            ingame_helper.SHOW_CHIP = True
            if logic.get_TURN() == 0:
                ingame_helper.PLAYER_TWO_SHOW_CHIP = False
                ingame_helper.PLAYER_ONE_SHOW_CHIP = True
            else:
                ingame_helper.PLAYER_ONE_SHOW_CHIP = False
                ingame_helper.PLAYER_TWO_SHOW_CHIP = True
        else: DROP = False;ingame_helper.SHOW_CHIP = False
        if image.BOARDRECT.left < mouse_pos[0] < image.BOARDRECT.right and image.BOARDRECT.top < mouse_pos[1] < image.BOARDRECT.bottom:
            BOARD_BOUNDS = True
            if hover_count%2 == 0:
                _I_BOARD2 = False
                _I_BOARD = True
            if hover_count%2 != 0:
                _I_BOARD = False
                _I_BOARD2 = True
            hover_count += 1
            if hover_count == 10:
                hover_count = 0
        else: BOARD_BOUNDS = False
        if image.CLOCKRECT.left < mouse_pos[0] < image.CLOCKRECT.right and image.CLOCKRECT.top < mouse_pos[1] < image.CLOCKRECT.bottom:
            CLOCK_GLOW = True
        else: CLOCK_GLOW = False
        if image.OPTION_BRECT.left < mouse_pos[0] < image.OPTION_BRECT.right and image.OPTION_BRECT.top < mouse_pos[1] < image.OPTION_BRECT.bottom: #option
            OPTION_GLOW =  True
        else: OPTION_GLOW = False
        if image.NEW_BRECT.left < mouse_pos[0] < image.NEW_BRECT.right and image.NEW_BRECT.top < mouse_pos[1] < image.NEW_BRECT.bottom: #new
            NEW_GLOW = True
        else: NEW_GLOW = False
        if image.UNDO_BRECT.left < mouse_pos[0] < image.UNDO_BRECT.right and image.UNDO_BRECT.top < mouse_pos[1] < image.UNDO_BRECT.bottom:  #swap
            SWAP_GLOW = True
        else: SWAP_GLOW = False


#--------------------------------------------------- EVENTS
    for event in pg.event.get():
        if event.type == QUIT:
            scenes.create_scene('EXIT DIALOG')
        elif event.type == KEYDOWN:
#---------------------------------------------- test buttons for home an ingame
            if event.key == K_j:
                logic.FROM_SAVES = True
            elif event.key == K_n:
                logic.FROM_SAVES = False
            elif event.key == K_ESCAPE:
                options2.pause = True
                scenes.create_scene('OPTIONS2')
        elif event.type == MOUSEBUTTONDOWN:
            if DROP:
                if ingame_helper.ENABLE_INGAME_MOUSE:
                    click = CLICK('option 2')
                    if click[0]:
                        disable_swap() #TELL THE SCRIPT THAT PLAYER STARTED TO CLICK
                        if ingame_bool.executed == 0:
                            ##==================================================================== CHECK THE GAME MODE
                            if logic.get_GAME_MODE() == 'SINGLE MATCH': ingame_bool.game_mode_0 = True; ingame_bool.game_mode_1 = False
                            elif logic.get_GAME_MODE() == 'BEST OF 4': ingame_bool.game_mode_1 = True; ingame_bool.game_mode_0 = False
                            ingame_bool.executed += 1

                        colx = identify_POSITIONDROP(mouse_pos[0])
                        x = get_POSITIONCOL(colx)
                        if x == None: x = get_POSITIONCOL(colx) #if player is clicking midway the holes
                        else: logic.Player_input(x) #FUNCTION ON LOGIC
##================================================================ SINGLE MATCH =====================================================
                        if ingame_bool.game_mode_0:
                            ##-------------------------------------------------- WINNER CHECK
                            THERE_IS_A_WINNER = logic.tell_WINNER()
                            if THERE_IS_A_WINNER[1]:
                                sounds.fadeout_ALL()
                                ingame_helper.DISABLE_INGAME_MOUSE()
                                ingame_helper.FALSE_OTHER_INFOS()
                                if THERE_IS_A_WINNER[0] == 1:
                                    win.show_winner(THERE_IS_A_WINNER[0])
                                if THERE_IS_A_WINNER[0] == 2:
                                    win.show_winner(THERE_IS_A_WINNER[0])
                                if sounds.GLOBAL_SOUND:
                                    sounds.WIN_SOUND()
                            ##--------------------------------------------------- TIE CHECK
                            elif logic.get_GAME_CONDITION() == 'TIE':
                                ingame_helper.DISABLE_INGAME_MOUSE()
                                ingame_helper.FALSE_OTHER_INFOS()
                                win.show_winner(0)
##================================================================ BEST OF 4 =====================================================
                        elif ingame_bool.game_mode_1:
                            ##-------------------------------------------------- WINNER CHECK
                            THERE_IS_A_WINNER = logic.tell_WINNER()
                            if THERE_IS_A_WINNER[1]:
                                sounds.fadeout_ALL()
                                ingame_helper.DISABLE_INGAME_MOUSE()
                                ingame_helper.FALSE_OTHER_INFOS()
                                if THERE_IS_A_WINNER[0] == 1:
                                    win.show_winner(THERE_IS_A_WINNER[0])
                                if THERE_IS_A_WINNER[0] == 2:
                                    win.show_winner(THERE_IS_A_WINNER[0])
                                if sounds.GLOBAL_SOUND:
                                    sounds.WIN_SOUND()
                            ##--------------------------------------------------- TIE CHECK
                            elif logic.game_condition == 'NEXT ROUND':
                                ingame_helper.DISABLE_INGAME_MOUSE()
                                ingame_helper.FALSE_OTHER_INFOS()
                                if logic.get_B4_winner() == 1:  win.show_winner(1)
                                elif logic.get_B4_winner() == 2: win.show_winner(2)
                            elif logic.game_condition == 'GAME TIED':
                                ingame_helper.DISABLE_INGAME_MOUSE()
                                ingame_helper.FALSE_OTHER_INFOS()
                                win.show_winner(0)

                        blit_loc = logic.get_BLITPOS()
                        #print(blit_loc) #FUNCTION ON LOGIC blit_loc is  list 0 is the turn number 1 is the tuple of input row and col
                        TURN_NUMBER = logic.get_TURN() #FUNCTION ON LOGIC
                        #=================================================================== FOR RED
                        #---------------------------------------------------- ROW 0
                        if blit_loc[1]  == (0,0) and blit_loc[0] == 1:
                            a_R00 = True
                        elif  blit_loc[1] == (0,1)and blit_loc[0] == 1:
                            a_R01 = True
                        elif  blit_loc[1] == (0,2)and blit_loc[0] == 1:
                            a_R02 = True
                        elif  blit_loc[1] == (0,3)and blit_loc[0] == 1:
                            a_R03 = True
                        elif  blit_loc[1] == (0,4)and blit_loc[0] == 1:
                            a_R04 = True
                        elif  blit_loc[1] == (0,5)and blit_loc[0] == 1:
                            a_R05 = True
                        elif  blit_loc[1] == (0,6)and blit_loc[0] == 1:
                            a_R06 = True
                        #---------------------------------------------------- ROW 1
                        elif  blit_loc[1] == (1,0)and blit_loc[0] == 1:
                            MULTIPLIER1 = 3
                            a_R10 = True
                        elif  blit_loc[1] == (1,1)and blit_loc[0] == 1:
                            MULTIPLIER1 = 3
                            a_R11 = True
                        elif  blit_loc[1] == (1,2)and blit_loc[0] == 1:
                            MULTIPLIER1 = 3
                            a_R12 = True
                        elif  blit_loc[1] == (1,3)and blit_loc[0] == 1:
                            MULTIPLIER1 = 3
                            a_R13 = True
                        elif  blit_loc[1] == (1,4)and blit_loc[0] == 1:
                            MULTIPLIER1 = 3
                            a_R14 = True
                        elif  blit_loc[1] == (1,5)and blit_loc[0] == 1:
                            MULTIPLIER1 = 3
                            a_R15 = True
                        elif  blit_loc[1] == (1,6)and blit_loc[0] == 1:
                            MULTIPLIER1 = 3
                            a_R16 = True
                        #---------------------------------------------------- ROW 2
                        elif  blit_loc[1] == (2,0)and blit_loc[0] == 1:
                            MULTIPLIER2 = 5
                            a_R20 = True
                        elif  blit_loc[1] == (2,1)and blit_loc[0] == 1:
                            MULTIPLIER2 = 5
                            a_R21 = True
                        elif  blit_loc[1] == (2,2)and blit_loc[0] == 1:
                            MULTIPLIER2 = 5
                            a_R22 = True
                        elif  blit_loc[1] == (2,3)and blit_loc[0] == 1:
                            MULTIPLIER2 = 5
                            a_R23 = True
                        elif  blit_loc[1] == (2,4)and blit_loc[0] == 1:
                            MULTIPLIER2 = 5
                            a_R24 = True
                        elif  blit_loc[1] == (2,5)and blit_loc[0] == 1:
                            MULTIPLIER2 = 5
                            a_R25 = True
                        elif  blit_loc[1] == (2,6)and blit_loc[0] == 1:
                            MULTIPLIER2 = 5
                            a_R26 = True
                        #---------------------------------------------------- ROW 3
                        elif  blit_loc[1] == (3,0)and blit_loc[0] == 1:
                            MULTIPLIER3 = 7
                            a_R30 = True
                        elif  blit_loc[1] == (3,1)and blit_loc[0] == 1:
                            MULTIPLIER3 = 7
                            a_R31 = True
                        elif  blit_loc[1] == (3,2)and blit_loc[0] == 1:
                            MULTIPLIER3 = 7
                            a_R32 = True
                        elif  blit_loc[1] == (3,3)and blit_loc[0] == 1:
                            MULTIPLIER3 = 7
                            a_R33 = True
                        elif  blit_loc[1] == (3,4)and blit_loc[0] == 1:
                            MULTIPLIER3 = 7
                            a_R34 = True
                        elif  blit_loc[1] == (3,5)and blit_loc[0] == 1:
                            MULTIPLIER3 = 7
                            a_R35 = True
                        elif  blit_loc[1] == (3,6)and blit_loc[0] == 1:
                            MULTIPLIER3 = 7
                            a_R36 = True
                        #---------------------------------------------------- ROW 4
                        elif  blit_loc[1] == (4,0)and blit_loc[0] == 1:
                            MULTIPLIER4 = 9
                            a_R40 = True
                        elif  blit_loc[1] == (4,1)and blit_loc[0] == 1:
                            MULTIPLIER4 = 9
                            a_R41 = True
                        elif  blit_loc[1] == (4,2)and blit_loc[0] == 1:
                            MULTIPLIER4 = 9
                            a_R42 = True
                        elif  blit_loc[1] == (4,3)and blit_loc[0] == 1:
                            MULTIPLIER4 = 9
                            a_R43 = True
                        elif  blit_loc[1] == (4,4)and blit_loc[0] == 1:
                            MULTIPLIER4 = 9
                            a_R44 = True
                        elif  blit_loc[1] == (4,5)and blit_loc[0] == 1:
                            MULTIPLIER4 = 9
                            a_R45 = True
                        elif  blit_loc[1] == (4,6)and blit_loc[0] == 1:
                            MULTIPLIER4 = 9
                            a_R46 = True
                        #---------------------------------------------------- ROW 5
                        elif  blit_loc[1] == (5,0)and blit_loc[0] == 1:
                            MULTIPLIER5 = 11
                            a_R50 = True
                        elif  blit_loc[1] == (5,1)and blit_loc[0] == 1:
                            MULTIPLIER5 = 11
                            a_R51 = True
                        elif  blit_loc[1] == (5,2)and blit_loc[0] == 1:
                            MULTIPLIER5 = 11
                            a_R52 = True
                        elif  blit_loc[1] == (5,3)and blit_loc[0] == 1:
                            MULTIPLIER5 = 11
                            a_R53 = True
                        elif  blit_loc[1] == (5,4)and blit_loc[0] == 1:
                            MULTIPLIER5 = 11
                            a_R54 = True
                        elif  blit_loc[1] == (5,5)and blit_loc[0] == 1:
                            MULTIPLIER5 = 11
                            a_R55 = True
                        elif  blit_loc[1] == (5,6)and blit_loc[0] == 1:
                            MULTIPLIER5 = 11
                            a_R56 = True
                        #============================================================= FOR YELLOW
                        #---------------------------------------------------- ROW 0
                        if blit_loc[1]  == (0,0) and blit_loc[0] == 2:
                            a_Y00 = True
                        elif  blit_loc[1] == (0,1)and blit_loc[0] == 2:
                            a_Y01 = True
                        elif  blit_loc[1] == (0,2)and blit_loc[0] == 2:
                            a_Y02 = True
                        elif  blit_loc[1] == (0,3)and blit_loc[0] == 2:
                            a_Y03 = True
                        elif  blit_loc[1] == (0,4)and blit_loc[0] == 2:
                            a_Y04 = True
                        elif  blit_loc[1] == (0,5)and blit_loc[0] == 2:
                            a_Y05 = True
                        elif  blit_loc[1] == (0,6)and blit_loc[0] == 2:
                            a_Y06 = True
                        #---------------------------------------------------- ROW 1
                        elif  blit_loc[1] == (1,0)and blit_loc[0] == 2:
                            MULTIPLIER1 = 3
                            a_Y10 = True
                        elif  blit_loc[1] == (1,1)and blit_loc[0] == 2:
                            MULTIPLIER1 = 3
                            a_Y11 = True
                        elif  blit_loc[1] == (1,2)and blit_loc[0] == 2:
                            MULTIPLIER1 = 3
                            a_Y12 = True
                        elif  blit_loc[1] == (1,3)and blit_loc[0] == 2:
                            MULTIPLIER1 = 3
                            a_Y13 = True
                        elif  blit_loc[1] == (1,4)and blit_loc[0] == 2:
                            MULTIPLIER1 = 3
                            a_Y14 = True
                        elif  blit_loc[1] == (1,5)and blit_loc[0] == 2:
                            MULTIPLIER1 = 3
                            a_Y15 = True
                        elif  blit_loc[1] == (1,6)and blit_loc[0] == 2:
                            MULTIPLIER1 = 3
                            a_Y16 = True
                        #---------------------------------------------------- ROW 2
                        elif  blit_loc[1] == (2,0)and blit_loc[0] == 2:
                            MULTIPLIER2 = 5
                            a_Y20 = True
                        elif  blit_loc[1] == (2,1)and blit_loc[0] == 2:
                            MULTIPLIER2 = 5
                            a_Y21 = True
                        elif  blit_loc[1] == (2,2)and blit_loc[0] == 2:
                            MULTIPLIER2 = 5
                            a_Y22 = True
                        elif  blit_loc[1] == (2,3)and blit_loc[0] == 2:
                            MULTIPLIER2 = 5
                            a_Y23 = True
                        elif  blit_loc[1] == (2,4)and blit_loc[0] == 2:
                            MULTIPLIER2 = 5
                            a_Y24 = True
                        elif  blit_loc[1] == (2,5)and blit_loc[0] == 2:
                            MULTIPLIER2 = 5
                            a_Y25 = True
                        elif  blit_loc[1] == (2,6)and blit_loc[0] == 2:
                            MULTIPLIER2 = 5
                            a_Y26 = True
                        #---------------------------------------------------- ROW 3
                        elif  blit_loc[1] == (3,0)and blit_loc[0] == 2:
                            MULTIPLIER3 = 7
                            a_Y30 = True
                        elif  blit_loc[1] == (3,1)and blit_loc[0] == 2:
                            MULTIPLIER3 = 7
                            a_Y31 = True
                        elif  blit_loc[1] == (3,2)and blit_loc[0] == 2:
                            MULTIPLIER3 = 7
                            a_Y32 = True
                        elif  blit_loc[1] == (3,3)and blit_loc[0] == 2:
                            MULTIPLIER3 = 7
                            a_Y33 = True
                        elif  blit_loc[1] == (3,4)and blit_loc[0] == 2:
                            MULTIPLIER3 = 7
                            a_Y34 = True
                        elif  blit_loc[1] == (3,5)and blit_loc[0] == 2:
                            MULTIPLIER3 = 7
                            a_Y35 = True
                        elif  blit_loc[1] == (3,6)and blit_loc[0] == 2:
                            MULTIPLIER3 = 7
                            a_Y36 = True
                        #---------------------------------------------------- ROW 4
                        elif  blit_loc[1] == (4,0)and blit_loc[0] == 2:
                            MULTIPLIER4 = 9
                            a_Y40 = True
                        elif  blit_loc[1] == (4,1)and blit_loc[0] == 2:
                            MULTIPLIER4 = 9
                            a_Y41 = True
                        elif  blit_loc[1] == (4,2)and blit_loc[0] == 2:
                            MULTIPLIER4 = 9
                            a_Y42 = True
                        elif  blit_loc[1] == (4,3)and blit_loc[0] == 2:
                            MULTIPLIER4 = 9
                            a_Y43 = True
                        elif  blit_loc[1] == (4,4)and blit_loc[0] == 2:
                            MULTIPLIER4 = 9
                            a_Y44 = True
                        elif  blit_loc[1] == (4,5)and blit_loc[0] == 2:
                            MULTIPLIER4 = 9
                            a_Y45 = True
                        elif  blit_loc[1] == (4,6)and blit_loc[0] == 2:
                            MULTIPLIER4 = 9
                            a_Y46 = True
                        #---------------------------------------------------- ROW 5
                        elif  blit_loc[1] == (5,0)and blit_loc[0] == 2:
                            MULTIPLIER5 = 11
                            a_Y50 = True
                        elif  blit_loc[1] == (5,1)and blit_loc[0] == 2:
                            MULTIPLIER5 = 11
                            a_Y51 = True
                        elif  blit_loc[1] == (5,2)and blit_loc[0] == 2:
                            MULTIPLIER5 = 11
                            a_Y52 = True
                        elif  blit_loc[1] == (5,3)and blit_loc[0] == 2:
                            MULTIPLIER5 = 11
                            a_Y53 = True
                        elif  blit_loc[1] == (5,4)and blit_loc[0] == 2:
                            MULTIPLIER5 = 11
                            a_Y54 = True
                        elif  blit_loc[1] == (5,5)and blit_loc[0] == 2:
                            MULTIPLIER5 = 11
                            a_Y55 = True
                        elif  blit_loc[1] == (5,6)and blit_loc[0] == 2:
                            MULTIPLIER5 = 11
                            a_Y56 = True


            else:
                if pg.mouse.get_pressed() == (1,0,0):
                    if sounds.GLOBAL_SOUND:
                        sounds.B_CLICK()
                if OPTION_GLOW: scenes.create_scene('OPTIONS2')
                if NEW_GLOW:
                    fade_out.start_fade_out();scenes.create_scene('GAME MODE')
                    ingame_helper.P1_COLOR = image.RED_C1
                    ingame_helper.P2_COLOR = image.YELLOW_C1
                    logic.reset_LOGIC()
                if SWAP_GLOW:
                    if GAME_STARTED: pass
                    else: SWAP()
                if TITLE_GLOW:
                    scenes.from_home_access = False
                    scenes.from_ingame_access = True
                    fade_out.start_fade_out()
                    scenes.create_scene('HOW TO PLAY')

##============================================================================================== ingame

alter = 0
board_alter = 0
board_illum = Ticker(0.2)
bulb_illum = Ticker(0.4)


def IN_GAME():
    global _I_BOARD, _I_BOARD2, alter, GAME_OVER
    global CURSOR_RED, CURSOR_YELLOW, MAIN_CURSOR
#----------------------------------------------------------------- FOR RED
    global R_00, R_01, R_02, R_03, R_04, R_05, R_06
    global R_10, R_11, R_12, R_13, R_14, R_15, R_16
    global R_20, R_21, R_22, R_23, R_24, R_25, R_26
    global R_30, R_31, R_32, R_33, R_34, R_35, R_36
    global R_40, R_41, R_42, R_43, R_44, R_45, R_46
    global R_50, R_51, R_52, R_53, R_54, R_55, R_56
#----------------------------------------------------------------- FOR YELLOW
    global Y_00, Y_01, Y_02, Y_03, Y_04, Y_05, Y_06
    global Y_10, Y_11, Y_12, Y_13, Y_14, Y_15, Y_16
    global Y_20, Y_21, Y_22, Y_23, Y_24, Y_25, Y_26
    global Y_30, Y_31, Y_32, Y_33, Y_34, Y_35, Y_36
    global Y_40, Y_41, Y_42, Y_43, Y_44, Y_45, Y_46
    global Y_50, Y_51, Y_52, Y_53, Y_54, Y_55, Y_56


##--------------------------------------- show current player chips color
    if ingame_helper.P1_CHIP_YELLOW:
        image._BG2()
    else: image._BG()
##------------------------------------------- glow indicator
    if logic.get_TURN() == 0:
        BLIT(image.P1_GLOW,image.ORIGIN)
    elif logic.get_TURN() == 1:
        BLIT(image.P2_GLOW,image.P2_GLOW_RECT)

    image._CLOCK()
    if CLOCK_GLOW:
        image._I_CLOCK()

    image.BOARD_BACK()

    if logic.get_GAME_MODE() == 'BEST OF 4':
        #-------------------------------------------- player 1
        if ingame_helper.P1_score_0:
            BLIT(image.P1_SCORE_0,image.ORIGIN)
        if ingame_helper.P1_score_1:
            BLIT(image.P1_SCORE_1,image.ORIGIN)
        if ingame_helper.P1_score_2:
            BLIT(image.P1_SCORE_2,image.ORIGIN)
        if ingame_helper.P1_score_3:
            BLIT(image.P1_SCORE_3,image.ORIGIN)
        if ingame_helper.P1_score_4:
            BLIT(image.P1_SCORE_4,image.ORIGIN)
        #--------------------------------------------- player 2
        if ingame_helper.P2_score_0:
            BLIT(image.P2_SCORE_0,image.ORIGIN)
        if ingame_helper.P2_score_1:
            BLIT(image.P2_SCORE_1,image.ORIGIN)
        if ingame_helper.P2_score_2:
            BLIT(image.P2_SCORE_2,image.ORIGIN)
        if ingame_helper.P2_score_3:
            BLIT(image.P2_SCORE_3,image.ORIGIN)
        if ingame_helper.P2_score_4:
            BLIT(image.P2_SCORE_4,image.ORIGIN)

    if DROP:
        ingame_helper.SHOW_WELCOME = False

    if not ingame_helper.SHOW_WELCOME:
        if ingame_helper.FALSE_OTHER:
            if logic.get_TURN() == 0:
                BLIT(image.INFO_P1,image.INFO_P1_RECT)
            elif logic.get_TURN() == 1:
                BLIT(image.INFO_P2,image.INFO_P1_RECT)

    if SWAP_GLOW:
        ingame_helper.FALSE_OTHER = False
        BLIT(image.INFO_SWAP,image.INFO_P1_RECT)
    else: ingame_helper.SHOW_WELCOME = True;ingame_helper.FALSE_OTHER = True
    if NEW_GLOW:
        ingame_helper.FALSE_OTHER = False
        BLIT(image.INFO_NEW,image.INFO_P1_RECT)
    else: ingame_helper.SHOW_WELCOME = True;ingame_helper.FALSE_OTHER = True
    if OPTION_GLOW:
        ingame_helper.FALSE_OTHER = False
        BLIT(image.INFO_OPTIONS,image.INFO_P1_RECT)
    else: ingame_helper.SHOW_WELCOME = True;ingame_helper.FALSE_OTHER = True

    if BOARD_BOUNDS: ingame_helper.SHOW_WELCOME = True
    else: ingame_helper.SHOW_WELCOME = False
    if ingame_helper.SHOW_WELCOME:
        BLIT(image.INFO_WELCOME,image.INFO_P1_RECT)



    if ingame_helper.SHOW_CHIP:
        MAIN_CURSOR = False
        mouse_pos2 = get_MOUSEPOS()
        if ingame_helper.PLAYER_ONE_SHOW_CHIP:
            if ingame_helper.THEY_SWAP:
                CURSOR_RED = True
                CURSOR_YELLOW = False
                image._YELLOW_C(mouse_pos2)
            else:
                CURSOR_RED = False
                CURSOR_YELLOW = True
                image._RED_C(mouse_pos2)
        if ingame_helper.PLAYER_TWO_SHOW_CHIP:
            if ingame_helper.THEY_SWAP:
                CURSOR_RED = False
                CURSOR_YELLOW = True
                image._RED_C(mouse_pos2)
            else:
                CURSOR_YELLOW = False
                CURSOR_RED = True
                image._YELLOW_C(mouse_pos2)
    else: MAIN_CURSOR = True


##===============================================================================
    if a_R00:
        if R_00 == image.BOARDRECT.bottom-SQUARE_SIZE:
            R_00 = image.BOARDRECT.bottom-SQUARE_SIZE
        else: R_00+=DROP_SPEED
        DRAW._R_00(R_00, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R01:
        if R_01 == image.BOARDRECT.bottom-SQUARE_SIZE:
            R_01 = image.BOARDRECT.bottom-SQUARE_SIZE
        else: R_01+=DROP_SPEED
        DRAW._R_01(R_01, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R02:
        if R_02 == image.BOARDRECT.bottom-SQUARE_SIZE:
            R_02 = image.BOARDRECT.bottom-SQUARE_SIZE
        else: R_02+=DROP_SPEED
        DRAW._R_02(R_02, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R03:
        if R_03 == image.BOARDRECT.bottom-SQUARE_SIZE:
            R_03 = image.BOARDRECT.bottom-SQUARE_SIZE
        else: R_03+=DROP_SPEED
        DRAW._R_03(R_03, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R04:
        if R_04 == image.BOARDRECT.bottom-SQUARE_SIZE:
            R_04 = image.BOARDRECT.bottom-SQUARE_SIZE
        else: R_04+=DROP_SPEED
        DRAW._R_04(R_04, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R05:
        if R_05 == image.BOARDRECT.bottom-SQUARE_SIZE:
            R_05 = image.BOARDRECT.bottom-SQUARE_SIZE
        else: R_05+=DROP_SPEED
        DRAW._R_05(R_05, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R06:
        if R_06 == image.BOARDRECT.bottom-SQUARE_SIZE:
            R_06 = image.BOARDRECT.bottom-SQUARE_SIZE
        else: R_06+=DROP_SPEED
        DRAW._R_06(R_06, CHIP_RECT, ingame_helper.P1_COLOR)
#=====================================================================
    if a_R10:
        if R_10 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1:
            R_10 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1
        else: R_10+=DROP_SPEED
        DRAW._R_10(R_10, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R11:
        if R_11 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1:
            R_11 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1
        else: R_11+=DROP_SPEED
        DRAW._R_11(R_11, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R12:
        if R_12 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1:
            R_12 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1
        else: R_12+=DROP_SPEED
        DRAW._R_12(R_12, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R13:
        if R_13 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1:
            R_13 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1
        else: R_13+=DROP_SPEED
        DRAW._R_13(R_13, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R14:
        if R_14 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1:
            R_14 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1
        else: R_14+=DROP_SPEED
        DRAW._R_14(R_14, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R15:
        if R_15 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1:
            R_15 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1
        else: R_15+=DROP_SPEED
        DRAW._R_15(R_15, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R16:
        if R_16 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1:
            R_16 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1
        else: R_16+=DROP_SPEED
        DRAW._R_16(R_16, CHIP_RECT, ingame_helper.P1_COLOR)
#===================================================================
    if a_R20:
        if R_20 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2:
            R_20 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2
        else: R_20+=DROP_SPEED
        DRAW._R_20(R_20, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R21:
        if R_21 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2:
            R_21 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2
        else: R_21+=DROP_SPEED
        DRAW._R_21(R_21, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R22:
        if R_22 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2:
            R_22 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2
        else: R_22+=DROP_SPEED
        DRAW._R_22(R_22, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R23:
        if R_23 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2:
            R_23 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2
        else: R_23+=DROP_SPEED
        DRAW._R_23(R_23, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R24:
        if R_24 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2:
            R_24 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2
        else: R_24+=DROP_SPEED
        DRAW._R_24(R_24, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R25:
        if R_25 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2:
            R_25 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2
        else: R_25+=DROP_SPEED
        DRAW._R_25(R_25, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R26:
        if R_26 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2:
            R_26 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2
        else: R_26+=DROP_SPEED
        DRAW._R_26(R_26, CHIP_RECT, ingame_helper.P1_COLOR)
#===================================================================
    if a_R30:
        if R_30 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3:
            R_30 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3
        else: R_30+=DROP_SPEED
        DRAW._R_30(R_30, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R31:
        if R_31 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3:
            R_31 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3
        else: R_31+=DROP_SPEED
        DRAW._R_31(R_31, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R32:
        if R_32 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3:
            R_32 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3
        else: R_32+=DROP_SPEED
        DRAW._R_32(R_32, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R33:
        if R_33 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3:
            R_33 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3
        else: R_33+=DROP_SPEED
        DRAW._R_33(R_33, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R34:
        if R_34 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3:
            R_34 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3
        else: R_34+=DROP_SPEED
        DRAW._R_34(R_34, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R35:
        if R_35 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3:
            R_35 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3
        else: R_35+=DROP_SPEED
        DRAW._R_35(R_35, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R36:
        if R_36 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3:
            R_36 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3
        else: R_36+=DROP_SPEED
        DRAW._R_36(R_36, CHIP_RECT, ingame_helper.P1_COLOR)

#===================================================================
    if a_R40:
        if R_40 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4:
            R_40 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4
        else: R_40+=DROP_SPEED
        DRAW._R_40(R_40, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R41:
        if R_41 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4:
            R_41 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4
        else: R_41+=DROP_SPEED
        DRAW._R_41(R_41, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R42:
        if R_42 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4:
            R_42 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4
        else: R_42+=DROP_SPEED
        DRAW._R_42(R_42, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R43:
        if R_43 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4:
            R_43 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4
        else: R_43+=DROP_SPEED
        DRAW._R_43(R_43, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R44:
        if R_44 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4:
            R_44 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4
        else: R_44+=DROP_SPEED
        DRAW._R_44(R_44, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R45:
        if R_45 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4:
            R_45 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4
        else: R_45+=DROP_SPEED
        DRAW._R_45(R_45, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R46:
        if R_46 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4:
            R_46 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4
        else: R_46+=DROP_SPEED
        DRAW._R_46(R_46, CHIP_RECT, ingame_helper.P1_COLOR)
#===================================================================
    if a_R50:
        if R_50 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5:
            R_50 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5
        else: R_50+=DROP_SPEED
        DRAW._R_50(R_50, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R51:
        if R_51 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5:
            R_51 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5
        else: R_51+=DROP_SPEED
        DRAW._R_51(R_51, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R52:
        if R_52 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5:
            R_52 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5
        else: R_52+=DROP_SPEED
        DRAW._R_52(R_52, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R53:
        if R_53 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5:
            R_53 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5
        else: R_53+=DROP_SPEED
        DRAW._R_53(R_53, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R54:
        if R_54 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5:
            R_54 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5
        else: R_54+=DROP_SPEED
        DRAW._R_54(R_54, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R55:
        if R_55 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5:
            R_55 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5
        else: R_55+=DROP_SPEED
        DRAW._R_55(R_55, CHIP_RECT, ingame_helper.P1_COLOR)

    if a_R56:
        if R_56 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5:
            R_56 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5
        else: R_56+=DROP_SPEED
        DRAW._R_56(R_56, CHIP_RECT, ingame_helper.P1_COLOR)

##=============================================================================== FOR YELLOW
    if a_Y00:
        if Y_00 == image.BOARDRECT.bottom-SQUARE_SIZE:
            Y_00 = image.BOARDRECT.bottom-SQUARE_SIZE
        else: Y_00+=DROP_SPEED
        DRAW._R_00(Y_00, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y01:
        if Y_01 == image.BOARDRECT.bottom-SQUARE_SIZE:
            Y_01 = image.BOARDRECT.bottom-SQUARE_SIZE
        else: Y_01+=DROP_SPEED
        DRAW._R_01(Y_01, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y02:
        if Y_02 == image.BOARDRECT.bottom-SQUARE_SIZE:
            Y_02 = image.BOARDRECT.bottom-SQUARE_SIZE
        else: Y_02+=DROP_SPEED
        DRAW._R_02(Y_02, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y03:
        if Y_03 == image.BOARDRECT.bottom-SQUARE_SIZE:
            Y_03 = image.BOARDRECT.bottom-SQUARE_SIZE
        else: Y_03+=DROP_SPEED
        DRAW._R_03(Y_03, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y04:
        if Y_04 == image.BOARDRECT.bottom-SQUARE_SIZE:
            Y_04 = image.BOARDRECT.bottom-SQUARE_SIZE
        else: Y_04+=DROP_SPEED
        DRAW._R_04(Y_04, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y05:
        if Y_05 == image.BOARDRECT.bottom-SQUARE_SIZE:
            Y_05 = image.BOARDRECT.bottom-SQUARE_SIZE
        else: Y_05+=DROP_SPEED
        DRAW._R_05(Y_05, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y06:
        if Y_06 == image.BOARDRECT.bottom-SQUARE_SIZE:
            Y_06 = image.BOARDRECT.bottom-SQUARE_SIZE
        else: Y_06+=DROP_SPEED
        DRAW._R_06(Y_06, CHIP_RECT, ingame_helper.P2_COLOR)
#=====================================================================
    if a_Y10:
        if Y_10 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1:
            Y_10 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1
        else: Y_10+=DROP_SPEED
        DRAW._R_10(Y_10, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y11:
        if Y_11 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1:
            Y_11 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1
        else: Y_11+=DROP_SPEED
        DRAW._R_11(Y_11, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y12:
        if Y_12 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1:
            Y_12 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1
        else: Y_12+=DROP_SPEED
        DRAW._R_12(Y_12, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y13:
        if Y_13 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1:
            Y_13 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1
        else: Y_13+=DROP_SPEED
        DRAW._R_13(Y_13, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y14:
        if Y_14 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1:
            Y_14 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1
        else: Y_14+=DROP_SPEED
        DRAW._R_14(Y_14, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y15:
        if Y_15 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1:
            Y_15 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1
        else: Y_15+=DROP_SPEED
        DRAW._R_15(Y_15, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y16:
        if Y_16 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1:
            Y_16 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER1
        else: Y_16+=DROP_SPEED
        DRAW._R_16(Y_16, CHIP_RECT, ingame_helper.P2_COLOR)
#===================================================================
    if a_Y20:
        if Y_20 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2:
            Y_20 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2
        else: Y_20+=DROP_SPEED
        DRAW._R_20(Y_20, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y21:
        if Y_21 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2:
            Y_21 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2
        else: Y_21+=DROP_SPEED
        DRAW._R_21(Y_21, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y22:
        if Y_22 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2:
            Y_22 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2
        else: Y_22+=DROP_SPEED
        DRAW._R_22(Y_22, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y23:
        if Y_23 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2:
            Y_23 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2
        else: Y_23+=DROP_SPEED
        DRAW._R_23(Y_23, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y24:
        if Y_24 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2:
            Y_24 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2
        else: Y_24+=DROP_SPEED
        DRAW._R_24(Y_24, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y25:
        if Y_25 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2:
            Y_25 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2
        else: Y_25+=DROP_SPEED
        DRAW._R_25(Y_25, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y26:
        if Y_26 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2:
            Y_26 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER2
        else: Y_26+=DROP_SPEED
        DRAW._R_26(Y_26, CHIP_RECT, ingame_helper.P2_COLOR)
#===================================================================
    if a_Y30:
        if Y_30 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3:
            Y_30 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3
        else: Y_30+=DROP_SPEED
        DRAW._R_30(Y_30, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y31:
        if Y_31 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3:
            Y_31 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3
        else: Y_31+=DROP_SPEED
        DRAW._R_31(Y_31, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y32:
        if Y_32 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3:
            Y_32 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3
        else: Y_32+=DROP_SPEED
        DRAW._R_32(Y_32, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y33:
        if Y_33 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3:
            Y_33 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3
        else: Y_33+=DROP_SPEED
        DRAW._R_33(Y_33, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y34:
        if Y_34 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3:
            Y_34 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3
        else: Y_34+=DROP_SPEED
        DRAW._R_34(Y_34, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y35:
        if Y_35 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3:
            Y_35 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3
        else: Y_35+=DROP_SPEED
        DRAW._R_35(Y_35, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y36:
        if Y_36 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3:
            Y_36 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER3
        else: Y_36+=DROP_SPEED
        DRAW._R_36(Y_36, CHIP_RECT, ingame_helper.P2_COLOR)

#===================================================================
    if a_Y40:
        if Y_40 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4:
            Y_40 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4
        else: Y_40+=DROP_SPEED
        DRAW._R_40(Y_40, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y41:
        if Y_41 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4:
            Y_41 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4
        else: Y_41+=DROP_SPEED
        DRAW._R_41(Y_41, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y42:
        if Y_42 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4:
            Y_42 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4
        else: Y_42+=DROP_SPEED
        DRAW._R_42(Y_42, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y43:
        if Y_43 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4:
            Y_43 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4
        else: Y_43+=DROP_SPEED
        DRAW._R_43(Y_43, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y44:
        if Y_44 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4:
            Y_44 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4
        else: Y_44+=DROP_SPEED
        DRAW._R_44(Y_44, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y45:
        if Y_45 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4:
            Y_45 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4
        else: Y_45+=DROP_SPEED
        DRAW._R_45(Y_45, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y46:
        if Y_46 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4:
            Y_46 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER4
        else: Y_46+=DROP_SPEED
        DRAW._R_46(Y_46, CHIP_RECT, ingame_helper.P2_COLOR)
#===================================================================
    if a_Y50:
        if Y_50 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5:
            Y_50 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5
        else: Y_50+=DROP_SPEED
        DRAW._R_50(Y_50, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y51:
        if Y_51 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5:
            Y_51 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5
        else: Y_51+=DROP_SPEED
        DRAW._R_51(Y_51, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y52:
        if Y_52 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5:
            Y_52 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5
        else: Y_52+=DROP_SPEED
        DRAW._R_52(Y_52, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y53:
        if Y_53 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5:
            Y_53 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5
        else: Y_53+=DROP_SPEED
        DRAW._R_53(Y_53, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y54:
        if Y_54 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5:
            Y_54 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5
        else: Y_54+=DROP_SPEED
        DRAW._R_54(Y_54, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y55:
        if Y_55 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5:
            Y_55 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5
        else: Y_55+=DROP_SPEED
        DRAW._R_55(Y_55, CHIP_RECT, ingame_helper.P2_COLOR)

    if a_Y56:
        if Y_56 == image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5:
            Y_56 = image.BOARDRECT.bottom-SQUARE_SIZE*MULTIPLIER5
        else: Y_56+=DROP_SPEED
        DRAW._R_56(Y_56, CHIP_RECT, ingame_helper.P2_COLOR)

#======================================================= play dropeed sound

    if _I_BOARD:
        if alter == 0:
            image._I_BOARDRED()
        elif alter == 1:
            image._I_BOARDBLUE()
    if _I_BOARD2:
        image._I_BOARDGREEN()
        alter += 1
        alter %= 2

    image.BOARD()

    image.OPTION_B()
    if OPTION_GLOW:
        image.I_OPTION_B()

    image.NEW_B()
    if NEW_GLOW:
        image.I_NEW_B()
    image.UNDO_B()
    if SWAP_GLOW:
        image.I_UNDO_B()

    #PUPPET_SHOWS()
    image._CURTAIN()
    image._SHADOW()

    image.BULB()
    y = bulb_illum.delay()
    BULB_I(y)

    image._TITLE()
    if TITLE_GLOW:
        image._TITLE_GLOW()

    combased_clock()

    if logic.get_GAME_MODE() == 'SINGLE MATCH':
        BLIT(image.SINGLE_MATCH_PROMPT_BOTTOM,image.B4_BOTTOM_RECT)
    elif logic.get_GAME_MODE() == 'BEST OF 4':
        BLIT(image.B4_PROMPT_BOTTOM,image.B4_BOTTOM_RECT)

    if ingame_helper.ENABLE_INGAME_MOUSE:
        if MAIN_CURSOR:
            image._CURSOR_MAIN()
        elif CURSOR_RED:
            image._CURSOR_RED()
        elif CURSOR_YELLOW:
            image._CURSOR_YELLOW()

def start_INGAME():
    #print(ingame_helper.swapper, ingame_helper.THEY_SWAP)
    if logic.FROM_SAVES: pass
    elif scenes.get_previous_SCENE() == 'GAME MODE' or scenes.get_previous_SCENE() == scenes.get_SCENE() or \
    scenes.get_previous_SCENE() == 'HOW TO PLAY' and scenes.from_ingame_access == False:
        NEW(); ingame_bool.reset(); ingame_helper._reset()
        win.reset_winner() #reset winn prompt
        ingame_helper.init_B4();  #if single match proceed to game mode if new
    else: pass

    if sounds.GLOBAL_SOUND:
        if scenes.get_previous_SCENE() == 'GAME MODE' or scenes.get_previous_SCENE() == 'HOW TO PLAY':
            sounds.fadeout_ALL()
            sounds.INGAME_SOUND()
    options2.pause = False

    if scenes.HOW_TO_PLAY_IS_SELECTED == False:
        scenes.HOW_TO_PLAY_IS_SELECTED = True
        scenes.from_ingame_access = True
        scenes.create_scene('HOW TO PLAY')

    while scenes.scene == 'INGAME':
        IN_GAME()
        if ingame_helper.ENABLE_INGAME_MOUSE:
            INGAME_Event_Handler()

        if ingame_helper.show_winner_info:
            if win.show_winner_one:
                BLIT(image.P1_WINNER,image.INFO_P1_RECT)
            if win.show_winner_two:
                BLIT(image.P2_WINNER,image.INFO_P1_RECT)
            if win.show_tie:
                BLIT(image.STALEMATE_GAME,image.INFO_P1_RECT)

        if win.show_winner_one:
            if logic.get_GAME_MODE() == 'BEST OF 4':
                if logic.get_CURRENT_SCORE(1) == 4: BLIT(image.FINAL_B4_P1,image.ORIGIN)
                else: BLIT(image.B4_P1_WINNER,image.ORIGIN)
            else: BLIT(image.WINNER_ONE,image.ORIGIN)
        if win.show_winner_two:
            if logic.get_GAME_MODE() == 'BEST OF 4':
                if logic.get_CURRENT_SCORE(2) == 4: BLIT(image.FINAL_B4_P2,image.ORIGIN)
                else: BLIT(image.B4_P2_WINNER,image.ORIGIN)
            else: BLIT(image.WINNER_TWO,image.ORIGIN)
        if win.show_tie:
            if logic.get_GAME_MODE() == 'BEST OF 4': BLIT(image.B4_STALEMATE,image.ORIGIN)
            else: BLIT(image.STALEMATE,image.ORIGIN)

        if win.new_glow: BLIT(image.NEW_BUTTON_GLOW,image.ORIGIN)
        if win.quit_glow: BLIT(image.QUIT_BUTTON_GLOW,image.ORIGIN)
        if win.show_next_round_glow: BLIT(image.NEXT_ROUND_GLOW,image.ORIGIN)

        if ingame_helper.ENABLE_WIN_MOUSE:
            image._CURSOR_MAIN()

        if not ingame_helper.ENABLE_INGAME_MOUSE:
            win.winner_event_handler()
        #print_current_mouse_position()

        UPDATE()

if  __name__ == '__main__':
    scenes.scene = 'INGAME'
    start_INGAME()


'''elif event.key == K_p: #---------------- p
                sounds.CIRCUS_E()
                MOVEx = -400
                MOVEy = 300
                puppet = True
            elif event.key == K_e: #---------------- e
                MOVEx = int(window_scale[0]/2)+800
                MOVEy = 400
                sounds.ELEPHANT_E()
                elephantleft = True'''
