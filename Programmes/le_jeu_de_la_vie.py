# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 21:58:00 2023

@author: faust
"""

class Cell :
    def __init__(self,coordinates:tuple):
        self.coordinates = coordinates
        self.state = False
    
    def is_alive (self):
        return self.state
    
    def get_N (self)->tuple:
        if self.coordinates[1]-1 >= 0 :
            return (self.coordinates[0],self.coordinates[1]-1)
    
    def get_S(self,board_depth:int)->tuple:
        if self.coordinates[1]+1 < board_depth :
            return (self.coordinates[0],self.coordinates[1]+1)
    
    def get_W (self)->tuple:
        if self.coordinates[0]-1 >= 0 :
            return (self.coordinates[0]-1,self.coordinates[1])
    
    def get_E (self,board_lengh)->tuple:
        if self.coordinates[0]+1 < board_lengh :
            return (self.coordinates[0]+1,self.coordinates[1])
    
    def get_NW (self)->tuple:
        N = self.get_N()
        W = self.get_W()
        if N is not None and W is not None :
            return (W[0],N[1])
    
    def get_NE (self,board_lengh:int)->tuple:
        N = self.get_N()
        E = self.get_E(board_lengh)
        if N is not None and E is not None :
            return (E[0],N[1])
    
    def get_SW (self,board_depth:int)->tuple:
        S = self.get_S(board_depth)
        W = self.get_W()
        if S is not None and W is not None :
            return (W[0],S[1])
    
    def get_SE (self,board_depth:int,board_lengh:int)->tuple:
        S = self.get_S(board_depth)
        E = self.get_E(board_lengh)
        if S is not None and E is not None :
            return (E[0],S[1])
    def get_neighbors (self,size:tuple)->list:
        """returns a list with the coordinates of all cells adjacent to the one given
        size : tuple (x,y) -> size of the board"""
        return [self.get_N(),self.get_S(size[1]),self.get_E(size[0]),self.get_W(),self.get_NW(),self.get_NE(size[0]),self.get_SW(size[1]),self.get_SE(size[0],size[1])]

class Jeu_de_la_vie :
    def __init__ (self,size:tuple):
        """creates a new evironment for cells. 
        size : tuple (x,y)"""
        self.board = [[Cell((x,y)) for x in range(size[0])] for y in range(size[1])]
        self.size = size
        print(self)
    
    def birth_cell (self,coordinates:tuple):
        """give birth to a cell at the given coordinates x and y"""
        if coordinates[1] < self.size[1] and coordinates[0] < self.size[0] :
            self.board[coordinates[1]][coordinates[0]].state = True
    
    def kill_cell(self,coordinates:tuple):
        """give birth a cell at the given coordinates x and y"""
        if coordinates[1] < self.size[1] and coordinates[0] < self.size[0] :
            self.board[coordinates[1]][coordinates[0]].state = False
    
    def start (self,n:int):
        """updates the environment for n rounds"""
        print(self)
        for k in range(n):
            self.update()

    def get_deaths (self)->list:
        """returns a list of coordinates of the cells with more than three other cells around them"""
        deaths = []
        for line in self.board:
            for cell in line:
                if cell.is_alive(): # if the cell is already dead there's no need to check if we can kill it
                    neighbors = cell.get_neighbors(self.size)
                    lives = 0
                    for coords in neighbors : # counts the amount of alive cells adjacent to the curent cell
                        if coords is not None and self.board[coords[1]][coords[0]].is_alive() : 
                            lives += 1
                    if lives > 3 or lives < 2:
                        deaths.append(cell.coordinates)
        return deaths
    
    def get_births (self)->list: 
        """returns a list of coordinates of the cells three cells around them"""
        births = []
        for line in self.board:
            for cell in line:
                if not cell.is_alive(): # if the cell is already alive there's no need to check if we can give birth to it
                    neighbors = cell.get_neighbors(self.size)
                    lives = 0
                    for coords in neighbors : # counts the amount of alive cells adjacent to the curent cell
                        if coords is not None and self.board[coords[1]][coords[0]].is_alive() : 
                            lives += 1
                    if lives == 3 :
                        births.append(cell.coordinates)
        return births
                
    def update (self):
        """bring the environment to the next round"""
        births = self.get_births()
        deaths = self.get_deaths()
        for coords in births :
            self.birth_cell(coords)
        for coords in deaths :
            self.kill_cell(coords)
        print(self)
    
    def __repr__(self):
        string = ""
        for y in self.board :
            for x in y:
                if x.is_alive() :
                    string += "⬛"
                else :
                    string += "⬜"
            string += "\n"
        return string
