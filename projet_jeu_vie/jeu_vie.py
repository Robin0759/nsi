import random


# implémentation de la classe cellule
class Cellule:
    def __init__(self, x, y):
        self.actuel = False
        self.futur = False
        self.voisins = []
        self.x = x
        self.y = y

    #est_vivant : renvoie l'état actueel de la cellule
    def est_vivant(self):
        if self.actuel == True:
            return True
        if self.actuel == False:
            return False


    # set_voisins : affecte comme voisins la liste passée en paramètre
    def set_voisins(self, voisins:list):
        self.voisins = voisins

    
    # get_voisins : renvoie la liste des voisins de la Cellule
    def get_voisins(self):
        return self.voisins


    # naitre : défini l'état futur d'une Cellule comme vivante
    def naitre(self):
        self.futur = True
    

    # mourir : défini l'état futur d'une Cellule comme morte
    def mourir(self):
        self.futur = False
    
    
    # basculer : met à jour les états des Cellule
    def basculer(self):
        self.futur = self.actuel
    

    # __str__ : renvoie l'élément défini quand la fonction est appelée en tant que string
    def __str__(self) -> str:
        if self.actuel == True:
            return 'x'
        else:
            return '-'
    

    # fais les actions nécessaires à l'évolution du jeu de la vie
    def calcule_etat_futur(self):
        if self.actuel == True:
            if self.voisins == 2 or self.voisins == 3:
                pass
            else:
                self.actuel == False
        
        elif self.actuel == False:
            if self.voisins == 3:
                self.actuel == True



class Grille:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.matrix = [[Cellule(largeur, hauteur) for _ in range(largeur)] for _ in range(hauteur)]
        cellule = Cellule(largeur, hauteur)


    def dans_grille(self, x, y):
        if 0 < x < self.largeur or 0 < y < self.hauteur:
            return True

    def setXY(self, x, y):
        self.largeur = x
        self.hauteur = y

    def getXY(self, x, y):
        return self.matrix[x][y]

    def get_largeur(self):
        return self.largeur

    def get_hauteur(self):
        return self.hauteur


    # aide exterieure
    def get_voisins(self, x, y):    
        # Parcourt toutes les positions voisines possibles (-1, 0, +1 sur x et y)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # Ignore la cellule elle-même
                if dx == 0 and dy == 0:
                    continue

                # Coordonnées potentielles du voisin
                nx, ny = x + dx, y + dy

                # Ajoute le voisin seulement s'il est dans les limites de la grille
                if self.dans_grille(nx, ny):
                    self.cellule.voisins.append((nx, ny))

        return self.cellule.voisins


    def get_voisins(self):
        return self.cellule.voisins

    def affecte_voisins(self):
        for _ in self.hauteur:
            for _ in self.largeur:
                self.get_voisins()

    def __str__(self):
        for i in range(self.largeur):
            for j in range(self.hauteur):
                return Cellule(i, j)


    def remplir_alea(self, taux):
        rand1 = random.randint(1, self.hauteur)
        rand2 = random.randint(1, self.largeur)
        for i in range(rand1):
            for j in range(rand2):
                self.matrix[i][j].actuel = True



print(str(Grille(10,10)))