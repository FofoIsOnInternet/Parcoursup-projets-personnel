# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:32:40 2022

@author: faust
"""
import random as r


class Morpion :
    def __init__ (self):
        self.board = {}
        for k in range (10):
            self.board[str(k)] = " "
        self.state = "ongoing"
    
    def move (self,cell:str,turn:str)->bool:
        """create a symbol in the given cell.
        returns True if the actions has been done successfully and False if not"""
        if cell not in "123456789": # is cell id  right?
            print("wrong cell input: " + cell)
            return False
        if self.board[cell] != " ": # is cell taken? 
            print("cell already taken: " + cell)
            return False
        self.board[cell] = turn
        return True
    
    def win (self,turn:str)->bool:
        """check if the morpion is over or still ongoing
        returns True if the game is over and False if not"""
        # vertical & horizontal
        for k in range (3):
            if self.board[str(1+k)] == turn and self.board[str(4+k)] == turn and self.board[str(7+k)] == turn or self.board[str(k*3+1)] == turn and self.board[str(k*3+2)] == turn and self.board[str(k*3+3)] == turn :
                self.state = "win"+turn
                return True
        #diagonals
        if self.board["1"] == turn and self.board["5"] == turn and self.board["9"] == turn or self.board["3"] == turn and self.board["5"] == turn and self.board["7"] == turn :
            self.state = "win"+turn
            return True
        return False
    
    def show (self):
        if self.state == "ongoing" :
            return  ["┏━━━┳━━━┳━━━┓" , 
                     "┃ "+self.board["1"]+" ┃ "+self.board["2"]+" ┃ "+self.board["3"]+" ┃" ,
                     "┣━━━╋━━━╋━━━┫",
                     "┃ "+self.board["4"]+" ┃ "+self.board["5"]+" ┃ "+self.board["6"]+" ┃",
                     "┣━━━╋━━━╋━━━┫",
                     "┃ "+self.board["7"]+" ┃ " +self.board["8"]+" ┃ "+self.board["9"]+" ┃",
                     "┗━━━┻━━━┻━━━┛"]
        else :
            return ["┏━━━┳━━━┳━━━┓",
                    "┃ * ┃ * ┃ * ┃",
                    "┣━━━╋━━━╋━━━┫",
                    "┃ * ┃ "+self.state[3]+" ┃ * ┃",
                    "┣━━━╋━━━╋━━━┫",
                    "┃ * ┃ * ┃ * ┃",
                    "┗━━━┻━━━┻━━━┛"]
        
    def __repr__(self):
        lines = self.show()
        string = ""
        for line in lines :
            string += line + "\n"
        return string


class Game :
    def __init__ (self):
        self.board = {}
        for k in ["A","B","C","D","E","F","G","H","I"]:
            self.board[k] = Morpion()
        self.state = "ongoing"
    
    def move (self,cell:str,turn:str)->bool:
        if len(cell) != 2 or cell[0] not in "ABCDEFGHI": # if the morpion id is right
            print("wrong cell input: "+cell)
            return False
        if self.board[cell[0]].state != "ongoing" : # if the morpion has already ended
            print("Morpion " + cell[0] +" already ended")
            return False
        if not self.board[cell[0]].move(cell[1:],turn) : # if the move can't be done in the morpion
            return False
        if self.board[cell[0]].win(turn) : # if that morpion ends
            print(self.board[cell[0]].state[3] + " won morpion " + cell[0])
        return True
    
    def win (self,turn:str)->bool:
        ids = ["A","B","C","D","E","F","G","H","I"]
        # vertical & horizontal
        for k in range (3):
            if self.board[ids[k]].state != "ongoing" and self.board[ids[k+1]].state != "ongoing" and self.board[ids[k+2]].state != "ongoing" or self.board[ids[k*3]].state != "ongoing" and self.board[ids[k*3+1]].state != "ongoing" and self.board[ids[k*3+2]].state != "ongoing":
                self.state = "win"+turn
                return True
        # diagonals
        if self.board["A"].state != "ongoing" and self.board["E"].state != "ongoing" and self.board["I"].state != "ongoing" or self.board["C"].state != "ongoing" and self.board["E"].state != "ongoing" and self.board["G"].state != "ongoing" :
            self.state = "win"+turn
            return True
        return False
    
    def show (self):
        ids = ["A","B","C","D","E","F","G","H","I"]
        explanations = [[" ┃ To select a morpion: ",
                         " ┃ ┏━━━┳━━━┳━━━┓",
                         " ┃ ┃ A ┃ B ┃ C ┃",
                         " ┃ ┣━━━╋━━━╋━━━┫",
                         " ┃ ┃ D ┃ E ┃ F ┃",
                         " ┃ ┣━━━╋━━━╋━━━┫",
                         " ┃ ┃ G ┃ H ┃ I ┃",],
                        [" ┃ ┗━━━┻━━━┻━━━┛",
                         " ┃ To select a cell: ",
                         " ┃ ┏━━━┳━━━┳━━━┓",
                         " ┃ ┃ 1 ┃ 2 ┃ 3 ┃",
                         " ┃ ┣━━━╋━━━╋━━━┫",
                         " ┃ ┃ 4 ┃ 5 ┃ 6 ┃",
                         " ┃ ┣━━━╋━━━╋━━━┫"],
                        [" ┃ ┃ 7 ┃ 8 ┃ 9 ┃",
                         " ┃ ┗━━━┻━━━┻━━━┛",
                         " ┃",
                         " ┃ EX: "+ ids[r.randint(0,8)] + str(r.randint(1,9)),
                         " ┃",
                         " ┃ To stop the game: type 'stopgame'",
                         " ┃",
                         ]]
        
        lines = []
        for i in range (3):
           morpion1 = self.board[ids[i*3]].show()
           morpion2 = self.board[ids[i*3+1]].show()
           morpion3 = self.board[ids[i*3+2]].show()
           explanation = explanations[i]
           for j in range (len(morpion1)):
               lines.append(morpion1[j] + morpion2[j] + morpion3[j] + explanation[j])
        return lines
    
    def __repr__ (self):
        lines = self.show()
        string = ""
        for line in lines :
            string += line + "\n"
        return string 


def MAIN ():
    game = Game()
    turn = "O"
    print(game)
    while not game.win(turn) :
        if turn == "O" :
            turn = "X"
        else :
            turn = "O"
        cell = input(turn+" turn: ")
        if cell == "stopgame" :
                print("Game stoped!")
                return
        while not game.move(cell,turn) :
            cell = input(turn+" turn: ")
        print(game)
    print(turn + " à gagné!")


MAIN()