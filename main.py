import pygame
import sys
import traceback
import myplane
import enemy
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
 # here is the main program
def main():

    # here we creat myplane
    myplane1 = myplane.Myplane(size)

     # here we creat the enemy planes
    enemies = pygame.sprite.Group()

    enemy1 = pygame.sprite.Group()
    add_enemy1(enemy1, enemies, 15)

    enemy2 = pygame.sprite.Group()
    add_enemy2(enemy2, enemies, 7)

    enemy3 = pygame.sprite.Group()
    add_enemy3(enemy3, enemies, 3)
    
    # the index of plane when it is destoried
    e1_destory_index = 0
    e2_destory_index = 0
    e3_destory_index = 0
    myplane1_destory_index = 0
    
    running = True
    clock = pygame.time.Clock()

    # here we check if it is ok to run the game
    while running:
        for event in pygame.event.get():

            # here we quit the game and exit the system
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

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

        screen.blit(background,(0,0))


        # here we check that if the user's plane is touched by the enemies
        enemies_down = pygame.sprite.spritecollide(myplane1, enemies, False)
        if enemies_down:
            myplane1.active = False
            for e in enemies_down:
                e.active = False

        # here we draw the user's plane
        if myplane1.active:
            screen.blit(myplane1.image, myplane1.rect)
        else:
            if not(delay % 3):
                # here we draw the destory pictures of the plane
                screen.blit(each.destory_images[mhyplane1_destory_index], each.rect)
                myplane1_destory_index = (myplane1_destory_index + 1) % 4
                if myplane1_destory_index == 0:
                    print("game over")
                    running = False

        # here we draw the enemy planes
        for each in enemy3:
            # here we check the condition of the plane
            if each.active:
                each.move()
                screen.blit(each.image, each.rect)
            else:
                if not(delay % 3):
                    # here we draw the destory pictures of the plane
                    screen.blit(each.destory_images[e3_destory_index], each.rect)
                    e3_destory_index = (e3_destory_index + 1) % 4
                    if e3_destory_index == 0:
                        each.reset()

        for each in enemy2:
            if each.active:
                each.move()
                screen.blit(each.image, each.rect)
            else:
                if not(delay % 3):
                    # here we draw the destory pictures of the plane
                    screen.blit(each.destory_images[e2_destory_index], each.rect)
                    e2_destory_index = (e3_destory_index + 1) % 4
                    if e2_destory_index == 0:
                        each.reset()

        for each in enemy1:
            if each.active:
                each.move()
                screen.blit(each.image, each.rect)
            else:
                if not(delay % 3):
                    # here we draw the destory pictures of the plane
                    screen.blit(each.destory_images[e1_destory_index], each.rect)
                    e1_destory_index = (e1_destory_index + 1) % 4
                    if e1_destory_index == 0:
                        each.reset()

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
