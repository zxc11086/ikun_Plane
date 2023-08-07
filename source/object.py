import pygame.sprite

from image_resourse import *
from constant import *
import random


# Player Object
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey((WHITE))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def updates(self):
        if self.rect.y <= HEIGHT - 25:
            self.rect.y += PLAYER_SPEED

    def updatew(self):
        if self.rect.y >= 10:
            self.rect.y -= PLAYER_SPEED

    def updatea(self):
        if self.rect.x >= 10:
            self.rect.x -= PLAYER_SPEED

    def updated(self):
        if self.rect.x <= WIDTH - 25:
            self.rect.x += PLAYER_SPEED


class GreenPlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = greenskin
        self.image.set_colorkey((WHITE))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def updates(self):
        if self.rect.y <= HEIGHT - 25:
            self.rect.y += PLAYER_SPEED

    def updatew(self):
        if self.rect.y >= 10:
            self.rect.y -= PLAYER_SPEED

    def updatea(self):
        if self.rect.x >= 10:
            self.rect.x -= PLAYER_SPEED

    def updated(self):
        if self.rect.x <= WIDTH - 25:
            self.rect.x += PLAYER_SPEED


class BluePlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = blueskin
        self.image.set_colorkey((WHITE))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def updates(self):
        if self.rect.y <= HEIGHT - 25:
            self.rect.y += PLAYER_SPEED

    def updatew(self):
        if self.rect.y >= 10:
            self.rect.y -= PLAYER_SPEED

    def updatea(self):
        if self.rect.x >= 10:
            self.rect.x -= PLAYER_SPEED

    def updated(self):
        if self.rect.x <= WIDTH - 25:
            self.rect.x += PLAYER_SPEED


class PurplePlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = purpleskin
        self.image.set_colorkey((WHITE))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def updates(self):
        if self.rect.y <= HEIGHT - 25:
            self.rect.y += PLAYER_SPEED

    def updatew(self):
        if self.rect.y >= 10:
            self.rect.y -= PLAYER_SPEED

    def updatea(self):
        if self.rect.x >= 10:
            self.rect.x -= PLAYER_SPEED

    def updated(self):
        if self.rect.x <= WIDTH - 25:
            self.rect.x += PLAYER_SPEED


# Create a player sprite group for the following reference
players = pygame.sprite.Group()


# player bullets
class player_Bullet(pygame.sprite.Sprite):
    def __init__(self):
        # global player
        for people in players:
            player = people
        pygame.sprite.Sprite.__init__(self)
        self.image = player_bullet_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (player.rect.x + 35, player.rect.y)

    def update(self):
        self.rect.y -= PLAYER_BULLET_SPEED
        if self.rect.y <= 0:
            self.kill()


# player unique bullets
class player_unique_Bullet(pygame.sprite.Sprite):
    def __init__(self):
        for people in players:
            player = people
        pygame.sprite.Sprite.__init__(self)
        self.image = player_unique_bullet_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (player.rect.x + 35, player.rect.y)

    def update(self):
        self.rect.y -= PLAYER_BULLET_SPEED
        if self.rect.y <= 0:
            self.kill()


# Big_Ememy
class Big_Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = big_enemy_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()  # get the location
        self.rect.center = (random.randint(0, WIDTH), 20)
        self.life = 10

    def update(self):
        for people in players:
            player = people
        # fly dowm
        if (HEIGHT - self.rect.y > 0):
            num = random.randint(1, 100)
            if num < 20:
                self.rect.y += ENEMY_SPEED_Y

        # fly to the player
        if (self.rect.x > player.rect.x):#On player's right
            if self.rect.x >= 0:
                num = random.randint(1, 100)
                if num < 20:
                    self.rect.x -= ENEMY_SPEED_X
        else:
            if self.rect.x <= WIDTH:  #On player's left
                num = random.randint(1, 100)
                if num < 20:
                    self.rect.x += ENEMY_SPEED_X
        if self.rect.y >= 760:#Out of the window
            self.kill()


# create the small plane
class Little_Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = little_enemy_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), 20)
        self.life = 5

    def update(self):
        for people in players:
            player = people
        # y
        if (HEIGHT - self.rect.y > 0):
            num = random.randint(1, 100)
            if num < 20:
                self.rect.y += ENEMY_SPEED_Y

        # x
        if (self.rect.x > player.rect.x):
            if self.rect.x >= 0:
                num = random.randint(1, 100)
                if num < 20:
                    self.rect.x -= ENEMY_SPEED_X
        else:
            if self.rect.x <= WIDTH:
                num = random.randint(1, 100)
                if num < 20:
                    self.rect.x += ENEMY_SPEED_X
        if self.rect.y >= 780:
            self.kill()


# the bullet of Big ememy
class Big_Enemy_Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = big_enemy_bullet_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position

    def update(self):
        self.rect.y += ENEMY_BULLET_SPEED
        if self.rect.y >= 800:
            self.kill()


# the bullet of Little ememy
class LittleEnemy_Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = little_enemy_bullet_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position

    def update(self):
        self.rect.y += ENEMY_BULLET_SPEED
        if self.rect.y >= 800:
            self.kill()


# coloregg
class ColorEgg_Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = coloregg_bullet_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position

    def update(self):
        self.rect.y += ENEMY_BULLET_SPEED


# bloodbag
class BloodBag(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bloodbag_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(10, WIDTH)
        self.time = 0
        self.position = random.randint(150, HEIGHT) #final positon

    def update(self):
        if self.rect.y >= self.position:
            self.time += 1
            if self.time == 200:
                self.kill()
        if self.rect.y <= self.position:
            self.rect.y += BLOOD_BAG_SPEED


# bomb
class Bomb_Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bomb_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left = random.randint(10, WIDTH)
        self.time = 0
        self.position = random.randint(150, HEIGHT / 2)

    def update(self):
        if self.rect.y >= self.position:
            self.time += 1
            if self.time == 100:
                self.kill()
        if self.rect.y <= self.position:
            self.rect.y += BLOOD_BAG_SPEED


# Creat the Elven Grunp
player_bullets = pygame.sprite.Group()
player_unique_bullet = pygame.sprite.Group()
big_enemies = pygame.sprite.Group()
little_enemies = pygame.sprite.Group()
big_enemy_bullets = pygame.sprite.Group()
little_enemy_bullets = pygame.sprite.Group()
coloregg_bullets = pygame.sprite.Group()
bomb_bullets = pygame.sprite.Group()
blood_bags = pygame.sprite.Group()
