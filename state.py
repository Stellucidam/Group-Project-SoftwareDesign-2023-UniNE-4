from typing import Any
from constants import BASE_SPEED, POINTS_PER_LEVEL, WHITE, WINDOWWIDTH

class State:
    def __init__(self, step, score, background_speed, missile_speed, jumping, double_jump_available, jump_count):
        self.step = step
        self.score = score
        self.background_speed = background_speed
        self.missile_speed = missile_speed
        self.jumping = jumping
        self.double_jump_available = double_jump_available
        self.jump_count = jump_count

    def __repr__(self):
        return self.name
    
    def add_step(self):
        self.step += 1

    def add_score(self, amount):
        self.score += amount

    def set_jumping(self, jumping):
        self.jumping = jumping

    def set_double_jump_available(self, double_jump_available):
        self.double_jump_available = double_jump_available

    def set_jump_count(self, jump_count):
        self.jump_count = jump_count
    
    # Accélérer l'image
    def set_difficulty(self):
        speed_modification = self.score // POINTS_PER_LEVEL  #augmente de 1 tous les 5 scores
        if self.background_speed < 10:
            self.background_speed = BASE_SPEED + speed_modification
        if self.missile_speed < 20:
            self.missile_speed += speed_modification

    # Fonction pour afficher le score
    def print_state(self, pygame, windowsurface):
        font = pygame.font.Font(None, 36)  # Police et taille du texte

        texte_score = font.render("Score : {}".format(int(self.score)), True, WHITE)
        texte_difficulty = font.render("Difficulté: {}".format(int(self.background_speed - BASE_SPEED)), True, WHITE)

        # Puis, quand vous dessinez le texte :
        windowsurface.blit(texte_score, (10, 10))
        windowsurface.blit(texte_difficulty, (10, 20 + texte_score.get_height()))
