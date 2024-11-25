import pygame

class Player:
    # Size of the player
    # Speed of the player
    # Position of the player
    # Image of the player (IDK how this will look atm)
    # Direction of the player avatar

    # Constructor
    def __init__(self, image, screenWidth, screenHeight):
        # All values are subject to change
        self.size = 50 # For now
        self.speed = 0.25

        # Position of the player to be centre of the screen
        self.x = (screenWidth - self.size) // 2
        self.y = (screenHeight - self.size) // 2

        # Load the image
        self.image = pygame.image.load(image)

        # Resize the image
        self.image = pygame.transform.scale(self.image, (self.size, self.size))

        # Direction of the player
        self.direction = 'right'

    # Since this is a 2D game, The player can only move along the x-axis
    def move(self, direction):
        if direction == 'left':
            # Check the player direction, if it is not the same as the direction we want to move, flip the image
            if self.direction != 'left':
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = 'left'
            self.x -= self.speed
        elif direction == 'right':
            if self.direction != 'right':
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = 'right'
            self.x += self.speed
    
    # Draw the player on the screen
    def draw (self, screen):
        screen.blit(self.image, (self.x, self.y))