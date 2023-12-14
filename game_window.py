from constants import PATH, WINDOWHEIGHT, WINDOWWIDTH


class GameWindow:  # Gère l'affichage du jeu
  # Initialisation de Pygame et de la fenêtre de jeu
  def __init__(
    self, pygame, game_title
  ):  # __init__ définit un objet avec les attributs donnés dans la class
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

  # Dessiner l'image de fond de la page d'accueil
  def draw_home_background(self):
    self.window_surface.blit(
      self.home_background, (0, 0)
    )  # Sur la surface du jeu on copie la surface accueil par dessus (blit)

    # Créer le bouton de démarrage
    start_button = self.pygame.image.load(PATH + "bouton_start.png")
    start_button = self.pygame.transform.scale(start_button, (474/2, 158/2))
    start_button_rect = start_button.get_rect()

    # Créer le bouton de sortie
    exit_button = self.pygame.image.load(PATH + "exit.png")
    exit_button = self.pygame.transform.scale(exit_button, (340/2, 130/2))
    exit_button_rect = exit_button.get_rect()

    # Centrer le bouton de démarrage et le bouton de sortie
    start_button_rect.center = (self.window_surface.get_width() / 2,
                                self.window_surface.get_height() / 2)
    exit_button_rect.center = (self.window_surface.get_width() / 2,
                               (self.window_surface.get_height() / 2) + 100)

    # Afficher le bouton de démarrage et le bouton de sortie
    self.window_surface.blit(
      start_button, start_button_rect.topleft
    )  # Sur la surface de jeu, copier l'image start et le rectangle de start. Le point 0,0 de l'image start (en haut à gauche) se trouve au coint en haut à gauche du rectangle
    self.window_surface.blit(exit_button, exit_button_rect.topleft)

    # Retourner les rectangles des boutons de démarrage et de sortie afin de les appeler sur le code principal
    return start_button_rect, exit_button_rect

  # Dessiner l'image de fond du jeu principal
  def draw_game_background(self):
    self.window_surface.blit(self.game_background, (0, 0))
    self.window_surface.blit(
      self.game_background,
      (self.game_background.get_width(),
       0))  # Permet de copier à côté pour permettre la boucle à l'infini
