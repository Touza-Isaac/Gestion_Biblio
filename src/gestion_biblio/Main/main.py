# main.py

from menu import afficher_menu_gui, RetourMenu
import PySimpleGUI as sg
import subprocess
from Gestion_Adherents import GestionAdherent

def Femer():
    layout = [[sg.Text('Voulez vous fermer la fenêtre ?')],
            [sg.Button('Oui'), sg.Button('Non')]]
    window = sg.Window('Confirmation', layout)
    event, values = window.read()
    if event == 'Oui':
        print('Fermeture de la fenêtre principale')
        window.close()
        exit() 
   
        

if __name__ == "__main__":

    choix = RetourMenu()
    print(choix)
    
    if choix=="Quitter":
        Femer()   
     
    if choix=="Gestion des Adherents":
        GestionAdherent()    
   

