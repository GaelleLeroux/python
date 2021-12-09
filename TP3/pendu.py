from random import randint


fichier = open("TP3/biblio.txt")
contenu=fichier.readlines()

MS=open("TP3/MeilleurScore.txt","a")
MS.write(f"{str(4)}\n")
MS.close()

MS=open("TP3/MeilleurScore.txt")
ms=MS.read
u=0
for i in MS:
    if int(i)>u:
        u=int(i)

print(u)
MS.close()





def pendu():
    print("Tu peux arrêter à tout moment en tapant : stop")
    nb=randint(0,len(contenu)-1)
    mot=contenu[nb]
    print(mot)
    Ladeviner=[]
    Ltrouver=[]
    Ldemander=[]
    i=0
    pa=''
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
    for mot in Ltrouver:
            pa=pa+mot
            pa=pa+' '
    print(pa)
    while Ladeviner!=Ltrouver and i<8:
        pa=''
        x=input("Quelle lettre ?")
        if x=='stop':
            break
        if x in Ldemander:
            print("tu as déà supposé cette lettre")
            Ldemander.remove(x)
            i-=1
        Ldemander.append(x)
        if x in Ladeviner:
            o=[]
            for t in range(0,len(Ladeviner)):
                if Ladeviner[t]==x:
                    o.append(t)
            for u in o:
                Ltrouver[u]=x
            i=i-1
        i=i+1
        for mot in Ltrouver:
            pa=pa+mot
            pa=pa+' '
        print("il te reste :",8-i,"chance")
        print(pa)
    print(i)
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
            return('A bientôt :)')




