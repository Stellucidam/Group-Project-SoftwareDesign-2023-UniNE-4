# The superclass, SuperElement is here to define all the elements we have to use for the sub-class element such as Trump, Greta, Missile and AlJabar

from constants import PATH


class SuperElement:
  
  def __init__(self, pygame, image_name, width, height, x_pos, y_pos):
    self.image_name = image_name
    self.width = width
    self.height = height
    self.x_pos = x_pos
    self.y_pos = y_pos

    image = pygame.image.load(PATH + self.image_name)
    image = pygame.transform.scale(image, (self.width, self.height))

    self.image = image
    self.rect = image.get_rect()
    self.rect.x = self.x_pos
    self.rect.y = self.y_pos