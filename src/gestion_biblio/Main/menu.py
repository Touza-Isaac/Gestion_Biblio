import PySimpleGUI as sg

def afficher_menu_gui():

    sg.theme('DarkTeal9') 
    button_size = (16, 4)

    layout = [
        [sg.Text('Application de Gestion de Bibliothèque',auto_size_text=True, font=('Arial', 25, 'bold'))],
        [sg.Text('')], 
        [sg.Text('Faites un choix :', font=('Arial', 20, 'bold'))],
        [sg.Text('')], # Ligne vide
        [sg.HorizontalSeparator()],
        [sg.Text('')], # Ligne vide
        [
            sg.Button(
                'Gestion des \n Adherents', 
                size=button_size,
                font=('Arial', 12, 'bold'),
                button_color="green"),
            
            sg.Button(
                'Gestion des \n  Documents', 
                size=button_size,
                font=('Arial', 12, 'bold'),
                button_color="fuchsia"),
            
            sg.Button(
                'Gestions des \n  Emprunts', 
                size=button_size,font=('Arial', 12, 'bold'),
                button_color="blue"),
            
             sg.Button(
                'Ajouter un \n utilisateur', 
                size=button_size,font=('Arial', 12, 'bold'),
                button_color="gray")
            
            ] 
       # [sg.Button('Quitter', size=button_size,button_color=('white','red'),font=('Arial', 12, 'bold'))]
    ]
    

    window = sg.Window('Menu Bibliothèque', layout,size=(750, 400))
    event, values = window.read()
    #window.close()
    
    return event

# Code pour lancer le menu 

def RetourMenu():
    choix = afficher_menu_gui()
    return choix