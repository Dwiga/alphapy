"""My Project"""
import tkinter
from tkinter import *
from kon import con, exe
con = con
exe = exe
from act import cba
import ctypes
import act
import datetime
from tkinter import ttk

today = datetime.date.today()
ndas = tkinter.Tk()
tree = ttk.Treeview(ndas)

able = StringVar(ndas)
able.set("English")

def sve():
    exe.execute("insert into movie (title, tanggal, episode, keterangan, rating, country, lang, genre, tglinput) values (?,?,?,?,?,?,?,?, ?)", (e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(),able.get(),e8.get(), today))
    con.commit()
    e1.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    e5.delete(0, "end")
    e6.delete(0, "end")
    e8.delete(0, "end")
    
def tst(dta):
    exe.execute("""delete from movie where id=?""", (dta))
    con.commit()

Label(ndas, text="Title").grid(row=0)
Label(ndas, text="Tanggal").grid(row=1)
Label(ndas, text="Episode").grid(row=2)
Label(ndas, text="Keterangan").grid(row=3)
Label(ndas, text="Rating").grid(row=4)
Label(ndas, text="Country").grid(row=5)
Label(ndas, text="Language").grid(row=6)
Label(ndas, text="Genre").grid(row=7)

e1 = Entry(ndas)
e2 = Entry(ndas)
e3 = Entry(ndas)
e4 = Entry(ndas)
e5 = Entry(ndas)
e6 = Entry(ndas)
e7 = OptionMenu(ndas, able, "English", "Japanese", "Korean", "Thai")
e8 = Entry(ndas)

e2.insert(10, today)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)
e8.grid(row=7, column=1)

Button(ndas, text='Quit', command=ndas.quit).grid(row=9, column=0, sticky=W, pady=4)
Button(ndas, text='Save', command=sve).grid(row=9, column=1, sticky=W, pady=4)
Button(ndas, text='Coba', command= lambda: cba(e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(),able.get(),e8.get())).grid(row=9, column=2, sticky=W, pady=4)

mainloop()
