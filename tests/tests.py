from unittest import TestCase

from domain.board import Board, BoardError
from domain.plane import PlaneError
from game.game import Game
from player.computer import Computer
from player.player import Player
from services.computerservices import ComputerServices
from services.services import Services


class PlanesTest(TestCase):
    def setUp(self):
        self.__player_board = Board()
        self.__services = Services(self.__player_board)

        self.__computer_board = Board()
        self.__computer_services = ComputerServices(self.__computer_board, self.__services.location_plane())

        GameBoard1 = Board()
        GameBoard2 = Board()
        self.__player = Player(GameBoard1, self.__computer_services.get_planes())
        self.__computer = Computer(GameBoard2, self.__services.location_plane())
        self.__game = Game(self.__player, self.__computer)

    def test1(self):
        self.__services.change_current_box(2, 2)
        with self.assertRaises(BoardError):
            self.__services.place_plane("U")


    def test2(self):
        self.__services.change_current_box(3, 5)
        with self.assertRaises(BoardError):
            self.__services.place_plane("D")

    def test3(self):
        self.__services.change_current_box(5, 8)
        with self.assertRaises(BoardError):
            self.__services.place_plane("L")

    def test4(self):
        self.__services.change_current_box(9, 4)
        with self.assertRaises(BoardError):
            self.__services.place_plane("R")

    def test5(self):
        self.__services.change_current_box(4, 4)
        self.assertEqual(self.__services.get_current_box(), [4, 4])

    def test6(self):
        with self.assertRaises(PlaneError):
            self.__services.change_current_box(9, 4)
            self.__services.place_plane("D")
            check_list = []
            check_list.append([[9, 4], [8, 4], [7, 4], [6, 4], [8, 5], [8, 6], [8, 3], [8, 2], [6, 5], [6, 3]])

            self.__services.change_current_box(4, 8)
            self.__services.place_plane("U")
            check_list.append([[4, 8], [5, 8], [6, 8], [7, 8], [5, 9], [5, 10], [5, 7], [5, 6], [7, 9], [7, 7]])

            self.__services.change_current_box(3, 5)
            self.__services.place_plane("R")
            check_list.append([[3, 5], [3, 4], [3, 3], [3, 2], [2, 4], [1, 4], [4, 4], [5, 4], [2, 2], [4, 2]])

            print(self.__services.draw_player_board())
            self.assertEqual(check_list, self.__services.location_plane())

    def test7(self):
        print(self.__services.draw_player_board())
        self.assertEqual(self.__game.player_move("I", 4), "cabin")

    def test8(self):
        try:
            self.__services.change_current_box(9, 4)
            self.__services.place_plane("D")
            check_list = []
            check_list.append([[9, 4], [8, 4], [7, 4], [6, 4], [8, 5], [8, 6], [8, 3], [8, 2], [6, 5], [6, 3]])

            self.__services.change_current_box(4, 8)
            self.__services.place_plane("U")
            check_list.append([[4, 8], [5, 8], [6, 8], [7, 8], [5, 9], [5, 10], [5, 7], [5, 6], [7, 9], [7, 7]])

            self.__services.change_current_box(3, 5)
            self.__services.place_plane("R")
            check_list.append([[3, 5], [3, 4], [3, 3], [3, 2], [2, 4], [1, 4], [4, 4], [5, 4], [2, 2], [4, 2]])
        except PlaneError:
            self.assertEqual(self.__game.player_move("5", 7), "box")

    def test9(self):
        try:
            self.__services.change_current_box(9, 4)
            self.__services.place_plane("D")
            check_list = []
            check_list.append([[9, 4], [8, 4], [7, 4], [6, 4], [8, 5], [8, 6], [8, 3], [8, 2], [6, 5], [6, 3]])

            self.__services.change_current_box(4, 8)
            self.__services.place_plane("U")
            check_list.append([[4, 8], [5, 8], [6, 8], [7, 8], [5, 9], [5, 10], [5, 7], [5, 6], [7, 9], [7, 7]])

            self.__services.change_current_box(3, 5)
            self.__services.place_plane("R")
            check_list.append([[3, 5], [3, 4], [3, 3], [3, 2], [2, 4], [1, 4], [4, 4], [5, 4], [2, 2], [4, 2]])
        except PlaneError:
            self.assertEqual(self.__game.player_move("B", 1), "air")

    def test10(self):
        try:
            self.__services.change_current_box(9, 4)
            self.__services.place_plane("D")
            check_list = []
            check_list.append([[9, 4], [8, 4], [7, 4], [6, 4], [8, 5], [8, 6], [8, 3], [8, 2], [6, 5], [6, 3]])

            self.__services.change_current_box(4, 8)
            self.__services.place_plane("U")
            check_list.append([[4, 8], [5, 8], [6, 8], [7, 8], [5, 9], [5, 10], [5, 7], [5, 6], [7, 9], [7, 7]])

            self.__services.change_current_box(3, 5)
            self.__services.place_plane("R")
            check_list.append([[3, 5], [3, 4], [3, 3], [3, 2], [2, 4], [1, 4], [4, 4], [5, 4], [2, 2], [4, 2]])
        except PlaneError:
            self.__game.player_move("9", 4)
            self.__game.player_move("4", 8)
            self.__game.player_move("3", 5)
            self.assertTrue(self.__game.check_won())
