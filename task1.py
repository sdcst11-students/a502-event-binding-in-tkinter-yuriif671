"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("520x300")

def enter():
    name = nameEntry.get()
    studentNumber = studentNumberEntry.get()
    grade = gradeEntry.get()

    output = f"Name: {name}\nStudent Number: {studentNumber}\nGrade: {grade}"
    outputLabel.configure(text = output)

#labels
nameLabel = tk.Label(window, text = "Name")
studentNumberLabel = tk.Label(window, text = "Number")
gradeLabel = tk.Label(window, text = "Grade")

outputLabel = tk.Label(window)

#Entry fields
nameEntry = tk.Entry(window)
studentNumberEntry = tk.Entry(window)
gradeEntry = tk.Entry(window)

#button
enterButton = tk.Button(window, text = "Enter", command = enter)

#grid
nameLabel.grid(row = 1, column = 1)
studentNumberLabel.grid(row = 1, column = 2)
gradeLabel.grid(row = 1, column = 3)

nameEntry.grid(row = 2, column = 1)
studentNumberEntry.grid(row = 2, column = 2)
gradeEntry.grid(row = 2, column = 3)

enterButton.grid(row = 3, column = 2, pady = 10)

outputLabel.grid(row = 4, column = 2)

window.mainloop()