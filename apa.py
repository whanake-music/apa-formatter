import tkinter as tk

root = tk.Tk()
root.title("APA Formatter")

canvas = tk.Canvas(root, width=300, height=20)
canvas.grid(columnspan=2)

TitleL = tk.Label(root, text="Title")
TitleL.grid(column=0, row=0)
TitleE = tk.Entry(root)
TitleE.grid(column=1, row=0)

NameL = tk.Label(root, text="First Name")
NameL.grid(column=0, row=1)
NameE = tk.Entry(root)
NameE.grid(column=1, row=1)

SurL = tk.Label(root, text="Surname")
SurL.grid(column=0, row=2)
SurE = tk.Entry(root)
SurE.grid(column=1, row=2)

DateL = tk.Label(root, text="Date")
DateL.grid(column=0, row=3)
DateE = tk.Entry(root)
DateE.grid(column=1, row=3)

LinkL = tk.Label(root, text="URL")
LinkL.grid(column=0, row=4)
LinkE = tk.Entry(root)
LinkE.grid(column=1, row=4)

button = tk.Button(root, text="Format")
button.grid(column=1, row=5)

root.mainloop()
