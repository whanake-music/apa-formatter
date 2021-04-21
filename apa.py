import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("APA Formatter")

canvas = tk.Canvas(root, width=300, height=20)
canvas.grid(columnspan=2)

mlist = ["test1", "test2"]

TypeL = tk.Label(root, text="Media Type")
TypeL.grid(column=0, row=0)
TypeM = ttk.Combobox(root, values = mlist)
TypeM.set("Select media type")
TypeM.grid(column=1, row=0)

TitleL = tk.Label(root, text="Title")
TitleL.grid(column=0, row=1)
TitleE = tk.Entry(root)
TitleE.grid(column=1, row=1)

NameL = tk.Label(root, text="First Name")
NameL.grid(column=0, row=2)
NameE = tk.Entry(root)
NameE.grid(column=1, row=2)

SurL = tk.Label(root, text="Surname")
SurL.grid(column=0, row=3)
SurE = tk.Entry(root)
SurE.grid(column=1, row=3)

DateL = tk.Label(root, text="Date")
DateL.grid(column=0, row=4)
DateE = tk.Entry(root)
DateE.grid(column=1, row=4)

LinkL = tk.Label(root, text="URL")
LinkL.grid(column=0, row=5)
LinkE = tk.Entry(root)
LinkE.grid(column=1, row=5)

button = tk.Button(root, text="Format")
button.grid(column=1, row=7)

root.mainloop()
