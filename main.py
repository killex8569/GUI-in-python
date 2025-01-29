from tkinter import *
import customtkinter
from customtkinter import CTkImage
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")  # Mode sombre (optionnel)
customtkinter.set_default_color_theme("blue")  # Thème par défaut

# prérequis
app = customtkinter.CTk()
app.geometry("700x600")
app.title("interface de connexion")

def login():
    login_admin = "admin"
    password_admin = "123456"
    
    # récup des infos
    user_login = entry_login.get()
    user_password = entry_password.get()
    
    if user_login == login_admin:
        print("le login est bon")
        if user_password == password_admin:
            print("le mot de passe est bon")
        else:
            print("le mot de passe n'est pas bon !")
    else:
        print("le login n'est pas bon")

# GUI python
main_frame = customtkinter.CTkFrame(master=app, width=200, height=200)
main_frame.pack(pady=100, padx=100, fill="both", expand=True)

title_label = customtkinter.CTkLabel(master=main_frame, text="Connexion")
title_label.pack(pady=12, padx=10)

entry_login = customtkinter.CTkEntry(master=main_frame, placeholder_text="entrez votre login")
entry_login.pack(pady=10, padx=12)

entry_password = customtkinter.CTkEntry(master=main_frame, placeholder_text="entrez votre mot de passe", show="*")
entry_password.pack(pady=10, padx=12)

validation_button = customtkinter.CTkButton(master=main_frame, text="connexion", corner_radius=10, command=login)
validation_button.pack(pady=12, padx=10)

chekbox = customtkinter.CTkCheckBox(master=main_frame, text="se souvenir de moi")
chekbox.pack(pady=12, padx=10)


            


app.mainloop()
