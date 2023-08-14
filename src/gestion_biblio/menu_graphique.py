import PySimpleGUI as sg

def afficher_menu_gui():

    sg.theme('DarkTeal9') 
    button_size = (22, 3)

    layout = [
        [sg.Text('Bienvenue dans votre Bibliothèque', font=('Arial', 30, 'bold'))],
        [sg.Text('Faites un choix :', font=('Arial', 20, 'bold'))],
        
        [sg.Button('Ajouter un Adhérent', size=button_size,font=('Arial', 12, 'bold')), sg.Button('Supprimer un adhérent', size=button_size,font=('Arial', 12, 'bold')), sg.Button('Afficher tous les adhérents', size=button_size,font=('Arial', 12, 'bold'))],
        [sg.Button('Ajouter un document', size=button_size,font=('Arial', 12, 'bold')), sg.Button('Supprimer un document', size=button_size,font=('Arial', 12, 'bold')), sg.Button('Afficher tous les documents', size=button_size,font=('Arial', 12, 'bold'))],
        [sg.Button('Ajouter Emprunts', size=button_size,font=('Arial', 12, 'bold')), sg.Button('Retour d\'un Emprunt', size=button_size,font=('Arial', 12, 'bold')), sg.Button('Afficher tous les Emprunts', size=button_size,font=('Arial', 12, 'bold'))], 
        [sg.Button('Quitter', size=button_size,button_color=('white','red'),font=('Arial', 12, 'bold'))]
    ]
    

    window = sg.Window('Menu Bibliothèque', layout,size=(750, 400))
    event, values = window.read()
    window.close()
    
    return event

# Code pour lancer le menu 

def RetourMenu():
    choix = afficher_menu_gui()
    return choix