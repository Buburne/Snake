from upemtk import *
from time import sleep

# dimensions du jeu
taille_case = 15
largeur_plateau = 40  # en nombre de cases
hauteur_plateau = 30  # en nombre de cases

def case_vers_pixel(case):
    """
    Fonction recevant les coordonnées d'une case du plateau sous la forme
    d'un couple d'entiers (ligne, colonne) et renvoyant les coordonnées du
    pixel se trouvant au centre de cette case. Ce calcul prend en compte la
    taille de chaque case, donnée par la variable globale taille_case.
    """
    i, j = case
    return (i + .5) * taille_case, (j + .5) * taille_case


def affiche_pommes(pommes):
    x, y = case_vers_pixel((1, 1))  # à modifier !!!

    cercle(x, y, taille_case/2,
           couleur='darkred', remplissage='red')
    rectangle(x-2, y-taille_case*.4, x+2, y-taille_case*.7,
              couleur='darkgreen', remplissage='darkgreen')


def affiche_serpent(serpent):
    x, y = case_vers_pixel((serpent[0], serpent [1]))  # à modifier !!!

    cercle(x, y, taille_case/2 + 1,
           couleur='darkgreen', remplissage='green')


def change_direction(direction, touche):
    # à compléter !!!
    if touche == 'Up':
        # flèche haut pressée
        return (direction[0] +0 , direction[1] - 1)
    elif touche == 'Down':
        return (direction [0] +0 ,direction  [1] +1)
    elif touche == 'Right':
        return (direction [0] +1, direction[1] +0)
    elif touche == 'Left':
        return (direction [0] -1, direction [1] +0)
    else:
        # pas de changement !
        return direction
        
# serpent est equivaut a direction 
# programme principal
if __name__ == "__main__":

    # initialisation du jeu
    framerate = 10    # taux de rafraîchissement du jeu en images/s
    direction = (0, 0)  # direction initiale du serpent
    cree_fenetre(taille_case * largeur_plateau,
                 taille_case * hauteur_plateau)
    # le serpent avance case par case indefinimment
    # boucle principale
    while True:
        # affichage des objets
        efface_tout()
        affiche_pommes(None)   # à modifier !
        affiche_serpent(direction)  # à modifier !
        mise_a_jour()

        # gestion des événements
        ev = donne_evenement()
        ty = type_evenement(ev)
        if ty == 'Quitte':
            break
        elif ty == 'Touche':
            print(touche(ev))
            direction = change_direction(direction, touche(ev))

        # attente avant rafraîchissement
        sleep(1/framerate)

    # fermeture et sortie
    ferme_fenetre()
