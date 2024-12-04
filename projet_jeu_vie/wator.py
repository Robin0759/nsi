import matplotlib, pylab as plt, random, numpy, time

n_lignes = 25
n_colonnes = 25


n_thon = 0
n_requin = 0

energie_init_thon = 10
energie_init_requin = 3
temps_gestation_thon = 2
temps_gestation_requin = 5



class Animal():
    
    def __init__(self, id, energie_base, temps_gestation, x, y):
        self.id = id
        self.energie_base = energie_base
        self.temps_gestation = temps_gestation
        self.gestation = 0
        self.x = x
        self.y = y
    
class Wator():

    def __init__(self, hauteur, largeur):

        self.hauteur = hauteur
        self.largeur = largeur
        self.grille = numpy.zeros((hauteur, largeur), object)
        self.animaux = []

    def peupler(self, n_thon, n_requin, energie_thon, energie_requin, gestation_thon, gestation_requin):
        #ajouter thons
        for _ in range(n_thon):
            self.ajouter_animal(1, energie_thon, gestation_thon)
            
        for _ in range(n_requin):
            self.ajouter_animal(2, energie_requin, gestation_requin)

    def ajouter_animal(self, id, energie_base, temps_gestation):
        while True:
            x, y = random.randint(0, self.largeur-1), random.randint(0, self.hauteur-1)
            if self.grille[y][x] == 0:
                animal = Animal(id, energie_base, temps_gestation, x,y)
                self.grille[y][x] = animal
                self.animaux.append(animal)
                break


    def voisin(self, x, y):
        voisins = []
        for dx, dy in ((0, -1),(1,0),(0,1),(-1,0)):
            xp, yp = (x+dx) % self.largeur, (y+dx) % self.hauteur
            voisins.append(xp, yp)
        return voisins


    def deplacer(self, animal, x, y):
        self.grille[animal.y][animal.x] = 0
        animal.x, animal.y = x, y
        self.grille[y][x] = animal
        animal.gestation +=1
    
    def evolution(self, animal):
        voisin = self.voisin(animal.x, animal.y)
        case = None
        self.gestation += 1
        déplacement = False
        xp, yp = random

        if not déplacement:
            try:
                xp, yp = random.choice([position for position in voisin if voisin[position]==case]), random.choice([position for position in voisin if voisin[position]==case])
                if animal.id != 1:
                    animal.energie -= 1
                déplacement = True
            except IndexError:
              
                xp, yp = animal.x, animal.y
                
                
        if animal.energie < 0:
            animal.vie = False
            self.grille[animal.y][animal.x] = case
        elif déplacement:
            x, y = animal.x, animal.y
            animal.x, animal.y = xp, yp
            self.grille[yp][xp] = animal
            if animal.gestation >= animal.temps_gestation:
                animal.gestation = 0
                self.pop_animal(animal.id, x, y)
            else:
                self.grille[y][x] = case
                



    def progression(self):
        random.shuffle(self.animal)
        
        n_animal = len(self.animal)
        for i in range(n_animal):
            animal = self.animal[i]
            if not animal.vie:
                continue
            self.evolution(animal)
            
        self.animaux = [animal for animal in self.animaux if self.animaux.vie]
    
    
    def manger(self, requin, x, y):
        self.grille[y][x].vie = False
        self.grille[y][x] = 0
        self.deplacer(requin)
        requin.energie = 3
    
    
    def reproduction(self, animal):
        animal.gestation = 0
        self.ajouter_animal(animal.id, animal.energie, animal.temps_gestation)
        
    def evolution(self, animal):
        voisins = self.voisin(animal, vx, vy)
        random.shuffle(voisins)
        
        if animal.id == 1:
            for vx, vy in voisins:
                if self.grille[vx][vy] == 0:
                    self.deplacer(animal, vx, vy)
                    if animal.gestation >= animal.temps_gestation:
                        self.reproduction(animal)
                    return

        elif animal.id == 2:
            for vx, vy in voisins:
                if isinstance(self.grille[vy][vx], Animal) and self.grille[vy][vx].id == 1:
                    self.manger()
                    
    
    def afficher(self):
        
        image = numpy.zeros((self.hauteur, self.largeur))
        for y in range(self.hauteur):
            for x in range(self.largeur):
                if isinstance(self.grille[y][x], Animal):
                    if self.grille[y][x].id == 1:
                        image[y,x] = 1
                    elif self.grille[y][x].id == 2:
                        image[y,x] = 2
        plt.imshow(image, cmap="viridis", interpolation="nearest")
        plt.colorbar(ticks=[0,1,2], label="0: vide | 1: thon | 2: requin")
        plt.title("Simulation de Wator")
        plt.show()


"""
    def structure(self):
        animal = Animal(self.id, self.energie_base[self.id], self.temps_gestation[self.id], random.randint(1,25), random.randint(1,25))
        self.animaux.append(animal)
        self.grille[y][x] = animal


    def peupler(self, n_thon = 30, n_requin = 10):
        self.n_thon = n_thon
        self.n_requin = n_requin


    def generer_placement(self, n_animaux, a_id):

        for i in range(n_animaux):
            while True:
                x, y = divmod(random.randrange(self.nbcase), self.hauteur)
                if not self.grid[y][x]:
                    self.pop_animal(a_id, x, y)
                    break       
    generer_placement(n_thon, thon)
    generer_placement(n_requin, requin)
    

    
    def tableau_grille(self):
        return [[self.grille[y][x].id if self.grille[y][x] else 0
                    for x in range(self.largeur)] for y in range(self.hauteur)]



        
    def voisin(self, x, y):
        
        voisin = {}
        for dx, dy in ((0,-1), (1,0), (0,1), (-1,0)):
            xp, yp = (x+dx) % self.largeur, (y+dy) % self.hauteur
            voisin[xp,yp] = self.grille[yp][xp]
        return voisin



    def evolution(self, animal):
        voisin = self.voisin(animal.x, animal.y)
        déplacement = False
            try:
                xp, yp = random.randint(1, 25), random.randint(1, 25)
        
        if not déplacement:
            try:
                xp, yp = random.choice([position
                            for position in voisin if voisin[position]==case])
                if animal.id != thon:
                    animal.energie -= 1
                déplacement = True
            except IndexError:
              
                xp, yp = animal.x, animal.y
                
                
        if animal.energie < 0:
            
            animal.vie = False
            self.grille[animal.y][animal.x] = case
        elif déplacement:
            x, y = animal.x, animal.y
            animal.x, animal.y = xp, yp
            self.grille[yp][xp] = animal
            if animal.gestation >= animal.temps_gestation:
                animal.gestation = 0
                self.pop_animal(animal.id, x, y)
            else:
                self.grille[y][x] = case
                



    def progression(self):
        random.shuffle(self.animal)
        
        n_animal = len(self.animal)
        for i in range(n_animal):
            animal = self.animal[i]
            if not animal.vie:
                continue
            self.evolution(animal)
            
        self.animaux = [animal for animal in self.animaux if animaux.vie]
        



    def image_grille(self):
            
            img = self.tableau_grille()
            trace = matplotlib.figure(figsize=(10, 5), dpi = 36)
            axe = fig.add_subplot(100)
            return trace
        
        def afficher_image(self):
            trace = self.image_grill()
            matplotlib.show()"""