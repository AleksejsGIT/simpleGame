import tkinter as tk
import random

# Vajag 1) lai koks ģenerētos līdz noteikajam līmenim un pielietot heiristisko funkciju kokam, 2)heiristiska funkcija, 3)algoritmus minimax un alfa_beta, 4)uzprogrammēt datora gājienus 
#5)vēlams kaut kadā veidā koku izprintēt lai parliecināties ka viss pareizi

class Node: #klase lai izveidot koka elementu (root, child)
    def __init__(self, state, is_max):
        self.state = state
        self.is_max = is_max
        self.children = []


class GameTree: #klase lai ģenerēt koku
    def __init__(self, root_state, depth, is_first=True): #konstruktors, kas veido GameTree objektus,
        # root_state - sākuma simbolu virkne, is_first=True nozime ka pirmais ir speletajs ar 0
        self.nodes = []
        self.root = Node(root_state, True)#veido koka sakni, True nozime ka pirmais speletajs ir maksimizētajs
        self.nodes.append(self.root)
        self.n_nodes = 1
        self.n_levels = depth
        self.turn = 0 if is_first else 1
        self.make_children(self.root, depth, self.turn )# izsauc make_children lai izveidot nākamos koka līmeņus
        self.n_levels = depth - self.n_levels + 1
        self.n_leaves = self.set_leaf_heuristics()



    def make_children(self, node, depth, turn):
        if depth == 0: # nulles vietā liekam skaitli cik līmeņus gribam
            return
        for state in self.generate_possible_states(node.state, turn): #izsaucam generate_possible_states un cikls iet pa visiem iespējamiem stāvokļiem
            child = Node(state, not node.is_max)
            node.children.append(child)
            self.nodes.append(child)
            self.make_children(child, depth - 1, (turn + 1) % 2) # rekursīvi izsaucam make_children - (depth - 1) un arī mainam spēlētāju -  (turn + 1) % 2

    def update_turn(self, turn): #metodi izmantojam lai padot uz  print_pos_states aktuālo spelētāju
        self.turn = turn

    def generate_possible_states(self, current_state, turn): #metode ģenerē visus iespējamos stāvokļus no dotas virknes atkarībā no spelētāja
        possible_states = []
        player_symbol = 'O' if turn % 2 == 0 else 'X'
        opponent_symbol = 'X' if turn % 2 == 0 else 'O'
        print(player_symbol+" player")
        print(opponent_symbol + " opponent")
        for i in range(len(current_state) - 1):
            if current_state[i:i + 2] == [opponent_symbol, opponent_symbol] or current_state[i:i + 2] == [opponent_symbol, player_symbol]:
                new_state = current_state[:i] + [player_symbol] + current_state[i + 2:]
                possible_states.append(new_state)
        return possible_states
        pass

    def set_leaf_heuristics(self):
            leaf_nodes = [node for node in self.nodes if not node.children]
            for leaf in leaf_nodes:
                leaf.heuristic_value = self.evaluate_state(leaf.state)
            return len(leaf_nodes)

    def evaluate_state(self, state): #heiristiska funkcija

            pass



    # def minimax(self, node, depth, is_maximizing_player): #tas pilnība nokopēts no ai, vienkārši idejai
    #     if depth == 0 or not node.children:
    #         return node.heuristic_value
    #
    #     if is_maximizing_player:
    #         max_eval = float('-inf')
    #         for child in node.children:
    #             eval = self.minimax(child, depth - 1, False)
    #             max_eval = max(max_eval, eval)
    #         return max_eval
    #     else:
    #         min_eval = float('inf')
    #         for child in node.children:
    #             eval = self.minimax(child, depth - 1, True)
    #             min_eval = min(min_eval, eval)
    #         return min_eval

class Game:

    def __init__(self, length):
        self.game_tree = None
        self.turn = 0
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
        length = int(self.entry.get())
        if 0 <= length <= 25:
            self.symbols = ''.join([random.choice(['X', 'O']) for _ in range(length)]) #tagad virkne generējas šeit, jo iepriekšēja vietā length parametrs nemainījās
            # un vienmēr ģenerējās virkne ar 20 elementiem(izsaukums programmas beigās). Tagad ņem parametru no ievades
            self.result_label.config(text="Generated string: " + ''.join(self.symbols))
            self.symbols_array = list(self.symbols)
            if not self.papildus_lauki and not self.game_tree: #if not self>game_tree nozimē to, ka ja vel nav koka(GameTree klases objekta, tad izveidot to)
                self.create_fields_for_move()
                self.game_tree = GameTree(self.symbols, 5, bool(self.turn))# veidojam GameTree objektu(koku)
                self.print_pos_states()# printē iespējamos stāvokļus atkarībā no tā kāds spelētājs tagad spēlē un kāda tagad ir virkne
        else:
            self.result_label.config(text="Number must be between 15 and 25.")



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
        if self.symbols_array[kartas_nr1] == 'X' and self.symbols_array[kartas_nr2] == 'X':
            self.human += 2
        elif self.symbols_array[kartas_nr1] == 'X' and self.symbols_array[kartas_nr2] == 'O':
            self.computer -= 1
        elif self.symbols_array[kartas_nr1] == 'O' and self.symbols_array[kartas_nr2] == 'O':
            self.computer += 2
        elif self.symbols_array[kartas_nr1] == 'O' and self.symbols_array[kartas_nr2] == 'X':
            self.human -= 1

            return True

    def update_points(self):
        self.human_label.configure(text="Human has " + str(self.human) + " points")
        self.computer_label.configure(text="Computer has " + str(self.computer) + " points")

    def get_human_move(self, player):
        # kods, kas iegūst gājienu no spēlētāja human(no grafiskas saskarnes)
        pass


    def computer_move(self):
        # šeit uzprogrammēt datora gājeinu ar kādu no diviem algoritmiem
        # šeit piemēram vienkārši ņemam random gājienu
        possible_moves = self.game_tree.generate_possible_states(self.symbols_array, self.game_tree.turn)
        computer_move = random.choice(possible_moves)
        return computer_move


    def replace_elements(self):
        # kods, kas aizvietos divus elementus
        # parveido ievadito par skaitli un -1, jo masīvā elementi sākas no 0

        kartas_nr1 = int(self.entry2.get()) - 1
        kartas_nr2 = int(self.entry3.get()) - 1

        if kartas_nr1 >= 0 and kartas_nr1 < len(self.symbols_array) and kartas_nr2 >= 0 and kartas_nr2 < len(self.symbols_array) and abs(kartas_nr1 - kartas_nr2) == 1:
            if self.symbols_array[kartas_nr1] == 'X' and self.symbols_array[kartas_nr2] == 'X' or self.symbols_array[kartas_nr1] == 'X' and self.symbols_array[kartas_nr2] == 'O':

                self.points_result(kartas_nr1, kartas_nr2)  # izsauc metodi, kas aprēķina spēlētāju punktus

                self.symbols_array[kartas_nr1] = 'O'
                del self.symbols_array[kartas_nr2]

                next_string = ''.join(self.symbols_array)
                self.result_label.configure(text="New string: " + next_string)

                self.update_points()  # Lai rāda, cik katram punktu, vienmēr

                # notīra ievades laukus
                self.entry2.delete(0, tk.END)
                self.entry3.delete(0, tk.END)



            elif self.symbols_array[kartas_nr1] == 'O' and self.symbols_array[kartas_nr2] == 'O' or self.symbols_array[kartas_nr1] == 'O' and self.symbols_array[kartas_nr2] == 'X':

                self.points_result(kartas_nr1, kartas_nr2)  # izsauc metodi, kas aprēķina spēlētāju punktus

                self.symbols_array[kartas_nr1] = 'X'
                del self.symbols_array[kartas_nr2]

                next_string = ''.join(self.symbols_array)
                self.result_label.configure(text="New string: " + next_string)

                self.update_points()

                # notīra ievades laukus
                self.entry2.delete(0, tk.END)
                self.entry3.delete(0, tk.END)
            else:
                self.result_label.configure(text="error")
        else:
            self.result_label.configure(text="error")
        self.turn = (self.turn + 1) % 2 #mainam spēlētāju
        self.print_pos_states()




    def is_over(self):
        # Pārbaude vai spēle ir beigusies
        return len(self.symbols) <= 2


    def play(self):
        # while not self.is_over(): ...
        self.root.mainloop()

    def print_pos_states(self):
        # šeit stradājam ar jau izveidoto generate_and_display metodē GameTree objektu(koku)
        self.game_tree.update_turn(self.turn)
        possible_states = self.game_tree.generate_possible_states(self.symbols_array, self.game_tree.turn)
        for state in possible_states:
           print(state)




game = Game(20)
game.play()

