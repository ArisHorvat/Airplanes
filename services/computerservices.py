from domain.board import BoardError
from domain.plane import PlaneError
from services.services import Services
from random import choice, randint


class ComputerServices:
    def __init__(self, board, planes):
        self.__board = board
        self.__services = Services(self.__board)
        box = self.__services.get_current_box()
        row = box[0]
        col = box[1]
        self.__board.change_cell(row, col, " ")
        self.__blocked = [[1, 1], [1, 2], [2, 1], [2, 2], [1, 9], [1, 10], [2, 9], [2, 10], [9, 1], [10, 1],
                          [9, 2], [10, 2], [9, 9], [10, 9], [9, 10], [10, 10]]
        self.__nr_planes = 0
        self.__planes = planes
        self.choose_position_planes()

    def choose_position_planes(self):
        """
        This function puts on the computer's board 3 planes.
        :return:
        """
        directions = ["U", "D", "L", "R"]
        while self.__nr_planes < 3:
            try:
                row = randint(1, 10)
                col = randint(1, 10)
                if [row, col] in self.__blocked:
                    continue
                elif self.__board.cell(row, col) == " ":
                    self.__services.change_current_box(row, col)
                    self.__services.place_plane(choice(directions))
                    box = self.__services.get_current_box()
                    row = box[0]
                    col = box[1]
                    self.__board.change_cell(row, col, " ")
                    self.__nr_planes += 1
            except BoardError:
                self.__blocked.append([row, col])
            except PlaneError:
                break

    def draw_computer_board(self):
        """
        This function returns the computer's board.
        :return:
        """
        return self.__board

    def get_planes(self):
        """
        This function returns a list containing the coordinates of the 3 planes of the computer.
        :return:
        """
        return self.__services.location_plane()
