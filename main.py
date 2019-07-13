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
background = pygame.image.load("images/background.png.jpg").convert()



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
    add_enemy2(enemy2, enemies, 5)

    enemy3 = pygame.sprite.Group()
    add_enemy3(enemy3, enemies, 2)
    
    
    
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

        # here we draw the user's plane
        screen.blit(myplane1.image, myplane1.rect)

        # here we draw the enemy planes
        for each in enemy3:
            each.move()
            screen.blit(each.image, each.rect)

        for each in enemy2:
            each.move()
            screen.blit(each.image, each.rect)

        for each in enemy1:
            each.move()
            screen.blit(each.image, each.rect)

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
