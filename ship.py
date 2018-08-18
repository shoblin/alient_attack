#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shoblin
#
# Created:     16.08.2018
# Copyright:   (c) Shoblin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame

class Ship():
    """
        Initializa the ship and its starting position
    """

    def __init__(self, ai_settings, screen):
        #  Initialize the ship and set its starting position and parameters
        self.screen =  screen
        self.ai_settings = ai_settings

        # Load sip image and set its starting position
        self.image = pygame.image.load('img/ship2.bmp')

        # Put our image into rect(object) - rectangel.
        # rect have x- & y-coordinates: top, bottom, right and left edges of the image
        # We can set any of this values to determine  the current position of  the rect
        self.rect = self.image.get_rect()   # Create rect object for image
        self.screen_rect = screen.get_rect() # Store the screen’s rect in self.screen_rec

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx # Make value of x-coordinate of Ship match the x-coofdinate of screen center
        self.rect.bottom  = self.screen_rect.bottom  # Set Y - coodinate for bottom edge of the ship

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left  = False

    def update(self):
        """Update the ship's position based on the movement flag."""

        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

