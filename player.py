import pygame

class Player:
    # Size of the player
    # Speed of the player
    # Position of the player
    # Image of the player (IDK how this will look atm)
    # Direction of the player avatar
    # Player Health (26/11/2024)

    # Constructor
    def __init__(self, sprite, screenWidth, screenHeight):
        # All values are subject to change
        self.speed = 0.5
        self.health = 100

        # Define the size of the frame
        self.frameWidth = 128
        self.frameHeight = 128

        # Position of the player to be centre of the screen
        self.x = (screenWidth - self.frameWidth) // 2
        self.y = (screenHeight - self.frameHeight) // 2

        # Direction of the player
        self.direction = 'right'

        # Load the sprite sheet (Currently hard coded to the walk animation)
        self.sprite_sheet = pygame.image.load('MaleSwordsMan/Walk.png')

        # Animation Speed
        self.animation_speed = 5
        self.animation_count = 0 # Counter for the animation. This will be used to change the image of the player
        sprite_sheet_width, sprite_sheet_height = self.sprite_sheet.get_size()
        self.num_frames = sprite_sheet_width // self.frameWidth

        # This is currently loading the walk animation
        self.frames = []
        for i in range(self.num_frames):
            # Get the frame from the sprite sheet
            # subsurface((x, y, width, height))
            frame = self.sprite_sheet.subsurface((i * self.frameWidth, 0, 75, self.frameHeight))
            self.frames.append(frame)

        # Set the initial image of the player walking sprite
        self.image_index = 0

        self.image = self.frames[self.image_index]
        


    # Since this is a 2D game, The player can only move along the x-axis
    def move(self, direction):
        if direction == 'left':
            # Check the player direction, if it is not the same as the direction we want to move, flip the image
            if self.direction != 'left':
                # Change the image of the player. This will be used to animate the player
                # pygame.transform.flip(image, x-axis, y-axis)
                self.frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]
                self.direction = 'left'
            
            # Move the player
            # If the player is at the edge of the screen, do not move
            if  self.x - self.speed > 0:
                self.x -= self.speed
            
        elif direction == 'right':
            if self.direction != 'right':
                # Change the image of the player. This will be used to animate the player
                # pygame.transform.flip(image, x-axis, y-axis)
                self.frames = [pygame.transform.flip(frame, True, False) for frame in self.frames]
                self.direction = 'right'
            
            # Move the player
            # Check if they are at the edge of the screen to avoid the character going off screen
            if self.x + self.speed < 726:
                self.x += self.speed

        elif direction == 'down':
            if self.y + self.speed < 600 - self.frameHeight:
                self.y += self.speed
        elif direction == 'up':
            if self.y - self.speed > 261:
                self.y -= self.speed

        # Update the animation frame
        self.animation_count += 1
        if self.animation_count >= self.animation_speed:
            self.animation_count = 0
            self.image_index = (self.image_index + 1) % self.num_frames
            self.image = self.frames[self.image_index]
    
    # Draw the player on the screen
    def draw (self, screen):
        screen.blit(self.image, (self.x, self.y))