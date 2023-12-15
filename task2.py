#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""

import tkinter as tk
from tkinter import ttk
import math

window = tk.Tk()
window.geometry("520x300")

def enter():
    a = float(aEntry.get())
    b = float(bEntry.get())

    c = f"Hypothenuse: {round(math.sqrt(a**2+b**2), 2)}"
    outputLabel.configure(text = c)

#labels
aLabel = tk.Label(window, text = "Side A")
bLabel = tk.Label(window, text = "Side B")

outputLabel = tk.Label(window)

#entries
aEntry = tk.Entry(window)
bEntry = tk.Entry(window)

#button
enterButton = tk.Button(window, text = "Enter", command = enter)

#grid
aLabel.grid(row = 1, column = 1)
bLabel.grid(row = 1, column = 2)

aEntry.grid(row = 2, column = 1)
bEntry.grid(row = 2, column = 2)

enterButton.grid(row = 3, column = 1)

outputLabel.grid(row = 4, column = 1)

window.mainloop()