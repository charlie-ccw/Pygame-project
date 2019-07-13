import pygame

# here we difine the basic bullet of the plane
class Bullet1(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/18.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 15
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    # here we difine the movement of the bullets
    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False
    # here we set the method of resetting the bullets
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
