pieces = {
    'pion': 1,
    'cavalier': 2,
    'fou': 3,
    'tour': 4,
    'reine': 5,
    'roi': 6
}

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