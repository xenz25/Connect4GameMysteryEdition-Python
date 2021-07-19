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

pg.init()
built_in_screen = game_window.MAIN_WINDOW
image = pg.image.load('BOX_GREEN.png')
built_in_clock = pg.time.Clock()


class MOVE_IP():
    def __init__(self,screen,image,current_pos =(0,0)):
        self.image = image
        self.image_rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.touched = False
        self.current_pos = current_pos

    def move_ip_event_handler_old(self):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                import sys; sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if self.image_rect.collidepoint(event.pos):
                    self.touched = True
                    pg.mouse.get_rel()
            elif event.type == MOUSEBUTTONUP:
                self.touched = False

    def move_ip_event_handler(self):
        if self.image_rect.collidepoint(event.pos):
            self.touched = True
            pg.mouse.get_rel()

    def move_ip_false_touched(self):
        self.touched = False


    def start_move_ip_animation(self):
        self.screen.blit(self.image,(self.current_pos))

        if self.touched:
            self.image_rect.move_ip(pg.mouse.get_rel())
            self.image_rect.clamp_ip(self.screen_rect)
            self.current_pos = self.image_rect.topleft
            self.screen.blit(self.image,self.image_rect)

built_in_move_in_place = MOVE_IP(built_in_screen,image)

def try_class():
    built_in_screen.fill ((0,0,255))
    built_in_move_in_place.start_move_ip_animation()
    built_in_move_in_place.move_ip_event_handler()
    pg.display.flip()
    built_in_clock.tick(60)



def main():
    FPS = 60

    clock = pg.time.Clock()

    screen = pg.display.set_mode((500,600))
    screen_rect = screen.get_rect()
    image = pg.image.load('BOX_GREEN.png')
    image_rect = image.get_rect()
    touched = False
    current_pos = (0,0)

    while 1:

        screen.fill ((0,0,255))

        screen.blit(image,(current_pos))

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                import sys;sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if image_rect.collidepoint(event.pos):
                    print(1)
                    touched = True
                    pg.mouse.get_rel()
            elif event.type == MOUSEBUTTONUP:
                print(2)
                touched = False

        if touched:
            image_rect.move_ip(pg.mouse.get_rel())
            image_rect.clamp_ip(screen_rect)
            current_pos = image_rect.topleft
            screen.blit(image,image_rect)

        pg.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    #main()
    while 1:
        try_class()






