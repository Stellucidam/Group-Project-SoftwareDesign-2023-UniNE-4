# From that we import all the class we create to use it in the game
import time
from game_window import GameWindow
from greta import Greta
from missile import Missiles
from state import State
from constants import BLACK, DOWN_DISTRIBUTION, FPS, JUMP_SIZE, UP_DISTRIBUTION, WINDOWWIDTH, WINDOWHEIGHT
from super_element import SuperElement
from trump import Trump
from al_jaber import AlJaber


# Main loop, the functions are defines in their classes
def main_game_loop(game_window: GameWindow, state: State, missiles: Missiles,
                   trump: Trump, greta: Greta, al_jaber: AlJaber, random):
  current_missile = missiles.get_random_missile(random)
  clock = game_window.pygame.time.Clock()
  running = True
  while running:
    for event in game_window.pygame.event.get():
      if event.type == game_window.pygame.QUIT:
        running = False
      elif event.type == game_window.pygame.KEYDOWN:
        if event.key == game_window.pygame.K_SPACE:
          if not state.jumping:
            state.set_jumping(True)
          elif state.double_jump_available:
            state.set_double_jump_available(False)
            state.set_jump_count(JUMP_SIZE)

    # Scroll background image
    game_window.game_background_x -= state.background_speed
    if game_window.game_background_x < -game_window.game_background.get_width(
    ):
      game_window.game_background_x = 0

    # Delete the screen
    game_window.window_surface.fill(BLACK)

    # Draw the background image
    game_window.window_surface.blit(game_window.game_background,
                                    (game_window.game_background_x, 0))
    game_window.window_surface.blit(
      game_window.game_background,
      (game_window.game_background_x + game_window.game_background.get_width(),
       0))

    # Jump management
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

    # Show Trump
    game_window.window_surface.blit(trump.image, trump.rect.topleft)

    # Show score
    state.print_state(game_window.pygame, game_window.window_surface)
    
    # Clarisse explained to us that al_jaber does not exist if the value state.al_jaber is False, which means we can do al_jaber.get_collision_rect(...) ONLY if state.al_jaber is True
    al_jaber_greta_collision = False
    if (state.al_jaber):
      al_jaber_greta_collision = al_jaber.get_collision_rect(game_window.pygame).colliderect(greta.get_collision_rect(game_window.pygame))

    # Collision and greta's death
    if current_missile.get_collision_rect(game_window.pygame).colliderect(greta.get_collision_rect(game_window.pygame)) or al_jaber_greta_collision:
      explosion = SuperElement(game_window.pygame, "explosion.png",
                               greta.width, greta.height, greta.rect.x,
                               greta.rect.y)
      game_window.window_surface.blit(explosion.image, explosion.rect.topleft)
      game_window.pygame.display.flip()

      # Wait for 2 seconds
      time.sleep(2)

      # Game over image
      game_over = SuperElement(game_window.pygame, "fond_fin.png", WINDOWWIDTH,
                               WINDOWHEIGHT, 0, 0)
      game_window.window_surface.blit(game_over.image, game_over.rect.topleft)
      game_window.pygame.display.flip()

      # Wait for 4 seconds before returning to the begining
      time.sleep(4)
      return

    # Display Greta
    game_window.window_surface.blit(greta.image, greta.rect)

    # Display missiles
    current_missile.rect.move_ip(-state.missile_speed, 0)
    if current_missile.rect.right < 0:
      current_missile.rect.x = WINDOWWIDTH
      current_missile.rect.y = greta.rect.y + random.randint(
        UP_DISTRIBUTION, DOWN_DISTRIBUTION)
      current_missile = missiles.get_random_missile(random)
    game_window.window_surface.blit(current_missile.image,
                                    current_missile.rect)

    # Show AlJabar
    if (state.al_jaber):
      game_window.window_surface.blit(al_jaber.image, al_jaber.rect.topleft)
      if(al_jaber.behaviour(state.missile_speed, greta.rect.y)):
        state.al_jaber = False
        al_jaber = None
    
    # Increase difficulty
    state.next_step()
    if (state.set_difficulty()):
      state.al_jaber = True
      al_jaber = AlJaber(game_window.pygame, greta.rect.y)

    # Update display
    game_window.pygame.display.flip()

    # Regulating the loop speed
    clock.tick(FPS)
