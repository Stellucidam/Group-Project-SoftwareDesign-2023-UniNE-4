from constants import BASE_SPEED, FPS, POINTS_PER_LEVEL, GREEN, MARGIN


class State:
  # Initialisation de l'état du jeu (score, vitesse, etc.) nombre de fois qu'on passe dans la loop
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

  def next_step(self): # Clarisse
    self.step += 1
    if (self.step % FPS == 0):
      self.score += 1

  def set_jumping(self, jumping):
    self.jumping = jumping

  def set_double_jump_available(self, double_jump_available):
    self.double_jump_available = double_jump_available

  def set_jump_count(self, jump_count):
    self.jump_count = jump_count

# Accélérer l'image

  def set_difficulty(self):
    new_level = self.step % (POINTS_PER_LEVEL * FPS) == 0
    speed_modification = self.score // POINTS_PER_LEVEL  #augmente de 1 tous les 5 scores
    
    if new_level:
      self.missile_speed = BASE_SPEED * 2 + speed_modification
      self.background_speed = BASE_SPEED + speed_modification
    return self.step % (POINTS_PER_LEVEL * FPS * 2) == 0

# Fonction pour afficher le score

  def print_state(self, pygame, windowsurface):
    font = pygame.font.Font(None, 36)  # Police et taille du texte

    # texte_score = font.render("Score : {}".format(int(self.score)), True, GREEN)
    texte_level = font.render(
      "Niveau: {}".format(int(self.score / POINTS_PER_LEVEL) + 1), True,
      GREEN)

    # Puis, quand vous dessinez le texte :
    # windowsurface.blit(texte_score, (MARGIN * 3, MARGIN))
    windowsurface.blit(texte_level, (MARGIN * 3, MARGIN))
                      #  (MARGIN * 3, MARGIN * 2 + texte_score.get_height()))
    