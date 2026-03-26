# PARTIE PILE

def pile_vide (pile):
    #On utilise len pour déterminer la taille puis on compare.
    #Il verif qu'il n'y a pas de sommet
    return len(pile) == 0

def empiler (pile, element):
    #On veut concatèner deux liste pour en faire une seule
    #On a déjà une liste de base donc on peut utiliser le paramètre normalement
    #On doit mettre element entre [] car notre paramètre n'est pas une pile de base et on ne pourrait pas concatèner
    return pile + [element] 

def depiler (pile):
    #On verif d'abord que la liste ne soit pas déjà vide en rappelant une fonction précédente
    if pile_vide(pile):
        print("La pile est déjà vide")
        return pile
    #On ne met pas de else car return met fin à la fonction d'elle même
    #On utilise : car sinon il commencerait au début (indice 0), hors on veut enlever la fin dans une pile
    # :-1 permet de garder les premiers et d'exclure le dernier
    nouvelle_pile = pile[:-1]
    return nouvelle_pile

# PARTIE FILE

def file_vide (file):
    #Même principe que la fonction pile_vide
    return len(file) == 0

def ajouter_file (file, element):
    #Même principe que la fonction empiler
    return file + [element]

def retirer_file (file):
    if file_vide(file):
        print("La file est déjà vide")
        return file
    #Dans une file, on veut que le premier élément soit supprimer
    #On crée une nouvelle file qui commence par l'indice 1 et le reste
    nouvelle_file = file[1:]
    return nouvelle_file

# PARTIE GESTION PRECISE

def recherche_element (type, element):
    #Rechercher un élément dans une liste, file ou pile
    #On parcourt chaque élément de notre liste, file ou pile
    for i in range(len(type)):
        #Si dans la liste l'indice i correspond à notre élément rechercher
        if type[i] == element:
            # f permet d'insérer des variables dans du texte sinon elle ne comprends pas 
            print(f"L'élément {element} trouvé")
            return True #on sort de la fonction car on a fini
    #On ne met pas de else pour remplacer les True car sinon on aurait un message pour chaque élément
    print(f"L'élement {element} n'a pas été trouvé")
    return False

def ajout_element(type, x, element):
    modification=[]
    for i in range(len(type)+1):
        if i < x :
            modification = modification + [type[i]]
        elif i == x :
            modification = modification + [element]
        else :
            modification = modification + [type[i-1]]
    print(f"Le nouvel élément {element} a bien été ajouté à l'indice {x}")
    return modification

def supprimer_element(type, element):
    modification=[]
    for i in range(len(type)):
        #Si l'élément à l'indice i est différent du paramètre élément alors il le recopie
        if i != element :
            modification = modification + [type[i]]
    print(f"L'élément {element} a bien été supprimé")
    return modification
