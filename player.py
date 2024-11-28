import pygame

class Player:

    # Size of the player
    # Speed of the player(adjusted to 2 for now)
    # Position of the player
    # Image of the player (IDK how this will look atm)
    # Direction of the player avatar
    # Player Health (26/11/2024)

    # Constructor
    def __init__(self, sprite, screenWidth, screenHeight):
        # All values are subject to change
        self.speed = 2
        self.running_speed = 6
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
        self.animation_speed = 1
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

        # Load the running sprite
        self.runSprite()
        self.run_animation_speed = 1
        self.run_animation_count = 0 # Counter for the running animation
        self.isRunning = False # Boolean to check if the player is running.

        # Load the jumping sprite
        self.jumpSprite()
        self.jump_animation_speed = 1
        self.jump_animation_count = 0 # Counter for the jumping animation
        self.isJumping = False # Boolean to check if the player is jumping. 

        # Load the hurt sprite
        self.hurtSprite()
        self.hurt_animation_count = 0 # Counter for the hurt animation
        self.isHurt = False # Boolean to check if the player is hurt.

        # Screen dimensions
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        #USED TO TEST THE PLAYER MOVEMENT
        self.rect = pygame.Rect(self.x, self.y, self.frameWidth, self.frameHeight)
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
    
    #Sprite running animation
    def runSprite(self):
        self.run_sprite = pygame.image.load('MaleSwordsMan/Run.png')
        runSpriteWidth, runSpriteHeight = self.run_sprite.get_size()
        self.numRunFrames = runSpriteWidth // self.frameWidth
        self.runFrames = []
        for i in range(self.numRunFrames):
            runFrame = self.run_sprite.subsurface((i * self.frameWidth, 0, 128, self.frameHeight))
            self.runFrames.append(runFrame)
        
        self.runIndex = 0
        self.run_image = self.runFrames[self.runIndex]

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

    #Sprite jumping animation
    def jumpSprite(self):
        self.jump_sprite = pygame.image.load('MaleSwordsMan/Jump.png')
        jumpSpriteWidth, jumpSpriteHeight = self.jump_sprite.get_size()
        self.numJumpFrames = jumpSpriteWidth // self.frameWidth
        self.jumpFrames = []
        for i in range(self.numJumpFrames):
            jumpFrame = self.jump_sprite.subsurface((i * self.frameWidth, 0, 128, self.frameHeight))
            self.jumpFrames.append(jumpFrame)
        
        self.jumpIndex = 0
        self.jump_image = self.jumpFrames[self.jumpIndex]

    def hurtSprite(self):
        self.hurt_sprite = pygame.image.load('MaleSwordsMan/Hurt.png')
        hurtSpriteWidth, hurtSpriteHeight = self.hurt_sprite.get_size()
        self.numHurtFrames = hurtSpriteWidth // self.frameWidth
        self.hurtFrames = []
        for i in range(self.numHurtFrames):
            hurtFrame = self.hurt_sprite.subsurface((i * self.frameWidth, 0, 128, self.frameHeight))
            self.hurtFrames.append(hurtFrame)
        
        self.hurtIndex = 0
        self.hurt_image = self.hurtFrames[self.hurtIndex]
    
    # Since this is a 2D game, The player can only move along the x-axis
    def move(self, direction, game_time, is_running=False):

        speed = self.running_speed if is_running else self.speed
        #Calculate distance player is moving 
        distance = speed 

        if direction == 'left':

            #check player direction 
            if self.direction != 'left':
                #flip the sprite to face direction of travel
                self.walkingFrames = [pygame.transform.flip(frame, True, False) for frame in self.walkingFrames]
                self.runFrames = [pygame.transform.flip(frame, True, False) for frame in self.runFrames]
                self.direction = 'left'
            #Move the player 
            if self.x - distance >= 0:
                self.x -= distance
        elif direction == 'right':

            #check player direction 
            if self.direction != 'right':
                #flip the sprite to face direction of travel
                self.walkingFrames = [pygame.transform.flip(frame, True, False) for frame in self.walkingFrames]
                self.runFrames = [pygame.transform.flip(frame, True, False) for frame in self.runFrames]
                self.direction = 'right'
            #Move the player 
            if self.x + distance <= self.screenWidth - self.frameWidth:
                self.x += distance
        elif direction == 'up':
            # Move the player up
            if self.y - distance >= 0:
                self.y -= distance
        
        elif direction == 'down':
            # Move the player down
            if self.y + distance <= self.screenHeight - self.frameHeight:
                self.y += distance

        #Check if player is within the screen boundaries
        if self.x < 0:
            self.x = 0
        if self.x > self.screenWidth - self.frameWidth:
            self.x = self.screenWidth - self.frameWidth
        if self.y < 0:
            self.y = 0
        if self.y > self.screenHeight - self.frameHeight:
            self.y = self.screenHeight - self.frameHeight
        
        #Following is a test to see if backwards player is fixed ** TEST **

        #UPDATED: 27/11/2024 animation frame
        if is_running:
            self.run_animation_count += 1
            if self.run_animation_count >= self.run_animation_speed:
                self.runIndex = (self.runIndex + 1) % self.numRunFrames
                self.image = self.runFrames[self.runIndex]
                self.run_animation_count = 0
        else:
            self.walking_animation_count += 1
            if self.walking_animation_count >= self.animation_speed:
                self.walkingIndex = (self.walkingIndex + 1) % self.numWalkingFrames
                self.image = self.walkingFrames[self.walkingIndex]
                self.walking_animation_count = 0

        #Updates the players location while moving
        self.rect.topleft = (self.x, self.y)
    
    # Method for attacking
    def attack(self):
        self.isAttacking = True # Set the boolean to true. This allows the program to know that the player is attacking
        self.attack_animation_count = 0
        self.attackIndex = 0

    # Method to check if the player has been hit
    def hurt(self):
        self.hurt_animation_count = 0
        self.hurtIndex = 0

    #Method for jumping
    def jump(self):
        self.jump_animation_count += 1
        if self.jump_animation_count >= self.jump_animation_speed:
            self.jump_animation_count = 0
            self.jumpIndex = (self.jumpIndex + 1) % self.numJumpFrames
            self.jump_image = self.jumpFrames[self.jumpIndex]

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
                    
        elif self.isJumping:
            self.jump_animation_count += 1
            if self.jump_animation_count >= self.jump_animation_speed:
                self.jumpIndex = (self.jumpIndex + 1) % self.numJumpFrames
                self.image = self.jumpFrames[self.jumpIndex]
                screen.blit(self.image, (self.x, self.y))
                pygame.time.delay(20)

                # If the player has reached the end of the jumping animation, reset the animation
                if self.jumpIndex == self.numJumpFrames - 1:
                    self.jump_animation_count = 0
                    self.isJumping = False
                    self.walkingIndex = 0
                    self.walking_animation_count = 0
                    self.image = self.walkingFrames[self.walkingIndex]
                    screen.blit(self.image, (self.x, self.y))

        elif self.isRunning:
            self.run_animation_count += 1
            if self.run_animation_count >= self.run_animation_speed:
                self.runIndex = (self.runIndex + 1) % self.numRunFrames
                self.image = self.runFrames[self.runIndex]
                screen.blit(self.image, (self.x, self.y))
                pygame.time.delay(10)

        else:
            screen.blit(self.image, (self.x, self.y))