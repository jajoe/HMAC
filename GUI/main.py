#!/usr/bin/env python3
# coding: utf-8

from os import getcwd
from tkinter import Tk
from tkinter import Label, StringVar, Entry
from tkinter.filedialog import *
from functools import partial
version = "0.1"


def update_field(field):
    fname = askopenfilename(initialdir=getcwd())
    field.set(fname)


root = Tk()  # Création de la fenêtre racine
root.wm_title("JSE \t-\t" + version)


input_file_text = StringVar(root)
input_file_entry = Entry(root, textvariable=input_file_text)
input_file_text.set(getcwd())

button = Button(root, text='add file',
                command=partial(update_field, input_file_text))

input_file_entry.grid(column=0, row=0)
button.grid(column=0, row=1)


root.mainloop()  # Lancement de la boucle principale
