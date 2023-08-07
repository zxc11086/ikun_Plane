import sys
import time

import pygame

from object import *
from sound_resourse import *
from constant import *


# Functions with a paragraph of text
# The four quantities are text content, font size, font color, and placement position
def drawtext(text, fontsize, textcolor, position):
    myfont1 = pygame.font.SysFont('microsoft Yahei', fontsize)
    text1 = myfont1.render(text, True, textcolor)
    textrect = text1.get_rect()
    textrect.center = position
    screen.blit(text1, textrect)


# start game function
def startgame():
    # screen.blit(background_img, (0, 0))
    screen.fill(WHITE)
    drawtext("Flying Ikun Battle", 60, (0, 0, 0), (652, 212))
    drawtext("Choose one skin to start game", 30, (0, 0, 0), (652, 312))
    pygame.display.flip()
    isRuning = True
    global choose  # Global variable, select the skin to be selected through choose
    # Select the corresponding skin by selecting a picture to enter the game
    while isRuning:
        pre_background_sound.play()
        buttons = pygame.mouse.get_pressed()
        x1, y1 = pygame.mouse.get_pos()
        screen.blit(originalskin, (300, 500))
        screen.blit(startgreenskin, (500, 500))
        screen.blit(startblueskin, (700, 500))
        screen.blit(startpurpleskin, (900, 500))
        # The position represents the coordinate range of the image.
        # If it is selected, the value of choose will be changed, indicating that the skin is selected
        if x1 <= 450 and x1 >= 300 and y1 >= 500 and y1 <= 652:
            if buttons[0]:
                choose = 0
                isRuning = False
        elif x1 <= 650 and x1 >= 500 and y1 >= 500 and y1 <= 652:
            if buttons[0]:
                choose = 1
                isRuning = False
        elif x1 <= 850 and x1 >= 700 and y1 >= 500 and y1 <= 652:
            if buttons[0]:
                choose = 2
                isRuning = False
        elif x1 <= 1050 and x1 >= 900 and y1 >= 500 and y1 <= 652:
            if buttons[0]:
                choose = 3
                isRuning = False

        if isRuning == False:
            pre_background_sound.stop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


# main function
def main():
    #global unique
    #unique=0
    running = True
    # player's life
    player_life = PLAYER_LIFE

    #score
    score = 0

    # Some control quantities used to control enemy aircraft refresh, enemy aircraft bullet firing, and egg refresh
    temp_bigenemy_num = 0
    #temp_unique_bullet=0
    temp_littleenemy_num = 0
    temp_bigenemy_bullet_num = 0
    temp_littleenemy_bullet_num = 0
    temp_coloregg_bullet_num = 0
    temp_heartbag_bullet_num=0
    temp_bomb_bullet_num = 0
    startgame()
    #Select skin to add objects according to choose
    if choose == 0:
        player = Player()
        players.add(player)
    elif choose == 1:
        player = GreenPlayer()
        players.add(player)
    elif choose == 2:
        player = BluePlayer()
        players.add(player)
    else:
        player = PurplePlayer()
        players.add(player)
    # main loop
    pygame.mixer.music.play(-1, 219)
    while running:
        clock.tick(FPS)
        # set the plane
        # big enemies
        temp_bigenemy_num += 1  # 根据帧率来添加敌机的对象，到达一定值后添加对象
        if temp_bigenemy_num == ENEMY_NUM:
            enemy = Big_Enemy()
            big_enemies.add(enemy)
            temp_bigenemy_num = 0
        # little enemies
        temp_littleenemy_num += 1
        if temp_littleenemy_num == ENEMY_NUM:
            enemy = Little_Enemy()
            little_enemies.add(enemy)
            temp_littleenemy_num = 0
        #bloodbag
        temp_heartbag_bullet_num+=1
        if temp_heartbag_bullet_num==BLOOD_BAG_NUM:
            heartbag=BloodBag()
            blood_bags.add(heartbag)
            temp_heartbag_bullet_num=0
        #bomb
        temp_bomb_bullet_num+=1
        if temp_bomb_bullet_num==BOMB_NUM:
            bombbag=Bomb_Bullet()
            bomb_bullets.add(bombbag)
            temp_bomb_bullet_num=0
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                running = False

            # shoot the bullet
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_bullet = player_Bullet()
                    player_shoot_sound.play()
                    player_bullets.add(player_bullet)
        # player_move
        key_pressed = pygame.key.get_pressed()
        if (key_pressed[pygame.K_w]):
            player.updatew()
        if (key_pressed[pygame.K_a]):
            player.updatea()
        if (key_pressed[pygame.K_s]):
            player.updates()
        if (key_pressed[pygame.K_d]):
            player.updated()

        # update the bullets
        player_bullets.update()
        big_enemies.update()
        little_enemies.update()

        # control the num of the enmies.
        temp_bigenemy_bullet_num += 1
        temp_littleenemy_bullet_num += 1
        temp_coloregg_bullet_num += 1
        if temp_bigenemy_bullet_num >BIG_ENEMY_BULLET_NUM:
            temp_bigenemy_bullet_num = 0
        if temp_littleenemy_bullet_num >LITTLE_ENEMY_BULLET_NUM:
            temp_littleenemy_bullet_num = 0
        if temp_coloregg_bullet_num > COLOR_EGG_NUM:
            temp_coloregg_bullet_num = 0

        # big enemy shoot bullets
        for item in big_enemies:
            if temp_bigenemy_bullet_num == int(BIG_ENEMY_BULLET_NUM / 2):
                num = random.randint(1, 10)
                if num == 8:
                    enemy_bullet = Big_Enemy_Bullet(item.rect.midtop)
                    big_enemy_bullets.add(enemy_bullet)

        # big enemy shoot Easter eggs
        for item in big_enemies:
            if temp_coloregg_bullet_num == int(COLOR_EGG_NUM / 2):
                num = random.randint(1, 10)
                if num == 8:
                    coloregg_enemy_bullet = ColorEgg_Bullet(item.rect.midtop)
                    coloregg_bullets.add(coloregg_enemy_bullet)

        # little enemy shoot bullets
        for item in little_enemies:
            if temp_littleenemy_bullet_num == int(LITTLE_ENEMY_BULLET_NUM / 2):
                num = random.randint(1, 10)
                if num == 8:
                    enemy_bullet = LittleEnemy_Bullet(item.rect.midtop)
                    little_enemy_bullets.add(enemy_bullet)

        # Update bullet and egg sprite groups
        big_enemy_bullets.update()
        little_enemy_bullets.update()
        coloregg_bullets.update()
        blood_bags.update()
        bomb_bullets.update()
        # Collision judgment between player's bullet and enemy aircraft
        # the big enemy
        for player_bullet in player_bullets:
            for enemy in big_enemies:
                if (pygame.sprite.collide_mask(player_bullet, enemy)):
                    enemy.life -= 2
                    player_shoot_sound.play()
                    player_bullets.remove(player_bullet)
                    if (enemy.life <= 0):
                        big_enemies.remove(enemy)
                        score += 10
                        if score % 5 == 0 and score % 10 != 0:
                            coloregg_excellent_sound.play()
                        if score % 10 == 0:
                            coloregg_unbelieveable_sound.play()
        # the little enemy
        for player_bullet in player_bullets:
            for enemy in little_enemies:
                if (pygame.sprite.collide_mask(player_bullet, enemy)):
                    enemy.life -= 2
                    player_shoot_sound.play()
                    player_bullets.remove(player_bullet)
                    if (enemy.life <= 0):
                        little_enemies.remove(enemy)
                        score += 5
                        if score % 5 == 0 and score % 10 != 0:
                            coloregg_excellent_sound.play()
                        if score % 10 == 0:
                            coloregg_unbelieveable_sound.play()

        # Judgment of collision between enemy aircraft bullets and players
        # big enemy
        for enemy_bullet in big_enemy_bullets:
            if pygame.sprite.collide_mask(player, enemy_bullet):
                player_life -= 2
                big_enemy_bullets.remove(enemy_bullet)
                player_shooted_sound.play()
        # little enemy
        for enemy_bullet in little_enemy_bullets:
            if pygame.sprite.collide_mask(player, enemy_bullet):
                player_life -= 1
                little_enemy_bullets.remove(enemy_bullet)
                player_shooted_sound.play()
        # When the color_eggs collide, special bullets will be automatically fired when they encounter the color_eggs.
        # When the special bullets look down, all obstacles encountered will be eliminated
        for coloregg in coloregg_bullets:
            if pygame.sprite.collide_mask(player, coloregg):
                coloregg_bullets.remove(coloregg)
                unique_bullet=player_unique_Bullet()
                player_unique_bullet.add(unique_bullet)

        #blood collision to inrease the life of player
        for bloodbag in blood_bags:
            if pygame.sprite.collide_mask(player,bloodbag):
                player_life+=5
                blood_bags.remove(bloodbag)
                #player_shooted_sound.play()
        #bomb collision
        for bombbag in bomb_bullets:
            if pygame.sprite.collide_mask(player,bombbag):
                bomb_bullets.remove(bombbag)
                score+=50
                for enemy in big_enemies:
                    big_enemies.remove(enemy)
                for enemy in little_enemies:
                    little_enemies.remove(enemy)
                #player_shooted_sound.play()
                for bloodbag in blood_bags:
                    blood_bags.remove(bloodbag)
        #Special bullets collide with enemies:
        for bigplane in player_unique_bullet:
            for enemy in big_enemies:
                if pygame.sprite.collide_mask(enemy,bigplane):
                    big_enemies.remove(enemy)
                    score+=10
        for bigplane in player_unique_bullet:
            for enemy in little_enemies:
                if pygame.sprite.collide_mask(enemy,bigplane):
                    little_enemies.remove(enemy)
                    score+=5
        # The enemy plane collides with the player
        # big one
        for enemy in big_enemies:
            if pygame.sprite.collide_mask(enemy, player):
                player_life -= 2
                big_enemies.remove(enemy)
        # little one
        for enemy in little_enemies:
            if pygame.sprite.collide_mask(enemy, player):
                player_life -= 1
                little_enemies.remove(enemy)
        #update
        player_unique_bullet.update()
         #paint the window
        # paint background
        if 40 <= score%250 <= 60:
         screen.blit(background_img, (0, 0))
        elif 61 <= score%250 <= 120:
         screen.blit(sea_background_img,(0,0))
        elif 121 <= score%250 <= 180:
          screen.blit(desert_background_img,(0,0))
        elif 180 <= score%250 <= 250:
          screen.blit(forest_background_img,(0,0))
        else:
          screen.blit(background_img,(0,0))
        # paint the score
        score_text = font.render('Score:', True, (0, 0, 255))
        score_num = font.render(str(score), True, (255, 0, 0))
        window.blit(score_text, (0, 0))
        window.blit(score_num, (70, 0)) #the location of text
        # paint the blood
        player_life_text = font.render('LIFE :', True, (0, 0, 255))
        player_life_num = font.render(str(player_life), True, (255, 0, 0))
        window.blit(player_life_text, (WIDTH - 100, HEIGHT - 50))
        window.blit(player_life_num, (WIDTH - 50, HEIGHT - 50))
        # paint the elven Group
        players.draw(screen)
        player_bullets.draw(screen)
        big_enemies.draw(screen)
        little_enemies.draw(screen)
        big_enemy_bullets.draw(screen)
        little_enemy_bullets.draw(screen)
        coloregg_bullets.draw(screen)
        blood_bags.draw(screen)
        bomb_bullets.draw(screen)
        player_unique_bullet.draw(screen)
        # flip()
        pygame.display.flip()
        # if the player dies
        if player_life <= 0:
            myfont1 = pygame.font.SysFont('microsoft Yahei', 40)
            get_score_text = myfont1.render('Score : %s' % str(score), True, (255, 0, 0))
            screen.blit(get_score_text, (550, 400))
            screen.blit(gameover_img, (500, 600))
            screen.blit(restart_img, (500, 500))
            pygame.display.flip()
            endrunning = True
            # end sound
            pygame.mixer.music.stop()
            while endrunning:
                buttons = pygame.mouse.get_pressed()
                x1, y1 = pygame.mouse.get_pos()
                if x1 >= 500 and x1 <= 730 and y1 >= 500 and y1 <= 560:
                    if buttons[0]:
                        # Delete all wizard groups and start again
                        for i in players:
                            players.remove(i)
                        for i in big_enemies:
                            big_enemies.remove(i)
                        for i in little_enemies:
                            little_enemies.remove(i)
                        for i in player_bullets:
                            player_bullets.remove(i)
                        for i in big_enemy_bullets:
                            big_enemy_bullets.remove(i)
                        for i in little_enemy_bullets:
                            little_enemy_bullets.remove(i)
                        for i in blood_bags:
                            blood_bags.remove(i)
                        for i in coloregg_bullets:
                            coloregg_bullets.remove(i)
                        for i in bomb_bullets:
                            bomb_bullets.remove(i)
                        for i in player_unique_bullet:
                            player_unique_bullet.remove(i)
                        main()
                elif x1 >= 500 and x1 <= 730 and y1 >= 600 and y1 <= 660:
                    if buttons[0]:
                        pygame.quit()
                        sys.exit()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()


if __name__ == '__main__':
    main()
