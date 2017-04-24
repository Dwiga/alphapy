import tkinter
from tkinter import *
from kon import con, exe
from tkinter import ttk

daeh = tkinter.Tk()
daeh.geometry("320x240")
tree = ttk.Treeview(daeh)

tree["columns"] = ("one", "two", "three")
tree.column("one", width=100)
tree.column("two", width=100)
tree.column("three", width=100)

tree.heading("one", text="NAME")
tree.heading("two", text="VOTES")
tree.heading("three", text="PERSENTAGE")

a = exe.execute("""select * from movie""")
for wor in a:
    tree.insert('', 'end', values=(wor[1], wor[2], wor[3]))

tree.pack()
mainloop()
