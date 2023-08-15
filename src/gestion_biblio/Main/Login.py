import PySimpleGUI as sg
import sqlite3

# Création de la base de données SQLite
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (login TEXT, password TEXT)''')
conn.commit()

# Fonction pour ajouter un utilisateur à la base de données
def add_user(login, password):
    c.execute("INSERT INTO users (login, password) VALUES (?, ?)", (login, password))
    conn.commit()
    sg.popup("Succès", "Utilisateur ajouté avec succès!")

# Fonction pour gérer la connexion
def login(login, password):
    c.execute("SELECT * FROM users WHERE login=? AND password=?", (login, password))
    user = c.fetchone()
    if user:
        return True
    else:
        sg.popup_error("Erreur", "Utilisateur inconnu")
        return False

# Mise en page de la fenêtre principale
layout_main = [
    [sg.Text("Gestion d'utilisateurs")],
    [sg.Button("Ajouter Utilisateur"), sg.Button("Connexion")],
]

#window_main = sg.Window("Gestion d'utilisateurs", layout_main)


def AddUSer():
    layout_add_user = [
      [sg.Text("Ajouter un utilisateur",font=('Arial',14,'bold'))],
          [
                sg.Column([[sg.Text('Login',font=('Arial',12,'bold'))], 
                        [sg.Text('Mot de passe',font=('Arial',12,'bold'))]], 
                        justification='right'
                        ),
                sg.Column([[sg.InputText(key='-ADDLOGIN-',text_color='black', background_color='white', size=35)], 
                        [sg.InputText(key="-ADDPASSWORD-", password_char="*",text_color='black', background_color='white', size=35)]], 
                        justification='left'
                        )
                ],
                
                [
                        [
                            sg.Text("",size=14) ,
                            sg.Button("Ajouter",size=12,font=('Bold'),button_color='green'), 
                            sg.Text(""),
                            sg.Button("Annuler",size=12,font=('Bold'),button_color='red')
                            ]
                ]
            ]
    
    window_add_user = sg.Window("Ajouter un utilisateur", layout_add_user)
    while True:
        event, values = window_add_user.read()
        if event == sg.WINDOW_CLOSED or event == "Annuler":
            break
        if event == "Ajouter":
            add_user(values["-ADDLOGIN-"], values["-ADDPASSWORD-"])
            window_add_user.close()

# Boucle d'événements principale
#while True:
#    event, _ = window_main.read()

#    if event == sg.WINDOW_CLOSED:
#        break
  
def Connexion():
    layout_login = [
            [sg.Text("Connexion",font=('Helvetica',14,'bold'))],
            
              [
               sg.Column([[sg.Text('Login',font=('Arial',12,'bold'))], 
                    [sg.Text('Mot de passe',font=('Arial',12,'bold'))]], 
                    justification='right'
                    ),
          
               sg.Column([[sg.InputText(key='-LOGIN-',text_color='black', background_color='white', size=35)], 
                    [sg.InputText(key="-PASSWORD-", password_char="*",text_color='black', background_color='white', size=35)]], 
                    justification='left'
                    )
            ],
            
            [
                    [
                        sg.Text("",size=14) ,
                        sg.Button("Connexion",size=12,font=('Bold'),button_color='green'), 
                        sg.Text(""),
                        sg.Button("Annuler",size=12,font=('Bold'),button_color='red')
                        ]
            ]
        ]

    window_login = sg.Window("Connexion", layout_login)
    
    while True:
            event, values = window_login.read()

            if event == sg.WINDOW_CLOSED or event == "Annuler":
                break

            if event == "Connexion":
                if login(values["-LOGIN-"], values["-PASSWORD-"]):
                    sg.popup("Succès", "Connexion réussie!")
                    window_login.close()
                    
                     
    
    if event == "Ajouter Utilisateur":
        AddUSer()                
    if event == "Connexion":
        Connexion() 

#window_main.close()
