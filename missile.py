# Thoses classes are used to create and manipulate the missile-related objects. They are the elements that put the player (aka Greta) in danger.
import random
from super_element import SuperElement
from constants import DOWN_DISTRIBUTION, MISSILE_FILE_NAMES, MISS_WIDTH, MISS_HEIGHT, UP_DISTRIBUTION, WINDOWHEIGHT, WINDOWWIDTH

# We call our superclass SuperElement to define a missile
class Missile(SuperElement):
  def __init__(self, pygame, image_name, width, height, x_pos, y_pos):
    super().__init__(pygame, image_name, width, height, x_pos, y_pos)

  # Get the collision rectangle
  def get_collision_rect(self, pygame):
    return pygame.Rect(
      self.rect.x,
      self.rect.y + MISS_HEIGHT / 2,
      MISS_WIDTH / 1.5, MISS_HEIGHT / 5)
    
# We define the missiles class in order to have the all the predefined missiles
class Missiles:
  def __init__(self, pygame):
    self.missiles = []
    for filename in MISSILE_FILE_NAMES:
      missile = Missile(pygame, filename, MISS_WIDTH, MISS_HEIGHT, WINDOWHEIGHT, random.randint(0, WINDOWHEIGHT - MISS_HEIGHT))
    self.missiles.append(missile)

  def get_random_missile(self, random): 
    return random.choice(self.missiles)

  # Define a movement so the missiles come from right to left (-speed) and don't change their height (0).
  def move(self, current_missile, missile_speed, greta_y, random):
    current_missile.rect.move_ip(-missile_speed, 0)
    if current_missile.rect.right < 0:
      current_missile.rect.x = WINDOWWIDTH
      current_missile.rect.y = greta_y + random.randint(
        UP_DISTRIBUTION, DOWN_DISTRIBUTION)
      
      # At the beginning the missile's spawn height was full random which means that it rarely came close to greta. We found a way to make it more accurate.
      current_missile = self.get_random_missile(random)