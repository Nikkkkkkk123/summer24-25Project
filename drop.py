import pygame
import random

class Drop(pygame.sprite.Sprite):
    def __init__(self):
        # Load the sprites
        self.frameWidth = 32
        self.frameHeight = 32

        self.healImage = pygame.image.load("Drops/heal.png")
        self.healImage = pygame.transform.scale(self.healImage, (self.frameWidth, self.frameHeight))
        self.rect = self.healImage.get_rect()
    
    def obtainItem(self):
        hasItem = random.choice([True, False])

        if hasItem:
            item = random.choice([self.healImage])
            return "Item"
        else:
            return None
    


