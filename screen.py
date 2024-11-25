import pygame
from player import Player

# Initialize the pygame
pygame.init()

# Defining a backgound color
background_color = (0, 0, 255)

# Define the screen dimensions 
# Screen object (width, height)
screen = pygame.display.set_mode((800, 600))

# 'pygame.display.flip()' updates the display

# Create a player object
player = Player('player.png', 800, 600) # Currently hardcoded

# Boolean variable to control the main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Check which key is being pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.move('left')
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.move('right')

    # Fill the screen with the background color
    screen.fill(background_color)

    # Create a player object
    player.draw(screen)

    pygame.display.flip()

pygame.quit()
