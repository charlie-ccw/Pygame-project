import pygame
from random import *

 # here we difine the smallest enemy plane
class Enemy1(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy1.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 4
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-5,0)


     # here we difine the movemont of the enemy
    def move(self):
        if self.rect.top < self.height:
            self.rect.top +=self.speed
        else:
            self.reset()

     # here we define how the enemy reset in the game
    def reset(self):
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-5,0)
        





 # here we difine the middle size enemy plane
class Enemy2(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy2.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 2
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-10,-self.height)


     # here we difine the movemont of the enemy
    def move(self):
        if self.rect.top < self.height:
            self.rect.top +=self.speed
        else:
            self.reset()

     # here we define how the enemy reset in the game
    def reset(self):
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-10,0)





 # here we difine the biggest size enemy plane
class Enemy3(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy3.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 1
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-12,-self.height*2)


     # here we difine the movemont of the enemy
    def move(self):
        if self.rect.top < self.height:
            self.rect.top +=self.speed
        else:
            self.reset()

     # here we define how the enemy reset in the game
    def reset(self):
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-10,0)
