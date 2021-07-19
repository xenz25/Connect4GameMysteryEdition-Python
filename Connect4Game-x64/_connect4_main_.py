import pygame as pg
from pygame.locals import *
import sys

from connect_4_ingame import *
from connect_4_home import *
from connect_4_construction import *
from connect_4_credits import *
from connect_4_STEVEN import *
from connect_4_XENpy import *
from connect_4_LAURENT import *
from connect_4_ELBERT import *
from connect_4_exit_dialog import *
from _connect_4_LOGO import *
from connect_4_game_mode import *
from connect_4_options import *
from connect_4_options2 import *
from connect_4_how_to_play import *


first = HOME_SCENE()
under_construction = UNDER_CONSTRUCTION()
main_game = True

scenes.scene = 'LOGO' #---------------------- modify to tell who comes first
MODE = 'HIGH' #---------------------- modify to NORMAL, HIGH, LOW to change speed preference based on processor power
FPS.graphics_speed(MODE)
#------------------------------------ main game loop controls scene switching with the help of scene switcher module
while scenes.END:
    scene = scenes.get_SCENE()
    print(scene)
    if scene == 'LOGO':
        logo.start_logo_animation()
    elif scene == 'HOME':
        first.start_HOME()
    elif scene == 'INGAME':
        start_INGAME()
    elif scene == 'UNDER CONSTRUCTION':
        under_construction.start_UNDER_CONSTRUCTION()
    elif scene == 'CREDITS':
        credits.start_CREDITS()
    elif scene == 'STEVEN':
        steven.start_STEVEN()
    elif scene == 'XEN':
        xen.start_XEN()
    elif scene == 'LAURENT':
        laurent.start_LAURENT()
    elif scene == 'ELBERT':
        elbert.start_ELBERT()
    elif scene == 'EXIT DIALOG':
        exit_dialog.start_EXIT_DIALOG()
    elif scene == 'GAME MODE':
        game_mode.start_GAME_MODE()
    elif scene == 'OPTIONS1':
        options1.start_OPTIONS1()
    elif scene == 'OPTIONS2':
        options2.start_OPTIONS2()
    elif scene == 'HOW TO PLAY':
        how_to_play.start_HOW_TO_PLAY()
    else: pg.quit(); sys.exit()

#--------------- caution
pg.quit()
sys.exit()

