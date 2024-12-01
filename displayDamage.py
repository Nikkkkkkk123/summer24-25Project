import pygame

# This class will be the visual representation of the damage 
# that the player does to the enemy

class displayDamage(pygame.sprite.Sprite):
    def __init__(self, x, y, damage,color=(255,0,0),duration=100):
        super().__init__()
        self.damage = damage # The damage that the player does to the enemy
        self.font = pygame.font.Font(None, 36) # Font for the damage
        self.image = self.font.render(str(self.damage), True, color) # The image of the damage
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.time = pygame.time.get_ticks()
        self.duration = duration

    def update(self):
        if pygame.time.get_ticks() - self.time > self.duration:
            self.kill()
        else:
            self.rect.y -= 1 # Move text upwards
            self.image.set_alpha(self.image.get_alpha() - 1,0) #fades out text
            