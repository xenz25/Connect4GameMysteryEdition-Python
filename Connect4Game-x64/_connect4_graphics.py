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
from _connect4_sounds import *

import random
import sys

pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#FPS = 60
clock = pg.time.Clock()
Fullscreen_mode = False

class Frames_Per_Second():
    def __init__(self):
        self.default_graphics = 'NORMAL'
        self.modified_graphics = ''
        self.FPS = 30

    def graphics_speed(self,mode=''):
        if mode.upper() == self.default_graphics:
            self.FPS = 40
        elif mode.upper() == 'HIGH':
            self.FPS = 60
        elif mode.upper() == 'LOW':
            self.FPS = 20

FPS = Frames_Per_Second()

##=================================================================================================== IDENTIFYING SCREEN MAX RESOLUTION
SCREEN_OFFSET = 50
def __ScreenInformation(mode=None):
    global Fullscreen_mode
    if mode == 'automatic':
        WIN= pg.display.Info()
        SCREENWIDTH= WIN.current_w
        SCREENHEIGHT = WIN.current_h
        return (SCREENWIDTH-SCREEN_OFFSET,SCREENHEIGHT-SCREEN_OFFSET)
    elif mode == 'fixed':
        return (1316,718)

    else: raise Exception('Please enter a mode')


main_scale = __ScreenInformation('fixed')
window_scale = __ScreenInformation('fixed')

##=================================================================================================== INIT OF MAIN WINDOW
class _start_MainWindow():
    def __init__(self):
        #,FULLSCREEN|HWSURFACE
        self.screen_counter = 0
        self.screen_condition = 0
        self.fullscreen = True
        self.MAIN_WINDOW = pg.display.set_mode(main_scale,FULLSCREEN|HWSURFACE) #------ MAIN GAME PANEL
        pg.display.set_caption('CONNECT 4 GAME (MYSTERY EDITION)') #---- GAME PANEL CAPTION
        self.GAME_PANEL_ICON = pg.image.load('images\\CONNECT_4_GAME_ICON.png').convert_alpha() #---- GAME PANEL ICON
        self.GAME_PANEL_ICON.set_colorkey(WHITE)
        pg.display.set_icon(self.GAME_PANEL_ICON)
        self.__Fullscreen_mode = True
        self.__WIN = pg.display.Info()

    '''def _analyze_screen(self):
        SCREENWIDTH = 1920#self.__WIN.current_w
        SCREENHEIGHT = 1080#self.__WIN.current_h
        if SCREENWIDTH > 1316 or SCREENHEIGHT > 718:
            self.__Fullscreen_mode = False
        else: self.__Fullscreen_mode = True'''

    def toggle_fullscreen(self):
        if self.screen_counter%2 == 0:
            self.screen_condition = 1
            if self.fullscreen:
                self._NORMAL()
                self.screen_counter+=1
                self.fullscreen = False
        elif self.screen_counter%2 == 1:
            self.screen_condition = 0
            if self.fullscreen == False:
                self.fullscreen = True
                self._FULLSCREEN()
                self.screen_counter=0

    def get_screen_condition(self):
        return self.screen_condition

    def _FULLSCREEN(self):
        self.MAIN_WINDOW = pg.display.set_mode(window_scale,FULLSCREEN|HWSURFACE)

    def _NORMAL(self):
        self.MAIN_WINDOW = pg.display.set_mode(window_scale)

game_window = _start_MainWindow()

##================================================ FUNCTION TO PROPORTIONATE BUTTONS
class NEW_XY_WH():
    def __init__(self,pos=(0,0),pos2=(0,0)):
        self.default_X = pos[0]
        self.default_Y = pos[1]
        self.default_W = pos[0]
        self.default_H = pos[1]
        self.default_screen_width = 1316
        self.default_screen_height = 718

        self.screen_information = pg.display.Info()
        self.screen_information_width = self.screen_information.current_w
        self.screen_information_height = self.screen_information.current_h

        self.x_relative = self.default_X/self.default_screen_width
        self.y_relative = self.default_Y/self.default_screen_height
        self.w_relative = self.default_W/self.default_screen_width
        self.h_relative = self.default_H/self.default_screen_height

        self.left = pos[0]
        self.top = pos[1]
        self.new_w = pos2[0]-pos[0]
        self.new_h = pos2[1]-pos[1]
        self.right = pos2[0]
        self.bottom = pos[1]+self.new_h

        self.__get_new_XY_WH()

    def __get_new_XY_WH(self):
        if self.default_screen_width != self.screen_information_width or self.default_screen_height != self.screen_information_height:
            self.left = self.x_relative*self.screen_information_width
            self.top = self.y_relative*self.screen_information_height
            self.right = self.left + int(self.w_relative*self.screen_information_width)
            self.bottom = self.top + int(self.h_relative*self.screen_information_height)
        else: pass

    def get_new_LF(self):
        return [self.left,self.right]

    def get_new_TB(self):
        return [self.top,self.bottom]


class ROTATE():
    def __init__(self,image=None,pos=(0,0),speed=5):
        self.angle = 0
        self.image = image
        self.image_rect = self.image.get_rect()
        self.image_rect.center = pos
        self.rotation_speed = speed
        self.new_rect = (0,0)
        self.new_image = None

    def show_rotation(self):
        self.angle+=self.rotation_speed
        self.new_image = pg.transform.rotate(self.image,self.angle)
        self.new_rect = self.new_image.get_rect()
        self.new_rect.center = self.image_rect.center
        game_window.MAIN_WINDOW.blit(self.new_image,self.new_rect)

class GAME_PAUSED():
    def __init__(self):
        self.game_paused = True
        self.black_surface = pg.Surface(game_window.MAIN_WINDOW.get_size())
        self.black_surface.set_alpha(50)

    def game_paused_event_handler(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.game_paused = False
                elif event.key == K_RETURN:
                    self.game_paused = False

    def start_PAUSED(self):
        while self.game_paused:
            #game_window.MAIN_WINDOW.fill(WHITE)
            game_window.MAIN_WINDOW.blit(self.black_surface,(0,0))

            self.game_paused_event_handler()
            UPDATE()

##=============================================================================================================EVENT FUNCTIONS
def UPDATE():
    pg.display.flip()
    clock.tick(FPS.FPS)

def print_current_mouse_position():
    mouse = pg.mouse.get_pos()
    print(mouse)

def CLICK(click_sound = 'option 1'):
    x = pg.mouse.get_pressed()
    if x == (1,0,0):
        if click_sound == 'option 1':
            if sounds.GLOBAL_SOUND:
                sounds.B_CLICK()
        elif click_sound == 'option 2':
            if sounds.GLOBAL_SOUND:
                sounds.CHIP_DROPPED()
    return x

def get_MOUSEPOS():
    mouse_pos = pg.mouse.get_pos()
    return mouse_pos

def get_MOUSECLICK():
    mouse_click = pg.mouse.get_pressed()
    return mouse_click

def get_POSITIONCOL(posx=0):
    return posx

def identify_Playground():
    print(image.BOARDRECT.bottom)

def HIDE_CURSOR(mode=False):
    pg.mouse.set_visible(mode)

class Ticker():
    def __init__(self,sec):
        self.SECONDS = int(sec*1000)
        self.current_num = 0
        self.tick = pg.time.get_ticks()

    def delay(self):
        if self.tick + self.SECONDS < pg.time.get_ticks():
            self.tick = pg.time.get_ticks()
            self.current_num +=1
            self.current_num %= 3
            return int(self.current_num)

HIDE_CURSOR(False)

class fade_out_screen():
    def __init__(self):
        self.BLACK = (0,0,0)
        self.black_surface = pg.Surface(game_window.MAIN_WINDOW.get_size())
        self.black_surface_rect = self.black_surface.get_rect()
        self.black_surface_rect.center = (int(window_scale[0]/2), int(window_scale[1]/2))

    def start_fade_out(self,do_next='',speed=3):
        if sounds.GLOBAL_SOUND:
            sounds.FADE_WOOSH()
        self.black_surface.fill(self.BLACK)
        for alpha in range(0,60,speed):
            self.black_surface.set_alpha(alpha)
            game_window.MAIN_WINDOW.blit(self.black_surface,self.black_surface_rect)
            UPDATE()
            pg.time.delay(10)
        if do_next == 'QUIT':
            pg.quit()
            sys.exit()
        elif do_next == '':
            pass

def MOUSE_inside(x=(),y=()):
    x1 = x[0]
    x2 = x[1]
    y1 = y[0]
    y2 = y[1]
    mouse_pos = get_MOUSEPOS()
    if x1 < mouse_pos[0] < x2 and y1 < mouse_pos[1] < y2: return True
    else: return False

fade_out = fade_out_screen()

if __name__ == '__main__':
    pass

