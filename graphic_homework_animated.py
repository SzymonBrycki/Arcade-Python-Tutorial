"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

TREE_BROWN = (153, 61, 18)
LAND = (227, 184, 11)
SKY_BLUE = (11,173, 227)
DARK_GREEN = (15, 97, 14)


pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

moving = 2
 
pygame.display.set_caption("My Game")
 
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
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(SKY_BLUE)
 
    # --- Drawing code should go here

    # drawing ground
    pygame.draw.rect(screen, DARK_GREEN, (0, 200, 700, 500), 0)

    # drawing trees
    x = 100

    for i in range(3):
        pygame.draw.rect(screen, TREE_BROWN, (x, 100, 25, 150), 0)
        pygame.draw.line(screen, TREE_BROWN, (x, 150), (x - 50, 125), 5)
        pygame.draw.line(screen, TREE_BROWN, (x, 150), (x + 50, 125), 5)
        pygame.draw.circle(screen, GREEN, (x + 14 + moving, 75), 50, 0)
        pygame.draw.circle(screen, GREEN, (x - 50 + moving, 125), 20, 0)
        pygame.draw.circle(screen, GREEN, (x + 50 + moving, 125), 20, 0)
        x = x + 200

    pygame.time.delay(1000)
    moving = moving * -1

    #drawing a lake
    pygame.draw.ellipse(screen, BLUE, (250, 350, 250, 100), 0)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()