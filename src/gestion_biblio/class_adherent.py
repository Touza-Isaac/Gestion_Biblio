# Classe Adherent

class Adherent:

  def __init__(self, nom, prenom, telephone, email):
    self.nom = nom
    self.prenom = prenom
    self.telephone = telephone 
    self.email = email

  # autres méthodes

# Fonctions

adherents = [] # Liste pour stocker les adhérents  

def ajouter_adherent(nom, prenom, telephone, email):
  adherent = Adherent(nom, prenom, telephone, email)
  adherents.append(adherent)

def supprimer_adherent(nom, prenom):
  for adherent in adherents:
    if adherent.nom == nom and adherent.prenom == prenom:
      adherents.remove(adherent)
      break 