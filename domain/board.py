from prettytable import PrettyTable
from tabulate import tabulate
from colorama import Fore, Style, Back
from pynput import keyboard

from domain.plane import Plane


class BoardError(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return self.__msg


class Board:
    def __init__(self):
        self.__table = []
        self.start_table()

    def start_table(self):
        """
        This function initializes the board
        :return:
        """
        columns = ["", " 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", "10"]
        self.__table.append(columns)
        self.__table.append(["A", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
        self.__table.append(["B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
        self.__table.append(["C", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
        self.__table.append(["D", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
        self.__table.append(["E", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
        self.__table.append(["F", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
        self.__table.append(["G", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
        self.__table.append(["H", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
        self.__table.append(["I", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
        self.__table.append(["J", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])

    def cell(self, row, col) -> str:
        """
        This function returns the cell with the coordinates row and column
        :param row: The row selected
        :param col: The column selected
        :return:
        """
        return self.__table[row][col]

    def change_cell(self, row, col, string):
        """
        This function changes the value from the cell selected
        :param row: The row selected
        :param col: The column selected
        :param string: The string which we want to put in the cell
        :return:
        """
        self.__table[row][col] = string

    def __str__(self):
        return tabulate(self.__table, tablefmt='fancy_grid', colalign='left')
