from pynput import keyboard
from colorama import Fore, Back
from domain.board import BoardError
from domain.plane import Plane, PlaneError


class Services:
    def __init__(self, player_board):
        self.__player_board = player_board
        self.__current_row = 1
        self.__current_col = 1
        self.__fore = [Fore.MAGENTA, Fore.GREEN, Fore.YELLOW]
        self.__back = [Back.MAGENTA, Back.GREEN, Back.YELLOW]
        self.__color_index = 0
        self.__planes = []
        my_string = " "
        self.__color_cell = (f"{self.__fore[self.__color_index]}{self.__back[self.__color_index]}{my_string}"
                             f"{Fore.RESET}{Back.RESET}")
        self.draw_current_box(1, 1)

    def draw_player_board(self):
        """
        This function returns the player's board
        :return:
        """
        return self.__player_board

    def draw_current_box(self, row: int, col: int):
        """
        This functions draws the current box when choosing where to put the cabin.
        It also erases the other cabins colored prior to the move.
        :param row: The row of the current selected position
        :param col: The column of the current selected position
        :return:
        """
        self.__player_board.change_cell(row, col, self.__color_cell)

        if self.__player_board.cell(row-1, col) == self.__player_board.cell(row, col):
            self.__player_board.change_cell(row - 1, col, " ")

        if row != 10:
            if self.__player_board.cell(row+1, col) == self.__player_board.cell(row, col):
                self.__player_board.change_cell(row + 1, col, " ")

        if self.__player_board.cell(row, col-1) == self.__player_board.cell(row, col):
            self.__player_board.change_cell(row, col - 1, " ")

        if col != 10:
            if self.__player_board.cell(row, col+1) == self.__player_board.cell(row, col):
                self.__player_board.change_cell(row, col + 1, " ")

    def start_plane_move(self, key: keyboard.Key):
        """
        This function checks if the current chosen direction to move the cabin doesn't go out of the board.
        And it calls the other function to draw the current selected cell
        :param key: The arrow key pressed by the user
        :return:
        """
        if key == keyboard.Key.up:
            if self.__current_row == 1:
                raise BoardError("You can't move up")

            row = self.__current_row
            while self.__player_board.cell(self.__current_row, self.__current_col) != " ":
                self.__current_row -= 1
                if self.__current_row == 0:
                    self.__current_row = row
                    break

            self.__player_board.change_cell(row, self.__current_col, " ")

            self.draw_current_box(self.__current_row, self.__current_col)

        elif key == keyboard.Key.down:
            if self.__current_row == 10:
                raise BoardError("You can't move down")

            row = self.__current_row
            while self.__player_board.cell(self.__current_row, self.__current_col) != " ":
                self.__current_row += 1
                if self.__current_row == 11:
                    self.__current_row = row
                    break

            self.__player_board.change_cell(row, self.__current_col, " ")

            self.draw_current_box(self.__current_row, self.__current_col)

        elif key == keyboard.Key.left:
            if self.__current_col == 1:
                raise BoardError("You can't move left")

            col = self.__current_col
            while self.__player_board.cell(self.__current_row, self.__current_col) != " ":
                self.__current_col -= 1
                if self.__current_col == 0:
                    self.__current_col = col
                    break

            self.__player_board.change_cell(self.__current_row, col, " ")

            self.draw_current_box(self.__current_row, self.__current_col)

        elif key == keyboard.Key.right:
            if self.__current_col == 10:
                raise BoardError("You can't move right")

            col = self.__current_col
            while self.__player_board.cell(self.__current_row, self.__current_col) != " ":
                self.__current_col += 1
                if self.__current_col == 11:
                    self.__current_col = col
                    break

            self.__player_board.change_cell(self.__current_row, col, " ")

            self.draw_current_box(self.__current_row, self.__current_col)

    def check_good_place(self, direction):
        """
        This function checks if a plane pointed to the direction chosen by the user can fit on the board.
        :param direction: The direction chosen by the user(up, down, left, right)
        :return:
        """
        row = self.__current_row
        col = self.__current_col
        if direction == "U":
            if row not in range(1, 8) or col not in range(3, 9):
                raise BoardError("A plane with direction %s doesn't fit there" % direction)
        elif direction == "D":
            if row not in range(4, 11) or col not in range(3, 9):
                raise BoardError("A plane with direction %s doesn't fit there" % direction)
        elif direction == "L":
            if row not in range(3, 9) or col not in range(1, 8):
                raise BoardError("A plane with direction %s doesn't fit there" % direction)
        elif direction == "R":
            if row not in range(3, 9) or col not in range(4, 11):
                raise BoardError("A plane with direction %s doesn't fit there" % direction)
        else:
            raise BoardError("You need to choose between U, D, L or R")

    def check_other_plane(self, direction):
        """
        This function checks if a plane chosen by the user can fit on the board and not go over other planes
            that are already in place. If it does the function raises an error.
        :param direction: The direction chosen by the user(up, down, left, right)
        :return:
        """
        row = self.__current_row
        col = self.__current_col
        if direction == "U":
            for i in range(row + 1, row + 4):
                if self.__player_board.cell(i, col) != " ":
                    raise BoardError("A plane with direction %s doesn't fit there" % direction)

            for i in range(col - 2, col + 3):
                if self.__player_board.cell(row + 1, i) != " ":
                    raise BoardError("A plane with direction %s doesn't fit there" % direction)

            if self.__player_board.cell(row + 3, col - 1) != " " or self.__player_board.cell(row + 3, col + 1) != " ":
                raise BoardError("A plane with direction %s doesn't fit there" % direction)

        elif direction == "D":
            for i in range(row - 3, row):
                if self.__player_board.cell(i, col) != " ":
                    raise BoardError("A plane with direction %s doesn't fit there" % direction)

            for i in range(col - 2, col + 3):
                if self.__player_board.cell(row - 1, i) != " ":
                    raise BoardError("A plane with direction %s doesn't fit there" % direction)

            if self.__player_board.cell(row - 3, col - 1) != " " or self.__player_board.cell(row - 3, col + 1) != " ":
                raise BoardError("A plane with direction %s doesn't fit there" % direction)

        elif direction == "L":
            for i in range(row - 2, row + 3):
                if self.__player_board.cell(i, col + 1) != " ":
                    raise BoardError("A plane with direction %s doesn't fit there" % direction)

            for i in range(col + 1, col + 4):
                if self.__player_board.cell(row, i) != " ":
                    raise BoardError("A plane with direction %s doesn't fit there" % direction)

            if self.__player_board.cell(row - 1, col + 3) != " " or self.__player_board.cell(row + 1, col + 3) != " ":
                raise BoardError("A plane with direction %s doesn't fit there" % direction)

        elif direction == "R":
            for i in range(row - 2, row + 3):
                if self.__player_board.cell(i, col - 1) != " ":
                    raise BoardError("A plane with direction %s doesn't fit there" % direction)

            for i in range(col - 3, col):
                if self.__player_board.cell(row, i) != " ":
                    raise BoardError("A plane with direction %s doesn't fit there" % direction)

            if self.__player_board.cell(row - 1, col - 3) != " " or self.__player_board.cell(row + 1, col - 3) != " ":
                raise BoardError("A plane with direction %s doesn't fit there" % direction)

    def place_plane(self, direction):
        """
        In this function we call other functions to check if the plane fits inside the board, draws the plane
            on the board, stops if there are 3 planes put on the board and also chooses the new position
                of start of the cabin.
        :param direction: The direction chosen by the user(up, down, left, right)
        :return:
        """
        self.check_good_place(direction)
        self.check_other_plane(direction)
        plane = Plane(direction, self.__player_board)
        plane.draw_plane([self.__current_row, self.__current_col], self.__fore[self.__color_index])

        plane = plane.plane_location()
        self.__planes.append(plane[:])
        my_string = " "
        self.__color_index += 1
        if self.__color_index != 3:
            self.__color_cell = (f"{self.__fore[self.__color_index]}{self.__back[self.__color_index]}"
                                 f"{my_string}{Fore.RESET}{Back.RESET}")
        else:
            raise PlaneError("You put 3 planes on the board")

        self.__current_row = 1
        self.__current_col = 1
        while self.__player_board.cell(self.__current_row, self.__current_col) != " ":
            self.__current_row += 1
            if self.__current_row == 11:
                self.__current_row = 1
                self.__current_col += 1
                break
        self.draw_current_box(self.__current_row, self.__current_col)

    def location_plane(self):
        """
        This function returns a list containing the coordinates of all planes
        :return:
        """
        return self.__planes

    def change_current_box(self, row, col):
        """
        This function changes the current box in which the cabin is.
        :param row: The row chosen by the user
        :param col: The col chosen by the user
        :return:
        """
        self.__current_row = row
        self.__current_col = col

    def get_current_box(self):
        """
        This function returns the current position of the cabin.
        :return:
        """
        return [self.__current_row, self.__current_col]
