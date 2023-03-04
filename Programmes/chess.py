# -*- coding: utf-8 -*-
"""
Created on Fri May 27 16:30:16 2022

@author: faust
"""
import tkinter as tk

#--------------------------------------------------------------GLOBAL VAR-----------------------------------------------------------------------------


# définition des pièces du jeu par défaut
global Pieces
Pieces = [{"id":0 , "name":"pawn" , "color":"black" , "coords":(0,6) , "status":"alive" , "symbol":"♟" , "value":1},
              {"id":1 , "name":"pawn" , "color":"black" , "coords":(1,6) , "status":"alive" , "symbol":"♟" , "value":1},
              {"id":2 , "name":"pawn" , "color":"black" , "coords":(2,6) , "status":"alive" , "symbol":"♟" , "value":1},
              {"id":3 , "name":"pawn" , "color":"black" , "coords":(3,6) , "status":"alive" , "symbol":"♟" , "value":1},
              {"id":4 , "name":"pawn" , "color":"black" , "coords":(4,6) , "status":"alive" , "symbol":"♟" , "value":1},
              {"id":5 , "name":"pawn" , "color":"black" , "coords":(5,6) , "status":"alive" , "symbol":"♟" , "value":1},
              {"id":6 , "name":"pawn" , "color":"black" , "coords":(6,6) , "status":"alive" , "symbol":"♟" , "value":1},
              {"id":7 , "name":"pawn" , "color":"black" , "coords":(7,6) , "status":"alive" , "symbol":"♟" , "value":1},
              {"id":8 , "name":"rook" , "color":"black" , "coords":(0,7) , "status":"alive" , "symbol":"♜" , "value":5},
              {"id":9 , "name":"rook" , "color":"black" , "coords":(7,7) , "status":"alive" , "symbol":"♜" , "value":5},
              {"id":10 , "name":"knight" , "color":"black" , "coords":(1,7) , "status":"alive" , "symbol":"♞" , "value":3},
              {"id":11 , "name":"knight" , "color":"black" , "coords":(6,7) , "status":"alive" , "symbol":"♞" , "value":3},
              {"id":12 , "name":"bishop" , "color":"black" , "coords":(2,7) , "status":"alive" , "symbol":"♝" , "value":3},
              {"id":13 , "name":"bishop" , "color":"black" , "coords":(5,7) , "status":"alive" , "symbol":"♝" , "value":3},
              {"id":14 , "name":"queen" , "color":"black" , "coords":(3,7) , "status":"alive" , "symbol":"♛" , "value":9},
              {"id":15 , "name":"king" , "color":"black" , "coords":(4,7) , "status":"alive" , "symbol":"♚"},
              {"id":16 , "name":"pawn" , "color":"white" , "coords":(0,1) , "status":"alive" , "symbol":"♙" , "value":1},
              {"id":17 , "name":"pawn" , "color":"white" , "coords":(1,1) , "status":"alive" , "symbol":"♙" , "value":1},
              {"id":18 , "name":"pawn" , "color":"white" , "coords":(2,1) , "status":"alive" , "symbol":"♙" , "value":1},
              {"id":19 , "name":"pawn" , "color":"white" , "coords":(3,1) , "status":"alive" , "symbol":"♙" , "value":1},
              {"id":20 , "name":"pawn" , "color":"white" , "coords":(4,1) , "status":"alive" , "symbol":"♙" , "value":1},
              {"id":21 , "name":"pawn" , "color":"white" , "coords":(5,1) , "status":"alive" , "symbol":"♙" , "value":1},
              {"id":22 , "name":"pawn" , "color":"white" , "coords":(6,1) , "status":"alive" , "symbol":"♙" , "value":1},
              {"id":23 , "name":"pawn" , "color":"white" , "coords":(7,1) , "status":"alive" , "symbol":"♙" , "value":1},
              {"id":24 , "name":"rook" , "color":"white" , "coords":(0,0) , "status":"alive" , "symbol":"♖" , "value":5},
              {"id":25 , "name":"rook" , "color":"white" , "coords":(7,0) , "status":"alive" , "symbol":"♖" , "value":5},
              {"id":26 , "name":"knight" , "color":"white" , "coords":(1,0) , "status":"alive" , "symbol":"♘" , "value":3},
              {"id":27 , "name":"knight" , "color":"white" , "coords":(6,0) , "status":"alive" , "symbol":"♘" , "value":3},
              {"id":28 , "name":"bishop" , "color":"white" , "coords":(2,0) , "status":"alive" , "symbol":"♗" , "value":3},
              {"id":29 , "name":"bishop" , "color":"white" , "coords":(5,0) , "status":"alive" , "symbol":"♗" , "value":3},
              {"id":30 , "name":"queen" , "color":"white" , "coords":(4,0) , "status":"alive" , "symbol":"♕" , "value":1},
              {"id":31 , "name":"king" , "color":"white" , "coords":(3,0) , "status":"alive" , "symbol":"♔"},
              {"name":"", "symbol":" "}]

# définition des profiles de joueurs
global Players
Players = [{"id":0 , "name":"" , "color":"white" , "points":0 },
               {"id":1 , "name":"" , "color":"black" , "points":0 }]

# global_info --> information utiles partout , variables condensé en un dictionaire
global global_info
global_info = {"game":False , "turn":0 , "b_click":0 , "start_square":(8,0) , "end_square":(8,0) , "board_sense":1}

# game --> indique si une partie est en cours
# turn --> indique à qui est le tour en indiquant l'id du joueur
# b_click --> indique si une pièce a déjà été sélectioné pour être déplacé (0-> pièce non-selectioné | 1-> pièce selectioné | 2-> coup a été joué | 3-> mauvais coup)
# start_square --> indique les coordonnées de la pièce sélectioner
# end_square --> indique les coordonnées où va aller là pièce


# board_squares --> frame avec l'echequier
# board_pieces --> simulation de l'échequier avec l'id de chaque pièce (32 s'il n'y en a pas)


#-----------------------------------------------------------GAME-FUNCTIONS------------------------------------------------------------------------------------


def next_turn ():
    if global_info["turn"] == 0 :
            global_info["turn"] = 1
    else :
            global_info["turn"] = 0


def eat (piece_id:int):
    # change le status de la pièce à "dead"
    Pieces [piece_id] ["status"] = "dead"
    # ajoute le bon nombre de point au joueur qui a mangé la pièce
    Players [ global_info["turn"] ] ["points"] = Players [ global_info["turn"] ] ["points"] + Pieces [piece_id]["value"]


def simu_coords ():
    """simule la position de chaque pièce pour permettre à chaque boutton d'identifier quel pièce à afficher"""
    global board_pieces
    board_pieces = [[32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32],[32,32,32,32,32,32,32,32],[32]]
    for piece_id in range (len(Pieces)-1) :
        if Pieces[piece_id]["status"] != "dead" :
            board_pieces [Pieces[piece_id]["coords"][0]] [Pieces[piece_id]["coords"][1]] = piece_id
    return board_pieces


def show_players ():

    Top_player.config ( text = "Player " + str(Players [0]["id"]+1) )
    Top_player_points.config ( text = "(" + str(Players [0] ["points"]) + ")" )

    Bottom_player.config( text = "Player " + str(Players [1]["id"]+1) )
    Bottom_player_points.config( text = "(" + str(Players [1] ["points"]) + ")" )

    if global_info ["game"] == True and global_info["turn"] == global_info["board_sense"]  :
        Top_player.config ( font = ("", 15 , "bold" ) )
        Bottom_player.config ( font = ("", 15 , "normal" ) )

        Top_player_arrow.pack()
        Top_player_frame.place(x=330,y=0)
        Bottom_player_arrow.pack_forget()

    elif global_info ["game"] == True :
        Top_player.config ( font = ("", 15 , "normal" ) )
        Bottom_player.config ( font = ("", 15 , "bold" ) )

        Top_player_arrow.pack_forget()
        Top_player_frame.place(x=360,y=0)
        Bottom_player_arrow.pack()


def show_board ():
    board_pieces = simu_coords()

    square_0_0.config(text = Pieces[board_pieces[0][0]]["symbol"])
    square_1_0.config(text = Pieces[board_pieces[1][0]]["symbol"])
    square_2_0.config(text = Pieces[board_pieces[2][0]]["symbol"])
    square_3_0.config(text = Pieces[board_pieces[3][0]]["symbol"])
    square_4_0.config(text = Pieces[board_pieces[4][0]]["symbol"])
    square_5_0.config(text = Pieces[board_pieces[5][0]]["symbol"])
    square_6_0.config(text = Pieces[board_pieces[6][0]]["symbol"])
    square_7_0.config(text = Pieces[board_pieces[7][0]]["symbol"])

    square_0_1.config(text = Pieces[board_pieces[0][1]]["symbol"])
    square_1_1.config(text = Pieces[board_pieces[1][1]]["symbol"])
    square_2_1.config(text = Pieces[board_pieces[2][1]]["symbol"])
    square_3_1.config(text = Pieces[board_pieces[3][1]]["symbol"])
    square_4_1.config(text = Pieces[board_pieces[4][1]]["symbol"])
    square_5_1.config(text = Pieces[board_pieces[5][1]]["symbol"])
    square_6_1.config(text = Pieces[board_pieces[6][1]]["symbol"])
    square_7_1.config(text = Pieces[board_pieces[7][1]]["symbol"])

    square_0_2.config(text = Pieces[board_pieces[0][2]]["symbol"])
    square_1_2.config(text = Pieces[board_pieces[1][2]]["symbol"])
    square_2_2.config(text = Pieces[board_pieces[2][2]]["symbol"])
    square_3_2.config(text = Pieces[board_pieces[3][2]]["symbol"])
    square_4_2.config(text = Pieces[board_pieces[4][2]]["symbol"])
    square_5_2.config(text = Pieces[board_pieces[5][2]]["symbol"])
    square_6_2.config(text = Pieces[board_pieces[6][2]]["symbol"])
    square_7_2.config(text = Pieces[board_pieces[7][2]]["symbol"])

    square_0_3.config(text = Pieces[board_pieces[0][3]]["symbol"])
    square_1_3.config(text = Pieces[board_pieces[1][3]]["symbol"])
    square_2_3.config(text = Pieces[board_pieces[2][3]]["symbol"])
    square_3_3.config(text = Pieces[board_pieces[3][3]]["symbol"])
    square_4_3.config(text = Pieces[board_pieces[4][3]]["symbol"])
    square_5_3.config(text = Pieces[board_pieces[5][3]]["symbol"])
    square_6_3.config(text = Pieces[board_pieces[6][3]]["symbol"])
    square_7_3.config(text = Pieces[board_pieces[7][3]]["symbol"])

    square_0_4.config(text = Pieces[board_pieces[0][4]]["symbol"])
    square_1_4.config(text = Pieces[board_pieces[1][4]]["symbol"])
    square_2_4.config(text = Pieces[board_pieces[2][4]]["symbol"])
    square_3_4.config(text = Pieces[board_pieces[3][4]]["symbol"])
    square_4_4.config(text = Pieces[board_pieces[4][4]]["symbol"])
    square_5_4.config(text = Pieces[board_pieces[5][4]]["symbol"])
    square_6_4.config(text = Pieces[board_pieces[6][4]]["symbol"])
    square_7_4.config(text = Pieces[board_pieces[7][4]]["symbol"])

    square_0_5.config(text = Pieces[board_pieces[0][5]]["symbol"])
    square_1_5.config(text = Pieces[board_pieces[1][5]]["symbol"])
    square_2_5.config(text = Pieces[board_pieces[2][5]]["symbol"])
    square_3_5.config(text = Pieces[board_pieces[3][5]]["symbol"])
    square_4_5.config(text = Pieces[board_pieces[4][5]]["symbol"])
    square_5_5.config(text = Pieces[board_pieces[5][5]]["symbol"])
    square_6_5.config(text = Pieces[board_pieces[6][5]]["symbol"])
    square_7_5.config(text = Pieces[board_pieces[7][5]]["symbol"])

    square_0_6.config(text = Pieces[board_pieces[0][6]]["symbol"])
    square_1_6.config(text = Pieces[board_pieces[1][6]]["symbol"])
    square_2_6.config(text = Pieces[board_pieces[2][6]]["symbol"])
    square_3_6.config(text = Pieces[board_pieces[3][6]]["symbol"])
    square_4_6.config(text = Pieces[board_pieces[4][6]]["symbol"])
    square_5_6.config(text = Pieces[board_pieces[5][6]]["symbol"])
    square_6_6.config(text = Pieces[board_pieces[6][6]]["symbol"])
    square_7_6.config(text = Pieces[board_pieces[7][6]]["symbol"])

    square_0_7.config(text = Pieces[board_pieces[0][7]]["symbol"])
    square_1_7.config(text = Pieces[board_pieces[1][7]]["symbol"])
    square_2_7.config(text = Pieces[board_pieces[2][7]]["symbol"])
    square_3_7.config(text = Pieces[board_pieces[3][7]]["symbol"])
    square_4_7.config(text = Pieces[board_pieces[4][7]]["symbol"])
    square_5_7.config(text = Pieces[board_pieces[5][7]]["symbol"])
    square_6_7.config(text = Pieces[board_pieces[6][7]]["symbol"])
    square_7_7.config(text = Pieces[board_pieces[7][7]]["symbol"])


def target_squares (king_color:str,king_coords:tuple)->list:
    targeted_squares = [[{"piece":"","target":False},{"piece":"","target":False},{"piece":"","target":False}],
                        [{"piece":"","target":False},{"piece":king_color,"target":False},{"piece":"","target":False}],
                        [{"piece":"","target":False},{"piece":"","target":False},{"piece":"","target":False}]]
    # regarde si le roi est en bordure d'echequier
    # haut et bas -> y
    if king_coords[1] == 0 :
        start_y = 0
        end_y = 2
    elif king_coords[1] == 7 :
        start_y = -1
        end_y = 1
    else :
        start_y = -1
        end_y = 2

    # droite et gauche -> x
    if king_coords[0] == 0 :
        start_x = 0
        end_x = 2
    elif king_coords[0] == 7 :
        start_x = -1
        end_x = 1
    else :
        start_x = -1
        end_x = 2


    # vérifie d'abort s'il y a des pièces adjacentes au roi
    for y in range (start_y , end_y):
        for x in range (start_x , end_x):
            # ignore la case avec le roi
            if (x,y) != (0,0) :
                # s'il y a une pièce
                if board_pieces[king_coords[0]+x][king_coords[1]+y] != 32 :
                    targeted_squares [y+1] [x+1] ["piece"] = Pieces [ board_pieces[king_coords[0]+x][king_coords[1]+y] ] ["color"]


    # vérifie si les cases adjacentes au roi et celle du roi sont target par une pièce de couleur opposé
    for y in range (start_y , end_y):
        for x in range (start_x , end_x):
            coords = (king_coords[0]+x , king_coords[1]+y)

            # tour
            def rook (x_:int , y_:int , x:int , y:int):
                """x_ & y_ -> coordonnées de la case sur laquelle on cherche à savoir s'il y a une tour
                    x & y -> coordonnées de la case sur laquelle on cherche à savoir si elle est regardé"""
                if board_pieces [x_] [y_] != 32 and Pieces [ board_pieces [x_] [y_] ] ["color"] != king_color and Pieces [ board_pieces [x_] [y_] ] ["name"] == "rook" :
                    targeted_squares [y] [x] ["target"] = True
                    return True
                elif board_pieces [y_] [x_] != 32 :
                    return True
                return False

            for direction , board_limit in zip( (-1,1,2) , (0,8,7) ):
                for x_ in range ( coords[0] , board_limit , direction ):
                    print (coords[0] , board_limit , direction)
                    if rook (x_ , coords[1] , x , y) == True :
                        print (True)
                        break

                for y_ in range ( coords[1] , board_limit , direction ) :
                     if rook (coords[0] , y_ , x , y) == True :
                         break




    return targeted_squares


def move (coords:tuple):
    """redirige le programme vers les fonctions pour faire bouger chaque pièces
        coords --> coordoné du boutton cliqué"""

    #on vérifie si une pièce a déjà été sélectioné    si c'est bien une pièce et non une case vide       si la pièce apartien au joueur qui joue
    if global_info["b_click"] == 0      and       Pieces [ board_pieces[ coords[0] ][ coords[1] ] ] ["name"] != ""      and      global_info["game"] == True     and    Players [global_info["turn"]]["color"] == Pieces [ board_pieces[ coords[0] ][ coords[1] ] ] ["color"]:
        global_info["start_square"] = coords #on note les coordonné de notre pièce
        global_info["b_click"] = 1

    # après la selection d'une pièce on exécute les fonctions de mouvement de chaque pièce
    elif global_info["b_click"] == 1 :
        global_info["end_square"] = coords #on note où on veut que la pièce aille
        if Pieces [ board_pieces[ global_info["start_square"][0] ][ global_info["start_square"][1] ] ] ["name"] == "pawn" :
            move_pawn (global_info["start_square"],global_info["end_square"])

        elif Pieces [ board_pieces[ global_info["start_square"][0] ][ global_info["start_square"][1] ] ] ["name"] == "rook" :
            move_rook (global_info["start_square"],global_info["end_square"])

        elif Pieces [ board_pieces[ global_info["start_square"][0] ][ global_info["start_square"][1] ] ] ["name"] == "knight" :
            move_knight (global_info["start_square"],global_info["end_square"])

        elif Pieces [ board_pieces[ global_info["start_square"][0] ][ global_info["start_square"][1] ] ] ["name"] == "bishop" :
            move_bishop (global_info["start_square"],global_info["end_square"])

        elif Pieces [ board_pieces[ global_info["start_square"][0] ][ global_info["start_square"][1] ] ] ["name"] == "queen" :
            move_rook (global_info["start_square"],global_info["end_square"])
            move_bishop (global_info["start_square"],global_info["end_square"])

        elif Pieces [ board_pieces[ global_info["start_square"][0] ][ global_info["start_square"][1] ] ] ["name"] == "king" :
            move_king (global_info["start_square"],global_info["end_square"])

        if global_info["b_click"] == 2 :

            # on actualise le plateau et les joueurs
            show_board()
            show_players()

            for color,c in zip(["black","white"],range(15,32,16)):
                print ()
                print ("---------"+color+"---------")
                targeted_squares = target_squares(color, Pieces[c]["coords"])
                for i in range (3):
                    for j in range (3):
                        print ("ligne " + str(i) + ", colonne " + str(j) + ", pièce " + targeted_squares [i][j]["piece"] + ", targeted : " + str(targeted_squares [i][j]["target"]))


            # on remet les valeurs des coordonnées de la sélection à leur valeur initiale
            global_info["b_click"] = 0
            global_info["start_square"] = (8,0)
            global_info["end_square"] = (8,0)
            # on passe au tour d'après
            next_turn()
        else :
            global_info["b_click"] = 0
            return


    # enfin si un mauvais coup est joué on cherche à renvoyer un message d'erreur
    else :
        if  global_info == False :
            if Players [global_info["turn"]]["color"] != Pieces [ board_pieces[ coords[0] ][ coords[1] ] ] ["color"] :
                alert_msg.config (text = "Vous ne pouvez pas jouer une pièce de la couleur opposé")


def move_pawn (start_square:tuple,end_square:tuple):
    start_id = board_pieces[start_square[0]] [start_square[1]]
    end_id = board_pieces [end_square[0]] [end_square [1]]

    #si la pièce est blanche
    if Pieces[start_id]["color"] == "white" :

        if Pieces[ start_id ] ["coords"] [1] == 1 and start_square [1]+2 == end_square[1] and end_id == 32 and board_pieces [ start_square[0] ] [ start_square[1]+1 ] == 32 :
            Pieces [start_id] ["coords"] = end_square
            global_info["b_click"] = 2

        #on verifie si le mouvement correspond au patern du pion et qu'il n'y a pas de pièce devant lui
        elif start_square[1]+1 == end_square[1] and start_square[0] == end_square[0] and board_pieces[ start_square[0] ][start_square[1]+1 ] == 32 :
            Pieces [start_id] ["coords"] = end_square
            global_info["b_click"] = 2

        # on vérifie si le mouvement correspond au patern du pion et qu'il a une pièce de couleur opposé à manger
        elif start_square[1]+1 == end_square[1] and (  (    start_square[0]+1 == end_square[0]   and    board_pieces[ start_square[0]+1 ][start_square[1]+1 ] != 32    )  or  (  start_square[0]-1 == end_square[0] and board_pieces[ start_square[0]-1 ][start_square[1]+1 ] != 32 ) )  and Pieces [end_id] ["color"] == "black" :
            Pieces [start_id] ["coords"] = end_square
            eat (end_id)
            global_info["b_click"] = 2

        else :
            global_info["b_click"] = 3

    #si la pièce est noire
    else :

        if Pieces[start_id] ["coords"] [1] == 6 and start_square [1]-2 == end_square[1] and end_id == 32 and board_pieces [ start_square[0] ] [ start_square[1]-1 ] == 32:
            Pieces [start_id] ["coords"] = end_square
            global_info["b_click"] = 2

        #on verifie si le mouvement correspond à celui du patern du pion et qu'il n'y a pas de pièce devant lui
        elif start_square[1]-1 == end_square[1] and start_square[0] == end_square[0] and board_pieces[ start_square[0] ][start_square[1]-1 ] == 32 :
            Pieces [start_id] ["coords"] = end_square
            global_info["b_click"] = 2

        # on vérifie si le mouvement correspond au patern du pion et qu'il a une pièce de couleur opposé à manger
        elif start_square[1]-1 == end_square[1] and ( (    start_square[0]+1 == end_square[0]   and    board_pieces[ start_square[0]+1 ][start_square[1]-1 ] != 32    )  or  (  start_square[0]-1 == end_square[0] and board_pieces[ start_square[0]-1 ][start_square[1]-1 ] != 32 )  ) and Pieces [end_id] ["color"] == "white" :
            Pieces [start_id] ["coords"] = end_square
            eat (end_id)
            global_info["b_click"] = 2

        else :
            global_info["b_click"] = 3


def move_rook (start_square:tuple,end_square:tuple):
    start_id = board_pieces[start_square[0]] [start_square[1]]
    end_id = board_pieces [end_square[0]] [end_square [1]]
    # son x ne bouge pas donc elle s'est déplacé verticalement
    if start_square[0] - end_square[0] == 0 :
        # elle se déplace vers le haut
        if start_square[1] - end_square[1] < 0 :
            direction = 1
        #  ici vers le bas
        else :
            direction = -1
        # verifie s'il n'y ai pas de pièce dans son chemin
        for k in range (start_square[1]+direction , end_square[1] , direction) :
            if board_pieces [start_square[0]] [k] != 32 :
                global_info["b_click"] = 3
                return
        # mange la pièce seulement si il y en a une de couleur opposé
        if end_id != 32  and Pieces [start_id]["color"] != Pieces [end_id]["color"] :
            eat (end_id)
            Pieces [start_id]["coords"] = end_square
            global_info["b_click"] = 2
        elif  end_id == 32:
            Pieces [start_id]["coords"] = end_square
            global_info["b_click"] = 2
        else :
            global_info["b_click"] = 3



    # dans le cas inverse elle se déplace horizontalement
    elif start_square[1] - end_square[1] == 0 :
        # elle se déplace vers le bas
        if start_square[0] - end_square[0] < 0 :
            direction = 1
        #  ici vers le bas
        else :
            direction = -1

        # verifie qu'il n'y ai pas de pièce dans son chemin
        for k in range (start_square[0]+direction , end_square[0] , direction) :
            if board_pieces [k] [start_square[1]] != 32 :
                global_info["b_click"] = 3
                return

        # mange la pièce seulement si il y en a une de couleur opposé
        if end_id != 32  and Pieces [start_id]["color"] != Pieces [end_id]["color"] :
            eat (end_id)
            Pieces [start_id]["coords"] = end_square
            global_info["b_click"] = 2
        elif  end_id == 32:
            Pieces [start_id]["coords"] = end_square
            global_info["b_click"] = 2
        else :
            global_info["b_click"] = 3



    else :
        global_info["b_click"] = 3


def move_knight (start_square:tuple,end_square:tuple):
    start_id = board_pieces[start_square[0]] [start_square[1]]
    end_id = board_pieces [end_square[0]] [end_square [1]]

    # verifie que le mouvement est valide
    if ( abs(start_square [0] - end_square[0]) == 2 and abs(start_square [1] - end_square[1]) == 1 ) or ( abs(start_square [0] - end_square[0]) == 1 and abs(start_square [1] - end_square[1]) == 2 ) :
        # vérifie si il y a une pièce à manger et qu'elle est de la même couleur
        if end_id != 32  and Pieces [start_id]["color"] != Pieces [end_id]["color"] :
            eat (end_id)
            Pieces [start_id]["coords"] = end_square
            global_info["b_click"] = 2
        # vérifie si il n'y a pas de pièce
        elif  end_id == 32:
            Pieces [start_id]["coords"] = end_square
            global_info["b_click"] = 2
        # si il y a une pièce est qu'elle est de la même couleur
        else :
            global_info["b_click"] = 3


    else :
        global_info["b_click"] = 3


def move_bishop (start_square:tuple,end_square:tuple):
    start_id = board_pieces[start_square[0]] [start_square[1]]
    end_id = board_pieces [end_square[0]] [end_square [1]]
    # diagonale secondaire
    if ( ( start_square[0] - end_square [0] > 0 and start_square[1] - end_square [1] < 0 ) or ( start_square[0] - end_square [0] < 0 and start_square[1] - end_square [1] > 0 ) ) and ( abs(start_square [0] - end_square [0]) == abs(start_square[1] - end_square[1]) ) :
        # vers le haut
        if start_square[0] - end_square [0] < 0 and start_square[1] - end_square [1] > 0 :
            direction = -1
        #  vers le bas
        else :
            direction = 1
        # verifie s'il n'y ai pas de pièce dans son chemin
        for i , j in zip(range(start_square[0]+direction , end_square[0] , direction) , range(start_square[1]+direction , end_square[1] , -direction)) :
            if board_pieces [i] [j] != 32 :
                global_info["b_click"] = 3
                return
        # mange la pièce seulement si il y en a une de couleur opposé
        if end_id != 32  and Pieces [start_id]["color"] != Pieces [end_id]["color"] :
            eat (end_id)
            Pieces [start_id]["coords"] = end_square
            global_info ["b_click"] = 2
        elif  end_id == 32:
            Pieces [start_id]["coords"] = end_square
            global_info ["b_click"] = 2
        else :
            global_info["b_click"] = 3


     # diagonale primaire
    elif ( ( start_square[0] - end_square [0] > 0 and start_square[1] - end_square [1] > 0 ) or ( start_square[0] - end_square [0] < 0 and start_square[1] - end_square [1] < 0 ) ) and ( abs(start_square [0] - end_square [0]) == abs(start_square[1] - end_square[1]) ) :
        # vers le haut
        if start_square[0] - end_square [0] < 0 and start_square[1] - end_square [1] < 0 :
            direction = -1
        #  vers le bas
        else :
            direction = 1
        # verifie s'il n'y ai pas de pièce dans son chemin
        for i , j in zip(range(start_square[0]+direction , end_square[0] , direction) , range(start_square[1]+direction , end_square[1] , direction)) :
            if board_pieces [i] [j] != 32 :
                global_info["b_click"] = 3
                return
        # mange la pièce seulement si il y en a une de couleur opposé
        if end_id != 32  and Pieces [start_id]["color"] != Pieces [end_id]["color"] :
            eat (end_id)
            Pieces [start_id]["coords"] = end_square
            global_info ["b_click"] = 2
        elif  end_id == 32:
            Pieces [start_id]["coords"] = end_square
            global_info ["b_click"] = 2
        else :
            global_info["b_click"] = 3


def move_king (start_square:tuple,end_square:tuple):
    a

#-------------------------------------------------------------------CHESS BOARD--------------------------------------------------------------------------------


#génération de l'echequier

#définition de la fenetre
board = tk.Tk()
board.title("chess board")
board.geometry("465x520")
board.configure(bg="#987456")

#definition de la frame pour l'echequier
board_squares = tk.Frame(board)
board_squares.place(x=0,y=40)
board_squares.columnconfigure(0,)

#définition des bouttons
board_pieces = simu_coords()


square_0_0 = tk.Button( board_squares , text = Pieces[board_pieces[0][0]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((0,0)) , bg = "#d99058" , activebackground = "#d99058")
square_0_0.grid(column=0,row=0)
square_1_0 = tk.Button( board_squares , text = Pieces[board_pieces[1][0]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((1,0)) , bg = "#b5651d" , activebackground = "#b5651d")
square_1_0.grid(column=1,row=0)
square_2_0 = tk.Button( board_squares , text = Pieces[board_pieces[2][0]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((2,0)) , bg = "#d99058" , activebackground = "#d99058")
square_2_0.grid(column=2,row=0)
square_3_0 = tk.Button( board_squares , text = Pieces[board_pieces[3][0]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((3,0)) , bg = "#b5651d" , activebackground = "#b5651d")
square_3_0.grid(column=3,row=0)
square_4_0 = tk.Button( board_squares , text = Pieces[board_pieces[4][0]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((4,0)) , bg = "#d99058" , activebackground = "#d99058")
square_4_0.grid(column=4,row=0)
square_5_0 = tk.Button( board_squares , text = Pieces[board_pieces[5][0]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((5,0)) , bg = "#b5651d" , activebackground = "#b5651d")
square_5_0.grid(column=5,row=0)
square_6_0 = tk.Button( board_squares , text = Pieces[board_pieces[6][0]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((6,0)) , bg = "#d99058" , activebackground = "#d99058")
square_6_0.grid(column=6,row=0)
square_7_0 = tk.Button( board_squares , text = Pieces[board_pieces[7][0]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((7,0)) , bg = "#b5651d" , activebackground = "#b5651d")
square_7_0.grid(column=7,row=0)

square_0_1 = tk.Button( board_squares , text = Pieces[board_pieces[0][1]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((0,1)) , bg = "#b5651d" , activebackground = "#b5651d")
square_0_1.grid(column=0,row=1)
square_1_1 = tk.Button( board_squares , text = Pieces[board_pieces[1][1]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((1,1)) , bg = "#d99058" , activebackground = "#d99058")
square_1_1.grid(column=1,row=1)
square_2_1 = tk.Button( board_squares , text = Pieces[board_pieces[2][1]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((2,1)) , bg = "#b5651d" , activebackground = "#b5651d")
square_2_1.grid(column=2,row=1)
square_3_1 = tk.Button( board_squares , text = Pieces[board_pieces[3][1]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((3,1)) , bg = "#d99058" , activebackground = "#d99058")
square_3_1.grid(column=3,row=1)
square_4_1 = tk.Button( board_squares , text = Pieces[board_pieces[4][1]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((4,1)) , bg = "#b5651d" , activebackground = "#b5651d")
square_4_1.grid(column=4,row=1)
square_5_1 = tk.Button( board_squares , text = Pieces[board_pieces[5][1]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((5,1)) , bg = "#d99058" , activebackground = "#d99058")
square_5_1.grid(column=5,row=1)
square_6_1 = tk.Button( board_squares , text = Pieces[board_pieces[6][1]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((6,1)) , bg = "#b5651d" , activebackground = "#b5651d")
square_6_1.grid(column=6,row=1)
square_7_1 = tk.Button( board_squares , text = Pieces[board_pieces[7][1]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((7,1)) , bg = "#d99058" , activebackground = "#d99058")
square_7_1.grid(column=7,row=1)

square_0_2 = tk.Button( board_squares , text = Pieces[board_pieces[0][2]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((0,2)) , bg = "#d99058" , activebackground = "#d99058")
square_0_2.grid(column=0,row=2)
square_1_2 = tk.Button( board_squares , text = Pieces[board_pieces[1][2]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((1,2)) , bg = "#b5651d" , activebackground = "#b5651d")
square_1_2.grid(column=1,row=2)
square_2_2 = tk.Button( board_squares , text = Pieces[board_pieces[2][2]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((2,2)) , bg = "#d99058" , activebackground = "#d99058")
square_2_2.grid(column=2,row=2)
square_3_2 = tk.Button( board_squares , text = Pieces[board_pieces[3][2]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((3,2)) , bg = "#b5651d" , activebackground = "#b5651d")
square_3_2.grid(column=3,row=2)
square_4_2 = tk.Button( board_squares , text = Pieces[board_pieces[4][2]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((4,2)) , bg = "#d99058" , activebackground = "#d99058")
square_4_2.grid(column=4,row=2)
square_5_2 = tk.Button( board_squares , text = Pieces[board_pieces[5][2]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((5,2)) , bg = "#b5651d" , activebackground = "#b5651d")
square_5_2.grid(column=5,row=2)
square_6_2 = tk.Button( board_squares , text = Pieces[board_pieces[6][2]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((6,2)) , bg = "#d99058" , activebackground = "#d99058")
square_6_2.grid(column=6,row=2)
square_7_2 = tk.Button( board_squares , text = Pieces[board_pieces[7][2]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((7,2)) , bg = "#b5651d" , activebackground = "#b5651d")
square_7_2.grid(column=7,row=2)

square_0_3 = tk.Button( board_squares , text = Pieces[board_pieces[0][3]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((0,3)) , bg = "#b5651d" , activebackground = "#b5651d")
square_0_3.grid(column=0,row=3)
square_1_3 = tk.Button( board_squares , text = Pieces[board_pieces[1][3]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((1,3)) , bg = "#d99058" , activebackground = "#d99058")
square_1_3.grid(column=1,row=3)
square_2_3 = tk.Button( board_squares , text = Pieces[board_pieces[2][3]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((2,3)) , bg = "#b5651d" , activebackground = "#b5651d")
square_2_3.grid(column=2,row=3)
square_3_3 = tk.Button( board_squares , text = Pieces[board_pieces[3][3]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((3,3)) , bg = "#d99058" , activebackground = "#d99058")
square_3_3.grid(column=3,row=3)
square_4_3 = tk.Button( board_squares , text = Pieces[board_pieces[4][3]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((4,3)) , bg = "#b5651d" , activebackground = "#b5651d")
square_4_3.grid(column=4,row=3)
square_5_3 = tk.Button( board_squares , text = Pieces[board_pieces[5][3]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((5,3)) , bg = "#d99058" , activebackground = "#d99058")
square_5_3.grid(column=5,row=3)
square_6_3 = tk.Button( board_squares , text = Pieces[board_pieces[6][3]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((6,3)) , bg = "#b5651d" , activebackground = "#b5651d")
square_6_3.grid(column=6,row=3)
square_7_3 = tk.Button( board_squares , text = Pieces[board_pieces[7][3]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((7,3)) , bg = "#d99058" , activebackground = "#d99058")
square_7_3.grid(column=7,row=3)

square_0_4 = tk.Button( board_squares , text = Pieces[board_pieces[0][4]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((0,4)) , bg = "#d99058" , activebackground = "#d99058")
square_0_4.grid(column=0,row=4)
square_1_4 = tk.Button( board_squares , text = Pieces[board_pieces[1][4]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((1,4)) , bg = "#b5651d" , activebackground = "#b5651d")
square_1_4.grid(column=1,row=4)
square_2_4 = tk.Button( board_squares , text = Pieces[board_pieces[2][4]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((2,4)) , bg = "#d99058" , activebackground = "#d99058")
square_2_4.grid(column=2,row=4)
square_3_4 = tk.Button( board_squares , text = Pieces[board_pieces[3][4]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((3,4)) , bg = "#b5651d" , activebackground = "#b5651d")
square_3_4.grid(column=3,row=4)
square_4_4 = tk.Button( board_squares , text = Pieces[board_pieces[4][4]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((4,4)) , bg = "#d99058" , activebackground = "#d99058")
square_4_4.grid(column=4,row=4)
square_5_4 = tk.Button( board_squares , text = Pieces[board_pieces[5][4]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((5,4)) , bg = "#b5651d" , activebackground = "#b5651d")
square_5_4.grid(column=5,row=4)
square_6_4 = tk.Button( board_squares , text = Pieces[board_pieces[6][4]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((6,4)) , bg = "#d99058" , activebackground = "#d99058")
square_6_4.grid(column=6,row=4)
square_7_4 = tk.Button( board_squares , text = Pieces[board_pieces[7][4]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((7,4)) , bg = "#b5651d" , activebackground = "#b5651d")
square_7_4.grid(column=7,row=4)

square_0_5 = tk.Button( board_squares , text = Pieces[board_pieces[0][5]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((0,5)) , bg = "#b5651d" , activebackground = "#b5651d")
square_0_5.grid(column=0,row=5)
square_1_5 = tk.Button( board_squares , text = Pieces[board_pieces[1][5]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((1,5)) , bg = "#d99058" , activebackground = "#d99058")
square_1_5.grid(column=1,row=5)
square_2_5 = tk.Button( board_squares , text = Pieces[board_pieces[2][5]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((2,5)) , bg = "#b5651d" , activebackground = "#b5651d")
square_2_5.grid(column=2,row=5)
square_3_5 = tk.Button( board_squares , text = Pieces[board_pieces[3][5]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((3,5)) , bg = "#d99058" , activebackground = "#d99058")
square_3_5.grid(column=3,row=5)
square_4_5 = tk.Button( board_squares , text = Pieces[board_pieces[4][5]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((4,5)) , bg = "#b5651d" , activebackground = "#b5651d")
square_4_5.grid(column=4,row=5)
square_5_5 = tk.Button( board_squares , text = Pieces[board_pieces[5][5]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((5,5)) , bg = "#d99058" , activebackground = "#d99058")
square_5_5.grid(column=5,row=5)
square_6_5 = tk.Button( board_squares , text = Pieces[board_pieces[6][5]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((6,5)) , bg = "#b5651d" , activebackground = "#b5651d")
square_6_5.grid(column=6,row=5)
square_7_5 = tk.Button( board_squares , text = Pieces[board_pieces[7][5]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((7,5)) , bg = "#d99058" , activebackground = "#d99058")
square_7_5.grid(column=7,row=5)

square_0_6 = tk.Button( board_squares , text = Pieces[board_pieces[0][6]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((0,6)) , bg = "#d99058" , activebackground = "#d99058")
square_0_6.grid(column=0,row=6)
square_1_6 = tk.Button( board_squares , text = Pieces[board_pieces[1][6]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((1,6)) , bg = "#b5651d" , activebackground = "#b5651d")
square_1_6.grid(column=1,row=6)
square_2_6 = tk.Button( board_squares , text = Pieces[board_pieces[2][6]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((2,6)) , bg = "#d99058" , activebackground = "#d99058")
square_2_6.grid(column=2,row=6)
square_3_6 = tk.Button( board_squares , text = Pieces[board_pieces[3][6]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((3,6)) , bg = "#b5651d" , activebackground = "#b5651d")
square_3_6.grid(column=3,row=6)
square_4_6 = tk.Button( board_squares , text = Pieces[board_pieces[4][6]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((4,6)) , bg = "#d99058" , activebackground = "#d99058")
square_4_6.grid(column=4,row=6)
square_5_6 = tk.Button( board_squares , text = Pieces[board_pieces[5][6]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((5,6)) , bg = "#b5651d" , activebackground = "#b5651d")
square_5_6.grid(column=5,row=6)
square_6_6 = tk.Button( board_squares , text = Pieces[board_pieces[6][6]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((6,6)) , bg = "#d99058" , activebackground = "#d99058")
square_6_6.grid(column=6,row=6)
square_7_6 = tk.Button( board_squares , text = Pieces[board_pieces[7][6]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((7,6)) , bg = "#b5651d" , activebackground = "#b5651d")
square_7_6.grid(column=7,row=6)

square_0_7 = tk.Button( board_squares , text = Pieces[board_pieces[0][7]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((0,7)) , bg = "#b5651d" , activebackground = "#b5651d")
square_0_7.grid(column=0,row=7)
square_1_7 = tk.Button( board_squares , text = Pieces[board_pieces[1][7]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((1,7)) , bg = "#d99058" , activebackground = "#d99058")
square_1_7.grid(column=1,row=7)
square_2_7 = tk.Button( board_squares , text = Pieces[board_pieces[2][7]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((2,7)) , bg = "#b5651d" , activebackground = "#b5651d")
square_2_7.grid(column=2,row=7)
square_3_7 = tk.Button( board_squares , text = Pieces[board_pieces[3][7]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((3,7)) , bg = "#d99058" , activebackground = "#d99058")
square_3_7.grid(column=3,row=7)
square_4_7 = tk.Button( board_squares , text = Pieces[board_pieces[4][7]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((4,7)) , bg = "#b5651d" , activebackground = "#b5651d")
square_4_7.grid(column=4,row=7)
square_5_7 = tk.Button( board_squares , text = Pieces[board_pieces[5][7]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((5,7)) , bg = "#d99058" , activebackground = "#d99058")
square_5_7.grid(column=5,row=7)
square_6_7 = tk.Button( board_squares , text = Pieces[board_pieces[6][7]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((6,7)) , bg = "#b5651d" , activebackground = "#b5651d")
square_6_7.grid(column=6,row=7)
square_7_7 = tk.Button( board_squares , text = Pieces[board_pieces[7][7]]["symbol"] , width = 3 , height = 1 , font=("Arial",20) , command = lambda: move((7,7)) , bg = "#d99058" , activebackground = "#d99058")
square_7_7.grid(column=7,row=7)


#-------------------------------------------------------------TOOLBAR------------------------------------------------------------------------------


# commandes de la toolbar


def start_game ():
    if global_info ["game"] == False :
        global_info ["game"] = True
        alert_msg.config (text = "vous avez commencé une partie")
    else :
        alert_msg.config (text = "une partie est déjà en cours")


def reset_game ():
    # si une partie n'est pas en cours
    if global_info ["game"] == True :
        # remet la partie à zero
        global_info["turn"] = 0
        global_info["game"] = False
        # met l'echequier dans le sens par defaut avant de le réinitialiser
        if global_info["board_sense"] == 0 :
            turn_board()
        # remet les pièces à leur etat initial
        Pieces [0] ["coords"],Pieces[0]["status"] = (0,6) , "alive"
        Pieces [1] ["coords"],Pieces[1]["status"] = (1,6) , "alive"
        Pieces [2] ["coords"],Pieces[2]["status"] = (2,6) , "alive"
        Pieces [3] ["coords"],Pieces[3]["status"] = (3,6) , "alive"
        Pieces [4] ["coords"],Pieces[4]["status"] = (4,6) , "alive"
        Pieces [5] ["coords"],Pieces[5]["status"] = (5,6) , "alive"
        Pieces [6] ["coords"],Pieces[6]["status"] = (6,6) , "alive"
        Pieces [7] ["coords"],Pieces[7]["status"] = (7,6) , "alive"
        Pieces [8] ["coords"],Pieces[8]["status"] = (0,7) , "alive"
        Pieces [9] ["coords"],Pieces[9]["status"] = (7,7) , "alive"
        Pieces [10] ["coords"],Pieces[10]["status"] = (1,7) , "alive"
        Pieces [11] ["coords"],Pieces[11]["status"] = (6,7) , "alive"
        Pieces [12] ["coords"],Pieces[12]["status"] = (2,7) , "alive"
        Pieces [13] ["coords"],Pieces[13]["status"] = (5,7) , "alive"
        Pieces [14] ["coords"],Pieces[14]["status"] = (3,7) , "alive"
        Pieces [15] ["coords"],Pieces[15]["status"] = (4,7) , "alive"
        Pieces [16] ["coords"],Pieces[16]["status"] = (0,1) , "alive"
        Pieces [17] ["coords"],Pieces[17]["status"] = (1,1) , "alive"
        Pieces [18] ["coords"],Pieces[18]["status"] = (2,1) , "alive"
        Pieces [19] ["coords"],Pieces[19]["status"] = (3,1) , "alive"
        Pieces [20] ["coords"],Pieces[20]["status"] = (4,1) , "alive"
        Pieces [21] ["coords"],Pieces[21]["status"] = (5,1) , "alive"
        Pieces [22] ["coords"],Pieces[22]["status"] = (6,1) , "alive"
        Pieces [23] ["coords"],Pieces[23]["status"] = (7,1) , "alive"
        Pieces [24] ["coords"],Pieces[24]["status"] = (0,0) , "alive"
        Pieces [25] ["coords"],Pieces[25]["status"] = (7,0) , "alive"
        Pieces [26] ["coords"],Pieces[26]["status"] = (1,0) , "alive"
        Pieces [27] ["coords"],Pieces[27]["status"] = (6,0) , "alive"
        Pieces [28] ["coords"],Pieces[28]["status"] = (2,0) , "alive"
        Pieces [29] ["coords"],Pieces[29]["status"] = (5,0) , "alive"
        Pieces [30] ["coords"],Pieces[30]["status"] = (4,0) , "alive"
        Pieces [31] ["coords"],Pieces[31]["status"] = (3,0) , "alive"
        # remet les points des joueurs à zero
        for k in range (len(Players)):
            Players[k]["points"] = 0
        show_board()
        alert_msg.config (text = "vous avez recommencé une partie")
    # si une partie est en cours
    else :
        alert_msg.config (text = "aucune partie n'est en cours")



def turn_board ():
    if global_info["game"] == False :
        # inverse les couleurs des pièces
        for dico in Pieces [:32] :
            if dico ["color"] == "white" :
                dico ["color"] = "black"
            else :
                dico["color"] = "white"

        # inverse les coordonnées des pièces
        for k in range (16):
            Pieces [k]["coords"] , Pieces [k+16] ["coords"] = Pieces [k+16] ["coords"] , Pieces [k]["coords"]

        # inverse l'id et la couleur des joueurs
        Players [0]["id"] , Players [1]["id"] = Players [1]["id"] , Players [0]["id"]
        Players [0]["color"] , Players [1]["color"] = Players [1]["color"] , Players [0]["color"]

        # met la variable global du sens de l'echequier
        if global_info["board_sense"] == 1 :
            global_info["board_sense"] = 0
        else :
            global_info["board_sense"] = 1

        show_board()
        show_players()
    else :
        alert_msg.config(text = "Une partie est en cours")


def player_selection ():
    if global_info["game"] == False :
        board_squares.grid_forget()


# definition de la frame de la bar
top_frame = tk.Frame(board)
top_frame.pack(side="top")

# définition des menus
menu_bar = tk.Menu(top_frame) # menu principal
game_menu = tk.Menu( menu_bar , tearoff=0) # menu de parametre de la partie
view_menu = tk.Menu(menu_bar , tearoff=0) # menu parametres d'affichage

# définition des option de game_menu
menu_bar.add_cascade(label="game" , menu = game_menu)
game_menu.add_command(label="start game" , command = start_game)
game_menu.add_command(label="reset game" , command = reset_game)
game_menu.add_command(label="players" , command = player_selection)



# définition des options d'affichage (view_menu)
menu_bar.add_cascade(label = "view" , menu = view_menu)
view_menu.add_command(label="turn board" , command = turn_board)

# attache le menu à la fenètre board
board.config(menu = menu_bar)


#----------------------------------------------------------------RESTE--------------------------------------------------------------------------


# définition de la frame du bas de page
bottom_frame = tk.Frame(board , bg="#987456")
bottom_frame.pack(side = "bottom")

# définition du label message d'alert
alert_msg = tk.Label (bottom_frame , text = "Aucune partie en cours" , font = ("",12) , bg="#987456")
alert_msg.pack(side = "bottom")

# définition de Bottom_player_frame
Bottom_player_frame = tk.Frame(board , bg="#987456")
Bottom_player_frame.place(x=0,y=490)

# définition des widgets de Bottom_player_frame
Bottom_player = tk.Label (Bottom_player_frame , text = "Player " + str(Players [1]["id"]+1) , font = ("", 15) , bg="#987456")
Bottom_player.pack(side="left")
Bottom_player_points = tk.Label(Bottom_player_frame , text = "(" + str(Players [1] ["points"]) + ")" , font = ("", 10) , bg="#987456")
Bottom_player_points.pack(side="left")
Bottom_player_arrow = tk.Label(Bottom_player_frame , text = "←" , font = ("", 20) , bg="#987456" )
Bottom_player_arrow.pack(side="left")

# définition de Top_player_frame
Top_player_frame = tk.Frame(board , bg="#987456")
Top_player_frame.place(x=330,y=0)

# définition des widgets de Top_player_frame
Top_player = tk.Label (Top_player_frame , text = "Player " + str(Players [0]["id"]+1) , font = ("", 15) , bg="#987456")
Top_player.pack(side="right")
Top_player_points = tk.Label(Top_player_frame , text = "(" + str(Players [0] ["points"]) + ")" , font = ("", 10) , bg="#987456")
Top_player_points.pack(side="right")
Top_player_arrow = tk.Label(Top_player_frame , text = "→" , font = ("", 20) , bg="#987456" )
Top_player_arrow.pack(side="right")


#---------------------------------PLAYER SELECTION---------------------------------------------------------------------------------------------------------------







board.mainloop()


