import pygame
import sys

# Initialize Pygame
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

# Chargement de l'image de fond
background = pygame.image.load("fond.png")
background_x = 0

# Score initial
score = 0

# Fonction pour afficher le score
def afficher_score():
    font = pygame.font.Font(None, 36)  # Police et taille du texte
    texte_score = font.render("Score : {}".format(score), True, WHITE)
    text_rect = texte_score.get_rect(center=(WINDOWWIDTH // 2, 20))
    windowsurface.blit(texte_score, (10, 10))  # Position du texte à l'écran

# Afficher Trump
Trump = pygame.image.load("trump.png")
Trump = pygame.transform.scale(Trump, (200, 150))
trump_rect = Trump.get_rect()
trump_rect.topright = (WINDOWWIDTH - 50, 10)

# Afficher Greta
Greta = pygame.image.load("Greta.png")
Greta = pygame.transform.scale(Greta, (200, 200))
greta_rect = Greta.get_rect()
greta_rect.center = (70, 20)
# Variables du saut
jumping = False
jump_count = 10
# Gravité
gravity = 1

# Boucle principale
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # running
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True

    # Défilement de l'image de fond
    background_x -= 1
    if background_x < -background.get_width():
        background_x = 0

    # Effacer l'écran
    windowsurface.fill(BLACK)

    # Dessiner nl'image de fond
    windowsurface.blit(background, (background_x, 0))
    windowsurface.blit(background, (background_x + background.get_width(), 0))

    # Gestion du saut
    if jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            greta_rect.y -= (jump_count**2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 10

    # Appliquer la gravité
    if greta_rect.y < WINDOWHEIGHT - 170:
        greta_rect.y += gravity
    else:
        greta_rect.y = WINDOWHEIGHT - 170

    # Afficher Trump
    windowsurface.blit(Trump, trump_rect)

    # Afficher Greta
    windowsurface.blit(Greta, greta_rect)

    # Afficher le score
    afficher_score()

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Réguler la vitesse de la boucle
    clock.tick(FPS)

def set_difficulty(
):  # function to progressively increase the speed of the background movement
  global score
  global background_speed
  speed_modification = score // 3
  background_speed = 3 + speed_modification

pygame.mouse.set_visible(False)

pygame.quit()
sys.exit()
