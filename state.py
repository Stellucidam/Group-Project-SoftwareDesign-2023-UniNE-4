# Clarisse advised us to create a Class State to sort our code and make it more lisible. This class allows us to define a lot of functions that are useful in various places in the game.

from constants import BASE_SPEED, FPS, POINTS_PER_LEVEL, GREEN, MARGIN, PATH


class State:
  
  # Initialization of the state of the game (score, speed, etc.) number of times it passes through the loop
  def __init__(self, score, background_speed, missile_speed, jumping,
               double_jump_available, jump_count):
    self.step = 1
    self.score = score
    self.background_speed = background_speed
    self.missile_speed = missile_speed
    self.jumping = jumping
    self.double_jump_available = double_jump_available
    self.jump_count = jump_count
    self.al_jaber = False

  # We had a problem with our score which was defined as (1/FPS), when we wanted AlJaber to appear every 3 levels, it was buggy because, even if the score was converted in integer when needed, the system recognised it as a decimal number. When AlJaber was supposed to appear on level 3, it appeared on level 3.0, 3.1, 3.2, etc. because it was always rounded up to 3. Clarisse therefore advised us to define the next_step function, which gives us an integer number and overcomes this problem.
  def next_step(self):
    self.step += 1
    if (self.step % FPS == 0):
      self.score += 1

  # Greta can jump
  def set_jumping(self, jumping):
    self.jumping = jumping

  # Greta can double jump
  def set_double_jump_available(self, double_jump_available):
    self.double_jump_available = double_jump_available

  # To know if double jump is available
  def set_jump_count(self, jump_count):
    self.jump_count = jump_count

  # Accelerate the game by increasing the difficulty by one every 5 points
  def set_difficulty(self):
    new_level = self.step % (POINTS_PER_LEVEL * FPS) == 0
    speed_modification = self.score // POINTS_PER_LEVEL

    if new_level:
      self.missile_speed = BASE_SPEED * 2 + speed_modification
      self.background_speed = BASE_SPEED + speed_modification
    return self.step % (POINTS_PER_LEVEL * FPS * 2) == 0

  # Size and font of the texte
  def print_state(self, pygame, windowsurface):
    font = pygame.font.Font(None, 36)
    texte_level = font.render(
      "Niveau: {}".format(int(self.score / POINTS_PER_LEVEL) + 1), True, GREEN)

    windowsurface.blit(texte_level, (MARGIN * 3, MARGIN))

  # With the help of ChatGPT
  def init_music(self, pygame, music_file):
    
    # Initialising the mixer module
    pygame.mixer.init()

    # Load MP3 audio file. We chose "Around the world" Daft Punk: because the planet is a theme of our game and it's repetitive
    pygame.mixer.music.load(PATH + music_file)
    
  # Play the music
  def play_music(self, pygame):
    pygame.mixer.music.play()

  # Stop the music
  def stop_music(self, pygame):
    pygame.mixer.music.stop()
