from api_binarytree import (
    Noeud, create_binary_tree, parcours_largeur,
    parcours_prefixe, parcours_infixe, parcours_postfixe,
    inserer_feuille, inserer_branche
)
from api_matrices import (
    creer_matrice_5x4, creer_matrice, operation_matrices, afficher_matrice
)
from api_gestion import (
    pile_vide, empiler, depiler,
    file_vide, ajouter_file, retirer_file,
    recherche_element, ajout_element, supprimer_element
)

# ══════════════════════════════════════════════════════════════════════════════
# PARTIE 1 — ARBRES BINAIRES
# ══════════════════════════════════════════════════════════════════════════════
print("\n========== PARTIE 1 : ARBRES BINAIRES ==========\n")

# Création
racine = create_binary_tree(7)
print("Arbre créé avec 7 sommets")

# Parcours
print("\nParcours en largeur :", parcours_largeur(racine))
print("Parcours préfixe    :", parcours_prefixe(racine))
print("Parcours infixe     :", parcours_infixe(racine))
print("Parcours postfixe   :", parcours_postfixe(racine))

# Insertion feuille
racine = inserer_feuille(racine, 100)
print("\nAprès insertion feuille 100 :")
print("Infixe :", parcours_infixe(racine))

# Insertion branche
nouveau = Noeud(999)
inserer_branche(racine, nouveau, cote='gauche')
print("\nAprès insertion branche 999 à gauche de la racine :")
print("Infixe :", parcours_infixe(racine))


# ══════════════════════════════════════════════════════════════════════════════
# PARTIE 2 — MATRICES
# ══════════════════════════════════════════════════════════════════════════════
print("\n========== PARTIE 2 : MATRICES ==========\n")

# Matrice 5x4
print("Matrice 5x4 :")
afficher_matrice(creer_matrice_5x4())

# Matrice n x m
print("\nMatrice 3x6 :")
afficher_matrice(creer_matrice(3, 6))

# Opérations
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

print("\nA + B :") ; afficher_matrice(operation_matrices(A, B, '+'))
print("\nA - B :") ; afficher_matrice(operation_matrices(A, B, '-'))
print("\nA x B :") ; afficher_matrice(operation_matrices(A, B, 'x'))
print("\nA / B :") ; afficher_matrice(operation_matrices(A, B, '/'))


# ══════════════════════════════════════════════════════════════════════════════
# PARTIE 3 — PILES, FILES & LISTES
# ══════════════════════════════════════════════════════════════════════════════
print("\n========== PARTIE 3 : PILES, FILES & LISTES ==========\n")

# Pile
print("-- PILE --")
pile = []
pile = empiler(pile, 10) ; pile = empiler(pile, 20) ; pile = empiler(pile, 30)
print("Après 3 empilements :", pile)
pile = depiler(pile)
print("Après dépiler       :", pile)
print("Pile vide ?         ", pile_vide(pile))

# File
print("\n-- FILE --")
file = []
file = ajouter_file(file, 'A') ; file = ajouter_file(file, 'B') ; file = ajouter_file(file, 'C')
print("Après 3 ajouts :", file)
file = retirer_file(file)
print("Après retirer  :", file)
print("File vide ?    ", file_vide(file))

# Liste
print("\n-- LISTE --")
liste = [10, 20, 30, 40, 50]
print("Liste de départ :", liste)
recherche_element(liste, 30)
recherche_element(liste, 99)
liste = ajout_element(liste, 2, 999)
print("Après insertion :", liste)
liste = supprimer_element(liste, 2)
print("Après suppression :", liste)