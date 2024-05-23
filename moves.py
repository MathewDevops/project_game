#moves

pieces = {
    'pion': 1,
    'cavalier': 2,
    'fou': 3,
    'tour': 4,
    'reine': 5,
    'roi': 6
}

def demander_coordonnees():
    print("\n")
    while True:
        try:
            ligne_depart = int(input("Entrez la ligne de départ : "))
            colonne_depart = int(input("Entrez la colonne de départ : "))
            ligne_arrivee = int(input("Entrez la ligne d'arrivée : "))
            colonne_arrivee = int(input("Entrez la colonne d'arrivée : "))
            type_piece = int(input("Entrez le type de pièce (numéro) : "))

            # Vérifier si les coordonnées sont dans les limites de l'échiquier
            if 0 <= ligne_depart < 8 and 0 <= colonne_depart < 8 and 0 <= ligne_arrivee < 8 and 0 <= colonne_arrivee < 8:
                return ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, type_piece
            else:
                print("Erreur : Les coordonnées doivent être comprises entre 0 et 7.")
        except ValueError:
            print("Erreur : Veuillez entrer des nombres entiers pour les coordonnées.")

def verifier_victoire(matrice, joueur):
    roi_joueur_1 = False
    roi_joueur_2 = False
    
    for ligne in matrice:
        if pieces['roi'] in ligne:
            roi_joueur_1 = True
        if -pieces['roi'] in ligne:
            roi_joueur_2 = True
    
    if not roi_joueur_1:
        return 2  # Joueur 2 gagne
    if not roi_joueur_2:
        return 1  # Joueur 1 gagne
    
    return False  # Pas de victoire


def est_en_echec(matrice, joueur):
    roi = pieces['roi'] if joueur == 1 else -pieces['roi']
    roi_position = trouver_roi(matrice, roi)

    if roi_position is None:
        return False

    roi_x, roi_y = roi_position
    print(f"Position du roi: ({roi_x}, {roi_y})")  

    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            piece = matrice[i][j]
            if piece != 0 and (piece > 0) != (joueur == 1):
                if mouvement_est_valide(matrice, i, j, roi_x, roi_y, piece):
                    return True
    return False

def trouver_pieces_adverses(matrice, joueur):
        pieces_adverses = []
        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                piece = matrice[i][j]
                if piece * joueur < 0:
                    pieces_adverses.append((i, j))
        return pieces_adverses

def est_en_echec_et_mat(matrice, joueur):
    echec = est_en_echec(matrice, joueur)
    
    if not echec:
        return False, False  # Pas en échec et mat
    
    pieces_joueur = trouver_pieces_joueur(matrice, joueur)
    roi_position = trouver_roi(matrice, joueur)
    
    if roi_position is None:
        return True, False  # Échec mais pas de roi
    
    roi_x, roi_y = roi_position
    
    # Générer tous les mouvements possibles pour chaque pièce du joueur en échec
    for piece_position in pieces_joueur:
        ligne_depart, colonne_depart = piece_position
        type_piece = abs(matrice[ligne_depart][colonne_depart])
        
        for ligne_arrivee in range(8):
            for colonne_arrivee in range(8):
                if mouvement_est_valide(matrice, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, type_piece):
                    # Simuler le mouvement
                    matrice_temp = [row[:] for row in matrice]  # Copie de la matrice pour tester le mouvement
                    matrice_temp[ligne_arrivee][colonne_arrivee] = matrice_temp[ligne_depart][colonne_depart]
                    matrice_temp[ligne_depart][colonne_depart] = 0
                    
                    # Vérifier si le roi peut être sauvé
                    if not est_en_echec(matrice_temp, joueur):
                        return False, False  # Il y a un mouvement possible pour sortir de l'échec et mat
                    
    return True, True  # Échec et mat
def trouver_roi(matrice, roi):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == roi:
                return (i, j)
    return None

def mouvement_est_valide(matrice, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, type_piece):
    piece = matrice[ligne_depart][colonne_depart]
    piece_arrivee = matrice[ligne_arrivee][colonne_arrivee]

    if ligne_arrivee < 0 or colonne_arrivee < 0 or ligne_arrivee >= len(matrice) or colonne_arrivee >= len(matrice[0]):
        return False

    if ligne_depart == ligne_arrivee and colonne_depart == colonne_arrivee:
        return False

    if type_piece in pieces.values():
        joueur = 1 if piece < 0 else 2
        direction = 1 if joueur == 1 else -1
        adverse_piece = lambda p: p < 0 if joueur == 1 else p > 0

        if type_piece == pieces['pion']:
            if colonne_depart == colonne_arrivee and ligne_arrivee == ligne_depart + direction and piece_arrivee == 0:
                return True
            elif abs(colonne_depart - colonne_arrivee) == 1 and ligne_arrivee == ligne_depart + direction and adverse_piece(piece_arrivee):
                return True
        elif type_piece == pieces['cavalier']:
            if (abs(colonne_depart - colonne_arrivee) == 1 and abs(ligne_depart - ligne_arrivee) == 2) or (abs(colonne_depart - colonne_arrivee) == 2 and abs(ligne_depart - ligne_arrivee) == 1):
                return True
        elif type_piece == pieces['fou']:
            if abs(colonne_depart - colonne_arrivee) == abs(ligne_depart - ligne_arrivee):
                step_col = 1 if colonne_arrivee > colonne_depart else -1
                step_row = 1 if ligne_arrivee > ligne_depart else -1
                clear_path = True
                for step in range(1, abs(colonne_depart - colonne_arrivee)):
                    if matrice[ligne_depart + step * step_row][colonne_depart + step * step_col] != 0:
                        clear_path = False
                        break
                if clear_path and (piece_arrivee == 0 or (piece_arrivee != 0 and adverse_piece(piece_arrivee))):
                    return True
        elif type_piece == pieces['tour']:
            if ligne_depart == ligne_arrivee or colonne_depart == colonne_arrivee:
                if ligne_depart == ligne_arrivee:
                    step = 1 if colonne_arrivee > colonne_depart else -1
                    clear_path = all(matrice[ligne_depart][col] == 0 for col in range(colonne_depart + step, colonne_arrivee, step))
                else:
                    step = 1 if ligne_arrivee > ligne_depart else -1
                    clear_path = all(matrice[row][colonne_depart] == 0 for row in range(ligne_depart + step, ligne_arrivee, step))
                if clear_path and (piece_arrivee == 0 or (piece_arrivee != 0 and adverse_piece(piece_arrivee))):
                    return True
        elif type_piece == pieces['reine']:
            if abs(colonne_depart - colonne_arrivee) == abs(ligne_depart - ligne_arrivee):
                step_col = 1 if colonne_arrivee > colonne_depart else -1
                step_row = 1 if ligne_arrivee > ligne_depart else -1
                clear_path = True
                for step in range(1, abs(colonne_depart - colonne_arrivee)):
                    if matrice[ligne_depart + step * step_row][colonne_depart + step * step_col] != 0:
                        clear_path = False
                        break
                if clear_path and (piece_arrivee == 0 or (piece_arrivee != 0 and adverse_piece(piece_arrivee))):
                    return True
            elif ligne_depart == ligne_arrivee or colonne_depart == colonne_arrivee:
                if ligne_depart == ligne_arrivee:
                    step = 1 if colonne_arrivee > colonne_depart else -1
                    clear_path = all(matrice[ligne_depart][col] == 0 for col in range(colonne_depart + step, colonne_arrivee, step))
                else:
                    step = 1 if ligne_arrivee > ligne_depart else -1
                    clear_path = all(matrice[row][colonne_depart] == 0 for row in range(ligne_depart + step, ligne_arrivee, step))
                if clear_path and (piece_arrivee == 0 or (piece_arrivee != 0 and adverse_piece(piece_arrivee))):
                    return True
        elif type_piece == pieces['roi']:
            if abs(colonne_depart - colonne_arrivee) <= 1 and abs(ligne_depart - ligne_arrivee) <= 1:
                if piece_arrivee == 0 or (piece_arrivee != 0 and adverse_piece(piece_arrivee)):
                    return True
    return False

def initialiser_matrice_jeu():
    matrice = [[0 for _ in range(8)] for _ in range(8)]
    
    # Placer les pions
    for i in range(8):
        matrice[1][i] = pieces['pion'] * -1  # Pions du joueur 2 (négatif)
        matrice[6][i] = pieces['pion']  # Pions du joueur 1 (positif)
    
    # Placer les pièces principales
    pieces_order = [
        pieces['tour'], pieces['cavalier'], pieces['fou'], pieces['reine'],
        pieces['roi'], pieces['fou'], pieces['cavalier'], pieces['tour']
    ]
    
    for i in range(8):
        matrice[0][i] = pieces_order[i] * -1  # Pièces du joueur 2 (négatif)
        matrice[7][i] = pieces_order[i]  # Pièces du joueur 1 (positif)
    
    return matrice

def verifier_victoire(matrice, joueur):
    roi_joueur_1 = False
    roi_joueur_2 = False
    
    for ligne in matrice:
        if pieces['roi'] in ligne:
            roi_joueur_1 = True
        if -pieces['roi'] in ligne:
            roi_joueur_2 = True
    
    if not roi_joueur_1:
        return 2  # Joueur 2 gagne
    if not roi_joueur_2:
        return 1  # Joueur 1 gagne
    
    return False  # Pas de victoire

def jouer():
    matrice = initialiser_matrice_jeu()
    joueur_actuel = 1
    
    while True:
        print(f"\nJoueur {joueur_actuel}, c'est votre tour.\n")
        for ligne in matrice:
            print(ligne)
        
        echec, echec_et_mat = est_en_echec_et_mat(matrice, joueur_actuel)
        if echec:
            if echec_et_mat:
                print(f"Le joueur {joueur_actuel} est en échec et mat. Le joueur {3 - joueur_actuel} gagne!")
                break
            else:
                print(f"Le joueur {joueur_actuel} est en échec. Vous devez jouer votre roi.")
        
        while True:
            ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, type_piece = demander_coordonnees()
            
            if echec and type_piece != pieces['roi']:
                print("Erreur : Vous êtes en échec. Vous devez déplacer votre roi.")
                continue

            piece = matrice[ligne_depart][colonne_depart]
            if (joueur_actuel == 1 and piece <= 0) or (joueur_actuel == 2 and piece >= 0):
                print("Erreur : Vous devez déplacer une de vos propres pièces.")
                continue
            
            if not mouvement_est_valide(matrice, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, type_piece):
                print("Erreur : Mouvement invalide.")
                continue
            
            matrice[ligne_depart][colonne_depart] = 0
            matrice[ligne_arrivee][colonne_arrivee] = piece
            break
            
        victoire = verifier_victoire(matrice, joueur_actuel)
        if victoire:
            print(f"Le joueur {victoire} gagne!")
            break
        
        joueur_actuel = 3 - joueur_actuel  # Déplacer cette ligne ici

jouer()

"""
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

print("\nEffectuer le mouvement:")
if mouvement_piece(matrice, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, type_piece):
    print("Mouvement réussi!")
else:
    print("Mouvement invalide.")


print("\nMatrice après le mouvement:")
for row in matrice:
    print(row)
"""