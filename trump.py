from constants import MARGIN, TRUMP_HEIGHT, TRUMP_WIDTH, WINDOWWIDTH
from super_element import SuperElement


class Trump(SuperElement):
  def __init__(self, pygame):
    super().__init__( pygame, "trump.png", TRUMP_WIDTH, TRUMP_HEIGHT,
              WINDOWWIDTH - TRUMP_WIDTH - MARGIN, MARGIN)
    