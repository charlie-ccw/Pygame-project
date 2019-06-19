import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 # Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Charlie's 'bullet hell'")

 # Loop until the user clicks the close button.
done = False
 # Used to manage how fast the screen updates
clock = pygame.time.Clock()
 # -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # Here, we clear the screen to black
    screen.fill(BLACK)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
pygame.quit()
