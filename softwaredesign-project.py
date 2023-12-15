# We planned to make a game that comes from Jetpack Joyride. We wanted to make it funnier so we came up with the Trump-Greta rivality. Like in JJ we only have one life so we made Greta small. Because replit sometimes has a hard time figuring out heavy code we decided to be permissive with Greta hait for example to avoid the frustrating effect of "It lagged and then touch my hair and I lost".
# In the code structure it seems easier to split as much as needed. That's why we have all these files (constants.py, greta.py, etc.). We just import them in softwaredesign-project.py.
# We also have a friend who's use to code and she helped us a lot. Her name is Clarisse. When her name is mentioned is because she helped us on the line.

import pygame
import sys
import random
from constants import BACKGROUND_SPEED, MISS_SPEED, JUMP_SIZE
from game import main_game_loop
from game_window import GameWindow
from missile import Missiles
from al_jaber import AlJaber
from state import State
from trump import Trump
from greta import Greta


def init_state():
  # Initializing Pygame
  pygame.init()
  game_window = GameWindow(pygame, "Run Greta, RUN")

  # Initial state
  state = State(0, BACKGROUND_SPEED, MISS_SPEED, False, True, JUMP_SIZE)
  # Create missiles
  missiles = Missiles(game_window.pygame)

  # Create Trump
  trump = Trump(pygame)

  # Create Greta
  greta = Greta(pygame)

  # Create AlJabar
  al_jaber = AlJaber(pygame, greta.y_pos)
  
  state.init_music(game_window.pygame, "OST.mp3")

  return game_window, state, missiles, trump, greta, al_jaber


game_window, state, missiles, trump, greta, al_jaber = init_state()

# Main loop
while True:

  # Draw home page
  start_button_rect, exit_button_rect = game_window.draw_home_background()

  # Refresh the display
  game_window.pygame.display.flip()
  start_game = False

  # On the home screen, we check whether the player clicks on the "Strat" button = start the game, or on the "Exit" button = quit the game.
  while not start_game:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if start_button_rect.collidepoint(mouse_pos):
          start_game = True
        elif exit_button_rect.collidepoint(mouse_pos):
          pygame.mouse.set_visible(False)
          pygame.quit()
          sys.exit()

    # If the mouse is on a useful button it becomes a cross to show the user it can be clicked
    if start_button_rect.collidepoint(
        mouse_pos) or exit_button_rect.collidepoint(mouse_pos):
      pygame.mouse.set_cursor(*pygame.cursors.broken_x)
    else:
      pygame.mouse.set_cursor(*pygame.cursors.arrow)
      
  # When the start button is clicked, the game starts
  if start_game:
    state.play_music(game_window.pygame)
    
    # Clarisse advised us to make sure that the game doesn't go round and round.
    start_game = False
    
    # Hide the mouse when the game starts
    pygame.mouse.set_visible(False)
    main_game_loop(game_window, state, missiles, trump, greta, al_jaber,
                   random)
    state.stop_music(game_window.pygame)

    # Make the mouse visible again when the player loses
    pygame.mouse.set_visible(True)

    # Reset variables to initial state
    game_window, state, missiles, trump, greta, al_jaber = init_state()
