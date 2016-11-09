#!/usr/bin/env python3
# coding: utf-8

from tkinter import Frame, StringVar, Entry, Button
from os import getcwd
from tkinter.filedialog import askopenfilename
from functools import partial


def update_field(field):
    fname = askopenfilename(initialdir=getcwd())
    field.set(fname)


class ChooseFileFrame(Frame):
    def __init__(self, parent):
        f_choix_fichier = super(ChooseFileFrame, self).__init__(parent)
        input_file_text = StringVar(f_choix_fichier)
        input_file_entry = Entry(f_choix_fichier, width=50, textvariable=input_file_text)
        input_file_text.set(getcwd())

        button = Button(f_choix_fichier, text='add file',
                 command=partial(update_field, input_file_text))

        input_file_entry.grid(column=0, row=0)
        button.grid(column=0, row=1)