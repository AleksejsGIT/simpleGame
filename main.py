import tkinter as tk
import random


class Game:

    def __init__(self, length):
        # Samazināju koda izmēru, lai īsāk un tas pats, saprotami (Alex)
        self.symbols = ''.join([random.choice(['X', 'O']) for _ in range(length)])

        self.human = 0
        self.computer = 0

        self.root = tk.Tk()
        self.root.title("13.komandas spēle")
        self.root.geometry("500x800")
        self.root.configure(bg="#B5C2B7")
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=40)
        self.input_label = tk.Label(self.root, text="Enter a number between 15 and 25:")
        self.input_label.configure(bg="#B5C2B7")
        self.input_label.pack()
        self.generate_button = tk.Button(self.root, text="Generate", command=self.generate_and_display)
        self.generate_button.configure(bg="#2D2327", fg="#B5C2B7")
        self.generate_button.pack()
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.configure(bg="#B5C2B7")
        self.result_label.pack()

        self.human_label = tk.Label(self.root, text="Human has " + str(self.human) + " points")
        self.human_label.configure(bg="#B5C2B7")
        self.human_label.pack()

        self.computer_label = tk.Label(self.root, text="Computer has " + str(self.computer) + " points")
        self.computer_label.configure(bg="#B5C2B7")
        self.computer_label.pack()

        # papildus ievade gājieniem tad, ja sanāk ģenerēt virkni
        self.papildus_lauki = []


    def generate_and_display(self):
        try:
            user_input = int(self.entry.get())
            if 15 <= user_input <= 25:

                self.result_label.config(text="Generated string: " + ''.join(self.symbols))
                self.symbols_array = list(
                    self.symbols)  # sadala virkni masīva elementos, lai spēlētājs var veikt gājienus, izvēloties konkrētus masīva elementus
                if not self.papildus_lauki:
                    self.create_fields_for_move()
            else:
                self.result_label.config(text="Number must be between 15 and 25.")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid number.")

    def create_fields_for_move(self):
        self.input_label2 = tk.Label(self.root, text="Enter the number of the first element")
        self.input_label2.configure(bg="#B5C2B7")
        self.input_label2.pack()

        self.entry2 = tk.Entry(self.root)
        self.entry2.pack(pady=20)
        self.papildus_lauki.append(self.entry2)

        self.input_label3 = tk.Label(self.root, text="Enter the number of the second element")
        self.input_label3.configure(bg="#B5C2B7")
        self.input_label3.pack()

        self.entry3 = tk.Entry(self.root)
        self.entry3.pack(pady=20)
        self.papildus_lauki.append(self.entry3)

        self.button2 = tk.Button(self.root, text="Replace", command=self.replace_elements)
        self.button2.configure(bg="#2D2327", fg="#B5C2B7")
        self.button2.pack()
        self.papildus_lauki.append(self.button2)

    def points_result(self, kartas_nr1, kartas_nr2):
        # Pārbaudīt, vai gājiens ir derīgs
        if kartas_nr1 == kartas_nr2:
            return False

        # Rēķināt punktus
        if self.symbols_array[kartas_nr1 - 1] == 'X' and self.symbols_array[kartas_nr2 - 1] == 'X':
            self.human += 2
        elif self.symbols_array[kartas_nr1 - 1] == 'X' and self.symbols_array[kartas_nr2 - 1] == 'O':
            self.computer -= 1
        elif self.symbols_array[kartas_nr1 - 1] == 'O' and self.symbols_array[kartas_nr2 - 1] == 'O':
            self.computer += 2
        elif self.symbols_array[kartas_nr1 - 1] == 'O' and self.symbols_array[kartas_nr2 - 1] == 'X':
            self.human -= 1

            return True

    def update_points(self):
        self.human_label.configure(text="Human has " + str(self.human) + " points")
        self.computer_label.configure(text="Computer has " + str(self.computer) + " points")

    def get_human_move(self, player):
        # kods, kas iegūst gājienu no spēlētāja human(no grafiskas saskarnes)
        pass

    # def get_computer_move(self):...

    def print_board(self):
        # vajag check vai ievadīti derīgi cipari
        #  kods, kas izprintē pašreizējo stāvokli
        pass

    def replace_elements(self):
        # kods, kas aizvietos divus elementus

        # parveido ievadito par skaitli un -1, jo masīvā elementi sākas no 0
        kartas_nr1 = int(self.entry2.get()) - 1
        kartas_nr2 = int(self.entry3.get()) - 1

        if kartas_nr1 >= 0 and kartas_nr1 < len(self.symbols_array) and kartas_nr2 >= 0 and kartas_nr2 < len(self.symbols_array) and abs(kartas_nr1 - kartas_nr2) == 1:
            if self.symbols_array[kartas_nr1] == 'X' and self.symbols_array[kartas_nr2] == 'X' or self.symbols_array[kartas_nr1] == 'X' and self.symbols_array[kartas_nr2] == 'O':

                    self.symbols_array[kartas_nr1] = 'O'
                    del self.symbols_array[kartas_nr2]

                    next_string = ''.join(self.symbols_array)
                    self.result_label.configure(text="New string: " + next_string)

                    self.points_result(kartas_nr1, kartas_nr2)  # izsauc metodi, kas aprēķina spēlētāju punktus

                    self.update_points() # Lai rāda, cik katram punktu, vienmēr

                    # notīra ievades laukus
                    self.entry2.delete(0, tk.END)
                    self.entry3.delete(0, tk.END)
            else:
                self.result_label.configure(text="error")
            

            if self.symbols_array[kartas_nr1] == 'O' and self.symbols_array[kartas_nr2] == 'O' or self.symbols_array[kartas_nr1] == 'O' and self.symbols_array[kartas_nr2] == 'X':

                    self.symbols_array[kartas_nr1] = 'X'
                    del self.symbols_array[kartas_nr2]

                    next_string = ''.join(self.symbols_array)
                    self.result_label.configure(text="New string: " + next_string)

                    self.points_result(kartas_nr1, kartas_nr2)  # izsauc metodi, kas aprēķina spēlētāju punktus

                    self.update_points()

                    # notīra ievades laukus
                    self.entry2.delete(0, tk.END)
                    self.entry3.delete(0, tk.END)
            else:
                self.result_label.configure(text="error")
        else:
            self.result_label.configure(text="error")

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