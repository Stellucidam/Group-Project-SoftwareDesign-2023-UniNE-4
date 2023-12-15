# Trump only appears in the corner of the game, he doesn't do anything appart from being pretty (or not)

from constants import MARGIN, TRUMP_HEIGHT, TRUMP_WIDTH, WINDOWWIDTH
from super_element import SuperElement

# We call our superclass SuperElement to define Trump
class Trump(SuperElement):
  def __init__(self, pygame):
    super().__init__( pygame, "trump.png", TRUMP_WIDTH, TRUMP_HEIGHT,
              WINDOWWIDTH - TRUMP_WIDTH - MARGIN, MARGIN)