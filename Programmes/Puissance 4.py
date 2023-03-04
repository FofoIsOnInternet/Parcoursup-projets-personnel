def joue_coup (tab:list,joueur:str,n_colonne:int)-> list :
    """revoie le tableau avec le coup du joueur
    Entrée :
        tab: liste contenant le plateau de jeu
        joueur: chaine de caractère indiquant le joueur en train de jouer
        n_colonne: entier indiquant la colonne dans lequel le coup est joué
    Sortie :
        tab"""
    if n_colonne > 6 or n_colonne < 0 :
        print ("Le numéreau de la colonne doit être compris entre 0 et 6")
        return tab
    if colonne_pleine (tab,n_colonne) == True :
        print ("cette colonne est pleine")
        return tab
    for k in range (len(tab)):
        if tab[len(tab)-k-1] [n_colonne-1] == " " :
            tab[len(tab)-k-1] [n_colonne-1] = joueur
            return tab


def colonne_pleine (tab:list,n_colonne:int)->bool:
    """renvoie un booléen différent si la colonne ou veut jouer le joueur est pleine ou non
    Entrée :
        tab: liste contenant le plateau de jeu
        n_colonne: entier indiquant la colonne dans lequel le coup est joué
    Sortie :
        booléen 
    """
    if tab [0][n_colonne-1] == " " :
        return False
    else :
        return True


def genere_tab():
    """génère un tableau de 6 X 7 """
    tab = [[" "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "],
           [" "," "," "," "," "," "," "]]

    return tab


def affiche(tab:list):
    """affiche un tableau"""
    print(" ","1"," ","2"," ","3"," ","4"," ","5"," ","6")
    for i in range(len(tab)-1):
        print("├",tab[i][0], "|",tab[i][1], "|",tab[i][2], "|",tab[i][3], "|",tab[i][4], "|",tab[i][5], "┤")
    print("├",tab[5][0],"|",tab[5][1],"|",tab[5][2],"|",tab[5][3],"|",tab[5][4],"|",tab[5][5],"┤")
    print("└","─","┴","─","┴","─","┴","─","┴","─","┴","─","┘")


def align_horiz (tab:list)-> bool :
    """renvoie True si un alignement horizontal est observé"""
    for j in range (5):
        for i in range (4):
            if tab [j][i] != " " and tab [j][i] == tab [j][i+1] and tab [j][i] == tab [j][i+2] and tab [j][i] == tab [j][i+3] :
                print ("joueur" , tab [j][i], "à gagné")
                return True
    return False


def align_verti(tab:list)->bool:
    """renvoie True si un alignement vertcale est observé"""
    for j in range(6):
        for i in range(2):
            if tab [i][j] != " " and tab [i][j] == tab [i+1][j] and tab [i][j] == tab [i+2][j] and tab [i][j] == tab [i+3][j] :
                print ("joueur" , tab [i][j], "à gagné")
                return True
    return False


def align_diag_prin (tab:list)->bool :
    """renvoie True si un alignement diagonale principal est observé"""
    for j in range(3):
        for i in range (2):
            if tab [i][j] != " " and tab [i][j] == tab [i+1][j+1] and tab [i][j] == tab [i+2][j+2] and tab [i][j] == tab [i+3][j+3] :
                print ("joueur" , tab [i][j], "à gagné")
                return True
    return False


def align_diag_sec (tab:list)->bool :
    """renvoie True si un alignement diagonale secondaire est observé"""
    for j in range(3,6):
        for i in range (2):
            if tab [i][j] != " " and tab [i][j] == tab [i-1][j-1] and tab [i][j] == tab [i-2][j-2] and tab [i][j] == tab [i-3][j-3] :
                print ("joueur" , tab [i][j], "à gagné")
                return True
    return False


def gagne_ou_pas (tab:list)->bool:
    """execute les fonctions pour vérifier qi l'un des deux joueurs a gagné"""
    if align_horiz(tab) == True :
        return True
    if align_verti(tab) == True:
        return True
    if align_diag_prin(tab) == True:
        return True
    if align_diag_sec(tab) == True:
        return True
    return False


joueur = "X"
tab = genere_tab()

affiche(tab)
        
while gagne_ou_pas(tab) == False :

    affiche(joue_coup(tab, joueur,int(input("Dans quelle colonne voulez vous jouer ?"))))

    if joueur == "X":
        joueur = "O"

    else:
        joueur = "X"