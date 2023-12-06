import pygame
import sys
import random
from PIL import Image, ImageDraw
from constants import *
from missile import *
from state import *
from trump import *

# Initialisation de Pygame
pygame.init()
windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Run Greta, RUN")

######################
#accueil

## Charger l'image de fond
#fond = pygame.image.load("fond.png")
#fond = pygame.transform.scale(fond, (largeur, hauteur))

## Charger l'image du bouton "Start"
#bouton_start = pygame.image.load("chemin/vers/votre/bouton_start.png")
#bouton_start_rect = bouton_start.get_rect()
#bouton_start_rect.x = (largeur - bouton_start_rect.width) // 2
#bouton_start_rect.y = hauteur // 2

## Boucle principale de la page d'accueil
#while True:
#for event in pygame.event.get():
#if event.type == pygame.QUIT:
#pygame.quit()
#sys.exit()
#elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
## Vérifier si le bouton "Start" a été cliqué
#if bouton_start_rect.collidepoint(event.pos):
## Lancer le jeu ici (remplacez cela par le code de votre jeu)
#print("Le jeu est lancé !")

# Afficher l'image de fond
#fenetre.blit(fond, (0, 0))

# Afficher le bouton "Start"
#fenetre.blit(bouton_start, bouton_start_rect.topleft)

# Mettre à jour l'affichage
#pygame.display.flip()
##########################################

# Etat initial
state = State(0, 0, BACKGROUND_SPEED, MISS_SPEED, False, True, JUMP_SIZE)

# Chargement de l'image de fond
background = pygame.image.load(PATH + "fond.png")
background_x = 0

missiles = Missiles(pygame)
miss = missiles.get_random_missile(random).image
miss_rect = miss.get_rect()

#Initialiser la position du missile comme çA on sait de quoi on parle
miss_rect.x = WINDOWWIDTH
miss_rect.y = random.randint(0, WINDOWHEIGHT - MISS_HAUTEUR)

# Afficher Trump
trump = Trump(pygame, "trump.png", 133, 100, WINDOWWIDTH - 40, 10)

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

# Boucle principale
clock = pygame.time.Clock()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    #running
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        if not state.jumping:
          state.set_jumping(True)
        elif state.double_jump_available:
          state.set_double_jump_available(False)
          state.set_jump_count(JUMP_SIZE)

  # Défilement de l'image de fond
  background_x -= state.background_speed
  if background_x < -background.get_width():
    background_x = 0

  #Effacer l'écran
  windowsurface.fill(BLACK)

  # Dessiner l'image de fond
  windowsurface.blit(background, (background_x, 0))
  windowsurface.blit(background, (background_x + background.get_width(), 0))

  # Gestion du saut
  if state.jumping:
    if state.jump_count >= JUMP_SIZE * -1:
      neg = 1
      if state.jump_count < 0:
        neg = -1
      greta_rect.y -= (state.jump_count**2) * 0.5 * neg
      state.set_jump_count(state.jump_count - 1)
    else:
      state.set_jumping(False)
      state.set_jump_count(JUMP_SIZE)

  # Appliquer la gravité
  if greta_rect.y < WINDOWHEIGHT - 170:
    greta_rect.y += GRAVITY
  else:
    greta_rect.y = WINDOWHEIGHT - 170
    state.set_double_jump_available(True) # Reset double jump availability

  ## Collision et mort de Greta
  if miss_rect.colliderect(greta_hitbox):
    pygame.quit()
    sys.exit() # évite une erreur de type "pygame.error: display Surface quit"

  #Afficher Trump
  windowsurface.blit(trump.image, trump.rect)

  #Afficher Greta
  windowsurface.blit(greta_surface, greta_hitbox, greta_rect)# à suppr
  windowsurface.blit(Greta, greta_rect)
  #Afficher missiles
  miss_rect.move_ip(-state.missile_speed, 0)  #rectangle du missile bouge avec la constante speed
  if miss_rect.right < 0:
    miss_rect.x = WINDOWWIDTH
    miss_rect.y = greta_rect.y + random.randint(UP_DISTRIBUTION, DOWN_DISTRIBUTION)
    miss = missiles.get_random_missile(random).image
  windowsurface.blit(miss, miss_rect)
  
  #test augmenter SCORE
  # SCORE += 1 / FPS
  state.add_score(1 / FPS)
  state.set_difficulty()
  state.add_step()

  # Afficher le score
  state.print_state(pygame, windowsurface)

  # Mettre à jour l'affichage
  pygame.display.flip()

  # Réguler la vitesse de la boucle
  clock.tick(FPS)

#
pygame.mouse.set_visible(False)

pygame.quit()
sys.exit()
