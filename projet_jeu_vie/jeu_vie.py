import random


# implémentation de la classe cellule
class Cellule:
    def __init__(self, x, y):
        self.actuel = False
        self.futur = False
        self.voisins = []
        self.x = x
        self.y = y

    #est_vivant : renvoie l'état actuel de la cellule
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
        self.actuel = self.futur
    

    # __str__ : renvoie l'élément défini quand la fonction est appelée en tant que string
    def __str__(self) -> str:
        return 'x' if self.actuel else '-'
    

    # fais les actions nécessaires à l'évolution du jeu de la vie
    def calcule_etat_futur(self):
        nb_voisins = len(self.voisins)
        if self.actuel == True:
            if nb_voisins != 2 or nb_voisins != 3:
                self.futur = False
            else:
                self.futur = True
        
        else:
            if self.voisins == 3:
                self.futur = True



class Grille:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.matrix = [[Cellule(x, y) for x in range(largeur)] for y in range(hauteur)]
        self.cellule = Cellule(largeur, hauteur)


    def dans_grille(self, x, y):
        if 0 <= x < self.largeur and 0 <= y < self.hauteur:
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



    def affecte_voisins(self):
        for _ in self.hauteur:
            for _ in self.largeur:
                self.get_voisins()

    def __str__(self):
        grille_str = ""
        for ligne in self.matrix:
            grille_str += "".join(str(cell) for cell in ligne) + "\n"
        return grille_str

    def remplir_alea(self, taux):
        for ligne in self.matrix:
            for cell in ligne:
                cell.actuel = random.random() < taux

    def jeu(self):
        # Calculer l'état futur de toutes les cellules
        for ligne in self.matrix:
            for cell in ligne:
                cell.calcule_etat_futur()



    def actualise(self):
        for ligne in self.matrix:
            for cell in ligne:
                cell.basculer()
    

def main():
    grille = Grille(10, 10)
    grille.remplir_alea(0.1)
    print(str(grille))
    grille.jeu()
    grille.actualise()
    print(str(grille))


main()