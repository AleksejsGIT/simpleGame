# Testa python kods

import tkinter as tk
import random

def generate_string(length):
    string = ""
    for _ in range(length):
        if random.random() < 0.5:  # 50% chance for X, 50% chance for O
            string += "X"
        else:
            string += "O"
    return string

def generate_and_display():
    try:
        user_input = int(entry.get())
        if 15 <= user_input <= 25:
            generated_string = generate_string(user_input)
            result_label.config(text="Generated string: " + generated_string)
        else:
            result_label.config(text="Number must be between 15 and 25.")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("X and O Generator")

# Create input label and entry
input_label = tk.Label(root, text="Enter a number between 15 and 25:")
input_label.pack()

entry = tk.Entry(root)
entry.pack()

# Create generate button
generate_button = tk.Button(root, text="Generate", command=generate_and_display)
generate_button.pack()

# Create label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
