from constants import BASE_SPEED, GREEN, MARGIN, POINTS_PER_LEVEL, WHITE

class State:
    # Initialisation de l'état du jeu (score, vitesse, etc.)
    def __init__(self, score: float, background_speed: float, missile_speed: float, jumping: bool, double_jump_available: bool, jump_count: int):
        self.score = score
        self.background_speed = background_speed
        self.missile_speed = missile_speed
        self.jumping = jumping
        self.double_jump_available = double_jump_available
        self.jump_count = jump_count

    def add_score(self, amount: float):
        self.score += amount

    def set_jumping(self, jumping: bool):
        self.jumping = jumping
    
    def set_double_jump_available(self, double_jump_available: bool):
        self.double_jump_available = double_jump_available

    def set_jump_count(self, jump_count: int):
        self.jump_count = jump_count

    # Accélérer l'image
    def set_difficulty(self):
        speed_modification = self.score // POINTS_PER_LEVEL  # augmente de 1 tous les 5 scores
        if self.background_speed < 10:
            self.background_speed = BASE_SPEED + speed_modification
        if self.missile_speed < 20:
            self.missile_speed += speed_modification

    # Fonction pour afficher le score
    def print_state(self, pygame, windowsurface):
        font = pygame.font.Font(None, 36)  # Police et taille du texte

        texte_score = font.render("Score : {}".format(int(self.score)), True, GREEN)
        texte_level = font.render("Difficulté: {}".format(int(self.background_speed - BASE_SPEED)), True, GREEN)

        # Puis, quand vous dessinez le texte :
        windowsurface.blit(texte_score, (MARGIN* 3, MARGIN))
        windowsurface.blit(texte_level, (MARGIN * 3, MARGIN *2 + texte_score.get_height()))
