#!/usr/bin/env python3
# coding: utf-8


from tkinter import Tk, StringVar, Entry, Button, Label
from file_chooser import ChooseFileFrame
from methode_chooser import ChooseMethode
from entry_with_label import EntryWithLabel
version = "0.3"


root = Tk()  # Création de la fenêtre racine
root.wm_title("JSE \t-\t" + version)
root.geometry("598x200+250+100")


f_choix_fichier = ChooseFileFrame(root)
f_choix_fichier.grid(column=0, row=0)

choses = {0: "sha1", 1: "sha224", 2: "sha512", 3: "md5"}
f_choose_methode = ChooseMethode(root, choses)
f_choose_methode.grid(column=0, row=1)

f_user_message = EntryWithLabel(root)
f_user_message.grid(column=0, row=2)

root.mainloop()
