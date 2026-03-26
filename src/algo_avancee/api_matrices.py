#Fonction1: Creer une matrice 5x4
def creer_matrice_5x4(): # définition d'une fonction qui cree une matrice de 5 lignes et 4 colonnes
    matrice = [] # on cree une liste vide qui va contenir toutes les lignes de la matrice
    for i in range(5):  # boucle pour creer 5 lignes
        ligne = [] # on cree une nouvelle ligne vide
        for j in range(4): # boucle pour creer 4 colonnes dans chaque ligne
            ligne.append(0) # on ajoute la valeur 0 dans la ligne
        matrice.append(ligne) # on ajoute la ligne complete dans la matrice
    return matrice # on retourne la matrice cree

#Focntion2: creer matrice de taille quelconque
def creer_matrice(n,m):  # fonction qui crée une matrice de n lignes et m colonnes
    matrice = []
    for i in range(n): # boucle pour créer n lignes
        ligne = []
        for j in range(m):  # boucle pour créer m colonnes
            ligne.append(0)
        matrice.append(ligne)
    return matrice


  #Fonction3: effectuer les operations 4          
def operation_matrices(A, B, operation): # Définition d'une fonction qui réalise une opération entre deux matrices A et B
    nb_lignes = len(A)      # Récupère le nombre de lignes de la matrice A
    nb_cols = len(A[0])     # Récupère le nombre de colonnes de la matrice A (longueur de la première ligne)


    C = creer_matrice(nb_lignes, nb_cols) # Crée une nouvelle matrice C de même taille que A et B pour stocker le resultat

    for i in range(nb_lignes):          # Boucle qui parcourt toutes les lignes de la matrice
        for j in range(nb_cols):        # Boucle qui parcourt toutes les colonnes de la matrice


            if operation == '+': # Si l'opération demandée est l'addition
                C[i][j] = A[i][j] + B[i][j] # On additionne les éléments correspondants de A et B et on stocke le résultat dans C

            elif operation == '-':
                C[i][j] = A[i][j] - B[i][j]

            elif operation == 'x':
                C[i][j] = A[i][j] * B[i][j]

            elif operation == '/':
                if B[i][j] == 0:# Vérifie si l'élément de B est égal à 0 pour éviter une division par zéro
                    C[i][j] = 1 # Si B[i][j] = 0, on met 1 dans la matrice résultat pour eviter l'erreur
                else:                    # Si le dénominateur n'est pas 0 On effectue la division normale
                    C[i][j] = A[i][j] / B[i][j]

    return C     # La fonction retourne la matrice résultat contenant le résultat de l'opération entre A et B


# Définition d'une fonction pour afficher une matrice (M est une liste des matrices)
def afficher_matrice(M):
    for ligne in M :         # Parcourt chaque "ligne" de la matrice M
        print(ligne)         #Affichage sous forme de liste


if __name__ == "__main__":  #Condition pour executer ssi le fichier est lance directement
    print("Matrice 5x4")    #Affiche un titre pour indiquer que l'on va montrer la matrice 5x4
    M = creer_matrice_5x4()# Appelle la fonction creer_matrice_5x4() ,chaque élément est initialisé à 0
    afficher_matrice(M) # Affiche la matrice 5x4 créée ligne par ligne

print("\n Matrice 3x3")
A = [[1, 2, 3],# Definition manuelle d'une matrice 3x3 A
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]


print("A + B :")
afficher_matrice(operation_matrices(A, B, '+'))# Appelle la fonction operation_matrices pour additionner A et B;Puis affiche le résultat ligne par ligne

print("\nA - B :")
afficher_matrice(operation_matrices(A, B, '-'))

print("\nA x B :")
afficher_matrice(operation_matrices(A, B, 'x'))

print("\nA / B :")
afficher_matrice(operation_matrices(A, B, '/'))



