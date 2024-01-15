##projet de notes journal 


##Trier les notes affichage par dernière utilisation
##Faire un systeme de login


import datetime
from pathlib import Path
import os 
from tkinter import * 




chemin_enregistrement = Path("./Notes")

date_actuelle = datetime.datetime.now()

jour = date_actuelle.strftime("%A")
nombre = date_actuelle.day 
mois = date_actuelle.strftime("%B")
heure = date_actuelle.strftime("%H_%M_%S")
date_complete = f"{jour} {nombre} {mois}"
date_complete_heure = f"{jour}_{nombre}_{mois}_{heure}"

nom_fichier =f"Note_{date_complete_heure}.txt"

journal = Tk()
journal.minsize(500,400)
journal.title(f"{date_complete}")

def ecrire_note():
        with chemin_enregistrement.joinpath(nom_fichier).open("w", encoding="UTF-8") as note:
            
            while True :
                ecriture = input("Ecrivez ce qui vous passe par la tête pour sortir appuyez sur 'q' : ")
                if ecriture == 'q':
                    break
            note.write(ecriture) 

            nom_note = input("Voulez-vous donner un nom à cette note (o/n): ").lower()
            if nom_note == 'o':
                titre_note = input("Titre de votre note : ")+".txt"
                nouveau_chemin_fichier = chemin_enregistrement.joinpath(titre_note)
                os.rename(nom_fichier,nouveau_chemin_fichier)
            else:
                print(f"Votre note porte le titre : {nom_fichier}")
            

def ouvrir_note():   
    test = input("Lire une note (read) sinon cela créera une nouvelle note :").lower()
    if test == 'read':
        while True :
            nom_note_a_lire = input("Quelle note ? :  ")
            chemin_note_a_lire = chemin_enregistrement.joinpath(f"{nom_note_a_lire}.txt")
            try:
                with chemin_note_a_lire.open("r", encoding="UTF-8") as note:
                    contenu = note.read()
                    print(contenu)
                    break
            except FileNotFoundError:
                print("Cette note n'existe pas réessayer ('exit' pour quitter)")
                continue
    else:
        ecrire_note()


def main():
    liste = Listbox(journal, height=10, width=50)
    affichage_notes = os.listdir(chemin_enregistrement)
    for note in affichage_notes:
        liste.insert(END, note)
        
    liste.pack()
    if affichage_notes : 
        print(f"Bienvenue dans ton journal personnel 'identifiant' nous sommes le : {date_complete}\n")
        for index,file in enumerate(affichage_notes, start=1):   ##start est un argument de enumerate pour faire commencer index à 1
            print(f"{index}) {file}")
        ouvrir_note()
    else: ##1ere fois que l'utilisateur arrive dans les notes
        print(f"Bienvenue dans ton journal personnel 'identifiant' nous sommes le : {date_complete}")
        ecrire_note()
    
    journal.mainloop()


    