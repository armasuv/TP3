#Crée par Victor Ionut Armasu en 2023
#TP3

#Importation

import random
import sys

#Fonctions:
puissance_boss = 0
vies_boss = 0
niveau_vie = 20
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
nombre_victoires_consecutives = 0
force_adversaire = 0
statut_combat = "Victoire"
god_mode = False

#Introduction
print("Vous êtes dans un monde plein de couloirs, et à chaque bout de couloir se trouve une porte qui cache un ennemi de différents niveaux.")
print("Vous êtes arrivés au premier combat:")

#fonction qui contient les règle du jeu
def regles_du_jeu():
   print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire."
    "Dans ce cas,le niveau de vie de l’usager est augmenté de la force de l’adversaire."
    "\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire." ""
    " Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. \nLa partie se termine lorsque les points de vie de l’usager tombent sous 0. "
    "\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

#Fonction qui définit le menu

def menu():
   print("Que voulez-vous faire ?\n"
  "1- Combattre cet adversaire \n"
  "2- Contourner cet adversaire et aller ouvrir une autre porte \n"
  "3- Afficher les règles du jeu\n"
  "4- Quitter la partie\n");


#Commencement de la fonction prinicpale, jeu
def jeu():
   global niveau_vie
   global numero_combat
   global nombre_victoires
   global nombre_defaites
   global nombre_victoires_consecutives
   global god_mode
   global vies_boss
   global puissance_boss
   while niveau_vie > 0:


        #Mode de jeu avec difficulté normale

       if god_mode == False:

           #Détécte si vous avez assez de victoires pour affronter le boss en difficulté normale

           if nombre_victoires_consecutives == 3:
               print("\n\nVous êtes arrivez devant un boss!!")
               print("Maintenant, vous allez les deux roulez des dès, et la personne qui a le plus grand montant peu attaquer l'autre avec ce montant. Le boss a le même nombre de vie que toi: ",niveau_vie)
               print("Vous gangez deux dès 3!!!")
               vies_boss = niveau_vie
               while vies_boss > 0:
                   puissance_boss = random.randint(1, 10)
                   print("Le boss attaque avec une puissance de ", puissance_boss)
                   choix_attaque = int(input("Vous voulez attaquer, 1, ou ésquiver, ce qui vous fait la moitié des dommages de son attaque, 2?"))
                   if choix_attaque == 1:
                       lancer_des10 = random.randint(1, 10)
                       if lancer_des10 > puissance_boss:
                           print("Bravo, vous faites ", lancer_des10,"dommages au boss!")
                           vies_boss -= 10
                           print("\nVous avez ",niveau_vie,"vies et le boss a ",vies_boss,"vies.")
                       else:
                           print("OH non, vous perdez ",puissance_boss,"dommages!")
                           niveau_vie -= puissance_boss
                           print("\nVous avez ", niveau_vie, "vies et le boss a ", vies_boss, "vies.")
                           if niveau_vie <= 0:
                               print("GAME OVER")
                               sys.exit()
                   else:
                       moitier_dommages = puissance_boss/2
                       print("Vous perdez ",moitier_dommages,"dommages!")
                       niveau_vie -= moitier_dommages
                       print("\nVous avez ", niveau_vie, "vies et le boss a ", vies_boss, "vies.")
                       if niveau_vie <= 0:
                           print("GAME OVER")
                           sys.exit()
               #Boss finit, le mode de jeu  normal recommence
               print("Bravo! Vous avez battus le boss!\nVous retournez dans le monde des corridors et poursuivaient votre aventure.")


           #Le mode de jeu normal avec les adversaires normals dans les corridors
           force_adversaire = random.randint(1, 10)
           print("\nLa force de l'adversaire est de", force_adversaire,"\n""")
           choix = int(input(menu()))
           if choix == 1:
               lancer_des = random.randint(1, 5)
               lancer_des2 = random.randint(1, 5)
               total_des = lancer_des + lancer_des2
               print("Vous avez roulez:", total_des)
               if total_des > force_adversaire:
                   print("Bravo! Vous avez gagné le combat, vous gagnez ", force_adversaire," vie!")
                   niveau_vie += force_adversaire
                   numero_combat += 1
                   nombre_victoires += 1
                   nombre_victoires_consecutives += 1
                   print("combat numéro= ", numero_combat,"\nvie= ", niveau_vie,"\nnombres de défaites =", nombre_defaites,"\nle nombre de victoires =", nombre_victoires,"\n et le nombre de victoires consécutifs: ", nombre_victoires_consecutives)
                   jeu()
                   if nombre_victoires_consecutives > 3:
                       print("\n\nVous êtes arrivez devant un boss!!")
               else:
                   print("\nVous avez perdu le combat et vous perdez ",force_adversaire," vies!!!")
                   nombre_victoires_consecutives = 0
                   niveau_vie -= force_adversaire
                   numero_combat += 1
                   nombre_defaites += 1
                   print("combat numéro= ", numero_combat,"\nvie= ", niveau_vie,"\nnombres de défaites =", nombre_defaites,"\nle nombre de victoires =", nombre_victoires,"\n et le nombre de victoires consécutifs: ", nombre_victoires_consecutives)
                   jeu()


           elif choix == 2:
               print("Vous passez au prochains adversaire en perdant 1 vie.")
               niveau_vie = niveau_vie -1
               print(niveau_vie)
           elif choix == 3:
               print(regles_du_jeu())
           elif choix == 69:
               god_mode = True
               print("GOD MODE ACTIVATED")
               niveau_vie +=10
               print("Vous avez ", niveau_vie,"vies et la force de l'adversaire est de maximum 3 ;)")


           else:
               print("Bye")
               sys.exit()

       #Mode de jeu facile/god, mais la difficulté du boss n'est pas facile

       elif god_mode == True:

           #Détécte si vous avez assez de victoires pour affronter le boss qui possède plus de vies

           if nombre_victoires_consecutives == 3:
               print("\n\nVous êtes arrivez devant un boss!!")
               print("Maintenant, vous allez les deux roulez des dès, et la personne qui a le plus grand montant peu attaquer l'autre avec ce montant. Le boss a le même nombre de vie que toi: ",niveau_vie)
               print("Vous gangez un des 10!!!")
               vies_boss = niveau_vie
               while vies_boss > 0:
                   puissance_boss = random.randint(1, 10)
                   print("Le boss attaque avec une puissance de ", puissance_boss)
                   choix_attaque = int(input("Vous voulez attaquer, 1, ou ésquiver, ce qui vous fait la moitié des dommages de son attaque, 2?"))
                   if choix_attaque == 1:
                       lancer_des10 = random.randint(1, 10)
                       if lancer_des10 > puissance_boss:
                           print("Bravo, vous faites ", lancer_des10,"dommages au boss!")
                           vies_boss -= 10
                           print("\nVous avez ",niveau_vie,"vies et le boss a ",vies_boss,"vies.")
                       else:
                           print("OH non, vous perdez ",puissance_boss,"dommages!")
                           niveau_vie -= puissance_boss
                           print("\nVous avez ", niveau_vie, "vies et le boss a ", vies_boss, "vies.")
                           if niveau_vie <= 0:
                               print("GAME OVER")
                               sys.exit()
                   else:
                       moitier_dommages = puissance_boss/2
                       print("Vous perdez ",moitier_dommages,"dommages!")
                       niveau_vie -= moitier_dommages
                       print("\nVous avez ", niveau_vie, "vies et le boss a ", vies_boss, "vies.")
                       if niveau_vie <= 0:
                           print("GAME OVER")
                           sys.exit()
               #Boss battus, retours dans le mode de jeu facile avec les corridors

               print("Bravo! Vous avez battus le boss!\nVous retournez dans le monde des corridors et poursuivaient votre aventure.")



           #Mode de jeu facile avec les monstres difficulté facile

           force_adversaire= 3
           print("\nLa force de l'adversaire est de", force_adversaire,"\n")
           choix = int(input(menu()))
           if choix == 1:
               lancer_des = random.randint(1, 5)
               lancer_des2 = random.randint(1, 5)
               total_des = lancer_des + lancer_des2
               print("Vous avez roulez:", total_des)
               if total_des > force_adversaire:
                   print("Bravo! Vous avez gagné le combat, vous gagnez ", force_adversaire," vie!")
                   niveau_vie += force_adversaire
                   numero_combat += 1
                   nombre_victoires += 1
                   nombre_victoires_consecutives += 1
                   print("combat numéro= ", numero_combat,"\nvie= ", niveau_vie,"\nnombres de défaites =", nombre_defaites,"\nle nombre de victoires =", nombre_victoires,"\n et le nombre de victoires consécutifs: ", nombre_victoires_consecutives)
                   jeu()

               else:
                   print("\nVous avez perdu le combat et vous perdez ",force_adversaire," vies!!!")
                   nombre_victoires_consecutives = 0
                   niveau_vie -= force_adversaire
                   numero_combat += 1
                   nombre_defaites += 1
                   print("combat numéro= ", numero_combat,"\nvie= ", niveau_vie,"\nnombres de défaites =", nombre_defaites,"\nle nombre de victoires =", nombre_victoires,"\n et le nombre de victoires consécutifs: ", nombre_victoires_consecutives)

           elif choix == 2:
               print("Vous passez au prochains adversaire en perdant 1 vie.")
               niveau_vie = niveau_vie -1
               print(niveau_vie)
           elif choix == 3:
               print(regles_du_jeu())
           else:
               print("Bye")
               sys.exit()

#On active la fonction jeu qui constitue tout le programme
jeu()


