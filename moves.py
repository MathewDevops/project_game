#moves

pieces = {
    'pion': 1,
    'cavalier': 2,
    'fou': 3,
    'tour': 4,
    'reine': 5,
    'roi': 6
}

def mouvement_piece(matrice, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, type_piece):
    piece = matrice[ligne_depart][colonne_depart]
    # Vérifier si le type de pièce est valide
    if type_piece in pieces.values():
        # Implémenter la logique de mouvement en fonction du type de pièce
        if type_piece == pieces['pion']:
            # Vérifier si le déplacement est valide pour un pion
            if colonne_depart == colonne_arrivee and ligne_arrivee == ligne_depart + 1:
                # Déplacer le pion vers la nouvelle position
                matrice[ligne_depart][colonne_depart] = 0
                matrice[ligne_arrivee][colonne_arrivee] = piece
                return True
        elif type_piece == pieces['cavalier']:
            if (colonne_depart == colonne_arrivee+1 or colonne_depart == colonne_arrivee-1) and (ligne_arrivee==ligne_depart+2 or ligne_arrivee==ligne_depart-2):
                print("if condition valid!")
                matrice[ligne_depart][colonne_depart] = 0
                matrice[ligne_arrivee][colonne_arrivee] = piece
            return True
        elif type_piece == pieces['fou']:
            # Logique de mouvement pour un fou
            # Implémentez la logique de mouvement pour le fou selon les règles d'échecs
            # ...
            pass
        elif type_piece == pieces['tour']:
            # Logique de mouvement pour une tour
            # Implémentez la logique de mouvement pour la tour selon les règles d'échecs
            # ...
            pass
        elif type_piece == pieces['reine']:
            # Logique de mouvement pour une reine
            # Implémentez la logique de mouvement pour la reine selon les règles d'échecs
            # ...
            pass
        elif type_piece == pieces['roi']:
            # Logique de mouvement pour un roi
            # Implémentez la logique de mouvement pour le roi selon les règles d'échecs
            # ...
            pass

# Initialiser une matrice 8x8 avec des zéros
matrice = [[0 for _ in range(8)] for _ in range(8)]

# Placer des pions sur la première rangée (indice 0)
for j in range(8):
    matrice[1][j] = pieces['pion']

# Placer des pions sur l'avant-dernière rangée (indice 6)
for j in range(8):
    matrice[6][j] = pieces['pion']

# Placer des autres pièces sur la deuxième rangée (indice 0)
matrice[0][0] = pieces['tour']
matrice[0][1] = pieces['cavalier']
matrice[0][2] = pieces['fou']
matrice[0][3] = pieces['reine']
matrice[0][4] = pieces['roi']
matrice[0][5] = pieces['fou']
matrice[0][6] = pieces['cavalier']
matrice[0][7] = pieces['tour']

# Placer des autres pièces sur la dernière rangée (indice 7)
matrice[7][0] = pieces['tour']
matrice[7][1] = pieces['cavalier']
matrice[7][2] = pieces['fou']
matrice[7][3] = pieces['reine']
matrice[7][4] = pieces['roi']
matrice[7][5] = pieces['fou']
matrice[7][6] = pieces['cavalier']
matrice[7][7] = pieces['tour']

# Afficher la matrice résultante
for row in matrice:
    print(row)

print(f'----------------------\n\n ----- DEBUG ----- ')

ligne_depart = int(input("ligne depart ? "))
colonne_depart = int(input("colonne depart ? "))
ligne_arrivee = int(input("ligne arrivee ? "))
colonne_arrivee = int(input("colonne arrivee ? "))
type_piece = pieces['cavalier']

print(f'\n')

print("Matrice avant le mouvement:")
for row in matrice:
    print(row)

mouvement_piece(matrice, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, type_piece)

"""
print("\nEffectuer le mouvement:")
if mouvement_piece(matrice, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, type_piece):
    print("Mouvement réussi!")
else:
    print("Mouvement invalide.")
"""

print("\nMatrice après le mouvement:")
for row in matrice:
    print(row)
