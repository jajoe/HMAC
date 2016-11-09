#!/usr/bin/env python3
# coding: utf-8


from tkinter import Tk
from file_chooser import ChooseFileFrame
version = "0.1"


root = Tk()  # Création de la fenêtre racine
root.wm_title("JSE \t-\t" + version)
root.geometry("598x120+250+100")


f_choix_fichier = ChooseFileFrame(root)
f_choix_fichier.grid(column=0, row=0)

root.mainloop()  # Lancement de la boucle principale
