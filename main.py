import pygame
import sys
import random
from constants import MARGIN, WINDOWWIDTH, WINDOWHEIGHT, BACKGROUND_SPEED, MISS_SPEED, MISSILE_HEIGHT, JUMP_SIZE, PATH
from game import main_game_loop
from game_window import GameWindow
from missile import Missiles
from state import State
from trump import Trump

# Initialisation de Pygame
pygame.init()
game_window = GameWindow(pygame, "Run Greta, RUN")

# Etat initial
state = State(0, BACKGROUND_SPEED, MISS_SPEED, False, True, JUMP_SIZE)

missiles = Missiles(game_window.pygame)
miss = missiles.get_random_missile(random).image
miss_rect = miss.get_rect()

#Initialiser la position du missile comme çA on sait de quoi on parle
miss_rect.x = WINDOWWIDTH
miss_rect.y = random.randint(0, WINDOWHEIGHT - MISSILE_HEIGHT)

# Afficher Trump
trump = Trump(pygame, "trump.png", Trump.default_width, Trump.default_height, WINDOWWIDTH - Trump.default_width - MARGIN, MARGIN)

#Afficher Greta
Greta = pygame.image.load(PATH + "Greta.png")
Greta = pygame.transform.scale(Greta, (200, 200))
greta_rect = Greta.get_rect()
greta_rect.center = (80, 350)
greta_surface = pygame.Surface((120, 120), pygame.SRCALPHA)
# greta_surface.fill(BLACK) # à suppr : montre qu'il y a un souci au moment du saut ^^
greta_hitbox = greta_surface.get_rect()
greta_hitbox.center = greta_rect.center
#pygame.draw.rect(greta_hitbox, (0, 255, 0), greta_hitbox.get_rect(), 10) # à suppr

##Afficher explosion #nouveau
#explosion = pygame.image.load(PATH + "explosion.gif")
#explosion = pygame.transform.scale(explosion, (100, 100))
#explosion_rect = explosion.get_rect()
#explosion_rect.center = greta_rect.center

# Boucle principale
while True:
  # Dessiner l'image de fond
  start_button_rect, exit_button_rect = game_window.draw_home_background()
  game_window.pygame.display.flip()
  start_game = False

  while not start_game:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        # Vérifier si le bouton "Start" a été cliqué
        if start_button_rect.collidepoint(mouse_pos):
          start_game = True
        # Vérifier si le bouton "Exit" a été cliqué
        elif exit_button_rect.collidepoint(mouse_pos):
          pygame.mouse.set_visible(False)
          pygame.quit()
          sys.exit()
    # Vérifier si le curseur est au-dessus du bouton "Start" ou du bouton "Exit"
    if start_button_rect.collidepoint(mouse_pos) or exit_button_rect.collidepoint(mouse_pos):
      pygame.mouse.set_cursor(*pygame.cursors.broken_x)  # Change cursor to pointer
    else:
      pygame.mouse.set_cursor(*pygame.cursors.arrow)  # Change cursor back to default

  # Une fois que le bouton de démarrage a été cliqué, le jeu principal commence
  if start_game:
    start_game = False
    pygame.mouse.set_visible(False)
    main_game_loop(
      game_window,
      state,
      missiles,
      trump,
      greta_rect,
      greta_hitbox,
      greta_surface,
      Greta, miss, miss_rect, random)
    pygame.mouse.set_visible(True)


####
#
#ennemi intelligent Al Jabar
#AlJabar_rect
#def AlJabar...
#if difficulté % 3 == 0:
#if AlJabar_rect.right < WINDOWWIDTH - 30:
#AlJabar_rect.x = WINDOWWIDTH
#AlJabar_rect.y = greta_rect.y
#else:
#AlJabar_rect.y = AlJabar_rect.y

