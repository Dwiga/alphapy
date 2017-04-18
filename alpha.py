import tkinter
from tkinter import *
from kon import *
import ctypes
import act

ndas = tkinter.Tk()

Label(ndas, text="First Name").grid(row=0)
Label(ndas, text="Last Name").grid(row=1)

e1 = Entry(ndas)
e2 = Entry(ndas)
e1.insert(10,"Miller")
e2.insert(10,"Jill")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def show_entry_fields():
    print ("first name : %s/nLast name : %s" % (e1.get(), e2.get()))
    exe.execute("insert into agenda (nome, telefone) values (?,?)", (e1.get(), e2.get()))
    con.commit()

Button(ndas, text='Quit', command=ndas.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(ndas, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop()
