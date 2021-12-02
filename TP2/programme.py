#Leroux Gaelle
#02/11/2021
#TP2 Automates

import re
import json

with open('biblio.json') as mon_fichier:
    dictionnaire= json.load(mon_fichier)


def liste(x):
    L=re.split(" |;|,|!|%|$",x) # on enlève tou sles caractère qui peuvent géner
    U=L[len(L)-1].split(".")
    p=[]
    i=0
    for mot in range(len(L)): # on récupère tous les indices ou un "" est apparu lors du split
        m=L[mot]
        if L[mot]=="":
            p.append(mot)
    for indice in p: # on enlève tou sles ""
        del L[indice-i]
        i=i+1        
    if L[len(L)-1]!=U[0] and L[len(L)-1]!=".": # on regarde si le dernier mot est lié avec un point ou pas; le cas échéant on le sépare
        del L[len(L)-1]
        L.append(U[0])
        L.append(".")
    return(L)

Table_de_Transitions=[[1,8,8,8,4,8],[8,1,2,8,8,8],[8,2,8,3,8,8],[5,8,8,8,7,9],[8,8,8,3,8,8],[8,5,6,8,8,8],[8,6,8,8,8,9],[8,8,8,8,8,9]]

def verification():
    x=input('Quel phrase voulez-vous vérifier ?')
    if x==" ": # on vérifie que l'utilisateur n'a pas juste rentré un espace
        return("phrase fausse")
    L=liste(x)
    etat_act=[0]
    entree_act=L[0]
    sortie_act=[0]
    i=0
    for mot in L: # on fait tourner jusqu'a ce que le sortie est la valeur 8 ou 9 ou qu el'on est fini de parcourir la liste
        if mot in dictionnaire:
            entree_act=mot
            v=dictionnaire[entree_act]
            sortie_act=Table_de_Transitions[etat_act[0]][v]
            etat_act=[Table_de_Transitions[etat_act[0]][v],v]
            if sortie_act==9:
                break
            elif sortie_act==8:
                break
        else:
            return("un mot n'est pas connu")
    if sortie_act==8:
        return("la phrase est fausse")
    elif sortie_act==9:
        return("la phrase est juste")
    else:
        return("la phrase est fausse")

print(verification())
