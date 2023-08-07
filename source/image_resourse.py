# -*- coding:utf-8-*-
import  os
import pygame
from constant import *
pygame.display.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

#Init window
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d"%(1000,100)


#Innt the page
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ikun_will_win")
clock = pygame.time.Clock()
pygame.mixer.init()
myfont = pygame.font.Font(None,30)
textImage = myfont.render("pygame", True, WHITE)
font = pygame.font.SysFont('microsoft Yahei', 20)


#the images
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, '../resurce/img')
player_img = pygame.image.load(os.path.join(img_folder,'player1.png'))
background_img=  pygame.image.load(os.path.join(img_folder,'background.jpg'))
sea_background_img=  pygame.image.load(os.path.join(img_folder,'sea_background.png'))
forest_background_img=  pygame.image.load(os.path.join(img_folder,'forest_background.png'))
desert_background_img=  pygame.image.load(os.path.join(img_folder,'desert_background.png'))
player_bullet_img=pygame.image.load(os.path.join(img_folder,'player_bullet.png'))
player_unique_bullet_img=pygame.image.load(os.path.join(img_folder,'player_unique_bullet.png'))
big_enemy_bullet_img=pygame.image.load(os.path.join(img_folder, '大蛋.png'))
big_enemy_img = pygame.image.load(os.path.join(img_folder, 'chicken.png'))
little_enemy_img=pygame.image.load(os.path.join(img_folder, 'littlechicken.png'))
little_enemy_bullet_img=pygame.image.load(os.path.join(img_folder, '小蛋.png'))
greenskin=pygame.image.load(os.path.join(img_folder, '人物1.png'))
blueskin=pygame.image.load(os.path.join(img_folder, '人物3.png'))
purpleskin=pygame.image.load(os.path.join(img_folder, '人物5.png'))
startgreenskin=pygame.image.load(os.path.join(img_folder, '绿色皮肤.png'))
startblueskin=pygame.image.load(os.path.join(img_folder, '蓝色皮肤.png'))
startpurpleskin=pygame.image.load(os.path.join(img_folder, '紫色皮肤.png'))
originalskin=pygame.image.load(os.path.join(img_folder, 'startplayer1.png'))
gameover_img=pygame.image.load(os.path.join(img_folder, 'Game Over.png'))
restart_img=pygame.image.load(os.path.join(img_folder, 'Restart.png'))
coloregg_bullet_img=pygame.image.load(os.path.join(img_folder, 'coloregg.png'))
bloodbag_img=pygame.image.load(os.path.join(img_folder, 'heart.png'))
bomb_img=pygame.image.load(os.path.join(img_folder, 'bomb.png'))
