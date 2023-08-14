import PySimpleGUI as sg
from class_adherent import Adherent

sg.theme('DarkTeal9') 
 
# Layout gauche avec les boutons
right_layout = [
    [sg.Button('Actualiser',font=('Arial', 12, 'bold'), size=(12, 2))],
    [sg.Button('Supprimer',font=('Arial', 12, 'bold'),size=(12, 2))]
]

layout_add=[
    [sg.Button('Ajouter',font=('Arial', 12, 'bold'),size=(12, 2))]
]

# Exemple de données 
adherents = [
  ['Jean', 'Dupont','06 12 34 56 78', 'jean.dupont@email.com'],
  ['Marie', 'Martin', '06 98 76 54 32', 'marie.martin@email.com'],
  ['Touza', 'ISaac', '6 91 80 53 21', 'isaac_touza@gmail.com'],
  ['Jean', 'Dupont','06 12 34 56 78', 'jean.dupont@email.com'],
  ['Marie', 'Martin', '06 98 76 54 32', 'marie.martin@email.com'],
  ['Touza', 'ISaac', '6 91 80 53 21', 'isaac_touza@gmail.com']
]

# Layout à droite pour afficher la liste
left_layout= [
    [sg.Text('Liste des adhérents',font=('Arial', 12, 'bold'))],
    [sg.Table(values=adherents, headings=['Nom', 'Prénom', 'Téléphone', 'Email'], auto_size_columns=True,
      display_row_numbers=True, justification='center', key='adherents',size=(80, 10),text_color='black', background_color='white')]
]

# Layout du bas pour le formulaire
add_layout = [
    [sg.Text('Ajouter des adhérents',font=('Arial', 12, 'bold'))],
    [
        sg.Column([[sg.Text('Nom',font=('Arial', 12, 'bold'),size=(10,1))], 
                   [sg.Text('Prenom',font=('Arial', 12, 'bold'))]], justification='right'),
        
        sg.Column([[sg.InputText(key='nom',text_color='black', background_color='white',font=('Arial', 11, 'bold'))], 
                   [sg.InputText(key='prenom',text_color='black', background_color='white',font=('Arial', 11, 'bold'))]], justification='left')

    ],
    [
        sg.Column([[sg.Text('Telephone',font=('Arial', 12, 'bold'),size=(10,1))], 
                   [sg.Text('Email',font=('Arial', 12, 'bold'))]], justification='right'),
                   
        sg.Column([[sg.InputText(key='telephone',text_color='black', background_color='white',font=('Arial',11, 'bold'))], 
                   [sg.InputText(key='email',text_color='black', background_color='white',font=('Arial', 11, 'bold'))]], justification='left')       
    ]
]


# Assemblage des layouts  
layout = [
    [
        sg.Column(left_layout ),
        sg.VerticalSeparator(), 
        sg.Column(right_layout,size=(150, 200))
    ],
    [    
     sg.Column(add_layout, element_justification='c')  ,
     sg.Column(layout_add, element_justification='a')  
     ]
]

window = sg.Window('Gestion adhérents', layout,size=(700, 450))

def add_adherents():
  nom = values['nom'] 
  prenom = values['prenom']
  telephone = values['telephone']
  email = values['email']
  adherent=Adherent(nom, prenom, telephone, email)
  ad=[nom,prenom,telephone,email]
  adherents.append(ad)
  window['adherents'].update(adherents)


def supprimer_adherent(nom, prenom):
  for adherent in adherents:
    if adherent[0] == nom and adherent[1] == prenom:
      adherents.remove(adherent)
      window['adherents'].update(adherents)
      break 

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break

    # Ajouter un adherent    
    if event=="Ajouter":
      add_adherents()
    
    #Actualiser la liste
    if event == "Actualiser":
       window['adherents'].update(adherents)
    
    #Supprimer un adherent de la liste
    if event=="Supprimer":
      index = values["adherents"][0]
      ad=adherents[index]
      nom=ad[0]
      prenom=ad[1]
      supprimer_adherent(nom,prenom)
      # Mettre à jour l'affichage
      window["adherents"].update(adherents)
      #adherents.pop(index)
      #window["adherents"].update(adherents) 

window.close()

