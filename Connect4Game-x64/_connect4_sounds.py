import pygame as pg
from pygame_functions import *
from pygame.locals import *
import sys, random

pg.init()
pg.mixer.init()



def loadMusic(path=''):
    x = pg.mixer.Sound(path)
    return x

class SOUNDS():
    def __init__(self):
        self.sounds_condition = 0
        self.DEFAULT_FADE_MS = 3000
        self.GLOBAL_SOUND = True
        self.music_counter = 0
        self.INTRO_S = loadMusic('sounds\INTRO2.wav')
        self.BUTTON_CLICK = loadMusic('sounds\B_CLICK.wav')
        self.INGAME_S = loadMusic('sounds\INGAME21.wav')
        self.INGAME_2 = loadMusic('sounds\INGAME2.wav')
        self.INGAME_3 = loadMusic('sounds\INGAME3.wav')
        self.CIRCUSMAN_E = loadMusic('sounds\C_E.wav')
        self.ELEPHANT_E1 = loadMusic('sounds\ELEPHANT_E.wav')
        self.MINUTE = loadMusic('sounds\MINUTE.wav')
        self.CHIP_DROP = loadMusic('sounds\CHIP_DROP.wav')
        self.WIN = loadMusic('sounds\WIN.wav')
        self.FADE_WOOSH1 = loadMusic('sounds\FADE_WOOSH.wav')
        self.OPENING = loadMusic('sounds\OPENING_SOUND.wav')
        self.INGAME_MYSTERY = loadMusic('sounds\INGAME_MAIN.wav')
        self.CREDITS_S = loadMusic('sounds\CREDITS.wav')
        self.MOVING_PANELS = loadMusic('sounds\MOVING PANELS2.wav')
        self.HOW_TO_PLAY = loadMusic('sounds\HOW_TO_PLAY.wav')

    def toggle_mute(self,scene):
        stops_at = pg.mixer.music.get_pos()
        if sounds.music_counter == 2:
            sounds.music_counter = 0
        if sounds.music_counter%2 == 0:
            self.sounds_condition = 1
            sounds.GLOBAL_SOUND = False
            sounds.fadeout_ALL()
            sounds.music_counter+=1
        elif sounds.music_counter%2 != 0:
            self.sounds_condition = 0
            sounds.stop_ALL()
            sounds.GLOBAL_SOUND = True
            if scene == 'HOME':
                self.OPENING_SOUND(start_at = stops_at)
            elif scene == 'INGAME':
                self.INGAME_SOUND(start_at = stops_at)
            elif scene == 'CREDITS':
                self.CREDITS_SOUND(start_at = stops_at)
            elif scene == 'LOGO':
                self.OPENING_SOUND(start_at = stops_at)
            sounds.music_counter+=1

    def get_sound_condition(self):
        return self.sounds_condition

    def play_next(self,music,times=0,fade=3000):
        if not pg.mixer.music.get_busy():
            music.play(times,fade_ms=fade)

    def stop_ALL(self):
        pg.mixer.stop()

    def pause_ALL(self):
        pg.mixer.pause()

    def unpause_ALL(self):
        pg.mixer.unpause()

    def fadeout_ALL(self):
        pg.mixer.fadeout(self.DEFAULT_FADE_MS)

    def INTRO(self):
        self.INTRO_S.play(-1,fade_ms = self.DEFAULT_FADE_MS)

    def OPENING_SOUND(self,start_at=0.0):
        self.OPENING.play(-1,int(start_at),fade_ms = self.DEFAULT_FADE_MS).set_volume(0)

    def CREDITS_SOUND(self,start_at=0.0):
        self.CREDITS_S.play(-1,int(start_at),fade_ms = self.DEFAULT_FADE_MS)

    def INGAME_SOUND(self,start_at=0.0):
        self.INGAME_MYSTERY.play(-1,int(start_at)).set_volume(0.5)

    def B_CLICK(self):
        self.BUTTON_CLICK.play()

    def INGAME(self):
        self.INGAME_S.play(0,fade_ms=self.DEFAULT_FADE_MS)
        self.INGAME_S.set_volume(0.5)

    def INGAME2(self):
        self.INGAME_2.set_volume(0.5)
        self.INGAME_2.play(0,fade_ms=self.DEFAULT_FADE_MS)


    def INGAME3(self,times=0):
        self.INGAME_3.set_volume(0.5)
        self.INGAME_3.play(times,fade_ms=self.DEFAULT_FADE_MS)

    def CIRCUS_E(self,times=0):
        self.CIRCUSMAN_E.play(times,fade_ms=self.DEFAULT_FADE_MS)

    def ELEPHANT_E(self,times=0):
        self.ELEPHANT_E1.play(times)

    def MINUTE_BEEP(self,times=0):
        self.MINUTE.play(times)

    def MINUTE_BEEP12(self,times=0):
        self.MINUTE.play(times)

    def CHIP_DROPPED(self,times=0):
        self.CHIP_DROP.play(times)

    def WIN_SOUND(self,times=0):
        self.WIN.play(times)

    def FADE_WOOSH(self,times=0):
        self.FADE_WOOSH1.set_volume(1)
        self.FADE_WOOSH1.play(times)

    def MOVING_PANEL_SOUND(self):
        self.MOVING_PANELS.set_volume(0.2)
        self.MOVING_PANELS.play()

    def HOW_TO_PLAY_SOUND(self,times=-1):
        self.HOW_TO_PLAY.play(times,fade_ms=self.DEFAULT_FADE_MS)


sounds = SOUNDS() #CLASS SOUNDS


if __name__ == '__main__':
    win = pg.display.set_mode((300,200))
    songs = SOUNDS()
    songINGAME = [songs.INGAME, songs.INGAME2, songs.INGAME3]



    def chooseAndPlay():
        x = random.choice(songINGAME)
        pg.mixer.music.set_endevent(pg.constants.USEREVENT)
        return x()


    chooseAndPlay()
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        if pg.mixer.music.get_endevent() == pg.constants.USEREVENT:
            print('YES')

        pg.display.update()


