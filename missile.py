import random
from super_element import SuperElement
from constants import DOWN_DISTRIBUTION, MISSILE_FILE_NAMES, MISS_WIDTH, MISS_HEIGHT, UP_DISTRIBUTION, WINDOWHEIGHT, WINDOWWIDTH

class Missile(SuperElement):
  def __init__(self, pygame, image_name, width, height, x_pos, y_pos):
    super().__init__(pygame, image_name, width, height, x_pos, y_pos)

  def get_collision_rect(self, pygame):
    return pygame.Rect(
      self.rect.x,
      self.rect.y + MISS_HEIGHT / 2,
      MISS_WIDTH / 1.5, MISS_HEIGHT / 5)
    

class Missiles:
  def __init__(self, pygame):
    self.missiles = []
    for filename in MISSILE_FILE_NAMES:
      missile = Missile(pygame, filename, MISS_WIDTH, MISS_HEIGHT, WINDOWHEIGHT, random.randint(0, WINDOWHEIGHT - MISS_HEIGHT))
    self.missiles.append(missile)

  def get_random_missile(self, random):
    return random.choice(self.missiles)

  def move(self, current_missile, missile_speed, greta_y, random):
    current_missile.rect.move_ip(-missile_speed, 0)  #rectangle du missile bouge avec la constante speed
    if current_missile.rect.right < 0:
      current_missile.rect.x = WINDOWWIDTH
      current_missile.rect.y = greta_y + random.randint(
        UP_DISTRIBUTION, DOWN_DISTRIBUTION)
      current_missile = self.get_random_missile(random)