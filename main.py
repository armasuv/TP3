#Crée par Victor Ionut Armasu en 2023
#TP3

#Fonctions:

niveau_vie = 20
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
nombre_victoires_consecutives = 0

def regles_du_jeu():
    print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire. Dans ce cas,le niveau de vie de l’usager est augmenté de la force de l’adversaire.\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. \nLa partie se termine lorsque les points de vie de l’usager tombent sous 0. \nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

