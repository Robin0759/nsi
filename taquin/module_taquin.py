import random

class Taquin:
    def __init__(self):
        self.grille = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]


    #verifie si la valeur est 0 <= valeur <= 15
    def dans_intervale(self, nombre):
        if 0 <= nombre <= 15:
            return True
        else:
            return False


    def acc_valeur(self, indice):
        '''
        renvoie le contenu de la case d'indice précisé avec 0 <= indice <= 15
        : param indice : (int)
        : return : contenu de la case d'indice donné
        >>> t = Taquin()
        >>> t.acc_valeur(0)
        1
        >>> t.acc_valeur(10)
        11
        >>> t.acc_valeur(15)
        0
        '''

        if self.dans_intervale(indice):
            return self.grille[indice]
    

    
    def mut_valeur(self, indice , valeur):
        '''
        modifie le contenu de la case d'indice précisé avec 0 <= indice <= 15 
        en y plaçant la valeur précisée avec 0 <= valeur <= 15
        : param indice : (int)
        : param valeur : (int)
        : Pas de return, self est modifié par effet de bord
        >>> t = Taquin()
        >>> t.mut_valeur(0, 1)
        >>> t.acc_valeur(0)
        1
        >>> t.mut_valeur( , )
        >>> t.acc_valeur( )
        '''

        if self.dans_intervale(indice) and self.dans_intervale(valeur):
            self.grille[indice] = valeur



    def acc_indice(self, valeur):
        '''
        renvoie l'indice de la case de la grille qui contient la valeur précisée
        avec 0 <= valeur <= 15
        : param valeur : (int)
        : return : indice de la case de la grille qui contient la valeur précisée
        >>> t = Taquin()
        >>> t.acc_indice(10)
        10
        >>> t.acc_indice(0)
        15
        '''
        if self.dans_intervale(valeur):
            return self.grille.index(valeur)




    def est_vide(self, indice) :
        '''
        renvoie True si (0 <= indice <= 15 et la case d'indice précisé est vide)
        et False sinon
        : param indice : (int)
        : return : True ou False, respectivement la case est vide, la case n'est pas vide
        >>> t = Taquin()
        >>> t.est_vide(5)
        False
        >>> t.est_vide(15)
        True
        '''

        if self.dans_intervale(indice):
            if self.acc_valeur(indice) == 0:
                return True
            else:
                return False
    
    def est_gagne(self):
        '''
        renvoie True si la grille est en position initiale et False sinon
        : return : True si la grille est en position initiale, False sinon
        >>> t = Taquin()
        >>> t.est_gagne()
        True
        >>> t.est_gagne()
        False
        '''

        if self.grille == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
            return True
    
    
    
    def est_possible(self, valeur) :
        '''
        renvoie True si la case contenant la valeur (entre 0 et 15)
        passée en paramète est déplaçable et False sinon
        : param valeur (int) avec 0 < valeur <= 15
        : return (boolean)
        >>> t = Taquin()
        >>> t.est_possible(12)
        True
        >>> t.est_possible(11)
        False
        '''
        if self.dans_intervale(valeur):
            #initialise les conditions
            index_valeur = self.acc_indice(valeur)
            index_case_vide = self.grille.index(0)

            x_valeur = index_valeur % 4
            y_valeur = index_valeur // 4

            x_case_vide = index_case_vide % 4
            y_case_vide = index_case_vide // 4
            # distance de Manhattan
            if abs(x_valeur-x_case_vide) + abs(y_valeur-y_case_vide) == 1:
                return True
            else:
                return False

    def deplacer(self, valeur) :
        '''
        deplace, si cela est possible, la case contenant la valeur précisée
        en paramètre (entre 1 et 15) dans la case vide. Si le déplacement n'est pas 
        possible, il ne se passe rien.
        : param valeur : (int)
        : pas de return mais self est mofifié par effet de bord
        >>> t = Taquin()
        >>> t.deplacer(12)
        >>> t.deplacer(1)
        déplacement impossible
        '''
        if self.est_possible(valeur):
            index_nb_demande = self.grille.index(0)
            index_nb_echange = self.acc_indice(valeur)

            valeur_nb_demande = self.grille[self.grille.index(0)]
            valeur_nb_echange = valeur

            self.grille[index_nb_demande] = valeur_nb_echange
            self.grille[index_nb_echange] = valeur_nb_demande

        else:
            return 'déplacement impossible'


    def valeurs_deplacables(self):
        '''
        renvoie une liste des valeurs des cases déplaçables
        : return (list)
        >>> t = Taquin()
        >>> t.valeurs_deplacables()
        [12, 15]
        >>> t.deplacer(12)
        >>> t.valeurs_deplacables()
        [8, 11, 12]
        '''

        index_case_vide = self.grille.index(0)

        x_vide = index_case_vide%4
        y_vide = index_case_vide//4

        voisins = [(x_vide-1, y_vide), (x_vide+1, y_vide), (x_vide, y_vide-1), (x_vide, y_vide+1)]
        
        #filtre les voisins en dehors du cadre
        voisins_fin = []

        for x, y in voisins:
            if 0<=x<4 and 0<=y<4:
                indice_voisins = x + y*4
                voisins_fin.append(self.grille[indice_voisins])

        return voisins_fin



    def melanger(self, niveau):
        '''
        melange le jeu
        :param niveau: (int) niveau de jeu

        '''
        
        if niveau == 0:
            for _ in range(5):
                self.deplacer(random.choice(self.valeurs_deplacables()))
        
        if niveau == 1:
            for _ in range(10):
                self.deplacer(random.choice(self.valeurs_deplacables()))
        
        if niveau == 2:
            for _ in range(30):
                self.deplacer(random.choice(self.valeurs_deplacables()))
        
        if niveau == 3:
            for _ in range(100):
                self.deplacer(random.choice(self.valeurs_deplacables()))
        
        if niveau == 4:
            for _ in range(200):
                self.deplacer(random.choice(self.valeurs_deplacables()))


    def __str__(self):
        '''
        Renvoie une chaîne de caractères pour représenter la grille.
        :return: str
        '''
        chaine = ''
        separateur = "+----+----+----+----+\n"  # Séparateur horizontal

        for y in range(4):  # Parcourir les lignes (indices y)
            chaine += separateur  # Ajouter le séparateur au début de chaque ligne
            ligne = ''
            for x in range(4):  # Parcourir les colonnes (indices x)
                n = x + y * 4  # Calculer l'indice de la case dans la liste
                valeurs = self.grille[n]  # Récupérer la valeur correspondante
                # Ajouter la valeur formatée ou un espace vide pour 0
                if valeurs == 0:
                    ligne += "|    "
                else:
                    # Après un peu de galère et plusieurs recherches, j'ai découvert le formatage python '^' qui permet d'aligner des éléments au centre d'une chaîne de caractère.
                    # Il en existe plusieurs:     '<': alignement à gauche     '^': alignement au centre     '>': alignement à droite
                    # Ainsi:  'valeurs': valeur affichée     '^': alignement au centre     '4': chaine de 4 caractères
                    ligne += f"|{valeurs:^4}" 
            chaine += ligne + "|\n"  # Terminer la ligne avec une barre verticale et un retour à la ligne
        chaine += separateur  # Ajouter le dernier séparateur en bas
        return chaine

    def __repr__(self):
        représentation = f"Nom de la classe: {self.__class__.__name__}\ngrille: {self.grille}\n"
        return représentation