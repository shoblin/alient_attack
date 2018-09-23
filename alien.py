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

class Alien(Sprite):
    """A Class of our enemies """

    def __init__(self, ai_settings, screen):
        super.__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the alien image and set its rect attribute.
        self.image = pygame.image.load('img/alien.bmp')
        self.rect = self.image.get_rect()

        #Create new alient in position near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)


