#!/usr/bin/env python3
# coding: utf-8


from tkinter import Tk
from file_chooser import ChooseFileFrame
from methode_chooser import ChooseMethode
version = "0.2"


root = Tk()  # Création de la fenêtre racine
root.wm_title("JSE \t-\t" + version)
root.geometry("598x200+250+100")


f_choix_fichier = ChooseFileFrame(root)
f_choix_fichier.grid(column=0, row=0)
choses = {0: "sha1", 1: "sha224", 2: "sha512", 3: "md5"}
f_choose_methode = ChooseMethode(root, choses)
f_choose_methode.grid(column=0, row=1)
root.mainloop()
