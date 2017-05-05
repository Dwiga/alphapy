import tkinter
from tkinter import *
from kon import con, exe
from act import btn
from alpha import tst
from tkinter import ttk

daeh = tkinter.Tk()
daeh.geometry("320x240")
tree = ttk.Treeview(daeh)

tree["columns"] = ("one", "two", "three")
tree.column("one", width=100)
tree.column("two", width=100)
tree.column("three", width=100)
"""tree.column("four", width=100)"""

tree.heading("one", text="NAME")
tree.heading("two", text="VOTES")
tree.heading("three", text="PERSENTAGE")
"""tree.heading("four", text="button")"""

a = exe.execute("""select * from movie""")
for wor in a:
    """b = Button(daeh, text="Hapus", command = lambda : tst(wor[0])).grid(row=9, column=2, sticky=W, pady=4)"""
    tree.insert('', 'end', values=(wor[1], wor[2], wor[3]))

tree.bind("<button-1>", btn(wor[1]))

tree.pack()
mainloop()
