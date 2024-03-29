import pygame
import math
from random import *

 # here we difine the smallest enemy plane
class Enemy1(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/6.png").convert_alpha()
        # here we difine the destory picture of the enemy
        self.destroy_images = []
        self.destroy_images.extend([\
             pygame.image.load("images/7.png").convert_alpha(),\
             pygame.image.load("images/8.png").convert_alpha(),\
             pygame.image.load("images/9.png").convert_alpha(),\
             pygame.image.load("images/1.png").convert_alpha(),\
             ])
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 4
        # here we set the condition of the picture
        self.active = True
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-5,0)
        self.mask = pygame.mask.from_surface(self.image)


     # here we difine the movemont of the enemy
    def move(self):
        if self.rect.top < self.height:
            self.rect.top +=self.speed
        else:
            self.reset()

     # here we define how the enemy reset in the game
    def reset(self):
        self.active = True
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-5,0)
        





 # here we difine the middle size enemy plane
class Enemy2(pygame.sprite.Sprite):
    energy = 14
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/14.png").convert_alpha()
        # here we difine the destory picture of the enemy
        self.destroy_images = []
        self.destroy_images.extend([\
             pygame.image.load("images/15.png").convert_alpha(),\
             pygame.image.load("images/16.png").convert_alpha(),\
             pygame.image.load("images/17.png").convert_alpha(),\
             pygame.image.load("images/1.png").convert_alpha(),\
             ])
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 2
        # here we set the condition of the picture
        self.active = True
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-3,-self.height)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = Enemy2.energy


     # here we difine the movemont of the enemy
    def move(self):
        if self.rect.top < self.height:
            self.rect.top +=self.speed
        else:
            self.reset()

     # here we define how the enemy reset in the game
    def reset(self):
        self.active = True
        self.energy = Enemy2.energy
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-3,0)





 # here we difine the biggest size enemy plane
class Enemy3(pygame.sprite.Sprite):
    energy = 20
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/2.png").convert_alpha()
        # here we difine the destory picture of the enemy
        self.destroy_images = []
        self.destroy_images.extend([\
             pygame.image.load("images/3.png").convert_alpha(),\
             pygame.image.load("images/4.png").convert_alpha(),\
             pygame.image.load("images/5.png").convert_alpha(),\
             pygame.image.load("images/1.png").convert_alpha(),\
             ])
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 1
        # here we set the condition of the picture
        self.active = True
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(-1000,0)
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = Enemy3.energy


     # here we difine the movemont of the enemy
    def move(self):
        if self.rect.top < self.height:
            self.rect.top +=self.speed
        else:
            self.reset()

     # here we define how the enemy reset in the game
    def reset(self):
        self.active = True
        self.energy = Enemy3.energy
        self.rect.left = randint(0,self.width - self.rect.width)
        self.rect.bottom = randint(self.height*-1,0)


 # here we difine the smallest enemy plane
class Enemy4(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/6.png").convert_alpha()
        # here we difine the destory picture of the enemy
        self.destroy_images = []
        self.destroy_images.extend([\
             pygame.image.load("images/7.png").convert_alpha(),\
             pygame.image.load("images/8.png").convert_alpha(),\
             pygame.image.load("images/9.png").convert_alpha(),\
             pygame.image.load("images/1.png").convert_alpha(),\
             ])
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 5
        # here we set the condition of the picture
        self.active = True
        self.rect.left = randint(150,self.width - self.rect.width-150)
        self.rect.bottom = randint(self.height*-5,0)
        self.mask = pygame.mask.from_surface(self.image)


     # here we difine the movemont of the enemy
    def move(self):
        if self.rect.top < self.height:
            self.rect.top +=self.speed
            self.rect.left += 4*math.sin(self.rect.top/50)
        else:
            self.reset()

     # here we define how the enemy reset in the game
    def reset(self):
        self.active = True
        self.rect.left = randint(150,self.width - self.rect.width-150)
        self.rect.bottom = randint(self.height*-5,0)


 # here we difine the smallest enemy plane
class Enemy5(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/b1.png").convert_alpha()
        # here we difine the destory picture of the enemy
        self.destroy_images = []
        self.destroy_images.extend([\
             pygame.image.load("images/b2.png").convert_alpha(),\
             pygame.image.load("images/b3.png").convert_alpha(),\
             pygame.image.load("images/b4.png").convert_alpha(),\
             pygame.image.load("images/1.png").convert_alpha(),\
             ])
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 4
        # here we set the condition of the picture
        self.active = True
        self.rect.left = randint(-300,0)
        self.rect.bottom = randint(-100,150)
        self.mask = pygame.mask.from_surface(self.image)


     # here we difine the movemont of the enemy
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += 1.2*self.speed+2*math.sin(self.rect.top/50)
            self.rect.left += self.speed
        else:
            self.reset()

     # here we define how the enemy reset in the game
    def reset(self):
        self.active = True
        self.rect.left = randint(-300,0)
        self.rect.bottom = randint(-100,150)


 # here we difine the smallest enemy plane
class Enemy6(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/b1.png").convert_alpha()
        # here we difine the destory picture of the enemy
        self.destroy_images = []
        self.destroy_images.extend([\
             pygame.image.load("images/b2.png").convert_alpha(),\
             pygame.image.load("images/b3.png").convert_alpha(),\
             pygame.image.load("images/b4.png").convert_alpha(),\
             pygame.image.load("images/1.png").convert_alpha(),\
             ])
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 4
        # here we set the condition of the picture
        self.active = True
        self.rect.left = randint(700,1000)
        self.rect.bottom = randint(-100,150)
        self.mask = pygame.mask.from_surface(self.image)


     # here we difine the movemont of the enemy
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += 1.2*self.speed-2*math.sin(self.rect.top/50)
            self.rect.left -= self.speed
        else:
            self.reset()

     # here we define how the enemy reset in the game
    def reset(self):
        self.active = True
        self.rect.left = randint(700,1000)
        self.rect.bottom = randint(-100,150)


 # here we difine the smallest enemy plane
class Enemy7(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/r1.png").convert_alpha()
        # here we difine the destory picture of the enemy
        self.destroy_images = []
        self.destroy_images.extend([\
             pygame.image.load("images/r2.png").convert_alpha(),\
             pygame.image.load("images/r3.png").convert_alpha(),\
             pygame.image.load("images/r4.png").convert_alpha(),\
             pygame.image.load("images/1.png").convert_alpha(),\
             ])
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 4
        # here we set the condition of the picture
        self.active = True
        self.rect.left = randint(100,600)
        self.rect.bottom = randint(1000,2000)
        self.mask = pygame.mask.from_surface(self.image)


     # here we difine the movemont of the enemy
    def move(self):
        if self.rect.top > 0:
            self.rect.top -= 3
            self.rect.left += 3*math.sin(self.rect.top/40)
        else:
            self.reset()

     # here we define how the enemy reset in the game
    def reset(self):
        self.active = True
        self.rect.left = randint(100,600)
        self.rect.bottom = randint(1000,2000)

 # here we difine the biggest size enemy plane
class Enemy8(pygame.sprite.Sprite):
    energy = 1000
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/boss1.png").convert_alpha()
        # here we difine the destory picture of the enemy
        self.destroy_images = []
        self.destroy_images.extend([\
             pygame.image.load("images/boss2.png").convert_alpha(),\
             pygame.image.load("images/boss3.png").convert_alpha(),\
             pygame.image.load("images/boss4.png").convert_alpha(),\
             pygame.image.load("images/boss5.png").convert_alpha(),\
             ])
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 1
        # here we set the condition of the picture
        self.active = False
        self.rect.left = 0
        self.rect.bottom = -100
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = Enemy8.energy


     # here we difine the movemont of the enemy
    def move(self):
        if self.rect.top < 0:
            self.rect.top += self.speed

    def reset(self):
        self.active = True
        self.rect.left = 0
        self.rect.bottom = -1000


    
