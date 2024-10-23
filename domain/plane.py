from colorama import Fore, Style, Back


class PlaneError(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return self.__msg


class Plane:
    def __init__(self, direction, board):
        self.__direction = direction
        self.__board = board
        self.__location = []

    def draw_plane(self, cabin, fore):
        """
        This function draws the plane on the board depending on the direction chosen
        :param cabin: The coordinates of the cabin
        :param fore: The foreground color
        :return:
        """
        if self.__direction == "R":
            # Cabin
            my_string = "▶"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0], cabin[1], format_string)
            self.__location.append([cabin[0], cabin[1]])

            # Body
            my_string = "━"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0], cabin[1]-2, format_string)
            self.__location.append([cabin[0], cabin[1]-2])

            # Front Wings
            my_string = "┃"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0], cabin[1] - 1, format_string)
            self.__board.change_cell(cabin[0] - 1, cabin[1] - 1, format_string)
            self.__board.change_cell(cabin[0] - 2, cabin[1] - 1, format_string)
            self.__board.change_cell(cabin[0] + 1, cabin[1] - 1, format_string)
            self.__board.change_cell(cabin[0] + 2, cabin[1] - 1, format_string)
            self.__location.append([cabin[0], cabin[1] - 1])
            self.__location.append([cabin[0] - 1, cabin[1] - 1])
            self.__location.append([cabin[0] - 2, cabin[1] - 1])
            self.__location.append([cabin[0] + 1, cabin[1] - 1])
            self.__location.append([cabin[0] + 2, cabin[1] - 1])


            # Back Wings
            my_string = "┃"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0], cabin[1] - 3, format_string)
            self.__board.change_cell(cabin[0] - 1, cabin[1] - 3, format_string)
            self.__board.change_cell(cabin[0] + 1, cabin[1] - 3, format_string)
            self.__location.append([cabin[0], cabin[1] - 3])
            self.__location.append([cabin[0] - 1, cabin[1] - 3])
            self.__location.append([cabin[0] + 1, cabin[1] - 3])

        elif self.__direction == "L":
            # Cabin
            my_string = "◀"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0], cabin[1], format_string)
            self.__location.append([cabin[0], cabin[1]])

            # Body
            my_string = "━"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0], cabin[1]+2, format_string)
            self.__location.append([cabin[0], cabin[1] + 2])

            # Front Wings
            my_string = "┃"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0], cabin[1] + 1, format_string)
            self.__board.change_cell(cabin[0] - 1, cabin[1] + 1, format_string)
            self.__board.change_cell(cabin[0] - 2, cabin[1] + 1, format_string)
            self.__board.change_cell(cabin[0] + 1, cabin[1] + 1, format_string)
            self.__board.change_cell(cabin[0] + 2, cabin[1] + 1, format_string)
            self.__location.append([cabin[0], cabin[1] + 1])
            self.__location.append([cabin[0] - 1, cabin[1] + 1])
            self.__location.append([cabin[0] - 2, cabin[1] + 1])
            self.__location.append([cabin[0] + 1, cabin[1] + 1])
            self.__location.append([cabin[0] + 2, cabin[1] + 1])

            # Back Wings
            my_string = "┃"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0], cabin[1] + 3, format_string)
            self.__board.change_cell(cabin[0] - 1, cabin[1] + 3, format_string)
            self.__board.change_cell(cabin[0] + 1, cabin[1] + 3, format_string)
            self.__location.append([cabin[0], cabin[1] + 3])
            self.__location.append([cabin[0] - 1, cabin[1] + 3])
            self.__location.append([cabin[0] + 1, cabin[1] + 3])

        elif self.__direction == "U":
            # Cabin
            my_string = "▲"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0], cabin[1], format_string)
            self.__location.append([cabin[0], cabin[1]])

            # Body
            my_string = "┃"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0] + 2, cabin[1], format_string)
            self.__location.append([cabin[0] + 2, cabin[1]])

            # Front Wings
            my_string = "━"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0] + 1, cabin[1], format_string)
            self.__board.change_cell(cabin[0] + 1, cabin[1] - 1, format_string)
            self.__board.change_cell(cabin[0] + 1, cabin[1] - 2, format_string)
            self.__board.change_cell(cabin[0] + 1, cabin[1] + 1, format_string)
            self.__board.change_cell(cabin[0] + 1, cabin[1] + 2, format_string)
            self.__location.append([cabin[0] + 1, cabin[1]])
            self.__location.append([cabin[0] + 1, cabin[1] - 1])
            self.__location.append([cabin[0] + 1, cabin[1] - 2])
            self.__location.append([cabin[0] + 1, cabin[1] + 1])
            self.__location.append([cabin[0] + 1, cabin[1] + 2])

            # Back Wings
            my_string = "━"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0] + 3, cabin[1], format_string)
            self.__board.change_cell(cabin[0] + 3, cabin[1] - 1, format_string)
            self.__board.change_cell(cabin[0] + 3, cabin[1] + 1, format_string)
            self.__location.append([cabin[0] + 3, cabin[1]])
            self.__location.append([cabin[0] + 3, cabin[1] - 1])
            self.__location.append([cabin[0] + 3, cabin[1] + 1])

        elif self.__direction == "D":
            # Cabin
            my_string = "▼"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0], cabin[1], format_string)
            self.__location.append([cabin[0], cabin[1]])

            # Body
            my_string = "┃"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0] - 2, cabin[1], format_string)
            self.__location.append([cabin[0] - 2, cabin[1]])

            # Front Wings
            my_string = "━"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0] - 1, cabin[1], format_string)
            self.__board.change_cell(cabin[0] - 1, cabin[1] - 1, format_string)
            self.__board.change_cell(cabin[0] - 1, cabin[1] - 2, format_string)
            self.__board.change_cell(cabin[0] - 1, cabin[1] + 1, format_string)
            self.__board.change_cell(cabin[0] - 1, cabin[1] + 2, format_string)
            self.__location.append([cabin[0] - 1, cabin[1]])
            self.__location.append([cabin[0] - 1, cabin[1] - 1])
            self.__location.append([cabin[0] - 1, cabin[1] - 2])
            self.__location.append([cabin[0] - 1, cabin[1] + 1])
            self.__location.append([cabin[0] - 1, cabin[1] + 2])

            # Back Wings
            my_string = "━"
            format_string = f"{fore}{my_string}{Fore.RESET}{Back.RESET}"
            self.__board.change_cell(cabin[0] - 3, cabin[1], format_string)
            self.__board.change_cell(cabin[0] - 3, cabin[1] + 1, format_string)
            self.__board.change_cell(cabin[0] - 3, cabin[1] - 1, format_string)
            self.__location.append([cabin[0] - 3, cabin[1]])
            self.__location.append([cabin[0] - 3, cabin[1] + 1])
            self.__location.append([cabin[0] - 3, cabin[1] - 1])


    def plane_location(self):
        """
        This returns a list of the coordinates of the plane's part
        :return:
        """
        return self.__location

