import random

from domain.board import Board, BoardError
from pynput import keyboard
from pynput.keyboard import Key
import time

from game.game import Game, GameError
from domain.plane import PlaneError
from player.computer import Computer
from player.player import Player
from services.computerservices import ComputerServices
from services.services import Services


class UI:
    def __init__(self):
        players = ["player", "computer"]
        self.__turn = random.choice(players)

        self.__player_board = Board()
        self.__services = Services(self.__player_board)
        self.choose_planes()

        self.__computer_board = Board()
        self.__computer_services = ComputerServices(self.__computer_board, self.__services.location_plane())

        GameBoard1 = Board()
        GameBoard2 = Board()
        self.__player = Player(GameBoard1, self.__computer_services.get_planes())
        self.__computer = Computer(GameBoard2, self.__services.location_plane())
        self.__game = Game(self.__player, self.__computer)

        self.start_game()

    def get_board(self):
        print(self.__services.draw_player_board())

    def on_key_press(self, key):
        if key in (Key.right, Key.left, Key.up, Key.down):
            try:
                self.__services.start_plane_move(key)
                self.get_board()
                print("Move the cabin: ")
            except BoardError as be:
                print(be)
        elif key == Key.space:
            direction = input("Choose in which direction the cabin should be pointed to"
                              " U(UP), D(DOWN), R(RIGHT), L(LEFT): ").strip().upper()
            try:
                self.__services.place_plane(direction)
                self.get_board()
                print("Move the key: ")
            except BoardError as be:
                print(be)
                print("Move the key: ")
            except PlaneError as pe:
                self.get_board()
                print(pe)
                time.sleep(2)
                return False

    def choose_planes(self):
        while True:
            self.get_board()
            print("Move the cabin: ")
            with keyboard.Listener(on_press=self.on_key_press) as listener:
                listener.join()
            break

    def start_game(self):
        while True:
            print("Do you want to start?")
            option = input("If you choose yes we will start the game and "
                           "if you choose no you exit the game:").strip().upper()
            if option == "YES":
                print("Let's begin!")
                time.sleep(2)
                break
            elif option == "NO":
                print("Bye!")
                exit(0)

        print("The %s starts the game." % self.__turn)
        time.sleep(2)
        while True:
            if self.__turn == "player":
                try:
                    print("This is the board you are playing on:")
                    print(self.__game.player_board())
                    row = input("Choose a row: ").upper()
                    col = int(input("Choose a column: "))
                    part = self.__game.player_move(row, col)
                    print(self.__game.player_board())
                    if part == "air":
                        print("Missed!")
                    elif part == "cabin":
                        print("You destroyed a plane! Good job!")
                    else:
                        print("Hit!")
                    time.sleep(2)
                    print("\n")

                    if self.__game.check_won():
                        print("You won! Congratulations!")
                        break
                    self.__turn = "computer"
                except GameError as ge:
                    print(ge)
                except ValueError as ve:
                    print(ve)
            else:
                try:
                    part = self.__game.computer_move()
                    print("This is the board the computer is playing on:")
                    print(self.__game.computer_board())
                    if part == "air":
                        print("The computer missed!")
                    elif part == "cabin":
                        print("The computer destroyed one of your planes! Be careful!")
                    else:
                        print("The computer hit a domain!")
                    time.sleep(2)
                    print("\n")

                    if self.__game.check_won():
                        print("You lost. Unlucky")
                        break
                    self.__turn = "player"
                except GameError as ge:
                    print(ge)
