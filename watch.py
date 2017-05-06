import tkinter
from tkinter import *
from kon import con, exe
con = con
exe = exe
import ctypes
import datetime

now = datetime.date.today()
root = tkinter.Tk()

isi = StringVar(root)
isi.set("-")

Label(root, text="Tanggal").grid(row=0)
Label(root, text="Judul").grid(row=1)
Label(root, text="Episode").grid(row=2)
Label(root, text="Waktu").grid(row=3)
Label(root, text="Keterangan").grid(row=4)

val1 = Entry(root)
ta = exe.execute("""select * from movie""")
for da in ta:
    val2 = OptionMenu(root, isi, da[1])
val3 = Entry(root)
val4 = Entry(root)
val5 = Entry(root)

val1.insert(10, now)

val1.grid(row=0, column=1)
val1.grid(row=1, column=1)
val1.grid(row=2, column=1)
val1.grid(row=3, column=1)
val1.grid(row=4, column=1)