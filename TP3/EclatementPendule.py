from random import randint


def ajout_score(i,mot):
    MS=open("TP3/MeilleurScore.txt","a")
    if mot!='stop':
        MS.write(f"{str(i)}\n")
    MS.close()

def dire_ms():
    MS=open("TP3/MeilleurScore.txt")
    ms=MS.read
    u=0
    for i in MS:
        if int(i)<u:
            u=int(i)
    MS.close()
    return(u)

def mot_a_deviner():
    fichier = open("TP3/biblio.txt")
    contenu=fichier.readlines()
    nb=randint(0,len(contenu)-1)
    mot=contenu[nb]
    Ladeviner=[]
    Ltrouver=[]
    Ldemander=[]
    for q in mot:
        Ladeviner.append(q)
        Ltrouver.append('_')
    if '\n' in Ladeviner:
        Ladeviner.remove('\n')
        Ltrouver.pop(0)
    o=[]
    for t in range(0,len(Ladeviner)):
            if Ladeviner[t]==Ladeviner[0]:
                o.append(t)
            for u in o:
                Ltrouver[u]=Ladeviner[0]
    Ldemander.append(Ladeviner[0])
    fichier.close()
    return(Ladeviner,Ltrouver,Ldemander)

def demande_x():
    x=input("Quelle lettre ?")
    return(x)

def affichage(x,i):
    pa=''
    for mot in x:
            pa=pa+mot
            pa=pa+' '
    return(pa,"il te reste :",8-i,"chance")

def vérif_x(Ldemander,Ladeviner,Ltrouver,x,i):
    if x in Ldemander:
        print("tu as déà supposé cette lettre")
        Ldemander.remove(x)
    Ldemander.append(x)
    if x in Ladeviner:
        o=[]
        for t in range(0,len(Ladeviner)):
            if Ladeviner[t]==x:
                o.append(t)
        for u in o:
            Ltrouver[u]=x
        i=i-1
    return(Ldemander,Ladeviner,Ltrouver,i)

def gagne(Ltrouver,Ladeviner):
    if Ltrouver==Ladeviner:
        return(True)
    else:
        return(False)

def on_retourne(x,i):
    if x=='stop':
        return("le jeu c'est arrêter")
    elif i==8:
        print("Tu as perdu")
        re=input("Tu veux rejouer ?")
        if re=='oui':
            return(pendu())
        else:
            return('A bientôt')
    else:
        print("Tu as gagné !!!")
        re=input("Tu veux rejouer ?")
        if re=='oui':
            return(pendu())
        else:
            return 'A bientôt :)'

def pendu():
    Ladeviner,Ltrouver,Ldemander=mot_a_deviner()
    i=0
    print(affichage(Ltrouver,i))
    gagne2=gagne(Ltrouver,Ladeviner)
    i=0
    print(Ladeviner)
    while gagne2!=True and i<8:
        mot=demande_x()
        if mot=='stop':
            break
        Ldemander,Ladeviner,Ltrouver,i=vérif_x(Ldemander,Ladeviner,Ltrouver,mot,i)
        gagne2=gagne(Ltrouver,Ladeviner)
        i=i+1
        print(affichage(Ltrouver,i))
    print(ajout_score(i,mot))
    print("le meuilleur score est de : ",dire_ms())
    return on_retourne(mot,i)



print(pendu())

