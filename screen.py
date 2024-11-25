import pygame
from player import Player

# Initialize the pygame
pygame.init()

# Initialise the font module
font = pygame.font.Font(None, 28)

# Set the window title
pygame.display.set_caption('Zombie Apocalypse')

# Defining a backgound color
background_color = (0, 0, 255)

# Load the background image
background = pygame.image.load('background.png')

# Define the screen dimensions 
# Screen object (width, height)
screen = pygame.display.set_mode((800, 600))

# 'pygame.display.flip()' updates the display

# Create a player object. Player(characterused, screenWidth, screenHeight)
player = Player('MaleSwordsMan', 800, 750) # Currently hardcoded

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
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.move('down')
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.move('up')

    # Using Blit you can draw the background image on the screen
    screen.blit(background, (0, 0))

    # Create a player object
    player.draw(screen)

    # Display the player health
    text = font.render(f'Health: {player.health}', True, (255, 255, 255))
    screen.blit(text, (0, 0))

    pygame.display.flip()

pygame.quit()
