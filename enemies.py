import pygame
import random

class Enemies:
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

    def __init__(self, x, y,screenWidth, screenHeight):
        self.health = 100
        self.damage = 10
        self.speed = 1
        self.attack_speed = 1
        self.attack_range = 1
        self.attack_type = "melee"
        self.drop = None  # create loot system later
        self.drop_rate = None  # create loot system later
        self.drop_amount = None  # create loot system later
        self.drop_type = None  # create loot system later

        # AI attributes
        self.target = None  # target player
        self.targeted_player = False
        self.vison_range = 500
        self.walk_speed = 0.75

        # Enemy Dimensions
        self.frameWidth = 45
        self.frameHeight = 75

        # Load and scale the enemy image
        self.image = pygame.image.load("Enemies/enemy.png")
        self.image = pygame.transform.scale(self.image, (self.frameWidth, self.frameHeight))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Screen dimensions
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

    def move(self):
        # Move the enemy
        if self.targeted_player:
            # Move towards the player
            direction = pygame.math.Vector2(self.target.rect.center) - pygame.math.Vector2(self.rect.center)
            if direction.length() > 0:
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
        if self.x < 0:
            self.x = 0
        if self.x > self.screenWidth:
            self.x = self.screenWidth
        elif self.y < 566:
            self.y = 566
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)