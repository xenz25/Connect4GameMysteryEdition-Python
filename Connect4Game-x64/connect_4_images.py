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
from _connect4_graphics import *
from _connect4_sounds import *


def loadImage(path='',convert = '', transform = False, scale = (0,0)):
    x = pg.image.load(path)
    if convert == 'mode1' and transform == False:
        x = x.convert()
    elif convert == 'mode2' and transform == False:
        x = x.convert_alpha()
    elif transform == True and convert == False:
        x = pg.transform.scale(scale)
    elif convert == 'mode1' and transform == True and scale != (0,0):
        x = x.convert()
        x = pg.transform.scale(x,scale)
    elif convert == 'mode2' and transform == True and scale != (0,0):
        x = x.convert_alpha()
        x = pg.transform.scale(x,scale)
    else: pass
    return x

def BLIT(surf, pos=()):
    game_window.MAIN_WINDOW.blit(surf,pos)

def RECT(surf):
    x= surf.get_rect()
    return x

def DRAW_RECT(pos=(),size=()):
    pg.draw.rect(game_window.MAIN_WINDOW,WHITE,(pos[0],pos[1],size[0],size[1]))


class IMAGES():
    def __init__(self):
        self.ORIGIN = (0,0)
        self.YOFFSET = 20
        self.BG = loadImage('images\BG_MAIN3.png','mode1',True,window_scale)
        self.BG_2 = loadImage('images\BG_MAIN4.png','mode1',True,window_scale)
        self.BGRECT = RECT(self.BG)
        self.BGRECT.center = (int(window_scale[0]/2),int(window_scale[1]/2))

        self.LOGO = loadImage('images\\SAMPLE_LOGO_IMAGE.png','mode1',True, window_scale)
        self.FULL_LOGO = loadImage('images\\CONNECT_4_LOGO_FULL.png','mode1',True, window_scale)
        self.FULL_LOGO_MAX_BRIGHT = loadImage('images\\CONNECT_4_LOGO_FULL_MAX_BRIGHT.png','mode1',True, window_scale)
        self.WARNING = loadImage('images\\WARNING_INTRO.png','mode1',True, window_scale)
        self.BORDER_INTRO = loadImage('images\\INTRO_BORDER.png','mode1',True, window_scale)
        self.PRODUCTIONS = loadImage('images\\PRODUCTIONS_INTRO.png','mode1',True, window_scale)

        self.CONSTRUCTION = loadImage('images\\UNDER_NOTICE.png','mode2',True, window_scale)
        self.BACK_CURSOR = loadImage('images\\BACK_CURSOR_RED.png','mode2')
        self.BACK_CURSOR_RECT = RECT(self.BACK_CURSOR)

        self.CURTAIN_LEFT = loadImage('images\CURTAIN_LEFT.png','mode2')
        self.CURTAIN_LPOS = (0,0)

        self.CURTAIN_RIGHT = loadImage('images\CURTAIN_RIGHT.png','mode2')
        self.CURTAIN_RECT = RECT(self.CURTAIN_RIGHT)
        self.CURTAIN_RECT.topright = (1316,0)
        self.CURTAIN_RPOS = self.CURTAIN_RECT

        self.SHADOW_TOP1 = loadImage('images\SHADOW_TOP.png','mode2')
        self.SHADOW_TOPPOS = (0,0)

        self.MAN_CIRCUS1 = loadImage('images\MAN_CIRCUS.png','mode2')
        self.BMAN_CIRCUSGRECT = RECT(self.BG)

        self.ELEPHANT_L1 = loadImage('images\ELEPHANT_L.png','mode2')
        self.ELEPHANT_R1 = loadImage('images\ELEPHANT_R.png','mode2')

        self.SHADOW_BOTTOM1 = loadImage('images\SHADOW_BOTTOM.png','mode2')
        self.SHADOW_BOTTOMRECT = RECT(self.SHADOW_BOTTOM1)
        self.SHADOW_BOTTOMRECT.bottomleft = (0,718)#(self.TEMPLATERECT.bottomleft[0],self.TEMPLATERECT.bottomleft[1]+25)

        self.TITLE = loadImage('images\TITLE.png','mode2')
        self.TITLE_RECT = RECT(self.TITLE)
        self.TITLE_G = loadImage('images\TITLE_GLOW.png','mode2')
        self.TITLERECT = RECT(self.TITLE)
        self.TITLERECT.center = (int(window_scale[0]/2),75)

        self.CLOCK = loadImage('images\CLOCK.png','mode2')
        self.CLOCKRECT = RECT(self.CLOCK)
        self.CLOCKRECT.center = (int(window_scale[0]/2),150)

        self.I_CLOCK1 = loadImage('images\_I_CLOCK.png','mode2')
        self.I_CLOCKRECT = RECT(self.CLOCK)
        self.I_CLOCKRECT.center = (int(window_scale[0]/2),150)

        L_BULB1 = loadImage('images\L_BULB.png','mode1')
        self.L_BULB1 = pg.transform.scale(L_BULB1,(20,20))
        self.BULB1 = loadImage('images\BULB.png','mode1',True,(20,20))

        self.BOARDSIZE = (476,408)
        self.BOARD1 = loadImage('images\BOARD.png','mode2')
        self.BOARD1 = pg.transform.scale(self.BOARD1,self.BOARDSIZE)
        self.BOARD_BACK1 = loadImage('images\BOARD_BACK.png','mode2')
        self.BOARDRECT = RECT(self.BOARD1)
        self.BOARDRECT.center = (int(window_scale[0]/2),456)
##---------------------------------------
        self.I_BOARDBLUE = loadImage('images\I_BOARDBLUE.png','mode2')
        self.I_BOARDRECT = RECT(self.I_BOARDBLUE)
        self.I_BOARDRECT.center = (int(window_scale[0]/2),456)

        self.I_BOARDRED = loadImage('images\I_BOARDRED.png','mode2')
        self.I_BOARDGREEN = loadImage('images\I_BOARDGREEN.png','mode2')
##---------------------------------------
        self.RED_C1 = loadImage('images\RED_C.png','mode2')
        self.RED_C1RECT = RECT(self.RED_C1)
        self.YELLOW_C1 = loadImage('images\YELLOW_C.png','mode2')
        self.YELLOW_C1RECT = RECT(self.YELLOW_C1)

        self.OPTION_B1 = loadImage('images\OPTION_B.png','mode2')
        self.OPTION_BRECT = RECT(self.OPTION_B1)
        self.OPTION_BRECT.center = (window_scale[0]-200,window_scale[1]-100)

        self.I_OPTION_B1 = loadImage('images\I_OPTION_B.png','mode2')
        self.I_OPTION_BRECT = RECT(self.I_OPTION_B1)
        self.I_OPTION_BRECT.center = (window_scale[0]-200,window_scale[1]-100)

        self.NEW_B1 = loadImage('images\\NEW_B.png','mode2')
        self.NEW_BRECT = RECT(self.NEW_B1)
        self.NEW_BRECT.center = (window_scale[0]-200,window_scale[1]-170)

        self.I_NEW_B1 = loadImage('images\\I_NEW_B.png','mode2')
        self.I_NEW_BRECT = RECT(self.I_NEW_B1)
        self.I_NEW_BRECT.center = (window_scale[0]-200,window_scale[1]-170)

        self.UNDO_B1 = loadImage('images\\UNDO_B.png','mode2')
        self.UNDO_BRECT = RECT(self.UNDO_B1)
        self.UNDO_BRECT.center = (window_scale[0]-200,window_scale[1]-240)

        self.I_UNDO_B1 = loadImage('images\\I_UNDO_B.png','mode2')
        self.I_UNDO_BRECT = RECT(self.I_UNDO_B1)
        self.I_UNDO_BRECT.center = (window_scale[0]-200,window_scale[1]-240)

##------------------------------------------------------------------------------------ HOME ASSETS
        self.HOME_BRICK = loadImage('images\\HOME\\HOME_BRICK2.png','mode2', True, window_scale)
        self.HOME_BRICKRECT = RECT(self.HOME_BRICK)
        self.HOME_BRICKRECT.center = (int(window_scale[0]/2),int(window_scale[1]/2))
        self.ARROW_GLOW = loadImage('images\\HOME\\ARROW_GLOW.png','mode2', True, window_scale) #ARROW GLOW
        self.BALLOON = loadImage('images\\HOME\\BALLOON.png','mode2', True, window_scale) #BALLOON
        self.CONNECT_GLOW = loadImage('images\\HOME\\CONNECT_GLOW.png','mode2', True, window_scale) #TITLE CONNECT GLOW
        self.EXIT = loadImage('images\\HOME\\EXIT.png','mode2', True, window_scale)     #EXIT
        self.EXIT_GLOW = loadImage('images\\HOME\\EXIT_GLOW.png','mode2', True, window_scale) #EXIT GLOW
        self.EXTRAS = loadImage('images\\HOME\\EXTRAS.png','mode2', True, window_scale) #EXTRAS
        self.EXTRAS_GLOW = loadImage('images\\HOME\\EXTRAS_GLOW.png','mode2', True, window_scale) #EXTRAS GLOW
        self.HOW_TO_PLAY = loadImage('images\\HOME\\HOW_TO_PLAY.png','mode2', True, window_scale) #HOW TO PLAY
        self.HOW_TO_PLAY_GLOW = loadImage('images\\HOME\\HOW_TO_PLAY_GLOW.png','mode2', True, window_scale) #HOW TO PLAY GLOW
        self.OPTIONS = loadImage('images\\HOME\\OPTIONS.png','mode2', True, window_scale) #OPTIONS
        self.OPTIONS_GLOW = loadImage('images\\HOME\\OPTIONS_GLOW.png','mode2', True, window_scale) #OPTIONS GLOW
        self.PLAY = loadImage('images\\HOME\\PLAY.png','mode2', True, window_scale) #PLAY
        self.PLAY_GLOW = loadImage('images\\HOME\\PLAY_GLOW.png','mode2', True, window_scale) #PLAY GLOW
##------------------------------------------------------------------------------------------ QUIT DIALOG FAMILY
        self.QUIT_DIALOG = loadImage('images\\QUIT_DIALOG.png','mode2', True, window_scale) #PLAY GLOW
        self.QUIT_DIALOG_RECT  = RECT(self.QUIT_DIALOG)
        self.QUIT_DIALOG_RECT.center = (int(window_scale[0]/2), int(window_scale[1]/2))
        self.FLICKER = loadImage('images\\HOME\\LIGHT_FLICK.png','mode2', True, window_scale)
        self.QUIT_DIALOG_YES_GLOW = loadImage('images\\QUIT_DIALOG_YES_GLOW.png','mode2', True, window_scale) #YES GLOW OF QUIT DIALOG
        self.QUIT_DIALOG_NO_GLOW = loadImage('images\\QUIT_DIALOG_NO_GLOW.png','mode2', True, window_scale) #NO GLOW OF QUIT DIALOG

##---------------------------------------------------------------------------- CREDITS FAMILY
        self.CREDITS = loadImage('images\\CREDITS\\CREDITS.png','mode1', True, window_scale)
        self.STEVEN = loadImage('images\\CREDITS\\STEVEN_CREDITS.png','mode1', True, window_scale)
        self.XEN = loadImage('images\\CREDITS\\XEN_CREDITS.png','mode1', True, window_scale)
        self.ELBERT = loadImage('images\\CREDITS\\ELBERT_CREDITS.png','mode1', True, window_scale)
        self.LAURENT = loadImage('images\\CREDITS\\LAURENT_CREDITS.png','mode1', True, window_scale)

##---------------------------------------------------------------------- CURSOR FAMILY
        self.CURSOR_M = loadImage('images\CURSOR.png','mode2')
        self.CURSOR_R = loadImage('images\CURSOR_RED.png','mode2')
        self.CURSOR_Y = loadImage('images\CURSOR_YELLOW.png','mode2')
        self.CURSOR_RECT = RECT(self.CURSOR_R)
##----------------------------------------------------------------------- GAME NODE FAMILY
        self.GEAR = loadImage('images\\GAME MODE\\GEAR.png','mode2')
        self.SHADE = loadImage('images\\GAME MODE\\LIGHT SHADE.png','mode2')
        self.GAME_MODE_BG_NORMAL = loadImage('images\\GAME MODE\\GAME MODE NORMAL.png','mode1', True, window_scale)
        self.GAME_MODE_BG_GLOW = loadImage('images\\GAME MODE\\GAME MODE GLOW.png','mode1', True, window_scale)
        self.AI_GLOW = loadImage('images\\GAME MODE\\AI GLOW.png','mode2') #AI
        self.BEST_OF_4_GLOW = loadImage('images\\GAME MODE\\BEST OF 4 GLOW.png','mode2') #BEST OF 4
        self.SINGLE_MATCH_GLOW = loadImage('images\\GAME MODE\\SINGLE MATCH GLOW.png','mode2') #SINGLE MATCH
        self.BACK_BUTTON = loadImage('images\\GAME MODE\\BACK NORMAL.png','mode2') #back button
        self.BACK_BUTTON_GLOW = loadImage('images\\GAME MODE\\BACK GLOW NORMAL.png','mode2') #back button GLOW

##----------------------------------------------------------------------- OPTIONS FAMILY
        self.OPTIONS_BLUR = loadImage('images\\OPTIONS\\OPTIONS BLUR.png','mode1', True, window_scale) #OPTIONS BLUR
        self.OPTIONS_PANEL = loadImage('images\\OPTIONS\\OPTIONS PANEL.png','mode2', True, window_scale) #OPTIONS PANEL
        self.FULL_SCREEN_GLOW = loadImage('images\\OPTIONS\\FULL SCREEN GLOW.png','mode2') #FULL SCREEN BUTTON
        self.FULL_SCREEN_NON_ACTIVE = loadImage('images\\OPTIONS\\FULL SCREEN NON ACTIVE.png','mode2') #FULL SCREEN NON ACTIVE
        self.SOUND_GLOW = loadImage('images\\OPTIONS\\SOUND GLOW.png','mode2') #SOUND GLOW
        self.SOUND_NON_ACTIVE = loadImage('images\\OPTIONS\\SOUND NON ACTIVE.png','mode2') #SOUND NON ACTIVE

##----------------------------------------------------------------------- OPTIONS 2 FAMILY
        self.OPTIONS_BLUR2 = loadImage('images\\OPTIONS2\\OPTIONS BLUR.png','mode1', True, window_scale) #OPTIONS BLUR
        self.GAME_PAUSED_PANEL = loadImage('images\\OPTIONS2\\GAME PAUSED.png','mode2', True, window_scale) #GAME PAUSE PANEL
        self.OPTIONS2_PANEL = loadImage('images\\OPTIONS2\\OPTIONS PANEL.png','mode2', True, window_scale) #OPTIONS PANEL
        self.FULL_SCREEN_GLOW2 = loadImage('images\\OPTIONS2\\FULL SCREEN GLOW.png','mode2') #FULL SCREEN BUTTON
        self.FULL_SCREEN_NON_ACTIVE2 = loadImage('images\\OPTIONS2\\FULL SCREEN NON ACTIVE.png','mode2') #FULL SCREEN NON ACTIVE
        self.SOUND_GLOW2 = loadImage('images\\OPTIONS2\\SOUND GLOW.png','mode2') #SOUND GLOW
        self.SOUND_NON_ACTIVE2 = loadImage('images\\OPTIONS2\\SOUND NON ACTIVE.png','mode2') #SOUND NON ACTIVE
        self.HOME_GLOW2 = loadImage('images\\OPTIONS2\\HOME GLOW.png','mode2') #HOME GLOW
        self.HOME_NON_ACTIVE2 = loadImage('images\\OPTIONS2\\HOME NON ACTIVE.png','mode2') #HOME NON ACTIVE

##----------------------------------------------------------------------- HOW TO PLAY FAMILY
        self.HOW_TO_PLAY_TOP_BG = loadImage('images\\HOW TO PLAY\\HOW TO PLAY TOP BG.png','mode2') #TOP ASSETS INCLUDE FRAMES
        self.BUTTON_LEFT_GLOW = loadImage('images\\HOW TO PLAY\\GLOW BUTTON LEFT.png','mode2') #BUTTON LEFT GLOW
        self.BUTTON_RIGHT_GLOW = loadImage('images\\HOW TO PLAY\\GLOW BUTTON RIGHT.png','mode2') #BUTTON RIGHT GLOW
        self.WELCOME_GLOW = loadImage('images\\HOW TO PLAY\\WELCOME GLOW.png','mode2') #WELCOME GLOW
        self.RULE_GLOW = loadImage('images\\HOW TO PLAY\\RULES GLOW.png','mode2') #RULE GLOW
        self.GUIDES_GLOW = loadImage('images\\HOW TO PLAY\\GUIDES GLOW.png','mode2') #GUIDES GLOW
        self.BACK_GLOW = loadImage('images\\HOW TO PLAY\\BACK GLOW.png','mode2') #BACK GLOW
        self.RULES1 = loadImage('images\\HOW TO PLAY\\RULES 1.png','mode1') #RULES 1
        self.RULES2 = loadImage('images\\HOW TO PLAY\\RULES 2.png','mode1') #RULES 2
        self.WELCOME = loadImage('images\\HOW TO PLAY\\WELCOME.png','mode1') #WELCOME

        self.SINGLE_MATCH = loadImage('images\\HOW TO PLAY\\SINGLE MATCH GUIDE.png','mode1') #SM
        self.AI_MATCH = loadImage('images\\HOW TO PLAY\\AI GUIDE.png','mode1') #AI
        self.B4_MATCH = loadImage('images\\HOW TO PLAY\\B4 GUIDE.png','mode1') #B4
        self.CHIP_INFO = loadImage('images\\HOW TO PLAY\\CHIP GUIDE.png','mode1') #CHIP
        self.BOARD_INFO = loadImage('images\\HOW TO PLAY\\BOARD GUIDE.png','mode1') #BOARD
        self.SWAP_B_INFO = loadImage('images\\HOW TO PLAY\\SWAP GUIDE.png','mode1') #SWAP
        self.OPTIONS_B_INFO = loadImage('images\\HOW TO PLAY\\OPTIONS GUIDE.png','mode1') #OPTIONS
        self.NEW_B_INFO = loadImage('images\\HOW TO PLAY\\NEW GUIDE.png','mode1') #NEW
        self.CLOCK_GUIDE = loadImage('images\\HOW TO PLAY\\CLOCK GUIDE.png','mode1')#CLOCK
        self.DROP_GUIDE = loadImage('images\\HOW TO PLAY\\DROP GUIDE.png','mode1') #DROP
        self.BACK_GUIDE = loadImage('images\\HOW TO PLAY\\BACK GUIDE.png','mode1') #BACK
        self.BLUE_CURSOR_GUIDE = loadImage('images\\HOW TO PLAY\\BLUE CURSOR GUIDE.png','mode1') #BLUE
        self.SCORE_GUIDE = loadImage('images\\HOW TO PLAY\\SCORE GUIDE.png','mode1') #score guide
        self.TURN_GUIDE = loadImage('images\\HOW TO PLAY\\TURN GUIDE.png','mode1') #turn guide

##------------------------------------------------------------------------------------ INGAME FAMILY
        ##---------------------- INFO TAB
        self.INFO_NEW = loadImage('images\\INGAME\\INFO\\INFO NEW.png','mode2')
        self.INFO_SWAP = loadImage('images\\INGAME\\INFO\\INFO SWAP.png','mode2')
        self.INFO_WELCOME = loadImage('images\\INGAME\\INFO\\INFO WELCOME.png','mode2')
        self.INFO_P1 = loadImage('images\\INGAME\\INFO\\INFO P1.png','mode2')
        self.INFO_P1_RECT = RECT(self.INFO_P1)
        self.INFO_P1_RECT.topright = (1316,0)
        self.INFO_P2 = loadImage('images\\INGAME\\INFO\\INFO P2.png','mode2')
        self.INFO_OPTIONS = loadImage('images\\INGAME\\INFO\\INFO OPTIONS.png','mode2')


        ##---------------------- P1
        self.P1_RED = loadImage('images\\INGAME\\P1\\P1 INFO RED.png','mode2')
        self.P1_YELLOW = loadImage('images\\INGAME\\P1\\P1 INFO YELLOW.png','mode2')
        self.P1_SCORE_0 = loadImage('images\\INGAME\\P1\\P1 SCORE 0.png','mode2')
        self.P1_SCORE_1 = loadImage('images\\INGAME\\P1\\P1 SCORE 1.png','mode2')
        self.P1_SCORE_2 = loadImage('images\\INGAME\\P1\\P1 SCORE 2.png','mode2')
        self.P1_SCORE_3 = loadImage('images\\INGAME\\P1\\P1 SCORE 3.png','mode2')
        self.P1_SCORE_4 = loadImage('images\\INGAME\\P1\\P1 SCORE 4.png','mode2')
        self.P1_GLOW = loadImage('images\\INGAME\\P1\\P1 GLOW.png','mode2')


        ##---------------------- P2
        self.P2_RED = loadImage('images\\INGAME\\P2\\P2 INFO RED.png','mode2')
        self.P2_YELLOW = loadImage('images\\INGAME\\P2\\P2 INFO YELLOW.png','mode2')
        self.P2_SCORE_0 = loadImage('images\\INGAME\\P2\\P2 SCORE 0.png','mode2')
        self.P2_SCORE_1 = loadImage('images\\INGAME\\P2\\P2 SCORE 1.png','mode2')
        self.P2_SCORE_2 = loadImage('images\\INGAME\\P2\\P2 SCORE 2.png','mode2')
        self.P2_SCORE_3 = loadImage('images\\INGAME\\P2\\P2 SCORE 3.png','mode2')
        self.P2_SCORE_4 = loadImage('images\\INGAME\\P2\\P2 SCORE 4.png','mode2')
        self.P2_GLOW = loadImage('images\\INGAME\\P2\\P2 GLOW.png','mode2')
        self.P2_GLOW_RECT = RECT(self.P2_GLOW)
        self.P2_GLOW_RECT.bottomleft = (0,718)

        ##---------------------- WIN PROMPT
        self.WINNER_ONE = loadImage('images\\INGAME\\PLAYER ONE WIN.png','mode2')
        self.WINNER_TWO = loadImage('images\\INGAME\\PLAYER TWO WIN.png','mode2')
        self.STALEMATE = loadImage('images\\INGAME\\STALEMATE.png','mode2')
        self.NEW_BUTTON_GLOW = loadImage('images\\INGAME\\NEW GLOW.png','mode2')
        self.QUIT_BUTTON_GLOW = loadImage('images\\INGAME\\QUIT GLOW.png','mode2')
        self.P1_WINNER = loadImage('images\\INGAME\\INFO\\P1 WIN.png','mode2')
        self.P2_WINNER = loadImage('images\\INGAME\\INFO\\P2 WIN.png','mode2')
        self.STALEMATE_GAME = loadImage('images\\INGAME\\INFO\\STALEMATE.png','mode2')
        self.B4_P1_WINNER = loadImage('images\\INGAME\\B4 PLAYER ONE WIN.png','mode2')
        self.B4_P2_WINNER = loadImage('images\\INGAME\\B4 PLAYER TWO WIN.png','mode2')
        self.B4_STALEMATE = loadImage('images\\INGAME\\B4 STALEMATE.png','mode2')
        self.NEXT_ROUND_GLOW = loadImage('images\\INGAME\\NEXT ROUND GLOW.png','mode2')
        self.FINAL_B4_P1 = loadImage('images\\INGAME\\B4 PLAYER ONE WIN FINAL.png','mode2')
        self.FINAL_B4_P2 = loadImage('images\\INGAME\\B4 PLAYER TWO WIN FINAL.png','mode2')
        self.B4_PROMPT_BOTTOM = loadImage('images\\INGAME\\BEST OF 4 PROMPT.png','mode2')
        self.B4_BOTTOM_RECT = RECT(self.B4_PROMPT_BOTTOM)
        self.B4_BOTTOM_RECT.bottomright = (1316,718)
        self.SINGLE_MATCH_PROMPT_BOTTOM = loadImage('images\\INGAME\\SINGLE MATCH PROMPT.png','mode2')

##======================================== IMAGES METHODS
    def _CURSOR_MAIN(self):
        pos = pg.mouse.get_pos()
        self.CURSOR_RECT.topleft = pos
        BLIT(self.CURSOR_M,self.CURSOR_RECT)

    def _CURSOR_BACK(self):
        pos = pg.mouse.get_pos()
        self.BACK_CURSOR_RECT.topleft = pos
        BLIT(self.BACK_CURSOR,self.BACK_CURSOR_RECT)

    def _CURSOR_RED(self):
        pos = pg.mouse.get_pos()
        self.CURSOR_RECT.topleft = pos
        BLIT(self.CURSOR_R,self.CURSOR_RECT)

    def _CURSOR_YELLOW(self):
        pos = pg.mouse.get_pos()
        self.CURSOR_RECT.topleft = pos
        BLIT(self.CURSOR_Y,self.CURSOR_RECT)

    def SHOW_LOGO(self):
        BLIT(self.LOGO,self.ORIGIN)

    def SHOW_LOGO_GLOW(self):
        BLIT(self.LOGO_GLOW,self.ORIGIN)

    def SHOW_FULL_LOGO(self):
        BLIT(self.FULL_LOGO,self.ORIGIN)

    def SHOW_FULL_LOGO_MAX_BRIGHT(self):
        BLIT(self.FULL_LOGO_MAX_BRIGHT,self.ORIGIN)
#--------------------------------------------------------------- HOME PARTS
##------------------------------------- CREDITS FAMILY
    def SHOW_CREDITS(self):
        BLIT(self.CREDITS, self.ORIGIN)

    def SHOW_STEVEN(self):
        BLIT(self.STEVEN,self.ORIGIN)

    def SHOW_XEN(self):
        BLIT(self.XEN,self.ORIGIN)

    def SHOW_ELBERT(self):
        BLIT(self.ELBERT,self.ORIGIN)

    def SHOW_LAURENT(self):
        BLIT(self.LAURENT,self.ORIGIN)
##------------------------------------- CREDITS FAMILY

    def _UNDER_CONSTRUCTION(self):
        BLIT(self.CONSTRUCTION,self.ORIGIN)

    def _BG(self):
        BLIT(self.BG,self.BGRECT)

    def _BG2(self):
        BLIT(self.BG_2,self.BGRECT)


    def _TITLE(self):
        BLIT(self.TITLE,self.TITLERECT)

    def _TITLE_GLOW(self):
        BLIT(self.TITLE_G,self.TITLERECT)

    def _CLOCK(self):
        BLIT(self.CLOCK,self.CLOCKRECT)

    def _I_CLOCK(self):
        BLIT(self.I_CLOCK1,self.I_CLOCKRECT)

    def BULB(self):
        for move in range(0,window_scale[0],50):
            BLIT(self.BULB1,(move,0))

    def L_BULB(self):
        for move in range(0,window_scale[0],50):
            BLIT(self.L_BULB1,(move,0))

    def BOARD(self):
        BLIT(self.BOARD1,self.BOARDRECT)

    def BOARD_BACK(self):
        BLIT(self.BOARD_BACK1,self.BOARDRECT)
##-----------------------------
    def _I_BOARDBLUE(self):
        BLIT(self.I_BOARDBLUE,self.I_BOARDRECT)

    def _I_BOARDRED(self):
        BLIT(self.I_BOARDRED,self.I_BOARDRECT)

    def _I_BOARDGREEN(self):
        BLIT(self.I_BOARDGREEN,self.I_BOARDRECT)
##-----------------------------
    def _RED_C(self,pos=(0,0)):
        self.RED_CRECT = self.RED_C1.get_rect()
        self.RED_CRECT.center = (pos)
        BLIT(self.RED_C1,self.RED_CRECT)

    def _YELLOW_C(self,pos=(0,0)):
        self.YELLOW_CRECT = self.YELLOW_C1.get_rect()
        self.YELLOW_CRECT.center = (pos)
        BLIT(self.YELLOW_C1,self.YELLOW_CRECT)

    def _CIRCUS_MAN(self,posx = 0,posy = 0):
        BLIT(self.MAN_CIRCUS1,(posx,posy))

    def _CURTAIN(self):
        BLIT(self.CURTAIN_LEFT,self.CURTAIN_LPOS)
        BLIT(self.CURTAIN_RIGHT,self.CURTAIN_RPOS)

    def _SHADOW(self):
        BLIT(self.SHADOW_TOP1,self.SHADOW_TOPPOS)
        BLIT(self.SHADOW_BOTTOM1,self.SHADOW_BOTTOMRECT)

    def _ELEPHANT_L(self,posx = 0,posy = 0):
        BLIT(self.ELEPHANT_L1,(posx,posy))

    def _ELEPHANT_R(self,posx = 0,posy = 0):
        BLIT(self.ELEPHANT_R1,(posx,posy))

    def OPTION_B(self):
        BLIT(self.OPTION_B1,self.OPTION_BRECT)

    def I_OPTION_B(self):
        BLIT(self.I_OPTION_B1,self.OPTION_BRECT)

    def NEW_B(self):
        BLIT(self.NEW_B1,self.NEW_BRECT)

    def I_NEW_B(self):
        BLIT(self.I_NEW_B1,self.NEW_BRECT)

    def UNDO_B(self):
        BLIT(self.UNDO_B1,self.UNDO_BRECT)

    def I_UNDO_B(self):
        BLIT(self.I_UNDO_B1,self.UNDO_BRECT)

    def get_REDC1RECT(self):
        self.RED_C1RECT = RECT(self.RED_C1)
        return self.RED_C1RECT.bottom
##--------------------------------------------------------- HOME BLITTING FUNCTIONS
    def HOME_BRICKBG(self):
        BLIT(self.HOME_BRICK,self.HOME_BRICKRECT)

    def CONNECT_4_GLOW(self):
        BLIT(self.CONNECT_GLOW,self.ORIGIN)

    def SHOW_BALLOON(self, posy=0):
        BLIT(self.BALLOON, (0,posy))

    def ARROW_G(self):
        BLIT(self.ARROW_GLOW,self.HOME_BRICKRECT)

    def PLAY_G(self):
        BLIT(self.PLAY_GLOW,self.HOME_BRICKRECT)

    def OPTIONS_G(self):
        BLIT(self.OPTIONS_GLOW,self.HOME_BRICKRECT)

    def EXTRAS_G(self):
        BLIT(self.EXTRAS_GLOW,self.HOME_BRICKRECT)

    def HOW_TO_PLAY_G(self):
        BLIT(self.HOW_TO_PLAY_GLOW,self.HOME_BRICKRECT)

#--------------------------- EXIT FAMILY
    def EXIT_G(self):
        BLIT(self.EXIT_GLOW,self.HOME_BRICKRECT)

    def SHOW_EXIT_DIALOG(self):
        BLIT(self.QUIT_DIALOG,self.QUIT_DIALOG_RECT)

    def SHOW_QUIT_DIALOG_YES_GLOW(self):
        BLIT(self.QUIT_DIALOG_YES_GLOW,self.QUIT_DIALOG_RECT)

    def SHOW_QUIT_DIALOG_NO_GLOW(self):
        BLIT(self.QUIT_DIALOG_NO_GLOW,self.QUIT_DIALOG_RECT)

#--------------------------- EXIT FAMILY
    def LIGHT_FLICK(self):
        BLIT(self.FLICKER,self.ORIGIN)

#------------------------------- GAME MOFE FAMILY
    def SHOW_LIGHT_SHADE(self):
        BLIT(self.SHADE,image.ORIGIN)





image = IMAGES() #CLASS IMAGES



