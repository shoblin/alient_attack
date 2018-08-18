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

class Settings():
    """
        Class where I save all main settings for Game
    """

    def __init__(self):
        """
            Initialize The game's settings
        """
        # Window settings
        self.caption = "Aliens Attack"

        # Screen settings
        self.width = 1200
        self.height = 800
        self.bg_color = (130, 130, 230)

        # Ship Settings
        self.ship_speed_factor =1.5



