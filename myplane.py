import pygame

 # here we difine the Myplane
class Myplane(pygame.sprite.Sprite):
    energy = 5
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/10.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/11.png").convert_alpha(),\
            pygame.image.load("images/12.png").convert_alpha(),\
            pygame.image.load("images/13.png").convert_alpha(),\
            pygame.image.load("images/1.png").convert_alpha(),\
            ])
        self.rect = self.image.get_rect()
        self.width = 700
        self.height = 960
        self.rect.left = (self.width - self.rect.width)/2
        self.rect.top = self.height - self.rect.height - 150
        self.speed = 10
        # here we set the condition of the picture
        self.active = True
        self.invincible = False
        self.mask = pygame.mask.from_surface(self.image)
        self.energy = Myplane.energy

        
 # here we set the movement of my plane
    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width


    # here we set the reset of my plane
    def reset(self):
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self. rect.height - 60
        self.active = True
        self.energy = Myplane.energy
        self.invincible = True
        

    
            
