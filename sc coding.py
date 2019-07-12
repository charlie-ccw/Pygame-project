import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


    
pygame.init()
 # Set the width and height of the screen [width, height]
size = (640, 960)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Charlie's 'bullet hell'")





class Plane(pygame.sprite.Sprite):
    def __init__(self,x,y):

        super().__init__()
        self.image = pygame.Surface([30,30])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def update(self):
        if self.rect.x <= 670 and self.rect.x >= 0:
            #self.rect.x += -1
            self.rect.x += x_speed
        if self.rect.y <= 990 and self.rect.y >= 0:
            #self.rect.y += -1
            self.rect.y += y_speed
        if self.rect.x<0:
            self.rect.x=0
        if self.rect.x>610:
            self.rect.x=610
        if self.rect.y<0:
            self.rect.y=0
        if self.rect.y>930:
            self.rect.y=930
        print(self.rect.x)
        print(self.rect.y)

myplane = Plane(320,700)


    
class Bullet(pygame.sprite.Sprite):
    # This class represents a simple block the player collects. 
 
    def __init__(self,x,y):
        # Constructor, create the image of the block. 
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
 
 
    def update(self):
        # Automatically called when we need to move the block. 
        self.rect.y -= 5



all_sprites_list = pygame.sprite.Group()


all_sprites_list.add(myplane)


# set up the speed of x and y 
x_speed = 0

y_speed = 0



 # Loop until the user clicks the close button.
done = False
 # Used to manage how fast the screen updates
clock = pygame.time.Clock()
 # -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    # Here, check if the player click the Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        # here we give the speed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_speed = -3
            if event.key == pygame.K_d:
                x_speed = 3
            if event.key == pygame.K_w:
                y_speed = -3
            if event.key == pygame.K_s:
                y_speed = 3
            if event.key==pygame.K_SPACE:
                mybullet = Bullet(myplane.rect.x+15,myplane.rect.y)
                all_sprites_list.add(mybullet)
                

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                x_speed = 0
            if event.key == pygame.K_d:
                x_speed = 0
            if event.key == pygame.K_w:
                y_speed = 0
            if event.key == pygame.K_s:
                y_speed = 0
                
    # Here, we clear the screen to black
    screen.fill(BLACK)
    

    # mybullet update here and redraw
    all_sprites_list.update()

    all_sprites_list.draw(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
pygame.quit()
