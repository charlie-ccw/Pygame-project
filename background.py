import pygame

 # here we difine the background
class Background(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/background.jpg").convert_alpha()
        # here we difine the destory picture of the enemy
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 1
        # here we set the condition of the picture
        self.active = True
        self.rect.left = 0
        self.rect.top = 0




    # here we difine the movement of the picture
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    # here we difine how the picture reset in the game
    def reset(self):
        self.active = True
        self.rect.left = 0
        self.rect.top = -960
        

 # here we difine the background
class background(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/background.jpg").convert_alpha()
        # here we difine the destory picture of the enemy
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.speed = 1
        # here we set the condition of the picture
        self.active = True
        self.rect.left = 0
        self.rect.top = -960




    # here we difine the movement of the picture
    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    # here we difine how the picture reset in the game
    def reset(self):
        self.active = True
        self.rect.left = 0
        self.rect.top = -960

