import pygame
import sys
import random
from constants import WINDOWWIDTH, WINDOWHEIGHT, BACKGROUND_SPEED, MISS_SPEED, MISS_HEIGHT, JUMP_SIZE, PATH, GRETA_WIDTH, GRETA_HEIGHT, TRUMP_WIDTH, TRUMP_HEIGHT, MARGIN
from game import main_game_loop
from game_window import GameWindow
from missile import Missiles
from al_jaber import AlJaber
from state import State
from trump import Trump
from greta import Greta

def init_state():
  # Initialisation de Pygame
  pygame.init()
  game_window = GameWindow(pygame, "Run Greta, RUN")  # Exécute la partie __init__ de la class GameWindow

  # Etat initial
  state = State(0, BACKGROUND_SPEED, MISS_SPEED, False, True, JUMP_SIZE)
  # Créer missiles
  missiles = Missiles(game_window.pygame)

  # Créer Trump
  trump = Trump(pygame)

  # Créer Greta
  greta = Greta(pygame)

  # Créer AlJabar
  al_jaber = AlJaber(pygame, greta.y_pos)
  return game_window, state, missiles, trump, greta, al_jaber

  
game_window, state, missiles, trump, greta, al_jaber = init_state()

# Boucle principale
while True:
  # Dessiner page d'accueil
  start_button_rect, exit_button_rect = game_window.draw_home_background(
  )  # Appelle: utilise ligne 22 de la class WindowSurface
  game_window.pygame.display.flip()
  start_game = False

  while not start_game:
    mouse_pos = pygame.mouse.get_pos()  # Récupérer position de la souris
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        # Vérifier si le bouton "Start" a été cliqué
        if start_button_rect.collidepoint(
            mouse_pos):  # Collision souris et bouton start
          start_game = True
        # Vérifier si le bouton "Exit" a été cliqué
        elif exit_button_rect.collidepoint(mouse_pos):
          pygame.mouse.set_visible(False)
          pygame.quit()
          sys.exit()
    # Vérifier si le curseur est au-dessus du bouton "Start" ou du bouton "Exit"
    if start_button_rect.collidepoint(
        mouse_pos) or exit_button_rect.collidepoint(mouse_pos):
      pygame.mouse.set_cursor(
        *pygame.cursors.broken_x)  # Change cursor to pointer
    else:
      pygame.mouse.set_cursor(
        *pygame.cursors.arrow)  # Change cursor back to default

# Une fois que le bouton de démarrage a été cliqué, le jeu principal commence
  if start_game:
    start_game = False  # Permet de revenir à la page d'accueil et ne pas boucler à l'infini
    pygame.mouse.set_visible(False)  # Faire diparaître la souris
    main_game_loop(  #mettre en argument ce qu'elle a besoin pour tourner
      game_window, state, missiles, al_jaber, trump, greta, random)
    pygame.mouse.set_visible(True)  # Si le joueur perd, la souris réaparait
    game_window, state, missiles, trump, greta, al_jaber = init_state() # Réinitialiser les variables
