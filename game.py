import time
from game_window import GameWindow
from greta import Greta
from missile import Missiles
from state import State
from constants import BLACK, DOWN_DISTRIBUTION, FPS, GRAVITY, JUMP_SIZE, PATH, UP_DISTRIBUTION, WINDOWHEIGHT, WINDOWWIDTH
from super_element import SuperElement
from trump import Trump


def main_game_loop(
  game_window: GameWindow,
  state: State,
  missiles: Missiles,
  trump: Trump,
  greta: Greta,
  random):
  
  current_missile = missiles.get_random_missile(random)
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
    if game_window.game_background_x < -game_window.game_background.get_width(
    ):
      game_window.game_background_x = 0

    # Effacer l'écran
    game_window.window_surface.fill(BLACK)

    # Dessiner l'image de fond
    game_window.window_surface.blit(game_window.game_background,
                                    (game_window.game_background_x, 0))
    game_window.window_surface.blit(
      game_window.game_background,
      (game_window.game_background_x + game_window.game_background.get_width(),
       0))

    # Gestion du saut
    if state.jumping:
      if state.jump_count >= JUMP_SIZE * -1:
        neg = 1
        if state.jump_count < 0:
          neg = -1
        greta.rect.y -= (state.jump_count**2) * 0.5 * neg
        state.set_jump_count(state.jump_count - 1)
      else:
        state.set_jumping(False)
        state.set_jump_count(JUMP_SIZE)
    
    greta.apply_gravity(state)

    # Afficher Trump
    game_window.window_surface.blit(trump.image, trump.rect.topleft)

    # Afficher le score
    state.print_state(game_window.pygame, game_window.window_surface)

    # Collision et mort de Greta
    if current_missile.get_collision_rect(game_window.pygame).colliderect(greta.get_collision_rect(game_window.pygame)):
      explosion = SuperElement(game_window.pygame, "explosion.png", greta.width, greta.height, greta.rect.x, greta.rect.y)
      game_window.window_surface.blit(explosion.image, explosion.rect.topleft)
      game_window.pygame.display.flip()
      
      clock.tick(10) #nouveau
      time.sleep(3) #nouveau
      return

    #Afficher Greta
    game_window.window_surface.blit(greta.image, greta.rect)
    
    # Afficher missiles
    current_missile.rect.move_ip(-state.missile_speed,
                      0)  #rectangle du missile bouge avec la constante speed
    if current_missile.rect.right < 0:
      current_missile.rect.x = WINDOWWIDTH
      current_missile.rect.y = greta.rect.y + random.randint(UP_DISTRIBUTION,
                                                  DOWN_DISTRIBUTION)
      current_missile = missiles.get_random_missile(random)
    game_window.window_surface.blit(current_missile.image, current_missile.rect)

    # test augmenter SCORE
    state.add_score(1 / FPS)
    state.set_difficulty()

    # Mettre à jour l'affichage
    game_window.pygame.display.flip()

    # Réguler la vitesse de la boucle
    clock.tick(FPS)
