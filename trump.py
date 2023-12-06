from constants import PATH

class Trump:
    def __init__(self, pygame, image_name, width, height, x_pos, y_pos):
        self.image_name = image_name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
    
        trump_image = pygame.image.load(PATH + self.image_name)
        trump_image = pygame.transform.scale(trump_image, (self.width, self.height))
        trump_rect = trump_image.get_rect()
        trump_rect.topright = (self.x_pos, self.y_pos)

        self.image = trump_image
        self.rect = trump_rect
