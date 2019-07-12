import pygame
import sys
import traceback
from pygame.locals import *

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
    running = True
    clock = pygame.time.Clock()

    # here we check if it is ok to run the game
    while running:
        for event in pygame.event.get():

            # here we quit the game and exit the system
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(background,(0,0))

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
