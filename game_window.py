from constants import PATH, WINDOWHEIGHT, WINDOWWIDTH


# Manage the game display
class GameWindow:

  # Initialization of Pygame and the game display
  def __init__(self, pygame, game_title):
    self.pygame = pygame
    self.pygame.display.set_caption(game_title)
    self.game_title = game_title
    self.window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    game_background = pygame.image.load(PATH + "fond.png")
    self.game_background = pygame.transform.scale(game_background,
                                                  (WINDOWWIDTH, WINDOWHEIGHT))

    self.game_background_x = 0

    home_background = pygame.image.load(PATH + "fond_acc.png")
    self.home_background = pygame.transform.scale(home_background,
                                                  (WINDOWWIDTH, WINDOWHEIGHT))

  # Draw the background image for the home page
  def draw_home_background(self):
    self.window_surface.blit(self.home_background, (0, 0))

    # Create the start button
    start_button = self.pygame.image.load(PATH + "bouton_start.png")
    start_button = self.pygame.transform.scale(start_button,
                                               (474 / 2, 158 / 2))
    start_button_rect = start_button.get_rect()

    # Create the exit button
    exit_button = self.pygame.image.load(PATH + "exit.png")
    exit_button = self.pygame.transform.scale(exit_button, (340 / 2, 130 / 2))
    exit_button_rect = exit_button.get_rect()

    # Center the start button and the exit button
    start_button_rect.center = (self.window_surface.get_width() / 2,
                                self.window_surface.get_height() / 2)
    exit_button_rect.center = (self.window_surface.get_width() / 2,
                               (self.window_surface.get_height() / 2) + 100)

    # On the playing surface, copy the start image and the start rectangle. The 0,0 point of the start image (top left) is at the top left corner of the rectangle.
    self.window_surface.blit(start_button, start_button_rect.topleft)
    self.window_surface.blit(exit_button, exit_button_rect.topleft)

    # Return the rectangles for the start and exit buttons to call them up in the main code
    return start_button_rect, exit_button_rect

  # Draw the background image for the main game
  def draw_game_background(self):
    self.window_surface.blit(self.game_background, (0, 0))
    self.window_surface.blit(self.game_background,
                             (self.game_background.get_width(), 0))
