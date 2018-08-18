#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      atopolskiy
#
# Created:     18.08.2018
# Copyright:   (c) atopolskiy 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen

        # Create a bullet andset correct  position
        self.image = pygame.image.load(ai_settings.bullet_img)
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a dicimal value
        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ Move the bullet up the screen"""
        # Update the decimal position
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        self.screen.blit(self.image, self.rect)



