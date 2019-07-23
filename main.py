import pygame

import sys
import traceback
import myplane
import enemy
import bullet
import supply
from pygame.locals import *
from random import *

pygame.init()
pygame.mixer.init()

 # set the background size of the game
size = width,height = 700, 960
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Charlie's bullet hell")

 # set the picture of the background
background = pygame.image.load("images/background.jpg").convert()

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

def add_enemy2(group1,group2,num):
    for i in range(num):
        e2 = enemy.Enemy2(size)
        group1.add(e2)
        group2.add(e2)

def add_enemy3(group1,group2,num):
    for i in range(num):
        e3 = enemy.Enemy3(size)
        group1.add(e3)
        group2.add(e3)

# here we difine the change of speed
def inc_speed(target, inc):
    for each in target:
        each.speed += inc
        
 # here is the main program
def main():

    # here we creat myplane
    myplane1 = myplane.Myplane(size)
   

     # here we creat the enemy planes
    enemies = pygame.sprite.Group()

    enemy1 = pygame.sprite.Group()
    add_enemy1(enemy1, enemies, 20)

    enemy2 = pygame.sprite.Group()
    add_enemy2(enemy2, enemies, 8)

    enemy3 = pygame.sprite.Group()
    add_enemy3(enemy3, enemies, 3)


    # here we creat the bullets
    bullet1 = []
    bullet1_index = 0
    bullet1_number = 7
    for i in range(bullet1_number):
        bullet1.append(bullet.Bullet1(myplane1.rect.midtop))


    # here we creat the super bullet
    bullet2 = []
    bullet2_index = 0
    bullet2_number = 26
    for i in range(bullet2_number//2):
        bullet2.append(bullet.Bullet2((myplane1.rect.centerx - 23, myplane1.rect.centery)))
        bullet2.append(bullet.Bullet2((myplane1.rect.centerx + 23, myplane1.rect.centery)))

    
    # the index of plane when it is destoried
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
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


    # here we set the supply
    bullet_supply = supply.Bullet_supply(size)
    bomb_supply = supply.Bomb_supply(size)
    supply_time = USEREVENT
    pygame.time.set_timer(supply_time, 20 * 1000)


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


    # here we check if it is ok to run the game
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
                        pygame.time.set_timer(supply_time, 20*1000)
                        

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
            add_enemy1(enemy1, enemies, 3)
            add_enemy2(enemy2, enemies, 2)
            add_enemy3(enemy3, enemies, 1)
            

            # increase the speed of the small enemy plane
            inc_speed(enemy1, 1)



        elif level == 2 and score > 3000:
            level = 3

            # add more enemy planes to increase the difficulty level
            add_enemy1(enemy1, enemies, 5)
            add_enemy2(enemy2, enemies, 3)
            add_enemy3(enemy3, enemies, 2)
            

            # increase the speed of the small enemy plane
            inc_speed(enemy1, 1)



        elif level == 3 and score > 8000:
            level = 4

            # add more enemy planes to increase the difficulty level
            add_enemy1(enemy1, enemies, 5)
            add_enemy2(enemy2, enemies, 3)
            add_enemy3(enemy3, enemies, 2)
            

            # increase the speed of the small enemy plane
            inc_speed(enemy1, 1)
            inc_speed(enemy2, 1)


        elif level == 4 and score > 15000:
            level = 5

            # add more enemy planes to increase the difficulty level
            add_enemy1(enemy1, enemies, 5)
            add_enemy2(enemy2, enemies, 3)
            add_enemy3(enemy3, enemies, 2)
            

            # increase the speed of the small enemy plane
            inc_speed(enemy1, 1)
            inc_speed(enemy2, 1)
            inc_speed(enemy3, 1)


        elif level == 5 and score > 25000:
            level = 6

            # add more enemy planes to increase the difficulty level
            add_enemy1(enemy1, enemies, 5)
            add_enemy2(enemy2, enemies, 3)
            add_enemy3(enemy3, enemies, 2)
            

            # increase the speed of the small enemy plane
            inc_speed(enemy1, 1)
            inc_speed(enemy2, 1)
            inc_speed(enemy3, 1)


        screen.blit(background,(0,0))


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
            print(myplane1.rect.left)
            print(myplane1.rect.top)

            
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
                    pygame.time.set_timer(super_bullet_time, 12 * 1000)
                    bullet_supply.active = False
                    


            # here we check that if the user's plane is touched by the enemies
            enemies_down = pygame.sprite.spritecollide(myplane1, enemies, False, pygame.sprite.collide_mask)
            if enemies_down and not myplane1.invincible:
                myplane1.active = False
                for e in enemies_down:
                    e.active = False

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


            # here we shot the bullets
            if not(delay % 10):
                if is_super_bullet:
                    bullets = bullet2
                    bullets[bullet2_index].reset((myplane1.rect.centerx - 23, myplane1.rect.centery))
                    bullets[bullet2_index+1].reset((myplane1.rect.centerx + 23, myplane1.rect.centery))
                    bullet2_index = (bullet2_index + 2) % bullet2_number
                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset(myplane1.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % bullet1_number


            # here we check if the bullet collides with the enemy plane
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active = False
                        for e in enemy_hit:
                            # here we check which type of planes is attacked
                            if e in enemy2 or e in enemy3:
                                e.energy -= 1
                                if e.energy == 0:
                                    e.active = False
                            else:
                                e.active = False
                
                
            # here we draw the enemy planes
            for each in enemy3:
                # here we check the condition of the plane
                if each.active:
                    each.move()
                    screen.blit(each.image, each.rect)
                    # here we draw the total blood of the enemy plane
                    pygame.draw.line(screen, BLACK, \
                                     (each.rect.left, each.rect.top - 5),\
                                     (each.rect.right, each.rect.top - 5),\
                                     2)
                    # when the energy is bigger than 20%, it will be green. else, it will be red
                    energy_remain = each.energy / enemy.Enemy3.energy
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
                        screen.blit(each.destroy_images[e3_destroy_index], each.rect)
                        e3_destroy_index = (e3_destroy_index + 1) % 4
                        if e3_destroy_index == 0:
                            score += 1000
                            each.reset()


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


        # here we creat the ending
        elif life_num == 0:
            # here we stop dropping the support
            pygame.timer.set_timer(supply_time, 0)

            # here we read the highest record
            with open("record.txt", "r") as f:
                record_score = int(f.read())

            # here we change the highest record
            if score > record_score:
                with open("record.txt", "w") as f:
                    f.write(str(score))
        # here we draw the score
        score_text = score_font.render("Score : %s" % str(score), True, BLACK)
        screen.blit(score_text, (10,5))


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
