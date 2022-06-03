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
        pass

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
                # print(row['dice'][randint(0, 5)])
                rolled_letters += row['dice'][randint(0, 5)]
            print(rolled_letters)
            grid = ""
            letter_tracker = 0
            for x in range(GRID_WIDTH):
                for y in range(GRID_HEIGHT):
                    letter = rolled_letters[letter_tracker]
                    if letter == "Q":
                        letter += "u"
                    grid += letter + "\t"
                    letter_tracker += 1
                grid += "\n"
            return grid


b = BoggleBoard()
print(b)
print("SHAKE IT!\n")
print(b.shake())
