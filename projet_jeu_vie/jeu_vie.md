# partie A  |  Modélisation objet


## 1. Quelles classes peut-on dégager de ce problème au premier abord ?
- De prime abord nous pourrions penser à créer les classes 'grille' et 'cellule' en observant ce problème.


## 2. Quelles sont quelques-unes des méthodes qu'on pourrait leur donner ?
 - méthodes pour la classe CELLULE: etat_actuel / calcul_etat_futur / voisins / str
 - méthodes pour la classe GRILLE: setXY, getXY, get_largeur, get_hauteur, est_voisin. 
## 3. Dans quelle classe pouvons-nous représenter simplement la notion de voisinnage d'une cellule ?

Nous pouvons représenter simplement la notion de voisinage d'une cellule dans la la classe GRILLE, idem pour le calcul.

## 4. Une cellule est au bord si x=0, x= L-1, y=0 ou y=H-1. Combien de voisins possède une cellule qui n'est pas au bord  ? Combien de voisins possède une cellule qui est au bord ?

## 5. Que pourions-nous aussi considérer comme voisins de droite de la case en haut à droite de la grille ? Et comme voisin du haut ?

La grille créé est comparable à quelque chose qui ne se termine jamais, c'est à dire que le voisin de droite de la case en haut à droite est la case en haut à gauche. Le voisin du haut sera donc le bas. 