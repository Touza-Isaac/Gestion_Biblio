
def afficher_menu():
  print("""
*************************************************

         Bienvenue à votre bibliothèque                        

                    Faites un choix :                                   

*************************************************

   _1. Ajouter adhérent_                                         
   _2. Supprimer adhérent_                                    
   _3. Afficher tous les adhérent_                         
   _4. Ajouter Document_                                       
   _5. Supprimer Document_                                   
   _6. Afficher tous les Documents_                       
   _7. Ajouter Emprunts_                                        
   _8. Retour d’un Emprunts_                                   
   _9. Afficher tous les Emprunts_                          
   _Q. Quitter_                                                        

*************************************************
""")
  
  choix = input("Choisissez une action : ")

  return choix

# Exemple d'utilisation :

#action = afficher_menu()
#print(f"Vous avez choisi l'action {action}")

