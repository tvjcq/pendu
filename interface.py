import tkinter
from tkinter import *


window = Tk()

# Personalisation fenêtre
window.title("Le pendu de bobby")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("./assets/logo.ico")
window.config(background="#404040")

##################################

label_title = Label(window, text="Bienvenue sur le pendu de bobby", font=("Arial", 25), bg="#404040", fg="white")
label_title.pack()


window.mainloop()

