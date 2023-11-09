#Crée par Victor Ionut Armasu en 2023
#TP3

#Fonctions:

import random
import sys

niveau_vie = 20
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
nombre_victoires_consecutives = 0
force_adversaire = 0
god_mode = False


print("Vous êtes dans un monde plein de couloirs, et à chaque bout de couloir se trouve une porte qui cache un ennemi de différents niveaux.")
print("Vous êtes arrivés au premier combat:")
def regles_du_jeu():
    print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. Dans ce cas,le niveau de vie de l’usager est augmenté de la force de l’adversaire.\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. \nLa partie se termine lorsque les points de vie de l’usager tombent sous 0. \nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

def menu():
    print("Que voulez-vous faire ?\n"
	"1- Combattre cet adversaire \n"
	"2- Contourner cet adversaire et aller ouvrir une autre porte \n"
	"3- Afficher les règles du jeu\n"
	"4- Quitter la partie\n");




def jeu():
    global niveau_vie
    global numero_combat
    global nombre_victoires
    global nombre_defaites
    global nombre_victoires_consecutives
    global god_mode
    while niveau_vie > 0:
        if god_mode == False:
            force_adversaire = random.randint(1, 5)
            print("La force de l'adversaire est de", force_adversaire)
            choix = int(input(menu()))
            if choix == 1:
                lancer_des = random.randint(1, 6)
                print("Vous avez roulez:", lancer_des)
                if lancer_des > force_adversaire:
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
                niveau_vie +=1000         
                print("Vous avez ", niveau_vie,"vies et la force de l'adversaire est de maximum 1 ;)")


            else:
                print("Bye")
                sys.exit()
        elif god_mode == True:
            if nombre_victoires_consecutives > 3:
                print("\n\nVous êtes arrivez devant un boss!!")
            force_adversaire= 1
            print("La force de l'adversaire est de", force_adversaire)
            choix = int(input(menu()))
            if choix == 1:
                lancer_des = random.randint(1, 6)
                print("Vous avez roulez:", lancer_des)
                if lancer_des > force_adversaire:
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


jeu()
