from constants import PATH

class SuperElement:
    def __init__(self, pygame, image_name, width, height):
        self.image_name = image_name
        self.width = width
        self.height = height
    
        image = pygame.image.load(PATH + self.image_name)
        image = pygame.transform.scale(image, (self.width, self.height))

        self.image = image
        self.image_rect = self.image.get_rect()
