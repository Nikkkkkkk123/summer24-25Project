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

        # Animation Walking animations
        self.animation_speed = 5
        self.animation_count = 0 # Counter for the animation. This will be used to change the image of the player
        self.walking_animation_count = 0 # Counter for the walking animation

        # Load the walking sprite
        self.loadWalkingSprite()

        # Load the attacking sprite
        self.loadAttackingSprite()
        self.attack_animation_speed = 1
        self.isAttacking = False # Boolean to check if the player is attacking. This allows for the player to be drawn to the screen. 
        self.attack_animation_count = 0 # Counter for the attack animation
        self.attackDirection = 'right' # Used to know if the sprite has to be flipped from the original orientation. This is caused from the user moving left and right
        
    def loadWalkingSprite(self):
        # Loads the walking sprite from the png
        self.walkingSprite = pygame.image.load('MaleSwordsMan/Walk.png')
        walkingSpriteWidth, walkingSpriteHeight = self.walkingSprite.get_size()
        self.numWalkingFrames = walkingSpriteWidth // self.frameWidth # Number of frames in the sprite

        self.walkingFrames = []
        # Subsurface is used to extract a portion of the image
        for i in range(self.numWalkingFrames):
            walkingFrame = self.walkingSprite.subsurface((i * self.frameWidth, 0, 128, self.frameHeight))
            self.walkingFrames.append(walkingFrame)

        self.walkingIndex = 0
        self.image = self.walkingFrames[self.walkingIndex]
    
    # Method to allow for the user to attack
    def loadAttackingSprite(self):
        self.attack_sprite = pygame.image.load('MaleSwordsMan/Attack_1.png')
        attackSpriteWidth, attackSpriteHeight = self.attack_sprite.get_size()
        self.numAttackFrames = attackSpriteWidth // self.frameWidth
        self.attackFrames = []
        for i in range(self.numAttackFrames):
            attackFrame = self.attack_sprite.subsurface((i * self.frameWidth, 0, 128, self.frameHeight))
            self.attackFrames.append(attackFrame)
        
        self.attackIndex = 0
        self.attack_image = self.attackFrames[self.attackIndex]

    # Since this is a 2D game, The player can only move along the x-axis
    def move(self, direction):
        if direction == 'left':
            # Check the player direction, if it is not the same as the direction we want to move, flip the image
            if self.direction != 'left':
                # Change the image of the player. This will be used to animate the player
                # pygame.transform.flip(image, x-axis, y-axis)
                self.walkingFrames = [pygame.transform.flip(frame, True, False) for frame in self.walkingFrames]
                self.direction = 'left'
            
            # Move the player
            # If the player is at the edge of the screen, do not move
            if  self.x - self.speed > 0:
                self.x -= self.speed
            
        elif direction == 'right':
            if self.direction != 'right':
                # Change the image of the player. This will be used to animate the player
                # pygame.transform.flip(image, x-axis, y-axis)
                self.walkingFrames = [pygame.transform.flip(frame, True, False) for frame in self.walkingFrames]
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
        self.walking_animation_count += 1
        if self.walking_animation_count >= self.animation_speed:
            self.walking_animation_count = 0
            self.walkingIndex = (self.walkingIndex + 1) % self.numWalkingFrames
            self.image = self.walkingFrames[self.walkingIndex]
    
    # Method for attacking
    def attack(self):
        self.isAttacking = True # Set the boolean to true. This allows the program to know that the player is attacking
        self.attack_animation_count = 0
        self.attackIndex = 0

    # Draw the player on the screen
    def draw (self, screen):
        # Check the boolean to see if the attacking animation is meant to be getting used
        if self.isAttacking:
            # Check the direction of the player so they attack in the correct direction
            if self.attackDirection != self.direction:
                self.attackFrames = [pygame.transform.flip(frame, True, False) for frame in self.attackFrames] # Flip the attack sprites to match the correct orientation that the user is currently in
                self.attackDirection = self.direction # Update the attack direction to the current direction of the player

            self.attack_animation_count += 1
            if self.attack_animation_count >= self.attack_animation_speed:
                self.attackIndex = (self.attackIndex + 1) % self.numAttackFrames # Update the attack index 
                self.attack_image = self.attackFrames[self.attackIndex]
                screen.blit(self.attack_image, (self.x, self.y)) # Display the frame change to the user
                pygame.time.delay(35) # Delay to make the attack animation slower

                # If the player has reached the end of the attacking animation, reset the animation
                if self.attackIndex == self.numAttackFrames - 1:
                    self.attack_animation_count = 0
                    self.isAttacking = False
                    
                    # Reset the sprite to the first frame of the walking sprite
                    self.walkingIndex = 0
                    self.walking_animation_count = 0
                    self.image = self.walkingFrames[self.walkingIndex]
                    screen.blit(self.image, (self.x, self.y))
                    
                
        else:
            screen.blit(self.image, (self.x, self.y))