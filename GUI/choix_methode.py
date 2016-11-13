#!/usr/bin/env python3
# coding: utf-8

from tkinter import IntVar, Radiobutton, Frame, W


class ChooseMethode(Frame):
    """docstring for ChooseMethode"""
    def __init__(self, arg):
        f_choose_methode = super(ChooseMethode, self).__init__()
        self.var = IntVar()
        button_sha1 = Radiobutton(f_choose_methode, text="sha1", variable=self.var, value=0)
        button_sha224 = Radiobutton(f_choose_methode, text="sha224", variable=self.var, value=1)
        button_sha512 = Radiobutton(f_choose_methode, text="sha512", variable=self.var, value=2)
        button_md5 = Radiobutton(f_choose_methode, text="md5", variable=self.var, value=3)

        button_sha1.pack(anchor=W)
        button_sha224.pack(anchor=W)
        button_sha512.pack(anchor=W)
        button_md5.pack(anchor=W)
