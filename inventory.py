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

        # Font for the item count
        font = pygame.font.Font(None, 32)

        for i in range(6):
            pygame.draw.rect(inventory_surface, (255, 255, 255, 200), (itemx_offset, margin, box_size, box_size))
            # If the inventory being held is not empty and not all items are being displayed than draw the item
            if i < self.itemCount:
                # Get the i'th item in the inventory
                itemName, noItem = self.dictionary_value(i)
                # Display it to the screen
                imgLocation = Drop.item_image(itemName)
                dropImage = pygame.image.load(imgLocation) # Get the image location of the item
                dropImage = pygame.transform.scale(dropImage, (box_size, box_size)) # Scales the image to the box size
                inventory_surface.blit(dropImage, (itemx_offset, margin))

                # Render the item count
                item_count_text = font.render(str(noItem), True, (0, 0, 0))  # White color
                inventory_surface.blit(item_count_text, (itemx_offset + box_size - 10, margin + box_size - 20))  # Adjust position as needed

            itemx_offset += box_size + margin
        
        screen.blit(inventory_surface, (x_offset, y_offset))
        pygame.display.flip()

    # Method Name: dictionary_value
    # Description: This method is used to get the value of a dictionary item.
    # Parameter: i
    # Date Created: 3/12/2024
    # Date Modified: 3/12/2024
    def dictionary_value(self, i):
        itemList = list(self.dictionary_items.items())

        # Just basic error handling. Currently if this method is called it should always be in range
        if i < len(itemList):
            print(itemList[i])
            return itemList[i]
        else:
            return None

    # Method Name: add_item
    # Description: This method is used to add an item to the player's inventory.
    # Parameter: item
    # Date Created: 3/12/2024
    # Date Modified: 3/12/2024
    def add_item(self, item: Drop):
        if self.itemCount == 6:
            return
        elif item.item not in self.dictionary_items:
            self.dictionary_items[item.item] = 1
            self.itemCount += 1
        elif item.item in self.dictionary_items:
            self.dictionary_items[item.item] += 1

    # Method Name: use_item
    # Description: This method is used to use an item from the player's inventory.
    # Parameter: item
    # Date Created: 3/12/2024
    # Date Modified: 3/12/2024
    def use_item(self, item):
        if item in self.dictionary_items:
            self.dictionary_items[item] -= 1
            if self.dictionary_items[item] == 0:
                del self.dictionary_items[item]
                self.itemCount -= 1

