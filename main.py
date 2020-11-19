import tkinter as tk
from tkinter import filedialog, Text
import os

window = tk.Tk()

greeting = tk.Button(
    text = "textttttxttxt",
    foreground = "yellow",
    background = "black",
    width = 10,
    height = 5
    )
entry = tk.Entry(
    fg='yellow',
    bg='grey',
    width=50
)
textbox = tk.Text(
    width = 20,
    height = 10
)

txt = str(entry.get())
textbox.insert("1.0", txt)


greeting.pack()
entry.pack()
textbox.pack()
window.mainloop()

