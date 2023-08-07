# -*- coding:utf-8-*-
import pygame
#set background song
pygame.mixer.music.load('../resurce/sound/background_sound.mp3')
pygame.mixer.music.set_volume(0.6)
#pygame.mixer.music.play(-1,219)


#Set player hit sound effect
player_shooted_sound=pygame.mixer.Sound('../resurce/sound/player_shooted_sound.mp3')
player_shooted_sound.set_volume(0.5)


#Set the bullet shoot sound effect
player_shoot_sound=pygame.mixer.Sound('../resurce/sound/player_shoot_sound.wav')
player_shoot_sound.set_volume(0.5)

#Set background effect
pre_background_sound=pygame.mixer.Sound('../resurce/sound/pre_background_music.mp3')
pre_background_sound.set_volume(0.5)

#Set trigger eggs sound
coloregg_amazing_sound=pygame.mixer.Sound('../resurce/sound/coloredgg_amazing.mp3')
coloregg_amazing_sound.set_volume(0.5)
coloregg_excellent_sound=pygame.mixer.Sound('../resurce/sound/coloredgg_excellent.mp3')
coloregg_excellent_sound.set_volume(0.5)
coloregg_great_sound=pygame.mixer.Sound('../resurce/sound/coloregg_great.mp3')
coloregg_great_sound.set_volume(0.5)
coloregg_unbelieveable_sound=pygame.mixer.Sound('../resurce/sound/coloredgg_unbelieveable.mp3')
coloregg_unbelieveable_sound.set_volume(0.5)