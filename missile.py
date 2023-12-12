from constants import MISSILE_FILE_NAMES, MISSILE_HEIGHT, MISSILE_WIDTH
from super_element import SuperElement

class Missile(SuperElement):
    def __init__(self, pygame, image_name, width, height):
        super().__init__(pygame, image_name, width, height)

class Missiles:
    def __init__(self, pygame):
        self.missiles = []
        for filename in MISSILE_FILE_NAMES:
            missile = Missile(pygame, filename, MISSILE_WIDTH, MISSILE_HEIGHT)
            self.missiles.append(missile)

    def get_missiles(self):
        return self.missiles
    
    def get_random_missile(self, random):
        return random.choice(self.missiles)
