
# ...

# Chargement de l'image de fond
background = pygame.image.load("fond.png")
background_x = 0

if background.get_width() > WINDOWWIDTH:
    print("L'image de fond est plus large que la fenêtre !")
