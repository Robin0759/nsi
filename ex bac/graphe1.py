adj = [[1, 2], [2], [0],[0]]

def voisins_entrants(adj, x):
    '''
    param adj: liste d'adjacence
    param x: sommet dont on veut connaitre les voisins
    return: liste des voisins d'un sommet
    '''
    return adj[x]

print(voisins_entrants([[1, 2], [2], [0], [0]], 0))


def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s en appliquant le procédé de lecture.
    >>> nombre_suivant('1211')
    '111221'
    >>> nombre_suivant('311')
    '1321'
    '''
    
    
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1,len(s)): 
        if s[i] == chiffre:
            compte = compte + 1
        else:
            resultat += str(compte) + chiffre
            chiffre = s[i]
            compte = 1
    lecture_chiffre = str(compte) + chiffre 
    resultat += lecture_chiffre
    return resultat

print(nombre_suivant('311'))