from typing import Any
from constants import BASE_SPEED, POINTS_PER_LEVEL, WHITE, WINDOWWIDTH

class State:
    # Initialisation de l'état du jeu (score, vitesse, etc.)
    def __init__(self, step: int, score: float, background_speed: float, missile_speed: float, jumping: bool, double_jump_available: bool, jump_count: int):
        self.step = step
        self.score = score
        self.background_speed = background_speed
        self.missile_speed = missile_speed
        self.jumping = jumping
        self.double_jump_available = double_jump_available
        self.jump_count = jump_count

    def __repr__(self):
        """
        Affiche l'état courant du jeu.

        Returns:
            str : L'état courant du jeu.
        """
        return "Etat courant :\n    Score : {}\n    Vitesse du fond : {}\n    Vitesse des missiles : {}\n".format(
            self.score, 
            self.background_speed, 
            self.missile_speed
        )
    
    def add_step(self):
        """
        Ajoute 1 au nombre de pas effectués par le joueur.
        """
        self.step += 1

    def add_score(self, amount: float):
        """
        Ajoute un nombre de points au score du joueur.

        Args:
            amount (float): Le nombre de points à ajouter.
        """
        self.score += amount

    def set_jumping(self, jumping: bool):
        """
        Définit si le joueur est en train de sauter.

        Args:
            jumping (bool): Un booléen indiquant si le joueur est en train de sauter.
        """
        self.jumping = jumping
    
    def set_double_jump_available(self, double_jump_available: bool):
        """
        Définit si le double saut est disponible pour le joueur.

        Args:
            double_jump_available (bool): Un booléen indiquant si le double saut est disponible.
        """
        self.double_jump_available = double_jump_available

    def set_jump_count(self, jump_count: int):
        """
        Définit le nombre de sauts que le joueur a effectués.

        Args:
            jump_count (int): Le nombre de sauts.
        """
        self.jump_count = jump_count

    # Accélérer l'image
    def set_difficulty(self):
        """
        Augmente la vitesse du fond et des missiles en fonction du score du joueur.
        """
        speed_modification = self.score // POINTS_PER_LEVEL  #augmente de 1 tous les 5 scores
        if self.background_speed < 10:
            self.background_speed = BASE_SPEED + speed_modification
        if self.missile_speed < 20:
            self.missile_speed += speed_modification

    # Fonction pour afficher le score
    def print_state(self, pygame, windowsurface):
        """
        Fonction pour afficher le score.

        Args:
            pygame (Any): le module pygame.
            windowsurface (Any): La surface de la fenêtre du jeu.
        """
        font = pygame.font.Font(None, 36)  # Police et taille du texte

        texte_score = font.render("Score : {}".format(int(self.score)), True, WHITE)
        texte_difficulty = font.render("Difficulté: {}".format(int(self.background_speed - BASE_SPEED)), True, WHITE)

        # Puis, quand vous dessinez le texte :
        windowsurface.blit(texte_score, (10, 10))
        windowsurface.blit(texte_difficulty, (10, 20 + texte_score.get_height()))
