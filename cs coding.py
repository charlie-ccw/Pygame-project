import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# here define the player's plane
def draw_stick_figure(screen,x,y):
    pygame.draw.rect(screen,WHITE,[x-10,y-10,20,20],20)
    
pygame.init()
 # Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Charlie's 'bullet hell'")


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

mybullet = Bullet(200,400)

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(mybullet)

# set up the coordinate of x and y  
x_coord = 350
y_coord = 470
# set up the speed of x and y 
x_speed1 = 0
x_speed2 = 0
y_speed1 = 0
y_speed2 = 0


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
                x_speed2 = -3
            if event.key == pygame.K_d:
                x_speed1 = 3
            if event.key == pygame.K_w:
                y_speed2 = -3
            if event.key == pygame.K_s:
                y_speed1 = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                x_speed = 0
            if event.key == pygame.K_d:
                x_speed = 0
            if event.key == pygame.K_w:
                y_speed = 0
            if event.key == pygame.K_s:
                y_speed = 0
    # here add the speed to object
    if x_coord > 20:
        x_coord += x_speed2
    if x_coord < 680:
        x_coord += x_speed1
    if y_coord > 20:
        y_coord += y_speed2
    if y_coord < 480:
        y_coord += y_speed1
    # Here, we clear the screen to black
    screen.fill(BLACK)
    
    # draw the player's plane
    draw_stick_figure(screen,x_coord,y_coord)

    # mybullet update here and redraw
    all_sprites_list.update()

    all_sprites_list.draw(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
pygame.quit()
