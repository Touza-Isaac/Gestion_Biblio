import PySimpleGUI as sg

def creer_fenetre_menu():
    layout = [
        [sg.Text('Bienvenue à la bibliothèque')],      
        [sg.Text('Que souhaitez-vous faire ?')],
        [sg.Button('1 Consulter livres'), sg.Button('2 Consulter DVDs')],
        [sg.Button('3 Emprunter'), sg.Button('4 Restituer')],
        [sg.Button('5 Quitter')]
    ]
    
    return sg.Window('Menu bibliothèque', layout)

def creer_fenetre_emprunt():
    layout = [
        [sg.Text('Emprunt de document')],
        [sg.Text('Titre'), sg.InputText(key='titre')],
        [sg.Text('Nom emprunteur'), sg.InputText(key='nom')],
        [sg.Button('Valider'), sg.Button('Retour menu')]
    ]
    
    return sg.Window('Emprunt', layout) 

def main():
    window = creer_fenetre_menu()
    
    while True:
        event, values = window.read()
        
        if event in (sg.WIN_CLOSED, '5 Quitter'):
            break
            
        if event == '3 Emprunter':
            window.close()
            window = creer_fenetre_emprunt()
            
            # traitement emprunt...
            
            window.close()
            window = creer_fenetre_menu()
            
    window.close()
    
main()