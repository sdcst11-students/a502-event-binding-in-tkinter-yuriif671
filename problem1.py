"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

import tkinter as tk
from tkinter import ttk
import math
import cmath

window = tk.Tk()

window.geometry("520x300")
window.title("Factoring ax^2 + bx + c = 0")

def enter():
    a = float(aEntry.get())
    b = float(bEntry.get())
    c = float(cEntry.get())

    discriminant = (b ** 2) - (4 * a * c)

    # Calculate the solutions
    solution1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    solution2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    outputLabel.configure(text = f"Solutions are: \n{solution1}\n{solution2}.")

#labels
aLabel = tk.Label(window, text = "a")
bLabel = tk.Label(window, text = "b")
cLabel = tk.Label(window, text = "c")

outputLabel = tk.Label(window)

#entries
aEntry = tk.Entry(window)

bEntry = tk.Entry(window)
cEntry = tk.Entry(window)

#button
enterButton = tk.Button(window, text = "Enter", command = enter)

#grid
aLabel.grid(row = 1, column = 1)
bLabel.grid(row = 1, column = 2)
cLabel.grid(row = 1, column = 3)

aEntry.grid(row = 2, column = 1)
bEntry.grid(row = 2, column = 2)
cEntry.grid(row = 2, column = 3)

aEntry.insert(0, 1)

enterButton.grid(row = 3, column = 2)

outputLabel.grid(row = 4, column = 2)

window.mainloop()