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
        self.root.title("13.komandas spēle")
        self.root.geometry("500x800")
        self.root.configure(bg="#B5C2B7")
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=40)
        self.input_label = tk.Label(self.root, text="Enter a number between 15 and 25:")
        self.input_label.configure(bg="#B5C2B7")
        self.input_label.pack()
        self.result_label = tk.Label(self.root, text="", font=("Arial",14))
        self.result_label.configure(bg="#B5C2B7")
        self.result_label.pack()
        self.generate_button = tk.Button(self.root, text="Generate", command=self.generate_and_display)
        self.generate_button.configure(bg="#2D2327", fg="#B5C2B7")
        self.generate_button.pack()

        #papildus ievade gājieniem tad, ja sanāk ģenerēt virkni
        self.papildus_lauki = []



    def generate_and_display(self):
        try:
            user_input = int(self.entry.get())
            if 15 <= user_input <= 25:

                self.result_label.config(text="Generated string: " + ''.join(self.symbols))
                self.symbols_array = list(self.symbols) #sadala virkni masīva elementos, lai spēlētājs var veikt gājienus, izvēloties konkrētus masīva elementus
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
                self.human += 2
            else:
                self.computer -= 1

        return True

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

        #parveido ievadito par skaitli un -1, jo masīvā elementi sākas no 0
        kartas_nr1 = int(self.entry2.get())-1
        kartas_nr2 = int(self.entry3.get())-1

        if kartas_nr1 >= 0 and kartas_nr1 < len(self.symbols_array) and kartas_nr2 >= 0 and kartas_nr2 < len(self.symbols_array):
            if self.symbols_array[kartas_nr1] == 'X' and self.symbols_array[kartas_nr2] == 'X' or self.symbols_array[kartas_nr1] == 'X' and self.symbols_array[kartas_nr2] == 'O' or self.symbols_array[kartas_nr1] == 'O' and self.symbols_array[kartas_nr2] == 'X':
                if abs(kartas_nr1 - kartas_nr2) == 1:
                    self.symbols_array[kartas_nr1] = 'O'
                    del self.symbols_array[kartas_nr2]

                    next_string = ''.join(self.symbols_array)
                    self.result_label.configure(text="New string: " + next_string)

                    #notīra ievades laukus
                    self.entry2.delete(0, tk.END)
                    self.entry3.delete(0, tk.END)
                else:
                    self.result_label.configure(text="error1")
            else:
                self.result_label.configure(text="error2")
        else:
            self.result_label.configure(text="error3")


        


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






