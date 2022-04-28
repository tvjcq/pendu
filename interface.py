from tkinter import *
# from main import *

window = Tk()

# Personalisation fenêtre
window.title("Le pendu de bobby")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("./assets/logo.ico")
window.config(background="#404040")

##################################
frame_title = Frame(window, bg="red", bd=1)
frame_subtitle = Frame(window, bg="black", bd=1)
frame_button = Frame(window, bg="white")

gt_button = Button(window, text="Le github de bobby", font=("Arial", 12), bg="white", fg="black")
gt_button.pack(pady=10, side=TOP)
frame_button.pack(side=TOP)

label_title = Label(frame_title, text="Bienvenue sur le pendu de bobby", font=("Arial", 25), bg="#404040", fg="white")
label_title.pack()

label_subtitle = Label(frame_subtitle, text="Entrez votre lettre", font=("Arial", 20), bg="#404040", fg="white")
label_subtitle.pack()
frame_title.pack(side=TOP)
frame_subtitle.pack(side=TOP)







window.mainloop()