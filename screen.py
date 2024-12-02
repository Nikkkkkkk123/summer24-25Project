import pygame
from player import Player
from enemies import Enemies
from displayDamage import displayDamage
from drop import Drop
import random

# Initialize the pygame
pygame.init()

# Define the cursors
default_cursor = pygame.cursors.arrow
pointer_cursor = pygame.SYSTEM_CURSOR_HAND

# Create sprite groups to sort the entities of characters
all_entities = pygame.sprite.Group()
enemies_group = pygame.sprite.Group() # Group for the enemy sprites
items_group = pygame.sprite.Group() # Group for the items   
enemy_list = pygame.sprite.OrderedUpdates()  # Group which keep order

# Initialise the font module
font = pygame.font.Font(None, 28)

# Set the window title
pygame.display.set_caption('Zombie Apocalypse')

display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

# Define the screen dimensions 
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED | pygame.FULLSCREEN)

background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (screen_width, screen_height))

# Create a player object. Player(characterused, screenWidth, screenHeight)
player = Player('MaleSwordsMan', screen_width, screen_height)
drop = Drop()
enemies = Enemies( 100, 100, player, screen_width, screen_height, drop)


# Boolean variable to control the main loop
running = True
menu_active = False
is_running = False # This is used to determine if the player is running or not. This is used to determine the speed of the player.

# Store the boxes. This allows for it to only be drawn once as the menu is being called
menu_click_box, char_select_click_box, settings_click_box, close_click_box = None, None, None, None

# Define the colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
       
# Define player health
bar_width = 20
max_health = player.health


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

# Draw the health bar of the player
def draw_health_bar(x, y, health, max_health):
    """Draws the health bar with a red background and a green foreground."""
    # Red background (initial health)
    pygame.draw.rect(screen, RED, (x, y,max_health, 20))
    # Green foreground (current health)
    pygame.draw.rect(screen, GREEN, (x, y, health, 20))

#List of Enemies that can be spawned
enemy_list = [Enemies(random.randint(0, screen_width), random.randint(600, screen_height), player, screen_width, screen_height, drop) for _ in range(5)]

# Add the player to the all_entities group
all_entities.add(player)

# Add the enemies to the enemies_group and all_entities group
for enemy in enemy_list:
    enemies_group.add([enemy])

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

                for enemy in enemies_group:
                    if player.attack_hitbox.colliderect(enemy.rect):
                        died = enemy.hurt(player.damage)
                        if died:
                            player.score += 1

    if not menu_active:
        keys = pygame.key.get_pressed()
        no_keys = keys.count(1)

        # Check if the player is running
        if keys[pygame.K_LSHIFT]:
            is_running = True
        elif is_running:
            is_running = False


        # print(keys.count(1)) This allows for the number of keys pressed to be displayed. This could be used to know the original direction. Potentially
        # could also be used to fix the issue with the player obtaining more speed when multiple keys are pressed.
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move('left', no_keys, is_running)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move('right',no_keys,is_running)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.move('down',no_keys, is_running)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.move('up',no_keys, is_running)
        if keys[pygame.K_SPACE]:
            player.isRunning = False
            player.jump()

        screen.blit(background, (0, 0))
        player.draw(screen)
        text = font.render(f'Health: {player.health}', True, (255, 255, 255))
        screen.blit(text, (10, 0))
        text = font.render(f'Score: {player.score}', True, (255, 255, 255))
        screen.blit(text, (10, 45))

        # Draw the enemies
        for enemy in enemies_group:
            enemy.move()
            enemies_group.draw(screen)
            if not enemies_group.has(enemy) and enemy.dropItem != None:
                new_drop = Drop(enemy.rect.centerx, enemy.rect.centery, enemy.dropItem, pygame.time.get_ticks())
                items_group.add(new_drop)
        
        # Draw the items
        for drop in items_group:
            drop.draw(screen, drop.item, pygame.time.get_ticks())
        
        #Check for collisons and apply damage will check if player or enemies collide with each other
        if pygame.sprite.spritecollideany(player, enemies_group):

            for enemy in enemies_group:
                if player.hitbox.colliderect(enemy.rect) and enemy.can_attack():
                    player.hurt(enemy.damage)
                    
                    # Set the time the last attack was to the current time
                    enemy.attackDelay = pygame.time.get_ticks()

                    #display damage text
                    damage_text = displayDamage(player.rect.centerx, player.rect.top - 20, enemies.get_damage(),color=(255,0,0))
                    player.damage_texts.add(damage_text)
                    player.damage_texts.update()
        
        # Use the item. Currently if sprite runs over it
        # If the player collides with the items sprite, the player will use the item
        if pygame.sprite.spritecollideany(player, items_group):
            for drop in items_group:
                if player.hitbox.colliderect(drop.rect):
                    drop.useItem(player)
                
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

    # Show the postion of the player on the screen for debugging purposes
    postion_text = font.render(f'Player Position: {player.rect.topleft}', True, (255, 255, 255))
    screen.blit(postion_text, (10, 65))

    # Player health bar (x, y, health, max_health)
    draw_health_bar(10,20, player.health, max_health)
    
    pygame.display.flip()

pygame.quit()