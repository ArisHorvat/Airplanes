import copy

from colorama import Fore, Back, Style

from game.game import GameError


class Player:
    def __init__(self, board, planes):
        self.__board = board
        self.__planes = planes
        self.__old_planes = copy.deepcopy(planes)
        self.__hit_planes = 0
        self.__hits = []

    def hit_air(self, row: int, col: int):
        """
        This function draws one of the cells with blue on the player's board
        :param row: The row of the cell
        :param col: The column of the cell
        :return:
        """
        my_string = "h"
        color = f"{Fore.BLUE}{Back.BLUE}{my_string}{Fore.RESET}{Back.RESET}"
        self.__board.change_cell(row, col, color)
        self.__hits.append([row, col])

    def hit_box(self, row: int, col: int):
        """
        This function draws one of the cells with red on the player's board
        :param row: The row of the cell
        :param col: The column of the cell
        :return:
        """
        my_string = "h"
        color = f"{Fore.RED}{Back.RED}{my_string}{Fore.RESET}{Back.RESET}"
        self.__board.change_cell(row, col, color)
        self.__hits.append([row, col])

    def hit_plane(self, plane_nr):
        """
        This function draws the whole plane with black and red on the player's board
        :param plane_nr: The number of the destroyed plane
        :return:
        """
        my_string = str(self.__hit_planes)
        color = f"{Fore.RED}{Back.BLACK}{my_string}{Fore.RESET}{Back.RESET}"
        for coord in self.__old_planes[plane_nr]:
            row = coord[0]
            col = coord[1]
            self.__board.change_cell(row, col, color)
            self.__hits.append([row, col])
        self.__planes.insert(plane_nr, [])
        self.__planes.pop(plane_nr + 1)
        self.__hit_planes += 1

    def make_move(self, row, col):
        """
        This function checks if the selected cell was already hit and sees what part of the board was hit
        :param row: The row selected by the user
        :param col: The column selected by the user
        :return:
        """
        if [row, col] in self.__hits:
            raise GameError("This cell was already hit! Choose another one")
        hit_cabin = -1
        hit_plane = -1
        hit_index = -1
        plane_nr = 0
        air = 0
        for plane in self.__planes:
            for index in range(len(plane)):
                if plane[index] == [row, col]:
                    if index == 0:
                        self.hit_plane(plane_nr)
                        air = 1
                        hit_cabin = 1
                        break
                    else:
                        self.hit_box(row, col)
                        hit_plane = plane_nr
                        hit_index = index
                        air = 1
                        break
            if hit_cabin == 1 or hit_plane != -1:
                break
            plane_nr += 1

        if air == 0:
            self.hit_air(row, col)
            return "air"
        elif hit_cabin != 1:
            self.__planes[hit_plane].pop(hit_index)
            return "box"
        elif hit_cabin == 1:
            return "cabin"

    def get_board(self):
        """
        This function returns the player's board
        :return:
        """
        return self.__board

    def number_planes(self):
        """
        This function returns the number of planes destroyed
        :return:
        """
        return self.__hit_planes
