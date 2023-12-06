from constants import *

class Missile:
    def __init__(self, pygame, image_name, width, height):
        self.image_name = image_name
        self.width = width
        self.height = height
        missile_image = pygame.image.load(PATH + self.image_name)
        missile_image = pygame.transform.scale(missile_image, (self.width, self.height))
        self.image = missile_image

class Missiles:
    def __init__(self, pygame):
        self.missiles = []
        for filename in MISSILE_FILE_NAMES:
            missile = Missile(pygame, filename, MISS_LONGUEUR, MISS_HAUTEUR)
            # self.missiles.append(missile.get_image(pygame))
            # self.images.append(missile.get_image(pygame))
            self.missiles.append(missile)

    def get_missiles(self):
        return self.missiles
    
    def get_random_missile(self, random):
        return random.choice(self.missiles)
