import tkinter
from tkinter import *
import sqlite3
import ctypes

con = sqlite3.connect('alpha.db')
exe = con.cursor()


class Application(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        self.master.minsize(width=256, height=256)
        self.master.config()
        self.pack()

        self.main_frame = tkinter.Frame()

        self.some_list = [
            'One',
            'Two',
            'Three',
            'Four'
        ]

        self.some_listbox = tkinter.Listbox(self.main_frame)

        # bind the selection event to a custom function
        # Note the absence of parentheses because it's a callback function
        self.some_listbox.bind('<<ListboxSelect>>', self.listbox_changed)
        self.some_listbox.pack(fill='both', expand=True)
        self.main_frame.pack(fill='both', expand=True)

        # insert our items into the list box
        for i, item in enumerate(self.some_list):
            self.some_listbox.insert(i, item)

        # make a label to show the selected item
        self.some_label = tkinter.Label(self.main_frame, text="Welcome to SO!")
        self.some_label.pack(side='top')

        # not really necessary, just make things look nice and centered
        self.main_frame.place(in_=self.master, anchor='c', relx=.5, rely=.5)

    def listbox_changed(self, *args, **kwargs):
        selection_index = self.some_listbox.curselection()
        selection_text = self.some_listbox.get(selection_index, selection_index)
        self.some_label.config(text=selection_text)
        t = ("john", "097")
        j = 1
        if j == "One":
            exe.execute("CREATE TABLE IF NOT EXISTS agenda("
                                 "nome TEXT PRIMARY KEY NOT NULL,"
                                 "telefone  TEXT NOT NULL)")
            con.commit()
        elif j == 1:
            exe.execute("INSERT INTO agenda(nome,telefone) VALUES (?,?)",t)
            con.commit()
            ctypes.windll.user32.MessageBoxW(0, "ct %s" % selection_text, "ypes", 1)
        else:
            print ("dobol %s" % selection_text)
            

root = tkinter.Tk()
app = Application(root)
app.mainloop()
