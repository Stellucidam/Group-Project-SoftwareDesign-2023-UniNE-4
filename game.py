from game_window import GameWindow
from state import State
from constants import BLACK, DOWN_DISTRIBUTION, FPS, GRAVITY, JUMP_SIZE, UP_DISTRIBUTION, WINDOWHEIGHT, WINDOWWIDTH


def main_game_loop(game_window: GameWindow, state: State, missiles, trump, greta_rect, greta_hitbox, greta_surface, Greta, miss, miss_rect, random):
  clock = game_window.pygame.time.Clock()
  running = True
  while running:
    for event in game_window.pygame.event.get():
      if event.type == game_window.pygame.QUIT:
        running = False

      # running
      elif event.type == game_window.pygame.KEYDOWN:
        if event.key == game_window.pygame.K_SPACE:
          if not state.jumping:
            state.set_jumping(True)
          elif state.double_jump_available:
            state.set_double_jump_available(False)
            state.set_jump_count(JUMP_SIZE)

    # Défilement de l'image de fond
    game_window.game_background_x -= state.background_speed
    if game_window.game_background_x < -game_window.game_background.get_width():
      game_window.game_background_x = 0

    # Effacer l'écran
    game_window.window_surface.fill(BLACK)

    # Dessiner l'image de fond
    game_window.window_surface.blit(game_window.game_background, (game_window.game_background_x, 0))
    game_window.window_surface.blit(game_window.game_background, (game_window.game_background_x + game_window.game_background.get_width(), 0))

    # Gestion du saut
    if state.jumping:
      if state.jump_count <= JUMP_SIZE:
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
      state.set_double_jump_available(True)  # Reset double jump availability

    # Collision et mort de Greta
    if miss_rect.colliderect(greta_hitbox):
      # windowsurface.blit(explosion, explosion_rect) #nouveau
      # clock.tick(10) #nouveau
      # pygame.quit()
      return

    # Afficher Trump
    game_window.window_surface.blit(trump.image, trump.rect)

    #Afficher Greta
    game_window.window_surface.blit(greta_surface, greta_hitbox, greta_rect)  # à suppr
    game_window.window_surface.blit(Greta, greta_rect)
    # Afficher missiles
    miss_rect.move_ip(-state.missile_speed,0)  #rectangle du missile bouge avec la constante speed
    if miss_rect.right < 0:
      miss_rect.x = WINDOWWIDTH
      miss_rect.y = greta_rect.y + random.randint(UP_DISTRIBUTION, DOWN_DISTRIBUTION)
      miss = missiles.get_random_missile(random).image
    game_window.window_surface.blit(miss, miss_rect)

    # test augmenter SCORE
    state.add_score(1 / FPS)
    state.set_difficulty()

    # Afficher le score
    state.print_state(game_window.pygame, game_window.window_surface)

    # Mettre à jour l'affichage
    game_window.pygame.display.flip()

    # Réguler la vitesse de la boucle
    clock.tick(FPS)