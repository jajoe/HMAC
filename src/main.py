#!/usr/bin/env python3
# coding: utf-8


from tkinter import Tk, StringVar, Entry, Button, Label
from GUI.file_chooser import ChooseFileFrame
from GUI.methode_chooser import ChooseMethode
from GUI.entry_with_label import EntryWithLabel
from hmac_script import hmac_encrypt
from os.path import isfile
from functools import partial
version = "0.4"


def hmac_function(res_field, file_choise, methode_choise, choses, key_choise):
    file = file_choise.input_file_text.get()
    if isfile(file):
        with open(file) as f:
            msg = f.read()
            methode = choses[methode_choise.var.get()]
            key = key_choise.message_str.get()
            res_field["text"] = hmac_encrypt(methode, msg, key)
    else:
        res_field["text"] = "You didn't give a file..."


root = Tk()  # Création de la fenêtre racine
root.wm_title("JSE \t-\t" + version)
root.geometry("598x200+250+100")


f_choix_fichier = ChooseFileFrame(root)
f_choix_fichier.grid(column=0, row=0)

choses = {0: "sha1", 1: "sha224", 2: "sha512", 3: "md5"}
f_choose_methode = ChooseMethode(root, choses)
f_choose_methode.grid(column=0, row=1)

f_user_key = EntryWithLabel(root, text="Your key")
f_user_key.grid(column=0, row=2)

label_hmac = Label(root, text="")
button_hmac = Button(root, text='GO HMAC', command=partial(hmac_function, label_hmac, f_choix_fichier, f_choose_methode, choses, f_user_key))

button_hmac.grid(column=0, row=3)
label_hmac.grid(column=0, row=4)

root.mainloop()
