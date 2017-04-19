import tkinter
from tkinter import *
from kon import *
from tkinter import ttk

daeh = tkinter.Tk()
tree = ttk.Treeview(daeh)

tree['columns']=("one", "two")
tree.column("one", width=100)
tree.column("two", width=100)
tree.heading("one", text="Column A")
tree.heading("two", text="column B")

a = exe.execute("select * from movie")
for wor in a:
    tree.insert('', 'end', values=(wor[1], wor[2], wor[3]))

mainloop()
