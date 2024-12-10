from module_taquin import *

taquin = Taquin()



def demarrer_jeu():
    nb_deplacement = 0

    level = int(input('Quel niveau de jeu vouslez-vous ? (0, 1, 2, 3, 4)'))
    taquin.melanger(level)
    print(taquin)

    while not taquin.est_gagne():
        deplacement = int(input('Quelle case souhaitez vous déplacer ? '))
        if deplacement in taquin.valeurs_deplacables():
            nb_deplacement += 1
            taquin.deplacer(deplacement)
            print(taquin)
    print(taquin)
    print(f"Félicitation, vous avez gagné... la gloire d'avoir gagné. C'est déjà pas mal ;)\nVous avez fait {nb_deplacement} déplacements pour un niveau {level}")



demarrer_jeu()