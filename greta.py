# This is the class that controls and creates Greta. This element is controlled by the player in the game.
from state import State
from constants import GRAVITY, GRETA_HEIGHT, GRETA_WIDTH, MARGIN, WINDOWHEIGHT
from super_element import SuperElement

# We call the superclass SuperElement to define Greta
class Greta(SuperElement):
  def __init__(self, pygame):
    SuperElement.__init__(self, pygame, "greta.png", GRETA_WIDTH, GRETA_HEIGHT, MARGIN,
              WINDOWHEIGHT + MARGIN + GRETA_HEIGHT)

  def get_surface(self, pygame):
    return pygame.Surface((120, 120), pygame.SRCALPHA)

  # Apply gravity to make jump logical
  def apply_gravity(self, state: State):
    if self.rect.y < WINDOWHEIGHT - GRETA_HEIGHT - MARGIN:
      self.rect.y += GRAVITY
    else:
      self.rect.y = WINDOWHEIGHT - GRETA_HEIGHT - MARGIN
      
      # Reset double jump availability
      state.set_double_jump_available(True)

  # Define a collision rectangle so it's smaller than Greta and doesn't take her hair in consideration
  def get_collision_rect(self, pygame):
    return pygame.Rect(
      self.rect.x + GRETA_WIDTH / 4,
      self.rect.y,
      GRETA_WIDTH / 2, GRETA_HEIGHT / 1.5)