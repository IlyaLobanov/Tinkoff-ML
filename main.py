import pygame
from pygame.locals import *
import random as rd
import pprint as pp



class TinkoffGame:
    def __init__(self, height: int = 500, width: int = 600, cellSize: int = 10, speed: int = 10):
        self.height = height
        self.width = width
        self.cellSize = cellSize
        self.speed = speed
        self.tab_size = width, height
        self.tab = pygame.display.set_mode(self.tab_size)
        self.cell_height = self.height // self.cellSize
        self.cell_width = self.width // self.cellSize
        arr = [[0] * (self.cell_height + 2) for i in range(self.cell_width + 2)]
        extraarr = [[0] * (self.cell_height + 2) for i in range(self.cell_width + 2)]
        self.array = arr
        self.earray = extraarr
        self.neighbour = 0
        self.flag = 1
        self.xcord = 0
        self.ycord = 0


    def Draw(self):
        for i in range(0, self.height, self.cellSize):
            pygame.draw.line(self.tab, pygame.Color("black"), (0, i), (self.width, i))
        for j in range(0, self.width, self.cellSize):
            pygame.draw.line(self.tab, pygame.Color("black"), (j, 0), (j, self.height))


    def Run(self):
        pygame.init()
        pygame.display.set_caption("Game of Life")
        self.tab.fill(pygame.Color("white"))
        timer = pygame.time.Clock()
        InGame = True
        self.Create_Grid(True)
        while InGame:
            for event in pygame.event.get():
                if event.type == QUIT:
                    InGame = False
            self.Draw()
            self.Draw_Grid()
            self.Clear()
            self.Get_Next_Array()
            pygame.display.flip()
            timer.tick(self.speed)
        pygame.quit()


    def Create_Grid(self, randomize: bool = False):
        if randomize == True:
            for i in range(self.cell_width):
                for j in range(self.cell_height):
                    self.array[i][j] = rd.randint(0, 1)
        #Test 1
        '''
        self.array[3][3] = 1
        self.array[4][3] = 1
        self.array[5][3] = 1
        self.array[5][4] = 1
        self.array[5][5] = 1
        self.array[4][5] = 1
        self.array[3][5] = 1
        self.array[3][4] = 1
        '''
        #Test 2
        '''
        self.array[1][1] = 1
        self.array[1][2] = 1
        self.array[1][3] = 1
        '''

    def Get_Neighbours(self):
        if self.flag == 1:
            if self.array[self.xcord - 1][self.ycord - 1] == 1:
                self.neighbour += 1
            if self.array[self.xcord][self.ycord - 1] == 1:
                self.neighbour += 1
            if self.array[self.xcord + 1][self.ycord - 1] == 1:
                self.neighbour += 1
            if self.array[self.xcord - 1][self.ycord] == 1:
                self.neighbour += 1
            if self.array[self.xcord + 1][self.ycord] == 1:
                self.neighbour += 1
            if self.array[self.xcord - 1][self.ycord + 1] == 1:
                self.neighbour += 1
            if self.array[self.xcord][self.ycord + 1] == 1:
                self.neighbour += 1
            if self.array[self.xcord + 1][self.ycord + 1] == 1:
                self.neighbour += 1
        else:
            if self.earray[self.xcord - 1][self.ycord - 1] == 1:
                self.neighbour += 1
            if self.earray[self.xcord][self.ycord - 1] == 1:
                self.neighbour += 1
            if self.earray[self.xcord + 1][self.ycord - 1] == 1:
                self.neighbour += 1
            if self.earray[self.xcord - 1][self.ycord] == 1:
                self.neighbour += 1
            if self.earray[self.xcord + 1][self.ycord] == 1:
                self.neighbour += 1
            if self.earray[self.xcord - 1][self.ycord + 1] == 1:
                self.neighbour += 1
            if self.earray[self.xcord][self.ycord + 1] == 1:
                self.neighbour += 1
            if self.earray[self.xcord + 1][self.ycord + 1] == 1:
                self.neighbour += 1


    def Get_Next_Array(self):
        if self.flag == 1:
            for i in range(self.cell_width):
                for j in range(self.cell_height):
                    self.xcord = i
                    self.ycord = j
                    self.Get_Neighbours()
                    if self.array[i][j] == 1:
                        if self.neighbour == 3 or self.neighbour == 2:
                            self.earray[i][j] = 1
                        else:
                            self.earray[i][j] = 0
                    else:
                        if self.neighbour == 3:
                            self.earray[i][j] = 1
                    self.neighbour = 0
        else:
            for i in range(self.cell_width):
                for j in range(self.cell_height):
                    self.xcord = i
                    self.ycord = j
                    self.Get_Neighbours()
                    if self.earray[i][j] == 1:
                        if self.neighbour == 3 or self.neighbour == 2:
                            self.array[i][j] = 1
                        else:
                            self.array[i][j] = 0
                    else:
                        if self.neighbour == 3:
                            self.array[i][j] = 1
                    self.neighbour = 0
        self.flag = -self.flag


    def Draw_Grid(self):
        if self.flag == 1:
            for i in range(self.cell_width):
                for j in range(self.cell_height):
                    if self.array[i][j] == 1:
                        pygame.draw.rect(self.tab, pygame.Color("black"),
                                         (i * self.cellSize, j * self.cellSize, self.cellSize, self.cellSize))
                    else:
                        pygame.draw.rect(self.tab, pygame.Color("white"),
                                         (i * self.cellSize, j * self.cellSize, self.cellSize, self.cellSize))
        else:
            for i in range(self.cell_width):
                for j in range(self.cell_height):
                    if self.earray[i][j] == 1:
                        pygame.draw.rect(self.tab, pygame.Color("black"),
                                         (i * self.cellSize, j * self.cellSize, self.cellSize, self.cellSize))
                    else:
                        pygame.draw.rect(self.tab, pygame.Color("white"),
                                         (i * self.cellSize, j * self.cellSize, self.cellSize, self.cellSize))
    def Clear(self):
        if self.flag == 1:
            for i in range(self.cell_width):
                for j in range(self.cell_height):
                    self.earray[i][j] = 0
        else:
            for i in range(self.cell_width):
                for j in range(self.cell_height):
                    self.array[i][j] = 0


if __name__ == '__main__':
    game = TinkoffGame(600, 600, 20, 5)
    game.Run()
