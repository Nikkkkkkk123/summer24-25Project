# Created: 3/12/2024
# Modified: 3/12/2024
# Class Name: Inventory
# Description: This class is used to manage the player's inventory.

import pygame
from drop import Drop

class Inventory:
    # Method Name: __init__
    # Description: This method is used to initialize the Inventory class.
    # Parameter: None
    # Date Created: 3/12/2024
    # Date Modified: 3/12/2024
    def __init__(self):
        self.dictionary_items = {} # Store the items in a dictionary (Similar to a hashmap in Java)
        self.itemCount = 0

    # Method Name: draw_inventory
    # Description: This method is used to draw the player's inventory.
    # Parameter: screen
    # Date Created: 3/12/2024
    # Date Modified: 3/12/2024
    def draw_inventory(self, screen):
        screen_width, screen_height = screen.get_size()
        box_size = 46
        margin = 5
        inventory_h = box_size + margin * 2
        inventory_w = 6 * box_size + 7 * margin # 6 boxes with 5 margins between them. This avoids going accross the whole width of the screen
        x_offset = (screen_width - inventory_w) // 2
        y_offset = margin

        # Create a semi-transparent surface
        inventory_surface = pygame.Surface((inventory_w, inventory_h), pygame.SRCALPHA)
        # fill((R, G, B, A)) where A is the alpha value
        inventory_surface.fill((50, 50, 50, 200))  # Dark grey with 50% transparency

        itemx_offset = margin

        for i in range(6):
            pygame.draw.rect(inventory_surface, (255, 255, 255, 200), (itemx_offset, margin, box_size, box_size))
            # If the inventory being held is not empty and not all items are being displayed than draw the item
            if i < self.itemCount:
                # Get the i'th item in the inventory
                itemName, noItem = self.dictionary_value(i)
                # Display it to the screen
                dropImage = pygame.image.load("Drops/heal.png") # Currently hard coded
                dropImage = pygame.transform.scale(dropImage, (box_size, box_size))
                inventory_surface.blit(dropImage, (itemx_offset, margin))

            itemx_offset += box_size + margin
        
        screen.blit(inventory_surface, (x_offset, y_offset))
        pygame.display.flip()

    def dictionary_value(self, i):
        itemList = list(self.dictionary_items.items())

        # Just basic error handling. Currently if this method is called it should always be in range
        if i < len(itemList):
            return itemList[i]
        else:
            return None

    def add_item(self, item: Drop):
        if self.itemCount == 6:
            return
        elif item.item not in self.dictionary_items:
            self.dictionary_items[item.item] = 1
            self.itemCount += 1
        elif item.item in self.dictionary_items:
            self.dictionary_items[item.item] += 1

