# ✈️Planes
Welcome to the **Planes** game! This project is a two-player game where one player competes against the computer to find and destroy planes on a grid. The objective is to strategically locate the opponent's planes while protecting your own.

## Game Overview

- **Description**: In **Planes**, players take turns trying to locate and destroy the opponent's planes on a grid-based board. The opponent is controlled by the computer, making each game unique and challenging.
- **Objective**: Successfully locate and destroy all of the opponent's planes before they do the same to you!

## Game Mechanics

- Each player has **3 planes** of the same size but different colors.
- Players place their planes on the board by selecting the cabin location and direction. If the plane fits, it can be placed; otherwise, an error is raised.
- Players take turns trying to hit each other's planes. Upon each turn:
  - If a plane is hit, a message is displayed, and the board reflects the hit.
  - Hitting the cabin destroys the entire plane.
  - Hitting any other part will turn the corresponding grid cell red.
  - Hitting air will turn the grid cell blue.

## Game Board

- The game board is structured as a 10x10 grid, using a standard table in Python.
- **Rows**: Labeled from A to J.
- **Columns**: Labeled from 1 to 10.

## Features

- **Layered Architecture**: The game is designed using a layered architecture to separate concerns, enhancing maintainability and scalability.
- **Custom Exception Classes**: Custom exceptions are provided to handle various game-related errors, improving robustness.
- **Unit Tests**: Comprehensive tests are included to ensure the functionality and reliability of the game.
- **Dynamic Plane Placement**: An algorithm is implemented to randomly position the computer's planes on the board for each game, ensuring a unique experience every time the user plays.

---

Thank you for checking out **Planes**! Enjoy the game and good luck!
