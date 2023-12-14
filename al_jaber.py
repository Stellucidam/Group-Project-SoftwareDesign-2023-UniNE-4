from super_element import SuperElement
from constants import AL_JABER_HEIGHT, AL_JABER_WIDTH, WINDOWHEIGHT, LIMITE_ENNEMI

class AlJaber(SuperElement):

  def __init__(self, pygame, greta_y_pos):
    super().__init__(pygame, "al_jaber.png", AL_JABER_WIDTH, AL_JABER_HEIGHT, WINDOWHEIGHT, greta_y_pos)

  def behaviour(self, greta_y_pos, speed):
    self.rect.move_ip(-speed, 0)
    
    if self.x_pos < LIMITE_ENNEMI:
      self.y_pos = greta_y_pos
      
    print(self.x_pos, self.y_pos, speed)
    return self.x_pos == 0