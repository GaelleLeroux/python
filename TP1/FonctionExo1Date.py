

def bisextile(x):
    if (x%100!=0 and x%4==0) or x%400==0:
        return(True)
    else:
        return(False)
    
def jours(mois,anne):
    if mois>12:
        return("ce n'est pas un mois valide")
    elif mois==1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12:
        return(31)
    elif bisextile(anne)==True:
        return(28)
    elif bisextile(anne)==False:
        return(29)
    else : 
        return(30)
    
def DateValide(jour,mois,anne):
    if mois>12:
        return(False)
    elif jours(mois,anne)<jour:
        return(False)
    else:
        return(True)
    
def DateValideFinal():
    anne=int(input("anne :"))
    mois=int(input("mois :"))
    jour=int(input("jours : "))
    if DateValide(jour,mois,anne)==True:
        return("date valide")
    else:
        return("date non valide")