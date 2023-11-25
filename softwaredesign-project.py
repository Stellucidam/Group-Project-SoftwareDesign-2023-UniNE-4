import pygame
import random
from PIL import Image, ImageDraw

WHITE = (255, 255, 255)
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
FPS = 60

windowsurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Run Greta, RUN")
score = 0

def afficher_score():
    print("Score actuel :", score)

pygame.init()
pygame.mouse.set_visible(False)

Trump = Image.open("trump.png")
cadre_x = 500
cadre_y = 300
cadre_largeur = 100
cadre_hauteur = 100
draw = ImageDraw.Draw(Trump)
draw.rectangle((cadre_x, cadre_y, cadre_x + cadre_largeur, cadre_y + cadre_hauteur), outline="red", width=0)
Trump.show()

background = pygame.image.load("fond.png")
clock = pygame.time.Clock()
background_x = 0
running = True

class Player:
    def __init__(self):
        self.image = pygame.image.load("Greta.png")
        self.rect = self.image.get_rect()

    def movement(self, position):
        self.rect.centerx = position[0]
        self.rect.centery = position[1]

class Enemy:
    def __init__(self):
        self.dead = False
        self.image = random.choice([missile1, missile2, bomb])  # Assuming missile1, missile2, and bomb are defined
        self.rect = self.image.get_rect()
        self.speed = [random.uniform(-3, 3), 2]

    def enemy_behaviour(self):
        self.rect.move_ip(self.speed)
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.left < 0 or self.rect.right > WINDOWWIDTH:
            self.speed[0] = -self.speed[0]
        elif self.rect.bottom > WINDOWHEIGHT - player.rect.height:  # Adjusted to use player.rect.height
            self.dead = True

player = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Défilement de l'image de fond
    background_x -= 1
    windowsurface.blit(background, (background_x, 0))
    windowsurface.blit(background, (background_x + background.get_width(), 0))
    pygame.display.update()
    clock.tick(60)  # Changed to a more reasonable value
pygame.quit()
