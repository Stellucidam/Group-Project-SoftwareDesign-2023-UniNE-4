# Aljabar is our smart enemy. His job is to be launched far less often than the other missiles. He'll follow Greta very precisely for a certain distance then stay in a straight line. If we decided to make him follow Greta as long as possible it wouldn't be possible to survive.

from super_element import SuperElement
from constants import AL_JABER_HEIGHT, AL_JABER_WIDTH, LIMITE_ENNEMI, WINDOWWIDTH


class AlJaber(SuperElement):

  def __init__(self, pygame, greta_y_pos):
    super().__init__(pygame, "al_jaber.png", AL_JABER_WIDTH, AL_JABER_HEIGHT,
                     WINDOWWIDTH, greta_y_pos)

  # AlJaber moves from right to left (-speed) and moves according to Greta on the y axis (greta_y_pos)
  def behaviour(self, speed, greta_y_pos):
    self.rect.move_ip(-speed, 0)

    # If AlJaber is above the LIMITE_ENNEMI distance, it follows the y position of greta
    if self.rect.x > LIMITE_ENNEMI:
      self.rect.y = greta_y_pos

    return self.rect.x <= -AL_JABER_WIDTH

  # Define a collision rectangle so it's a bit smaller than AlJaber
  def get_collision_rect(self, pygame):
    return pygame.Rect(
      self.rect.x + 10,
      self.rect.y + 10,
      AL_JABER_WIDTH - 20,
      AL_JABER_HEIGHT - 20)