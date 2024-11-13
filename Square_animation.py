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

rectX = 50
rectY = 50

rectChangeX = 5
rectChangeY = 5

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
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
    screen.fill(BLACK)
 
    # --- Drawing code should go here

    pygame.draw.rect(screen, WHITE, (rectX, rectY, 50, 50))

    rectX = rectX + rectChangeX
    rectY = rectY + rectChangeY

    if rectY > 450 or rectY < 0:
	    rectChangeY = rectChangeY * -1
    if rectX > 650 or rectX < 0:
	    rectChangeX = rectChangeX * -1

    '''
    if (rectY > 450) or (rectY < 0):
        rectChangeY = (rectChangeY * -1)
    if (rectX > 650) or (rectX < 0):
        rectChangeX = (rectChangeX * -1)
    '''

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()