import pygame
from player import Player

# Initialize the pygame
pygame.init()

# Define the cursors
default_cursor = pygame.cursors.arrow
pointer_cursor = pygame.SYSTEM_CURSOR_HAND

# Initialise the font module
font = pygame.font.Font(None, 28)

# Set the window title
pygame.display.set_caption('Zombie Apocalypse')

display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

# Define the screen dimensions 
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (screen_width, screen_height))

# Create a player object. Player(characterused, screenWidth, screenHeight)
player = Player('MaleSwordsMan', screen_width, screen_height)

# Boolean variable to control the main loop
running = True
menu_active = False

# Store the boxes. This allows for it to only be drawn once as the menu is being called
menu_click_box, char_select_click_box, settings_click_box, close_click_box = None, None, None, None

def resize_screen(width, height):
    global screen, player, background
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    player.updated_screen_size(width, height)
    background = pygame.transform.scale(background, (width, height))

# Conversion for hex to rgb
def hex_to_rgb(hex_color, alpha=10):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) + (alpha,)

# Draw rounded corners
def draw_rounded_corners(surface, color, rect, radius):
    pygame.draw.rect(surface, color, rect, border_radius=radius)

def draw_menu(screen):
    # Size of the menu
    menu_width, menu_height = 300, 250
    menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
    grey_color = hex_to_rgb('#595450', 5)  # Convert hex to RGBA with transparency
    draw_rounded_corners(menu_surface, grey_color, menu_surface.get_rect(), 25)
    
    # Menu font
    menu_font = pygame.font.Font(None, 36)
    
    # Menu text
    # menu_font.render(text, antialias, color)
    menu_text = menu_font.render('Menu', True, hex_to_rgb('#ad0202'))
    char_select = menu_font.render('Change Character', True, hex_to_rgb('#ad0202'))
    settings_text = menu_font.render('Settings', True, hex_to_rgb('#ad0202'))
    close_text = menu_font.render('Close Game', True, hex_to_rgb('#ad0202'))
    
    # Button positions get_rect(center=(x, y))
    menu_text_rect = menu_text.get_rect(center=(menu_width // 2, 50))
    char_select_rect = char_select.get_rect(center=(menu_width // 2, 100))
    settings_text_rect = settings_text.get_rect(center=(menu_width // 2, 150))
    close_text_rect = close_text.get_rect(center=(menu_width // 2, 200))
    
    # Draw borders around text
    border_color = hex_to_rgb('#fafafa', 5)
    draw_rounded_corners(menu_surface, border_color, menu_text_rect.inflate(15, 5), 20)
    draw_rounded_corners(menu_surface, border_color, char_select_rect.inflate(15, 5), 20)
    draw_rounded_corners(menu_surface, border_color, settings_text_rect.inflate(15, 5), 20)
    draw_rounded_corners(menu_surface, border_color, close_text_rect.inflate(15, 5), 20)

    # Blit text onto the menu surface
    menu_surface.blit(menu_text, menu_text_rect)
    menu_surface.blit(char_select, char_select_rect)
    menu_surface.blit(settings_text, settings_text_rect)
    menu_surface.blit(close_text, close_text_rect)
    
    # Blit the menu surface onto the screen
    screen.blit(menu_surface, (screen_width // 2 - 100, screen_height // 2 - 100))
    
    # Inflate the rectangles for larger click areas
    menu_click_box = menu_text_rect.inflate(15, 5)
    char_select_click_box = char_select_rect.inflate(15, 5)
    setting_click_box = settings_text_rect.inflate(15, 5)
    close_click_box = close_text_rect.inflate(15, 5)

    return menu_click_box, char_select_click_box,setting_click_box, close_click_box

while running:
    # GAME CLOCK 
    game_time = pygame.time.get_ticks() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Swap the menu boolean to indicate if the menu is in use or not
                menu_active = not menu_active

                # If the menu has been deactivated, reset the click boxes
                if not menu_active:
                    menu_click_box, char_select_click_box, settings_click_box, close_click_box = None, None, None, None

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if menu_active:
                # Obtain the position of the mouse cursor
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check if the mouse click is within the bounds of the buttons
                if settings_click_box.collidepoint(mouse_x - (screen_width // 2 - 100), mouse_y - (screen_height // 2 - 100)):
                    print("Settings button clicked")
                elif close_click_box.collidepoint(mouse_x - (screen_width // 2 - 100), mouse_y - (screen_height // 2 - 100)):
                    running = False
            else:
                player.attack()

    if not menu_active:
        keys = pygame.key.get_pressed()
        # print(keys.count(1)) This allows for the number of keys pressed to be displayed. This could be used to know the original direction. Potentially
        # could also be used to fix the issue with the player obtaining more speed when multiple keys are pressed.
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if keys[pygame.K_LSHIFT]:
                player.run('left', game_time)
            else:
                player.isRunning = False
                player.move('left',game_time)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if keys[pygame.K_LSHIFT]:
                player.run('right',game_time)
            else:
                player.isRunning = False
                player.move('right',game_time)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.move('down',game_time)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.move('up',game_time)
        if keys[pygame.K_SPACE]:
            player.isRunning = False
            player.jump()
        screen.blit(background, (0, 0))
        player.draw(screen)
        text = font.render(f'Health: {player.health}', True, (255, 255, 255))
        screen.blit(text, (0, 0))
    else:
        menu_click_box, char_select_click_box,settings_click_box, close_click_box = draw_menu(screen)

    # If no button is clicked and in the menu check if the mouse is hovering over a button.
    # If it is than change the cursor to a pointer, otherwise if the curser is not the default cursor
    # and is not hovering a button than change it back to the default cursor.
    if menu_active:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if any(box.collidepoint(mouse_x - (screen_width // 2 - 100), mouse_y - (screen_height // 2 - 100)) for box in [menu_click_box, char_select_click_box, settings_click_box, close_click_box]):
            pygame.mouse.set_cursor(pointer_cursor)
        elif pygame.mouse.get_cursor() != default_cursor:
            pygame.mouse.set_cursor(default_cursor)

    pygame.display.flip()

pygame.quit()