# French project
# By Killex8569

from tkinter import *
import customtkinter
from customtkinter import CTkImage
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")  # Mode sombre (optionnel)
customtkinter.set_default_color_theme("blue")  # Thème par défaut

# Pré-requis
app = customtkinter.CTk()
app.geometry("700x600")
app.title("Interface de Connexion")

# Fonction de connexion
def login():
    login_admin = "admin"
    password_admin = "123456"
    
    # Récupérer les informations de l'utilisateur
    user_login = entry_login.get()
    user_password = entry_password.get()
    
    # Vérification des informations
    if user_login == login_admin and user_password == password_admin:
        print("Connexion réussie.")
        
        # Masquer la frame de connexion
        main_frame.pack_forget()
        
        # Afficher la nouvelle interface utilisateur
        show_user_interface()
    else:
        print("Identifiants incorrects.")

# Fonction pour afficher l'interface utilisateur après connexion
def show_user_interface():
    user_frame = customtkinter.CTkFrame(master=app)
    user_frame.pack(pady=100, padx=100, fill="both", expand=True)

    user_label = customtkinter.CTkLabel(master=user_frame, text="Bienvenue dans l'interface utilisateur")
    user_label.pack(pady=12, padx=10)

    # Ajoute ici les éléments de ton interface utilisateur principale
    # Exemple : un bouton pour fermer l'application
    logout_button = customtkinter.CTkButton(master=user_frame, text="Déconnexion", command=app.quit)
    logout_button.pack(pady=10, padx=10)

# GUI python (Frame de connexion)
main_frame = customtkinter.CTkFrame(master=app, width=200, height=200)
main_frame.pack(pady=100, padx=100, fill="both", expand=True)

title_label = customtkinter.CTkLabel(master=main_frame, text="Connexion")
title_label.pack(pady=12, padx=10)

entry_login = customtkinter.CTkEntry(master=main_frame, placeholder_text="Entrez votre login")
entry_login.pack(pady=10, padx=12)

entry_password = customtkinter.CTkEntry(master=main_frame, placeholder_text="Entrez votre mot de passe", show="*")
entry_password.pack(pady=10, padx=12)

validation_button = customtkinter.CTkButton(master=main_frame, text="Connexion", corner_radius=10, command=login)
validation_button.pack(pady=12, padx=10)

chekbox = customtkinter.CTkCheckBox(master=main_frame, text="Se souvenir de moi")
chekbox.pack(pady=12, padx=10)

app.mainloop()
