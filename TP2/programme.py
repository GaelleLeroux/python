import re

dictionnaire ={"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "Jean" : 4,"joue" : 3, "." : 5}

def liste(x):
    L=re.split(" |;|,|!|%|$",x)
    U=L[len(L)-1].split(".")
    p=[]
    i=0
    for mot in range(len(L)):
        m=L[mot]
        if L[mot]=="":
            p.append(mot)
    for indice in p:
        del L[indice-i]
        i=i+1        
    if L[len(L)-1]!=U[0] and L[len(L)-1]!=".":
        del L[len(L)-1]
        L.append(U[0])
        L.append(".")
    return(L)
#print(liste("le ,joli chat! ; %joue!."))


Table_de_Transitions=[[1,8,8,8,4,8],[8,1,2,8,8,8],[8,2,8,3,8,8],[5,8,8,8,7,9],[8,8,8,3,8,8],[8,5,6,8,8,8],[8,6,8,8,8,9],[8,8,8,8,8,9]]
Table_de_Sorties=[1,2]


def verification(x):
    L=liste(x)
    etat_act=[0]
    entree_act=L[0]
    sortie_act=[0]
    i=0
    for mot in L:
        entree_act=mot
        v=dictionnaire[entree_act]
        sortie_act=Table_de_Transitions[etat_act[0]][v]
        etat_act=[Table_de_Transitions[etat_act[0]][v],v]
        if sortie_act==9:
            break
        elif sortie_act==8:
            break
    if sortie_act==8:
        return("la phrase est fausse")
    elif sortie_act==9:
        return("la phrase est juste")
    else:
        return("la phrase est fausse 2")

print(verification("la grosse souris verte mange le joli petite chat blanc."))
