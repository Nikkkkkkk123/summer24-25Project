import pygame
from player import Player

# Initialize the pygame
pygame.init()

# Initialise the font module
font = pygame.font.Font(None, 28)

# Set the window title
pygame.display.set_caption('Zombie Apocalypse')

#Dynamically get the screen size
display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h


# Load the background image
background = pygame.image.load('background.png')

# Define the screen dimensions 
# Screen object (width, height) of user's screen
screen = pygame.display.set_mode((screen_width, screen_height))

# 'pygame.display.flip()' updates the display

# Create a player object. Player(characterused, screenWidth, screenHeight)
player = Player('MaleSwordsMan', 800, 750) # Currently hardcoded

# Boolean variable to control the main loop
running = True

def resize_screen(width,height):
    global screen, player, background
    screen = pygame.display.set_mode((width, height))
    player.updated_screen_size(width, height)
    background = pygame.transform.scale(background, (width, height))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Add input for left mouse button click. This allows the user to attack
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            player.attack()
    
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
# End of the game loop