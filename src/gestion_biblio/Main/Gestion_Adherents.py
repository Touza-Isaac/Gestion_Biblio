import PySimpleGUI as sg
import sqlite3

def GestionAdherent():
  sg.theme('DarkTeal9')

  # Layout gauche avec les boutons
  right_layout = [
      [sg.Button('Actualiser',font=('Arial', 12, 'bold'), size=(12, 2))],
      [sg.Button('Modifier',font=('Arial', 12, 'bold'),size=(12, 2))],
      [sg.Button('Supprimer',font=('Arial', 12, 'bold'),size=(12, 2),button_color='red')]
  ]

  layout_add=[
      [sg.Text("")],
      [sg.Button('Enregistrer',font=('Arial', 12, 'bold'),size=(12, 2),button_color='green')],
      [sg.Button('Vider',font=('Arial', 12, 'bold'),size=(12, 2),button_color='gray')]
  
  ]
  
  def getAdherents():
      conn = sqlite3.connect('users.db')
      c = conn.cursor() 
    # Sélectionner tous les adhérents
      c.execute("SELECT nom, prenom, telephone, email FROM adherents")
      adherents = c.fetchall()
      conn.close()
      return adherents
  
  # Exemple de données 
  adherents = getAdherents()
  adherents_list = [list(row) for row in adherents]  # Convertir les tuples en listes

  # Layout à droite pour afficher la liste
  left_layout= [
      [sg.Text('Liste des adhérents',font=('Arial', 12, 'bold'))],
      [sg.Table(values=adherents_list, headings=['Nom', 'Prénom', 'Téléphone', 'Email'], auto_size_columns=True,
        display_row_numbers=True, justification='left', key='adherents',size=(0,13),text_color='black', background_color='white')]
  ]

  # Layout du bas pour le formulaire
  add_layout = [
      [sg.Text('Ajouter des adhérents',font=('Arial', 12, 'bold'))],
      [
          sg.Column([[sg.Text('Nom',font=('Arial', 12, 'bold'),size=(10,1))], 
                    [sg.Text('Prenom',font=('Arial', 12, 'bold'))]], 
                    justification='right'
                    ),
          
          sg.Column([[sg.InputText(key='nom',text_color='black', background_color='white',font=('Arial', 11, 'bold'))], 
                    [sg.InputText(key='prenom',text_color='black', background_color='white',font=('Arial', 11, 'bold'))]], 
                    justification='left'
                    )

      ],
      [
          sg.Column([[sg.Text('Telephone',font=('Arial', 12, 'bold'),size=(10,1))], 
                    [sg.Text('Email',font=('Arial', 12, 'bold'))]], justification='right'),
                    
          sg.Column(
            [[sg.InputText(key='telephone',text_color='black', background_color='white',font=('Arial',11, 'bold'))], 
                    [sg.InputText(key='email',text_color='black', background_color='white',font=('Arial', 11, 'bold'))]], justification='left')       
      ]
  ]


  # Assemblage des layouts  
  layout = [
      [
          sg.Column(left_layout),
          sg.VerticalSeparator(), 
          sg.Column(right_layout,size=(150, 200))
      ],
      [    
      sg.Column(add_layout, element_justification='c')  ,
      sg.Column(layout_add, element_justification='a')  
      ]
  ]

  window = sg.Window('Gestion adhérents', layout,size=(830, 450))
  
  def saveAdherent(nom, prenom, telephone, email):
    conn = sqlite3.connect('users.db')
    c = conn.cursor() 
     # Créer la table "adherents" s'elle n'existe pas
    c.execute('''CREATE TABLE IF NOT EXISTS adherents (nom TEXT, prenom TEXT, telephone TEXT, email TEXT)''')
    
    # Vérifier si les informations existent déjà
    c.execute("SELECT * FROM adherents WHERE (nom=? AND prenom=?) OR (telephone=? AND email=?)",
              (nom, prenom, telephone, email))
    existing_adherent = c.fetchone()
    
    if existing_adherent:
        # Mettre à jour les autres informations
         # Mettre à jour les autres informations
        c.execute("UPDATE adherents SET nom=?, prenom=?, telephone=?, email=? WHERE (nom=? AND prenom=?) OR (telephone=? AND email=?)",
                  (nom, prenom, telephone, email, nom, prenom, telephone, email))

    else:
        # Insérer les informations de l'adhérent dans la table
        c.execute("INSERT INTO adherents (nom, prenom, telephone, email) VALUES (?, ?, ?, ?)",
                  (nom, prenom, telephone, email))
    
    conn.commit()
    conn.close()

  
  def add_adherents():
    nom = values['nom'] 
    prenom = values['prenom']
    telephone = values['telephone']
    email = values['email']
    saveAdherent(nom,prenom,telephone,email)
    adherents_list = [list(row) for row in getAdherents()]
    window['adherents'].update(adherents_list)
     #Vider les informations
    window['nom'].update('')
    window['prenom'].update('')
    window['telephone'].update('')
    window['email'].update('')
    # adherent=Adherent(nom, prenom, telephone, email)
    #ad=[nom,prenom,telephone,email]
    #adherents.append(ad)
    #window['adherents'].update(adherents)
  
  def removeAdherent(nom,prenom):
    conn = sqlite3.connect('users.db')
    c = conn.cursor() 
    # Supprimer l'adhérent de la table
    c.execute("DELETE FROM adherents WHERE nom=? AND prenom=?", (nom, prenom)) 
    conn.commit()
    conn.close()
    
  def supprimer_adherent(nom, prenom,adherents_list):
    for adherent in adherents_list:
      if adherent[0] == nom and adherent[1] == prenom:
        removeAdherent(nom, prenom)
        break 
    adherents_list = [list(row) for row in getAdherents()]
    window['adherents'].update(adherents_list)
      
  while True:
      event, values = window.read()
      
      if event == sg.WIN_CLOSED:
          break

      # Ajouter un adherent    
      if event=="Enregistrer":
        add_adherents()
      
      #Actualiser la liste
      if event == "Actualiser":
        adherents_list = [list(row) for row in getAdherents()]
        window['adherents'].update(adherents_list)
      
      #Supprimer un adherent de la liste
      if event=="Supprimer":
        index = values["adherents"][0]
        ad=adherents[index]
        nom=ad[0]
        prenom=ad[1]
        supprimer_adherent(nom,prenom,adherents_list)
        
      if event=="Vider":
        #Vider les informations
        window['nom'].update('')
        window['prenom'].update('')
        window['telephone'].update('')
        window['email'].update('')
      
      if event=="Modifier":
        #on recupere les informations selectionnées
        index = values["adherents"][0]
        ad=adherents[index]
        nom=ad[0]
        prenom=ad[1]
        telephone=ad[2]
        email=ad[3]
        #on remet les informations dans le formulaire
        window['nom'].update(nom)
        window['prenom'].update(prenom)
        window['telephone'].update(telephone)
        window['email'].update(email)
      

  window.close()

GestionAdherent()