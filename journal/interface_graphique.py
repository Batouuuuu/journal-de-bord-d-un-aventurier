from tkinter import *
from tkinter import messagebox



def validation_login():

    global tentatives, photo
    entered_username = utilisateur.get()
    entered_password = mdp.get()   
    if entered_username in dico and dico[entered_username] == entered_password:   ##vérif que l'utilisateur est dans le dico et que son mot de passe est correct
        messagebox.showinfo("Login Successful", "Bienvenue dans ton journal cher Âtrien")
        fenetre.destroy()

    elif not entered_username:
        messagebox.showerror("Erreur", "Vous n'avez rien écrit")

    else:
        tentatives -= 1
        messagebox.showerror("Login Failed", f"Mot de passe ou non d'utilisateur faux, il reste {tentatives} essais") 
        if tentatives == 0:
            messagebox.showerror("Login Failed", "Nombre maximum de tentatives atteint. Veuillez réessayer plus tard.")
            fenetre.destroy()  




def sign_in():
    creation_utilisateur = Tk()
    creation_utilisateur.title("Création identifiant")
    creation_utilisateur.minsize(500,300)
    creation_utilisateur.mainloop()


def interface():
    global dico, mdp, utilisateur,fenetre, tentatives, photo
    tentatives = 3   
    dico  = {"root": 'root', "Baptiste": "123"}
    fenetre = Tk()
    fenetre.title("Journal de bord ")
    fenetre.minsize(500,400)
    label = Label(fenetre, text="Bienvenue dans votre journal")
    label.pack()
    label1 = Label(fenetre, text="Qui-êtes vous ? ")
    label1.pack()

    utilisateur = StringVar() 
    entree_username = Entry(fenetre, width=30, textvariable=utilisateur)
    entree_username.pack()

    label1 = Label(fenetre, text="Mot de passe")
    label1.pack()

    mdp = StringVar() 
    entree_password = Entry(fenetre, width=30, show="*", textvariable=mdp)
    entree_password.pack()

    button_login = Button(fenetre, text="Login", command=validation_login)
    button_login.pack()

    button_sign_in = Button(fenetre, text="Sign in", command=sign_in)
    button_sign_in.pack()

    photo = PhotoImage(file="images/outer_wilds.png")
    canvas = Canvas(fenetre,width=500, height=500)
    canvas.create_image(0, 0, anchor=NW, image=photo)
    canvas.pack()


    credit = Label(fenetre, text="Dev by -Batouuuuu ")
    credit.pack()


    fenetre.mainloop()

interface()





