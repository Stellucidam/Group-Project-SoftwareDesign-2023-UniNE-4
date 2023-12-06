import pygame
import sys
import random
from PIL import Image, ImageDraw

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BROWN = (165, 42, 42)

# Format de la fenêtre
WINDOWWIDTH = 744
WINDOWHEIGHT = 420
FPS = 30
windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Run Greta, RUN")

# Constantes
SCORE = 0
BACKGROUND_SPEED = 1
POINTS_PER_LEVEL = 10
BASE_SPEED = 3
MISS_SPEED = 10
MISS_LONGUEUR = 100
MISS_HAUTEUR = 40
JUMP_SIZE = 10 
GRAVITY = 5
UP_DISTRIBUTION = -50
DOWN_DISTRIBUTION = 100

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

# Chargement de l'image de fond
background = pygame.image.load("fond.png")
background_x = 0


#Accélérer l'image
def set_difficulty():
  global SCORE
  global BACKGROUND_SPEED
  global MISS_SPEED
  speed_modification = SCORE // POINTS_PER_LEVEL  #augmente de 1 tous les 5 scores
  if BACKGROUND_SPEED < 10:
    BACKGROUND_SPEED = BASE_SPEED + speed_modification
  if MISS_SPEED < 20:
    MISS_SPEED += speed_modification


# Fonction pour afficher le score
def afficher_score():
  font = pygame.font.Font(None, 36)  # Police et taille du texte
  #
  #
  #afficher texte difficulté pour que ça s'affiche dessous
  texte_score = font.render(
    "Score : {}, Difficulté: {}".format(int(SCORE),
                                        int(BACKGROUND_SPEED - BASE_SPEED)),
    True, WHITE)
  text_rect = texte_score.get_rect(center=(WINDOWWIDTH // 2, 20))
  windowsurface.blit(texte_score, (10, 10))  # Position du texte à l'écran


# Comportement des missiles
def miss_behavior():

  miss_rect.move_ip(-MISS_SPEED, 0)  #rectangle du missile bouge avec la constante speed


#Afficher Missiles
Miss1 = pygame.image.load("missile1.png")
Miss1 = pygame.transform.scale(Miss1, (MISS_LONGUEUR, MISS_HAUTEUR))
Miss2 = pygame.image.load("missile2.png")
Miss2 = pygame.transform.scale(Miss2, (MISS_LONGUEUR, MISS_HAUTEUR))
Miss3 = pygame.image.load("missile3.png")
Miss3 = pygame.transform.scale(Miss3, (MISS_LONGUEUR, MISS_HAUTEUR))
Miss4 = pygame.image.load("missile4.png")
Miss4 = pygame.transform.scale(Miss4, (MISS_LONGUEUR, MISS_HAUTEUR))
missiles = [Miss1, Miss2, Miss3, Miss4]
miss = random.choice(missiles)
miss_rect = miss.get_rect()  #choix d'un missile random dans la liste de 1 à 4

#Initialiser la position du missile comme çA on sait de quoi on parle
miss_rect.x = WINDOWWIDTH
miss_rect.y = random.randint(0, WINDOWHEIGHT - MISS_HAUTEUR)

# Afficher Trump
Trump = pygame.image.load("trump.png")
Trump = pygame.transform.scale(Trump, (133, 100))
trump_rect = Trump.get_rect()
trump_rect.topright = (WINDOWWIDTH - 40, 10)

#Afficher Greta
Greta = pygame.image.load("Greta.png")
Greta = pygame.transform.scale(Greta, (200, 200))
greta_rect = Greta.get_rect()
greta_rect.center = (80, 350)
greta_surface = pygame.Surface((120, 120))
greta_surface_rect = greta_surface.get_rect()
greta_surface_rect.center = (200,350)
pygame.draw.rect(greta_surface, (0, 255, 0), greta_surface.get_rect(), 10) # à suppr

# Variables du saut
jumping = False
jump_count = JUMP_SIZE
double_jump_available = True

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
        if not jumping:
          jumping = True
        elif double_jump_available:
          double_jump_available = False
          jump_count = JUMP_SIZE

  # Défilement de l'image de fond
  background_x -= BACKGROUND_SPEED
  if background_x < -background.get_width():
    background_x = 0

  #Effacer l'écran
  windowsurface.fill(BLACK)

  # Dessiner l'image de fond
  windowsurface.blit(background, (background_x, 0))
  windowsurface.blit(background, (background_x + background.get_width(), 0))

  # Gestion du saut
  if jumping:
    if jump_count >= JUMP_SIZE * -1:
      neg = 1
      if jump_count < 0:
        neg = -1
      greta_rect.y -= (jump_count**2) * 0.5 * neg
      jump_count -= 1
    else:
      jumping = False
      jump_count = JUMP_SIZE

  # Appliquer la gravité
  if greta_rect.y < WINDOWHEIGHT - 170:
    greta_rect.y += GRAVITY
  else:
    greta_rect.y = WINDOWHEIGHT - 170
    double_jump_available = True  # Reset double jump availability

  ## Collision et mort de Greta
  #if miss_rect.colliderect(greta_rect):
    #pygame.quit()

  #Afficher Trump
  windowsurface.blit(Trump, trump_rect)

  #Afficher Greta
  windowsurface.blit(greta_surface, greta_rect)# à suppr
  windowsurface.blit(Greta, greta_rect)
  #Afficher missiles
  miss_behavior()
  if miss_rect.right < 0:
    miss_rect.x = WINDOWWIDTH
    miss_rect.y = greta_rect.y + random.randint(UP_DISTRIBUTION, DOWN_DISTRIBUTION)
    miss = random.choice(missiles)
  windowsurface.blit(miss, miss_rect)

  #test augmenter SCORE
  SCORE += 1 / FPS
  set_difficulty()

  # Afficher le score
  afficher_score()

  # Mettre à jour l'affichage
  pygame.display.flip()

  # Réguler la vitesse de la boucle
  clock.tick(FPS)

#
pygame.mouse.set_visible(False)

pygame.quit()
sys.exit()
