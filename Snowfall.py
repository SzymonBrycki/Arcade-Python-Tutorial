"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

TREE_BROWN = (153, 61, 18)
LAND = (227, 184, 11)


pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

snow_list = list()

for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])
 
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
    screen.fill(BLACK)
 
    # --- Drawing code should go here

    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)

        snow_list[i][1] += 1

        if snow_list[i][1] > 400:
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            x = random.randrange(0, 400)
            snow_list[i][0] = x
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()