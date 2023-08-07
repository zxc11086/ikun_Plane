import random

WIDTH = 1304
HEIGHT = 824
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# enemy update speed
ENEMY_NUM=random.randint(60,80)

#player move speed
PLAYER_SPEED=10

#player bullet speed
PLAYER_BULLET_SPEED=6

#enemy bullrt speed
ENEMY_BULLET_SPEED=random.randint(7,14)

#enemy move speed(x)
ENEMY_SPEED_X=random.randint(3,10)

#enemy move speed(y)
ENEMY_SPEED_Y=random.randint(5,12)

#big enemy shoot speed
BIG_ENEMY_BULLET_NUM = 50

#little enemy shoot speed
LITTLE_ENEMY_BULLET_NUM=50

#color egg shooted speed
COLOR_ENEMY_BULLET_NUM=50

#blood bag producted speed
BLOOD_BAG_NUM=random.randint(200,300)

#boom producted speed
BOMB_NUM=random.randint(500,600)

#blood bag move speed
BLOOD_BAG_SPEED=5

#player life
PLAYER_LIFE=10

#color egg producted speed
COLOR_EGG_NUM=10

#Skin's chosion
choose=0
