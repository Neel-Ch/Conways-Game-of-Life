import os
import time
import math
import random

def create_cells(abundance=4, size=9):
    cell_list = []
    for i in range(size):
        cell_type = random.randint(1,abundance)
        if cell_type == 1:
            cell_list.append("O")
        else:
            cell_list.append(" ")
    return cell_list

class Board:
    def __init__(self, cells, width=20):
        self.cells = cells
        self.width = width

    def size(self):
        num_cells = len(self.cells)
        length = math.ceil(num_cells / self.width)
        return length, self.width

    def display(self):
        num_cells = len(self.cells)
        length = int(num_cells / self.width)
        for row in range(length):
            for column in range(self.width):
                print(self.cells[self.width*row + column], end="")
            print("")
        # print excess cells
        for cell_num in range(length*self.width, num_cells):
            print(self.cells[cell_num], end="")


class LifeSimulation:
    def __init__(self, cells, width=20):
        self.cells = cells
        self.width = width
        self.Board = Board(self.cells, self.width)

    def step(self, buffer):
        time.sleep(buffer)

        num_cells = len(self.cells)

        for index, cell in enumerate(self.cells):
            neighbor_cells = [self.cells[index - 1] if index % self.width != 0 else " ",
                              self.cells[index + 1] if index % self.width != self.width - 1 else " ",
                              self.cells[index - self.width] if index >= self.width else " ",
                              self.cells[index + self.width] if index < num_cells - self.width else " ",
                              self.cells[index - self.width + 1] if index + 1 >= self.width else " ",
                              self.cells[index - self.width - 1] if index - 1 >= self.width else " ",
                              self.cells[index + self.width + 1] if index + 1 < num_cells - self.width else " ",
                              self.cells[index + self.width - 1] if index - 1 < num_cells - self.width else " "]
            dead_neighbors = 0
            for neighbor in neighbor_cells:
                if neighbor == " ":
                    dead_neighbors += 1
            if self.cells[index] == " " and dead_neighbors == 5:
                self.cells[index] = "O"
            elif self.cells[index] == "O":
                if not dead_neighbors == 6 and not dead_neighbors == 5:
                    self.cells[index] = " "

def __main__():
    cells = create_cells(size=25*200, abundance=20)
    sim = LifeSimulation(cells, width=200)
    sim.Board.display()

    for i in range(100): 
        sim.step(0.5)
        os.system("cls")
        sim.Board.display()

__main__()
