import csv
import string
from random import randint

GRID_WIDTH = 4
GRID_HEIGHT = 4
GRID_DEFAULT = "_"
ALPHABET = string.ascii_uppercase
DICE_FILE_PATH = "data/dice.csv"


class BoggleBoard:
    def __init__(self):
        self.board_data = ''

    def __str__(self):
        print(ALPHABET)
        grid = ""
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                grid += GRID_DEFAULT
            grid += "\n"
        return grid

    def shake(self):
        with open(DICE_FILE_PATH, newline='') as file:
            rows_in_file = csv.DictReader(file)
            rolled_letters = ""
            for row in rows_in_file:
                rolled_letters += row['dice'][randint(0, 5)]
            print(list(rolled_letters))
            grid = ""
            grid_rows = []
            letter_tracker = 0
            for x in range(GRID_WIDTH):
                current_row = []
                for y in range(GRID_HEIGHT):
                    letter = rolled_letters[letter_tracker]
                    if letter == "Q":
                        letter += "u"
                    grid += letter + "\t"
                    letter_tracker += 1
                    current_row.append(letter)
                grid_rows.append(current_row)
                grid += "\n"
            print(grid_rows)
            self.board_data = grid_rows
            return grid
