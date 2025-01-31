import pygame
import random

from drop import Drop

# Inheritance from the pygame.sprite.Sprite class. The sprite clas allows for the creation of sprite objects
class Enemies (pygame.sprite.Sprite):
    # Enemies base level zombie(need good name) wonders, slow movers
    # Base level zombie
    # attributes:
    # health: 100
    # damage: 10
    # speed: 1
    # attack_speed: 1
    # attack_range: 1
    # attack_type: melee
    # drop: random loot or nothing (need to implement loot system)
    # drop_rate: need to implement loot system
    # drop_amount: need to implement loot system
    # drop_type: need to implement loot system
    # AI: wander

    def __init__(self, x, y, player, screenWidth, screenHeight, drop):
        super().__init__()
        self.health = 100
        self.damage = 10
        self.speed = 1
        self.attack_speed = 1
        self.attack_range = 1
        self.attack_type = "melee"
        self.drop = drop  # create loot system later
        self.dropItem = drop.obtainItem()
        self.drop_rate = None  # create loot system later
        self.drop_amount = None  # create loot system later
        self.drop_type = None  # create loot system later

        # AI attributes
        self.target = player  # target player
        self.targeted_player = True
        self.vison_range = 500
        self.attack_range = 50
        self.walk_speed = 0.75

        # Enemy Dimensions
        self.frameWidth = 45
        self.frameHeight = 75
        self.x = self.frameWidth
        self.y = self.frameHeight

        # Load and scale the enemy image
        self.image = pygame.image.load("Enemies/enemy.png")
        self.image = pygame.transform.scale(self.image, (self.frameWidth, self.frameHeight))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Screen dimensions
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        # Hitbox for the enemy took from player.py for testing 3/12/2024
        # Define a smaller hitbox. This is used to check for collisions with the enemy
        self.hitbox = pygame.Rect(self.x + 25, self.y + 40, self.frameWidth - 75, self.frameHeight - 40)

        # Attack hitbox. This defines the area that the player can hit an enemy in it is used to check for collisions with the enemy
        self.attack_hitbox = pygame.Rect(self.x + 70, self.y + 70, self.frameWidth - 70, self.frameHeight - 80)

        #Damage text 29/11/2024
        self.damage_text = pygame.sprite.Group()

        # Boolean variable to check if the enemy has died
        # time the sprite died to remove it from the group
        self.died = False
        self.timeDied = 0
        self.attackDelay = 0 # Used to delay the attack of the enemy

    def move(self):

        # If the sprite has died and enough time has passed than the sprite will be removed from the group
        # This visualises to the user that they sucessfully killed the enemy
        if self.died and pygame.time.get_ticks() - self.timeDied > 1000:
            self.kill() # This removes the sprite from the group. This allows them to no longer appear on the screen
        # If the sprite has died but not enough time return. This stops the sprite from still moving while it is dead
        elif self.died:
            return

        # Move the enemy
        if self.targeted_player:
            # Move towards the player
            direction = pygame.math.Vector2(self.target.rect.center) - pygame.math.Vector2(self.rect.center)
            if direction.length() > 0 and not self.rect.colliderect(self.target.hitbox):
                direction = direction.normalize()
                self.rect.center += direction * self.speed
        else:
            # Wander around
            self.rect.x += random.choice([-1, 1]) * self.walk_speed
            self.rect.y += random.choice([-1, 1]) * self.walk_speed


        # Check if player is within vision range
        if self.target and pygame.math.Vector2(self.rect.center).distance_to(self.target.rect.center) <= self.vison_range:
            self.targeted_player = True
        else:
            self.targeted_player = False

         # Check if Enemy is within the screen boundaries
        if self.hitbox.x < 0:
            self.x = 0
        if self.x > self.screenWidth:
            self.x = self.screenWidth
        elif self.y < 566:
            self.y = 566
        
    # Method for when the current enemy is hit
    def hurt (self, damage):

        # Added (29/11/2024) If user attacked multiple time it would rotate the dead enemy
        # and reset the tick counter. Updated to return if the enemy is already dead.
        if self.died:
            return
        self.health -= damage

        # Check if the enemy has no more health. Meaning that they were killed
        if self.health <= 0:
            self.died = True
            self.image = pygame.transform.rotate(self.image, 90)

            # The time the sprite died is recorded. This is used to remove the sprite from the group after a certain amount of time
            self.timeDied = pygame.time.get_ticks()
            return True
        return False

    #Method to get the damage done by enemy 29/11/2024
    def get_damage(self):
        return self.damage
    
    # Method: can_attack
    # Purpose: Check if the enemy attack delay has passed
    # Parameters: None
    # Date Added: 2024/12/02
    # Last Updated: 2024/12/02
    def can_attack(self):
        if pygame.time.get_ticks() - self.attackDelay > 500 and not self.died:
            self.attackDelay = pygame.time.get_ticks()
            return True
        return False


    def draw(self, screen):
        screen.blit(self.image, self.rect)