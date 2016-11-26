#!/usr/bin/env python3
# coding: utf-8

from tkinter import Tk, Frame, Entry, Label, StringVar


class EntryWithLabel(Frame):
    """docstring for ClassName"""
    def __init__(self, parent, text="Your message :\t"):
        super(EntryWithLabel, self).__init__(parent)
        self.message_label = Label(self, text=text)
        self.message_str = StringVar(self)
        self.message_entry = Entry(self, width=50, textvariable=self.message_str)
        self.message_label.grid(column=0, row=2)
        self.message_entry.grid(column=1, row=2)

    def get_message(self):
        return self.message_str.get()


def main():
    root = Tk()
    root.geometry("598x200+250+100")
    entry_label = EntryWithLabel(root)
    entry_label.grid(column=0, row=0)
    root.mainloop()


if __name__ == "__main__":
    main()
