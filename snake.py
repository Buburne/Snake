# snake python Cyril


from upemtk import *
from time import sleep
from random import *

# dimensions du jeu
taille_case = 15
largeur_plateau = 40  # en nombre de cases
hauteur_plateau = 30  # en nombre de cases

def deplacement(pos, direction, signe):
    """
    Fonction qui recoit la position accompagné d'une diréction et renvoie
    la position actualisée.
    """
    # Décomposition des tuples
    x, y = pos
    s, d = direction
    if signe == 1: # Gestion de l'inversion de position / composition d'un tuple
        nPos = (x + s, y + d)
    else:
        nPos = (x - s, y - d)
    return nPos
def case_vers_pixel(x):
    """
    Fonction recevant les coordonnées d'une case du plateau sous la forme
    d'un couple d'entiers (ligne, colonne) et renvoyant les coordonnées du
    pixel se trouvant au centre de cette case. Ce calcul prend en compte la
    taille de chaque case, donnée par la variable globale taille_case.
    """
    i, j = x
    return (i + .5) * taille_case, (j + .5) * taille_case


def affiche_pommes(pommes):
    """
    Fonction qui recoit des coordonnées sous la forme d'un couple 
    et y affiche une pomme.
    """
    x, y = case_vers_pixel(pommes)

    cercle(x, y, taille_case/2,
           couleur='darkred', remplissage='red')


def affiche_serpent(serpent, joueur):
    """
    Fonction qui recoit une liste de couples et qui affiche un serpent a
    chacune des positions de la liste selon la couleur définie par l'argument
    joueur
    """
    n = 0
    while n < len(serpent):
        x, y = case_vers_pixel(serpent[n])
        if joueur == 1:
            cercle(x, y, taille_case/2 + 1,
                   couleur='Blue', remplissage='Blue')
        if joueur == 2:
            cercle(x, y, taille_case/2 + 1,
                   couleur='Red', remplissage='Red')
        if joueur == 3:
            cercle(x, y, taille_case/2 + 1,
                   couleur='Black', remplissage='Black')
        n += 1

def change_direction(direction, touche, mode):
    """Permet de gérer le changement de direction selon les commandes"""
    if mode == 1:
        if touche == 'Up':
            # flèche haut pressée
            return(0, -1)
        elif touche == 'Down':
            # flèche bas pressée
            return(0, 1)
        elif touche == 'Left':
            # flèche gauche pressée
            return(-1 , 0)
        elif touche == 'Right':
            # flèche droite pressée
            return(1, 0)
        else:
            # pas de changement !
            return direction
    elif mode == 2:
        if touche == 'z':
            # flèche haut pressée
            return(0, -1)
        elif touche == 's':
            # flèche bas pressée
            return(0, 1)
        elif touche == 'q':
            # flèche gauche pressée
            return(-1 , 0)
        elif touche == 'd':
            # flèche droite pressée
            return(1, 0)
        else:
            # pas de changement !
            return direction

def ft_solo_mode(commandes, couleur):
    """
    Fonction du mode 1 joueur prennant comme argument l'indice des commandes
    si le joueur souhaite jouer avec ZQSD cet indice sera de 2
    """
    # initialisation du jeu
    framerate = 10    # taux de rafraîchissement du jeu en images/s
    direction = (0, 1)  # direction initiale du serpent
    pos_Pomme = (40, 30) # Création de la pomme originelle hors du terrain
    absence_pomme = True # Initialisation du booleen des pommes
    pos_Serpent = [(21,15),(21,14),(21,13)] # Initialisation du serpent
    cree_fenetre(taille_case * largeur_plateau,
                 taille_case * hauteur_plateau)
    # boucle principale
    while True:
        # affichage des objets
        efface_tout()
        #Comportement du programme si la tete du serpent touche une pomme
        if pos_Serpent[0] == pos_Pomme: 
            absence_pomme = True
            pos_Serpent.append(deplacement(pos_Pomme, direction, 0))
        # Génération d'une nouvelle pomme 
        if absence_pomme == True:
            px = randint(1, 38)
            py = randint(1, 28)
            absence_pomme = False
            pos_Pomme = px, py
            while pos_Serpent.count(pos_Pomme) != 0:# Création hors du corps du serpent
                px = randint(1, 39)
                py = randint(1, 29)
                pos_Pomme = px, py
        affiche_pommes(pos_Pomme) # Affichage de la pomme
        pos_Serpent.insert(0, (deplacement(pos_Serpent[0], direction, 1))) #Ajout de la nouvelle position en tete du serpent
        pos_Serpent.pop() #Suppression de la plus ancienne position
        collision = pos_Serpent.count(pos_Serpent[0]) #Gestion de la colision par repetition de la position de la tete
        if collision != 1:
            score = len(pos_Serpent) - 3
            print(score,"pommes mangées") #Affichage du score
            break
        x, y = pos_Serpent[0]
        #Gestion de la sortie du terrain
        if x > (largeur_plateau - 1) or x < 0 or y > (hauteur_plateau - 1) or y < 0:
            score = len(pos_Serpent) - 3
            print(score,"pommes mangées")
            break
        affiche_serpent(pos_Serpent, couleur)  # à modifier !
        mise_a_jour()


        # gestion des événements
        ev = donne_evenement()
        ty = type_evenement(ev)
        if ty == 'Escape':
            break
        elif ty == 'Touche':
            direction = change_direction(direction, touche(ev), commandes)

        # attente avant rafraîchissement
        sleep(1/framerate)

    # fermeture et sortie
    ferme_fenetre()



 #programme principal
if __name__ == "__main__":
    couleur = 0
    mode = 0
    print("Jouer avec les touches(1) ou ZQSD(2)")
    while mode > 2 or mode < 1:
        mode = int(input(""))
    print("Tu preferes etre: bleu(1), rouge(2) ou noir(3) ? ")
    while couleur > 3 or couleur < 1 :
        couleur = int(input(""))
    ft_solo_mode(mode, couleur)
