#!/usr/bin/env python3
# coding: utf-8

from tkinter import IntVar, Radiobutton, Frame, Tk


class ChooseMethode(Frame):
    """docstring for ChooseMethode"""
    def __init__(self, parent, var_dict, side="left"):
        super(ChooseMethode, self).__init__(parent)
        self.var = IntVar()

        def print_debug(value):
            print(value)

        for value, button_name in var_dict.items():
            self.button = Radiobutton(self, text=button_name, variable=self.var, value=value)
            self.button.pack(side=side)


def main():
    root = Tk()
    root.geometry("598x200+250+100")
    choses = {0: "sha1", 1: "sha224", 2: "sha512", 3: "md5"}
    f_choose_methode = ChooseMethode(root, choses)
    f_choose_methode.grid(column=0, row=0)

    root.mainloop()


if __name__ == "__main__":
    main()
