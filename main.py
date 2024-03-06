import tkinter as tk
import random

class Game:

    def __init__(self,length):
        self.symbols = ""
        for _ in range(length):
            if random.random() < 0.5:  # 50% chance for X, 50% chance for O
                self.symbols += "X"
            else:
                self.symbols += "O"

        # self.symbols = [random.choice(['X', 'O']) for _ in range(user_input)] #varēja izdarīt arī tā

        self.human = 0
        self.computer = 0

        self.root = tk.Tk()
        self.root.title("X and O Generator")
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.input_label = tk.Label(self.root, text="Enter a number between 15 and 25:")
        self.input_label.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
        self.generate_button = tk.Button(self.root, text="Generate", command=self.generate_and_display)
        self.generate_button.pack()



    def generate_and_display(self):
        try:
            user_input = int(self.entry.get())
            if 15 <= user_input <= 25:

                self.result_label.config(text="Generated string: " + ''.join(self.symbols))
            else:
                self.result_label.config(text="Number must be between 15 and 25.")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid number.")

    def make_move(self, player, start, end, new_symbol):
        # Pārbaudīt, vai gājiens ir derīgs
        if self.symbols[start:end] not in [['X', 'X'], ['O', 'O'], ['X', 'O'], ['O', 'X']]:
            return False

        # Veikt gājienu
        self.symbols[start:end] = [new_symbol]

        # Aprēķināt punktus
        if new_symbol == 'O':
            if self.symbols[start:end] == ['X', 'X']:
                self.human += 2
            else:
                self.computer -= 1
        else:
            if self.symbols[start:end] == ['O', 'O']:
                self.human += 1
            else:
                self.computer -= 1

        return True

    def get_human_move(self, player):
        # kods, kas iegūst gājienu no spēlētāja human(no grafiskas saskarnes)
        pass

    # def get_computer_move(self):...

    def print_board(self):
        #  kods, kas izprintē pašreizējo stāvokli
        pass

    def is_over(self):
        # Pārbaude vai spēle ir beigusies
        return len(self.symbols) <= 2

    # def minimax(self):...


    def play(self):
        # while not self.is_over(): ...
        self.root.mainloop()




    # Run the game
game = Game(20)
game.play()






