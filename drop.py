# Date Created: 2/12/2024
# Date Modified: 2/12/2024
# Description: This file contains the Drop class which is used to create a drop object that can be used to heal the player.

import pygame
import random

class Drop(pygame.sprite.Sprite):
    def __init__(self, x = 0, y = 0, item = "", time = 0):
        super().__init__()
        # Load the sprites
        self.frameWidth = 32
        self.frameHeight = 32

        self.healImage = pygame.image.load("Drops/heal.png")
        self.healImage = pygame.transform.scale(self.healImage, (self.frameWidth, self.frameHeight))
        self.rect = self.healImage.get_rect()

        self.item = ""
        self.x = 0
        self.y = 0
        self.timeCreated = 0

        # This is for when a new item is being created as it is being displayed in the world to the user
        if item != None:
            self.item = item
            self.x = x
            self.y = y
            self.rect.center = (self.x, self.y)
            self.timeCreated = time
    
    # Method Name: obtainItem
    # Description: This method is used to determine whether or not a drop will be created.
    # Parameter: None
    # Date Created: 2/12/2024  
    # Date Modified: 2/12/2024
    def obtainItem(self):
        # Currently 50% chance of an item being dropped
        hasItem = random.choice([True])

        if hasItem:
            self.item = "heal"
            return "heal"
        else:
            return None
    
    # Method Name: dropItem
    # Description: This method is used to drop an item in the world.
    # Parameter: x, y
    # Date Created: 2/12/2024
    # Date Modified: 2/12/2024
    def dropItem(self, x, y):
        if self.item == "heal":
            self.x = x
            self.y = y
            self.rect.center = (self.x, self.y)
            self.item = "heal"

    # Method Name: useItem
    # Description: This method is used to use the item that was dropped.
    # Parameter: player
    # Date Created: 2/12/2024
    # Date Modified: 2/12/2024
    def useItem (self, player):
        if self.item == "heal":
            player.heal(10)
            self.item = None
            self.kill()
            
    # Method Name: item_image
    # Description: This method is used to get the image of the item that was dropped.
    # Parameter: itemName
    # Date Created: 3/12/2024
    # Date Modified: 3/12/2024
    def item_image(itemName):
        return "Drops/"+itemName+".png"

    # Method Name: get_item_name
    # Description: This method is used to get the name of the item that was dropped.
    # Parameter: self
    # Date Created: 3/12/2024
    def get_item_name(self):
        return self.item


    # Method Name: draw
    # Description: This method is used to draw the item that was dropped.
    # Parameter: screen, item
    # Date Created: 2/12/2024
    # Date Modified: 2/12/2024
    def draw(self, screen, item, time):
        # If the item has been on screen for longer than the period of time it will despawn.
        if (time - self.timeCreated) > 3000:
            self.kill()
            return
        if item == "heal":
            screen.blit(self.healImage, self.rect)
    


