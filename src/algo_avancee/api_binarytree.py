import random
from collections import deque

class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

def inserer(noeud, valeur):
    """
Insère une valeur dans l'arbre en respectant la propriété d'ABR 
    """
    if noeud is None:
        return Noeud(valeur)
    if valeur < noeud.valeur:
        noeud.gauche = inserer(noeud.gauche, valeur)
    else:
        noeud.droite = inserer(noeud.droite, valeur)
    return noeud

def create_binary_tree (n):
    """
    Créer un arbre binaire avec n sommet 
    """
    if n <= 0:
        return None #arbre vide
    
    valeurs = list(range(1, n + 1))
    random.shuffle(valeurs)

    racine = Noeud(valeurs[0])

    for i in range (1, n):
        inserer(racine, valeurs[i])

    return racine

def parcours_largeur(racine):
    """
    Prend en paramètre la racine d'un arbre et renvoie la liste 
    des étiquettes ordonnées selon le parcours en largeur
    """
    if racine is None:
        return []
    
    resultat = []
    file = deque([racine])

    while len(file) > 0:
        noeud_courant = file.popleft()

        resultat.append(noeud_courant.valeur)

        if noeud_courant.gauche is not None:
            file.append(noeud_courant.gauche)
        if noeud_courant.droite is not None:
            file.append(noeud_courant.droite)
    
    return resultat

def parcours_prefixe(noeud):
    """
    Renvoie la liste des sommets dans l'ordre préfixe
    """
    if noeud is None:
        return[]
    # Ordre : racine -> gauche -> droite
    return [noeud.valeur] + parcours_prefixe(noeud.gauche) + parcours_prefixe(noeud.droite)

def parcours_infixe(noeud):
    """
    Renvoie la liste des sommets dans l'ordre infixe
    """
    if noeud is None:
        return []
    # Ordre : gauche -> racine -> droite
    return parcours_infixe(noeud.gauche) + [noeud.valeur] + parcours_infixe(noeud.droite)

def parcours_postfixe(noeud):
    """
    Renvoie la liste des sommets dans l'ordre postfixe
    """
    if noeud is None:
        return[]
    # Ordre : gauche -> droite -> racine
    return parcours_postfixe(noeud.gauche) + parcours_postfixe(noeud.droite) + [noeud.valeur]

def inserer_feuille(noeud, valeur):
    """
    Insère une nouvelle valeur en tant que feuille de l'arbre
    """
    if noeud is None:
        return Noeud(valeur)
    
    if valeur < noeud.valeur:
        noeud.gauche = inserer_feuille(noeud.gauche, valeur)
    else:
        noeud.droite = inserer_feuille(noeud.droite, valeur)

    return noeud

def inserer_branche(parent, nouveau_noeud, cote='gauche'):
    """
    Intercale un nouveau noeud entre un parent et son enfnant actuel
    """
    if cote == 'gauche':
        # 1. On mémorise l'ancien fils gauche
        ancien_fils = parent.gauche
        # 2. Le nouveau nœud devient le fils gauche du parent
        parent.gauche = nouveau_noeud
        # 3. L'ancien fils devient le fils gauche du nouveau nœud
        nouveau_noeud.gauche = ancien_fils
    else:
        ancien_fils = parent.droite
        parent.droite = nouveau_noeud
        nouveau_noeud.droite = ancien_fils
