# Greta vs f*cking Trump : Run Greta, RUN

## Table des matières

- [Classes](#classes)
    - [State](#state)
    - [Missile](#missile)
    - [Trump](#trump)
- [Fichiers](#fichiers)
    - [Constants](#constants)

## Classes

### State
La structure du code est organisée autour d'une classe `State` qui représente l'état actuel du jeu.
Voici une explication détaillée de chaque partie :

- Définition de la classe State avec les attributs 
    - `step`: numéro d'étape (nbr de frames parcourus)
    - `score` : score actuel du/de la joueur/joueuse
    - `background_speed` : vitesse actuelle du fond
    - `missile_speed` : vitesse actuelle des missiles
- La méthode `__init__` est le constructeur de la classe qui initialise les attributs de l'objet.
- La méthode `__repr__` retourne le nom de l'objet.
- La méthode `add_step` augmente la valeur de `step` de 1.
- La méthode `add_score` augmente la valeur de `score` de la quantité spécifiée.
- La méthode `set_difficulty` modifie les vitesses de fond et de missile en fonction du score actuel.
- La méthode `print_state` affiche le score et la difficulté actuels sur l'écran du jeu. Elle crée deux surfaces de texte pour le score et la difficulté, puis les dessine sur la fenêtre du jeu à des positions spécifiques.

La structure de ce code est typique d'un jeu où l'état du jeu est maintenu dans une classe spécifique. Cela permet de garder le code organisé et facile à comprendre.

### Missile
Le code est organisé autour de deux classes principales : `Missile` et `Missiles`. Voici une explication détaillée de chaque partie :

**Missile**
- Définition de la classe `Missile` avec les attributs `image_name`, `width`, `height` et `image`.
- La méthode `__init__` est le constructeur de la classe qui initialise les attributs de l'objet et charge l'image du missile.

**Missiles**
- Définition de la classe `Missiles` qui gère un ensemble de missiles.
- La méthode `__init__` est le constructeur de la classe qui initialise une liste vide de missiles, puis crée des objets `Missile` pour chaque nom de fichier dans `MISSILE_FILE_NAMES` et les ajoute à la liste.
- La méthode `get_missiles` retourne la liste des missiles.
- La méthode `get_random_missile` choisit et retourne un missile aléatoire de la liste.

La structure de ce code est typique d'un jeu où chaque missile est représenté par un objet et où un autre objet gère l'ensemble des missiles. Cela permet de garder le code organisé et facile à comprendre.

### Trump
Le fichier `trump.py` définit une classe `Trump` qui représente un personnage ou un objet dans le jeu. Voici une explication de chaque partie :

- Définition de la classe `Trump` avec les attributs `image_name`, `width`, `height`, `x_pos`, `y_pos`, `image` et `rect`.
- La méthode `__init__` est le constructeur de la classe qui initialise les attributs de l'objet, charge l'image du personnage, la redimensionne à la largeur et à la hauteur spécifiées, crée un rectangle pour l'image et positionne le rectangle à la position spécifiée. Les attributs `image` et `rect` sont ensuite définis pour être utilisés plus tard dans le jeu.

## Fichiers

### softwaredesign-project.py
Contient le programme principal faisant tourner toute la logique du jeu.

**TODO** : refactoriser ceci avec des classe afin de le rendre plus simple à lire.

### Constants
Ce fichier, `constants.py`, définit un ensemble de constantes qui sont utilisées dans le reste du programme. Voici une explication de chaque section :

- **Définition des couleurs** : Cette section définit plusieurs tuples qui représentent des couleurs en RGB. Par exemple, `WHITE` est défini comme `(255, 255, 255)`, ce qui correspond à la couleur blanche en RGB.
- **Format de la fenêtre** : Cette section définit les dimensions de la fenêtre du jeu (`WINDOWWIDTH` et `WINDOWHEIGHT`) et le nombre de frames par seconde (FPS).
- **Constantes** : Cette section définit plusieurs constantes qui sont utilisées dans le jeu, comme le score initial (`SCORE`), la vitesse de défilement du fond (`BACKGROUND_SPEED`), le nombre de points nécessaires pour passer au niveau suivant (`POINTS_PER_LEVEL`), la vitesse de base (`BASE_SPEED`), la vitesse des missiles (`MISS_SPEED`), les dimensions des missiles (`MISS_LONGUEUR` et `MISS_HAUTEUR`), la taille du saut (`JUMP_SIZE`), la gravité (`GRAVITY`), et les distributions vers le haut et vers le bas (`UP_DISTRIBUTION` et `DOWN_DISTRIBUTION`).
- **Images** : Cette section définit le chemin vers le dossier contenant les images (`PATH`) et une liste de noms de fichiers d'images de missiles (`MISSILE_FILE_NAMES`).