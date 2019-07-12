import pygame
import sys
import traceback
import myplane
from pygame.locals import *
from random import *

pygame.init()
pygame.mixer.init()

 # set the background size of the game
size = width,height = 640, 960
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Charlie's bullet hell")

 # set the picture of the background
background = pygame.image.load("images/background.png.jpg").convert()

 # here is the main program
def main():

    # here we creat myplane
    myplane1 = myplane.Myplane(size)
    
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
