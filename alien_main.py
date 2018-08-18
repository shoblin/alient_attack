#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shoblin
#
# Created:     09.08.2018
# Copyright:   (c) Shoblin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
import game_functions as gf

from pygame.sprite import Group
from settings import Settings
from ship import Ship


def game_run():
    #Initialize game and create sreen objects

    pygame.init()
    ai_settings = Settings()


    screen = pygame.display.set_mode((ai_settings.width, ai_settings.height))
    pygame.display.set_caption(ai_settings.caption)

    #Create a ship
    ship=Ship(ai_settings, screen)
    #Create a group within bullets
    bullets = Group()


    #Start the main loop for the game
    while True:
        #Watch keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()
        gf.update_bullets(bullets)

        # Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship, bullets)


def main():
    game_run()

if __name__ == '__main__':
    main()
