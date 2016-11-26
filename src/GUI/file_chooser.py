#!/usr/bin/env python3
# coding: utf-8

from tkinter import Tk, Frame, StringVar, Entry, Button
from os import getcwd
from tkinter.filedialog import askopenfilename
from functools import partial


class ChooseFileFrame(Frame):
    def __update_field(self, field):
        fname = askopenfilename(initialdir=getcwd())
        field.set(fname)

    def __init__(self, parent):
        super(ChooseFileFrame, self).__init__(parent)
        self.input_file_text = StringVar(self)
        self.input_file_entry = Entry(self, width=100, textvariable=self.input_file_text)
        self.input_file_text.set(getcwd())

        button = Button(self, text='add file',
                        command=partial(self.__update_field, self.input_file_text))

        self.input_file_entry.grid(column=0, row=0)
        button.grid(column=0, row=1)


def main():
    root = Tk()
    root.geometry("598x200+250+100")
    f_chooser = ChooseFileFrame(root)
    f_chooser.grid(column=0, row=0)
    root.mainloop()


if __name__ == "__main__":
    main()
