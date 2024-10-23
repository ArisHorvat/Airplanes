

class GameError(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return self.__msg


class Game:
    def __init__(self, player, computer):
        self.__player = player
        self.__computer = computer

    @staticmethod
    def get_row(row):
        """
        This function returns the number corresponding to the index of the row.
        :param row: The letter corresponding to the row chosen by the user
        :return:
        """
        row_index = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        for i in range(len(row_index)):
            if row == row_index[i]:
                return i + 1

    def player_move(self, char_row, col):
        """
        This function performs the move of the player. It returns the part of the board that was hit
        :param char_row: The letter given by the user
        :param col: The column given by the user
        :return:
        """
        if char_row in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            row = int(char_row)
        elif char_row in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
            row = self.get_row(char_row)
        else:
            raise GameError("This is not a valid input for the row")

        if col not in range(1, 11):
            raise GameError("This is not a valid input for the column")

        part = self.__player.make_move(row, col)
        self.check_won()
        return part

    def player_board(self):
        """
        This function returns the player's board
        :return:
        """
        return self.__player.get_board()

    def computer_move(self):
        """
        This function performs the computer's move and returns the part that the computer hit
        :return:
        """
        part = self.__computer.make_move()
        self.check_won()
        return part

    def computer_board(self):
        """
        This function returns the computer's board
        :return:
        """
        return self.__computer.get_board()

    def check_won(self):
        """
        This function checks if the player or the computer won.
        :return:
        """
        if self.__player.number_planes() == 3:
            return True
        elif self.__computer.number_planes() == 3:
            return True
        return False
