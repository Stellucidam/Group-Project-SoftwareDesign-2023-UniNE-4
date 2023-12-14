from state import State
from constants import GRAVITY, GRETA_HEIGHT, GRETA_WIDTH, MARGIN, WINDOWHEIGHT
from super_element import SuperElement


class Greta(SuperElement):
  def __init__(self, pygame):
    SuperElement.__init__(self, pygame, "greta.png", GRETA_WIDTH, GRETA_HEIGHT, MARGIN,
              WINDOWHEIGHT + MARGIN + GRETA_HEIGHT)

  def get_surface(self, pygame):
    return pygame.Surface((120, 120), pygame.SRCALPHA)
  
  def apply_gravity(self, state: State):
    # Appliquer la gravité
    if self.rect.y < WINDOWHEIGHT - GRETA_HEIGHT - MARGIN:
      self.rect.y += GRAVITY
    else:
      self.rect.y = WINDOWHEIGHT - GRETA_HEIGHT - MARGIN
      state.set_double_jump_available(True)  # Reset double jump availability

  def get_collision_rect(self, pygame):
    return pygame.Rect(
      self.rect.x + GRETA_WIDTH / 4,
      self.rect.y,
      GRETA_WIDTH / 4, GRETA_HEIGHT / 2)