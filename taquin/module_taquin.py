class Taquin:
    def __init__(self):
        self.grille = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

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

        if 0 <= indice <= 15:
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

        if 0 <= indice <= 15 and 0 <= valeur <= 15:
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
        if 0 <= valeur <= 15:
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

        if 0 <= indice <= 15:
            if self.grille[indice] == 0:
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
    
    def __str__(self) :
        '''
        renvoie une chaine de caractères pour représenter la grille.
        : return (str)
        '''
        
        for n in range(16):
            print(f'{len(str(self.grille[n]))}, "{self.grille[n]}"')
            if len(str(self.grille[n])) == 1:
                element = f"  {str(self.grille[n])} "
            else:
                element = f" {self.grille[n]} "
        
        chaine = f'+----+----+----+----+\n|{element}|{element}|{element}|{element}|\n+----+----+----+----+\n|{element}|{element}|{element}|{element}|\n+----+----+----+----+\n|{element}|{element}|{element}|{element}|\n+----+----+----+----+\n|{element}|{element}|{element}|{element}|\n+----+----+----+----+'
        return chaine

t = Taquin()
print(str(t))