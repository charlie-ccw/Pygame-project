import pygame
import math
import sys
import traceback
import myplane
import enemy
import bullet
import supply
import background
from pygame.locals import *
from random import *

pygame.init()
pygame.mixer.init()

 # set the background size of the game
size = width,height = 700, 960
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Charlie's bullet hell")

# set the basic color of the game
BLACK = [0, 0, 0]
GREEN = [0, 255, 0]
RED = [255, 0, 0]

# here we difine the group of enemy
def add_enemy1(group1,group2,num):
    for i in range(num):
        e1 = enemy.Enemy1(size)
        group1.add(e1)
        group2.add(e1)


def add_enemy4(group1,group2,num):
    for i in range(num):
        e4 = enemy.Enemy4(size)
        group1.add(e4)
        group2.add(e4)


def add_enemy5(group1,group2,num):
    for i in range(num):
        e5 = enemy.Enemy5(size)
        group1.add(e5)
        group2.add(e5)

def add_enemy6(group1,group2,num):
    for i in range(num):
        e6 = enemy.Enemy6(size)
        group1.add(e6)
        group2.add(e6)

def add_enemy7(group1,group2,num):
    for i in range(num):
        e7 = enemy.Enemy7(size)
        group1.add(e7)
        group2.add(e7)

# here we difine the change of speed
def inc_speed(target, inc):
    for each in target:
        each.speed += inc
        
 # here is the main program
def main():

    # here we creat background
    background1 = background.Background(size)
    background2 = background.background(size)
    
    # here we creat myplane
    myplane1 = myplane.Myplane(size)
   
     # here we creat the enemy planes
    enemies = pygame.sprite.Group()
    enemy3 = pygame.sprite.Group()
    enemy2 = pygame.sprite.Group()
    e21 = enemy.Enemy2(size)
    e22 = enemy.Enemy2(size)
    e23 = enemy.Enemy2(size)
    e24 = enemy.Enemy2(size)
    e25 = enemy.Enemy2(size)
    enemy2.add(e21)
    enemy2.add(e22)
    enemy2.add(e23)
    enemy2.add(e24)
    enemy2.add(e25)
    
    e3 = enemy.Enemy3(size)
    enemy3.add(e3)

    enemy1 = pygame.sprite.Group()
    add_enemy1(enemy1, enemies, 5)

    enemy4 = pygame.sprite.Group()
    add_enemy4(enemy4, enemies, 2)

    enemy5 = pygame.sprite.Group()
    add_enemy5(enemy5, enemies, 1)

    enemy6 = pygame.sprite.Group()
    add_enemy6(enemy6, enemies, 1)

    enemy7 = pygame.sprite.Group()
    add_enemy7(enemy7, enemies, 1)
    
    # here we creat the bullets
    bullet1 = []
    bullet1_index = 0
    bullet1_number = 16
    for i in range(bullet1_number//2):
        bullet1.append(bullet.Bullet1((myplane1.rect.centerx-13, myplane1.rect.centery)))
        bullet1.append(bullet.Bullet1((myplane1.rect.centerx+13, myplane1.rect.centery)))

    # here we creat the super bullet
    bullet2 = []
    bullet2_index = 0
    bullet2_number = 26
    for i in range(bullet2_number//2):
        bullet2.append(bullet.Bullet2((myplane1.rect.centerx - 13, myplane1.rect.centery)))
        bullet2.append(bullet.Bullet2((myplane1.rect.centerx + 13, myplane1.rect.centery)))
        
    # here we creat the super bullet
    bullet3 = []
    bullet3_index = 0
    bullet3_number = 13
    for i in range(bullet3_number):
        bullet3.append(bullet.Bullet3((myplane1.rect.centerx - 23, myplane1.rect.centery)))
                
    # here we creat the super bullet
    bullet4 = []
    bullet4_index = 0
    bullet4_number = 13
    for i in range(bullet4_number):
        bullet4.append(bullet.Bullet4((myplane1.rect.centerx + 23, myplane1.rect.centery)))

    # here we creat the enemy bullet
    bullet5 = bullet.Bullet5(size)
    b5 = pygame.sprite.Group()
    b5.add(bullet5)

    bullet51 = bullet.Bullet6(size)
    b51 = pygame.sprite.Group()
    b51.add(bullet51)

    bullet52 = bullet.Bullet6(size)
    b52 = pygame.sprite.Group()
    b52.add(bullet52)

    bullet53 = bullet.Bullet6(size)
    b53 = pygame.sprite.Group()
    b53.add(bullet53)

    bullet54 = bullet.Bullet6(size)
    b54 = pygame.sprite.Group()
    b54.add(bullet54)

    bullet55 = bullet.Bullet6(size)
    b55 = pygame.sprite.Group()
    b55.add(bullet55)

    # the index of plane when it is destoried
    e1_destroy_index = 0
    e2_destroy_index = 0
    en3_destroy_index = 0
    e4_destroy_index = 0
    e5_destroy_index = 0
    e6_destroy_index = 0
    e7_destroy_index = 0
    myplane1_destroy_index = 0

    # here we add the score to the game
    score = 0
    score_font = pygame.font.Font("font/font.ttf.ttf", 36)

    #here we set the stop condtion to the game
    paused = False
    pause_nor_image = pygame.image.load("images/22.png").convert_alpha()
    pause_pressed_image = pygame.image.load("images/23.png").convert_alpha()
    resume_nor_image = pygame.image.load("images/21.png").convert_alpha()
    resume_pressed_image = pygame.image.load("images/24.png").convert_alpha()
    paused_rect = pause_nor_image.get_rect()
    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
    paused_image = pause_nor_image

    # here we set the difficulty of the game
    level = 1

    # here we set the bomb skills
    bomb_image = pygame.image.load("images/25.png").convert_alpha()
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("font/font.ttf.ttf", 48)
    bomb_num = 3

    # here we set record time
    recorded = False
    
    # here we set the ending picture
    gameover_font = pygame.font.Font("font/font.ttf.ttf", 48)
    again_image = pygame.image.load("images/29.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("images/30.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()
    
    # here we set the supply
    bullet_supply = supply.Bullet_supply(size)
    bomb_supply = supply.Bomb_supply(size)
    supply_time = USEREVENT
    pygame.time.set_timer(supply_time, 15 * 1000)

    # here we set the timing of super bullet
    super_bullet_time = USEREVENT + 1

    # here we add the timing of myplane's invincibe
    invincible_time = USEREVENT + 2

    # here we set condition of the super bullet
    is_super_bullet = False

    # here we set the lives of my planes
    life_image =  pygame.image.load("images/28.png").convert_alpha()
    life_rect = life_image.get_rect()
    life_num = 3
    
    # here we set the delay to make the picture change smoothly
    delay = 100

    # here we set the state of running to check if we need to end the game
    running = True

    clock = pygame.time.Clock()

    # here we start the game
    while running:
        for event in pygame.event.get():

            # here we quit the game and exit the system
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused
                    if paused:
                        pygame.time.set_timer(supply_time, 0)
                    else:
                        pygame.time.set_timer(supply_time, 15*1000)
                        
            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image = resume_pressed_image
                    else:
                        paused_image = pause_pressed_image
                else:
                    if paused:
                        paused_image = resume_nor_image
                    else:
                        paused_image = pause_nor_image

        # here we set the function of the bomb
            elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        if bomb_num:
                            bomb_num -= 1
                            for each in enemies:
                                if each.rect.bottom > 0:
                                    each.active = False

        # here we set the supply type
            elif event.type == supply_time:
                if choice([True, False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()

            elif event.type == super_bullet_time:
                is_super_bullet = False
                pygame.time.set_timer(super_bullet_time, 0)

            elif event.type == invincible_time:
                myplane1.invincible = False
                pygame.time.set_timer(invincible_time, 0)
                            
        # here we change the levels
        if level == 1 and score > 1000:
            level = 2

            # add more enemy planes to increase the difficulty level
            add_enemy1(enemy1, enemies, 1)
            add_enemy4(enemy4, enemies, 1)
            
            # increase the speed of the small enemy plane
            inc_speed(enemy1, 1)

        elif level == 2 and score > 3000:
            level = 3

            # add more enemy planes to increase the difficulty level
            add_enemy1(enemy1, enemies, 2)
            add_enemy4(enemy4, enemies, 1)
            
            # increase the speed of the small enemy plane
            inc_speed(enemy1, 1)
            inc_speed(enemy5, 1)
            inc_speed(enemy6, 1)

        elif level == 3 and score > 8000:
            level = 4

            # add more enemy planes to increase the difficulty level
            add_enemy1(enemy1, enemies, 1)
            add_enemy5(enemy5, enemies, 1)
            add_enemy6(enemy6, enemies, 1)
            
            # increase the speed of the small enemy plane


        elif level == 4 and score > 15000:
            level = 5

            # add more enemy planes to increase the difficulty level
            add_enemy1(enemy1, enemies, 2)
            add_enemy4(enemy4, enemies, 1)
            add_enemy7(enemy7, enemies, 1)
            
            # increase the speed of the small enemy plane
            inc_speed(enemy4, 1)

        elif level == 5 and score > 25000:
            level = 6

            # add more enemy planes to increase the difficulty level
            add_enemy1(enemy1, enemies, 3)
            add_enemy4(enemy4, enemies, 1)
            add_enemy5(enemy5, enemies, 1)
            add_enemy6(enemy6, enemies, 1)
            add_enemy7(enemy7, enemies, 1)
            
            # increase the speed of the small enemy plane
            inc_speed(enemy1, 1)

        
        # here we draw the background picture
        if background1.active:
            background1.move()
            screen.blit(background1.image, background1.rect)

        if background2.active:
            background2.move()
            screen.blit(background2.image, background2.rect)

        if life_num and not paused:
            # here we check the keyboard of user
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w]:
                myplane1.moveUp()
            if key_pressed[K_s]:
                myplane1.moveDown()
            if key_pressed[K_a]:
                myplane1.moveLeft()
            if key_pressed[K_d]:
                myplane1.moveRight()
                        
            # here we draw the bomb and indicate if the player get it
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image, bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply, myplane1):
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False

            # here we draw the bullet supply and indicate if the player get it
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, myplane1):
                    # creat and shoot the super bullet
                    is_super_bullet = True
                    pygame.time.set_timer(super_bullet_time, 8 * 1000)
                    bullet_supply.active = False
                    
            # here we check that if the user's plane is touched by the enemies and their bullets
            enemies_down = pygame.sprite.spritecollide(myplane1, enemies, False, pygame.sprite.collide_mask)
            enemy3_down = pygame.sprite.spritecollide(myplane1, enemy3, False, pygame.sprite.collide_mask)
            enemy2_down = pygame.sprite.spritecollide(myplane1, enemy2, False, pygame.sprite.collide_mask)
            b5_down = pygame.sprite.spritecollide(myplane1, b5, False, pygame.sprite.collide_mask)
            b51_down = pygame.sprite.spritecollide(myplane1, b51, False, pygame.sprite.collide_mask)
            b52_down = pygame.sprite.spritecollide(myplane1, b52, False, pygame.sprite.collide_mask)
            b53_down = pygame.sprite.spritecollide(myplane1, b53, False, pygame.sprite.collide_mask)
            b54_down = pygame.sprite.spritecollide(myplane1, b54, False, pygame.sprite.collide_mask)
            b55_down = pygame.sprite.spritecollide(myplane1, b55, False, pygame.sprite.collide_mask)
            if enemies_down and not myplane1.invincible:
                myplane1.active = False
                for e in enemies_down:
                    e.active = False
            if enemy3_down and not myplane1.invincible:
                myplane1.active = False
                e3.active = False
            if enemy2_down and not myplane1.invincible:
                myplane1.active = False
                for m in enemy2_down:
                    m.active = False
            if b5_down and not myplane1.invincible:
                myplane1.active = False
                bullet5.active = False
                bullet5.reset((e3.rect.centerx , e3.rect.bottom))
            if b51_down and not myplane1.invincible:
                myplane1.active = False
                bullet51.active = False
                bullet51.reset((e21.rect.centerx , e21.rect.bottom))
            if b52_down and not myplane1.invincible:
                myplane1.active = False
                bullet52.active = False
                bullet52.reset((e22.rect.centerx , e22.rect.bottom))
            if b53_down and not myplane1.invincible:
                myplane1.active = False
                bullet53.active = False
                bullet53.reset((e23.rect.centerx , e23.rect.bottom))
            if b54_down and not myplane1.invincible:
                myplane1.active = False
                bullet54.active = False
                bullet54.reset((e24.rect.centerx , e24.rect.bottom))
            if b55_down and not myplane1.invincible:
                myplane1.active = False
                bullet55.active = False
                bullet55.reset((e25.rect.centerx , e25.rect.bottom))

            # here we draw the user's plane
            if myplane1.active:
                screen.blit(myplane1.image, myplane1.rect)
            else:
                if not(delay % 3):
                    # here we draw the destory pictures of the plane
                    screen.blit(myplane1.destroy_images[myplane1_destroy_index], myplane1.rect)
                    myplane1_destroy_index = (myplane1_destroy_index + 1) % 4
                    if myplane1_destroy_index == 0:
                        life_num -= 1
                        myplane1.reset()
                        pygame.time.set_timer(invincible_time, 3 * 1000)

            # here we draw the enemy bullet
            if bullet5.active:
                screen.blit(bullet5.image, bullet5.rect)
                bullet5.move()
                if bullet5.rect.centerx > myplane1.rect.centerx and bullet5.rect.top < myplane1.rect.top:
                    bullet5.rect.left -= 4
                if bullet5.rect.centerx < myplane1.rect.centerx and bullet5.rect.top < myplane1.rect.top:
                    bullet5.rect.left += 4
            else:
                if e3.rect.top > 0 and e3.rect.top <800:
                    bullet5.reset((e3.rect.centerx , e3.rect.bottom))

            if bullet51.active:
                screen.blit(bullet51.image, bullet51.rect)
                bullet51.move()
            else:
                if e21.rect.top > 0 and e21.rect.top <800:
                    bullet51.reset((e21.rect.centerx , e21.rect.bottom))

            if bullet52.active:
                screen.blit(bullet52.image, bullet52.rect)
                bullet52.move()
            else:
                if e22.rect.top > 0 and e22.rect.top <800:
                    bullet52.reset((e22.rect.centerx , e22.rect.bottom))

            if bullet53.active:
                screen.blit(bullet53.image, bullet53.rect)
                bullet53.move()
            else:
                if e23.rect.top > 0 and e23.rect.top <800:
                    bullet53.reset((e23.rect.centerx , e23.rect.bottom))

            if bullet54.active:
                screen.blit(bullet54.image, bullet54.rect)
                bullet54.move()
            else:
                if e24.rect.top > 0 and e24.rect.top <800:
                    bullet54.reset((e24.rect.centerx , e24.rect.bottom))

            if bullet55.active:
                screen.blit(bullet55.image, bullet55.rect)
                bullet55.move()
            else:
                if e25.rect.top > 0 and e25.rect.top <800:
                    bullet55.reset((e25.rect.centerx , e25.rect.bottom))

            
            # here we shot the bullets
            if not(delay % 10):
                if is_super_bullet:
                    bullets = bullet2
                    bullets[bullet2_index].reset((myplane1.rect.centerx - 13, myplane1.rect.centery))
                    bullets[bullet2_index+1].reset((myplane1.rect.centerx + 13, myplane1.rect.centery))
                    bullet3[bullet3_index].reset((myplane1.rect.centerx + 23, myplane1.rect.centery))
                    bullet4[bullet4_index].reset((myplane1.rect.centerx - 23, myplane1.rect.centery))
                    bullet2_index = (bullet2_index + 2) % bullet2_number
                    bullet3_index = (bullet3_index + 1) % bullet3_number
                    bullet4_index = (bullet4_index + 1) % bullet4_number
                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset((myplane1.rect.centerx - 13, myplane1.rect.centery))
                    bullets[bullet1_index+1].reset((myplane1.rect.centerx + 13, myplane1.rect.centery))
                    bullet1_index = (bullet1_index + 2) % bullet1_number

            # here we check if the bullet collides with the enemy plane
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    enemy3_hit = pygame.sprite.spritecollide(b, enemy3, False, pygame.sprite.collide_mask)
                    enemy2_hit = pygame.sprite.spritecollide(b, enemy2, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            # here we check which type of planes is attacked
                            if e in enemy2:
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False
                    if enemy3_hit:
                        b.active = False
                        # here we check which type of planes is attacked
                        e3.energy -= 1
                        if e3.energy == 0:
                            e3.active = False
                    if enemy2_hit:
                        b.active = False
                        for z in enemy2_hit:
                            z.energy -= 1
                            if z.energy == 0:
                                z.active = False

            for x in bullet3:
                if x.active:
                    x.move1()
                    x.move()
                    screen.blit(x.image, x.rect)
                    enemy_hit = pygame.sprite.spritecollide(x, enemies, False, pygame.sprite.collide_mask)
                    enemy3_hit = pygame.sprite.spritecollide(b, enemy3, False, pygame.sprite.collide_mask)
                    enemy2_hit = pygame.sprite.spritecollide(b, enemy2, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            # here we check which type of planes is attacked
                            if e in enemy2:
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False
                    if enemy3_hit:
                        b.active = False
                        # here we check which type of planes is attacked
                        e3.energy -= 1
                        if e3.energy == 0:
                            e3.active = False
                    if enemy2_hit:
                        b.active = False
                        for z in enemy2_hit:
                            z.energy -= 1
                            if z.energy == 0:
                                z.active = False

            for y in bullet4:
                if y.active:
                    y.move1()
                    y.move()
                    screen.blit(y.image, y.rect)
                    enemy_hit = pygame.sprite.spritecollide(y, enemies, False, pygame.sprite.collide_mask)
                    enemy3_hit = pygame.sprite.spritecollide(b, enemy3, False, pygame.sprite.collide_mask)
                    enemy2_hit = pygame.sprite.spritecollide(b, enemy2, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            # here we check which type of planes is attacked
                            if e in enemy2:
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False
                    if enemy3_hit:
                        b.active = False
                        # here we check which type of planes is attacked
                        e3.energy -= 1
                        if e3.energy == 0:
                            e3.active = False
                    if enemy2_hit:
                        b.active = False
                        for z in enemy2_hit:
                            z.energy -= 1
                            if z.energy == 0:
                                z.active = False
                
            # here we check the condition of the enemy3
            if e3.active:
                e3.move()
                screen.blit(e3.image, e3.rect)
                # here we draw the total blood of the enemy plane
                pygame.draw.line(screen, BLACK, \
                                 (e3.rect.left, e3.rect.top - 5),\
                                 (e3.rect.right, e3.rect.top - 5),\
                                 2)
                # when the energy is bigger than 20%, it will be green. else, it will be red
                energy_remain = e3.energy / enemy.Enemy3.energy
                if energy_remain > 0.35:
                    energy_color = GREEN
                else:
                    energy_color = RED
                pygame.draw.line(screen, energy_color,\
                                 (e3.rect.left, e3.rect.top - 5),\
                                 (e3.rect.left + e3.rect.width * energy_remain,\
                                 e3.rect.top - 5), 2)
            else:
                if not(delay % 3):
                    # here we draw the destory pictures of the plane
                    screen.blit(e3.destroy_images[en3_destroy_index], e3.rect)
                    en3_destroy_index = (en3_destroy_index + 1) % 4
                    if en3_destroy_index == 0:
                        score += 1000
                        e3.reset()
            if e3.rect.top > 960:
                e3.reset()

            for each in enemy2:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                     # here we draw the total blood of the enemy plane
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5),\
                                     (each.rect.right, each.rect.top - 5),\
                                     2)
                    # when the energy is bigger than 20%, it will be green. else, it will be red
                    energy_remain = each.energy / enemy.Enemy2.energy
                    if energy_remain > 0.35:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen, energy_color,\
                                     (each.rect.left, each.rect.top - 5),\
                                     (each.rect.left + each.rect.width * energy_remain,\
                                     each.rect.top - 5), 2)
                else:
                    if not(delay % 3):
                        # here we draw the destory pictures of the plane
                        screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                        e2_destroy_index = (e2_destroy_index + 1) % 4
                        if e2_destroy_index == 0:
                            score += 500
                            each.reset()
                if each.rect.top > 960:
                    each.reset()

            for each in enemy1:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    if not(delay % 3):
                        # here we draw the destory pictures of the plane
                        screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 100
                            each.reset()

            for each in enemy4:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    if not(delay % 3):
                        # here we draw the destory pictures of the plane
                        screen.blit(each.destroy_images[e4_destroy_index], each.rect)
                        e4_destroy_index = (e4_destroy_index + 1) % 4
                        if e4_destroy_index == 0:
                            score += 100
                            each.reset()

            for each in enemy5:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    if not(delay % 3):
                        # here we draw the destory pictures of the plane
                        screen.blit(each.destroy_images[e5_destroy_index], each.rect)
                        e5_destroy_index = (e5_destroy_index + 1) % 4
                        if e5_destroy_index == 0:
                            score += 100
                            each.reset()

            for each in enemy6:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    if not(delay % 3):
                        # here we draw the destory pictures of the plane
                        screen.blit(each.destroy_images[e6_destroy_index], each.rect)
                        e6_destroy_index = (e6_destroy_index + 1) % 4
                        if e6_destroy_index == 0:
                            score += 100
                            each.reset()

            for each in enemy7:
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                else:
                    if not(delay % 3):
                        # here we draw the destory pictures of the plane
                        screen.blit(each.destroy_images[e7_destroy_index], each.rect)
                        e7_destroy_index = (e7_destroy_index + 1) % 4
                        if e7_destroy_index == 0:
                            score += 100
                            each.reset()
                            
            # here we draw the score
            score_text = score_font.render("Score : %s" % str(score), True, BLACK)
            screen.blit(score_text, (10,5))

        # here we creat the ending
        elif life_num == 0:
            # here we stop dropping the support
            pygame.time.set_timer(supply_time, 0)

            if not recorded:
                recorded = True
                # here we read the highest record
                with open("record.txt.txt", "r") as f:
                    record_score = int(f.read())

                # here we change the highest record
                if score > record_score:
                    with open("record.txt.txt", "w") as f:
                        f.write(str(score))

            # here we draw the ending picture
            record_score_text = score_font.render("Best was : %d" % record_score, True, BLACK)
            screen.blit(record_score_text, (50,50))

            gameover_text1 = gameover_font.render("Your Score", True, BLACK)
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = \
                                      (width - gameover_text1_rect.width) // 2, height // 2
            screen.blit(gameover_text1, gameover_text1_rect)

            gameover_text2 = gameover_font.render(str(score), True, BLACK)
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = \
                                      (width - gameover_text2_rect.width) // 2, \
                                      gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top = \
                             (width - again_rect.width) // 2, \
                             gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = \
                                (width - again_rect.width) // 2, \
                                again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)

            # here we set the mouse
            # if the player click left mouse
            if pygame.mouse.get_pressed()[0]:
                # here we get the coordination of the mouse
                pos = pygame.mouse.get_pos()
                # if the player click restart
                if again_rect.left < pos[0] < again_rect.right and \
                   again_rect.top < pos[1] < again_rect.bottom:
                    main()
                # if the player click exit
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                     gameover_rect.top < pos[1] < gameover_rect.bottom:
                    pygame.quit()
                    sys.exit()

        # here we draw the bomb
        bomb_text = bomb_font.render("x %d" % bomb_num, True, BLACK)
        text_rect = bomb_text.get_rect()
        screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
        screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))

        # here we draw the number of lives of myplane
        if life_num:
            for i in range(life_num):
                screen.blit(life_image, \
                            (width-(i+1)*life_rect.width+30, \
                             height-life_rect.height+35))

        # here we draw the pause and continue picture
        screen.blit(paused_image, paused_rect)

        # here we change the value of delay
        delay -= 1
        if not delay:
            delay = 100
        
        pygame.display.flip()
        
        clock.tick(60)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
