
def mesImpots():
    revenu=int(input("vos revenus : "))
    if revenu<10085:
        return(0)
    elif revenu>1084 and revenu<25711 :
        return ((revenu-10084)*11/100)
    elif revenu>25711 and revenu<73517 :
        return((revenu-25711)*30/100,(25710-10085)*11%100)
    elif revenu>73516 and revenu<158123:
        return((revenu-73517*41/100+(73516-25711)*30/100+(25710-10085) * 11/100))
    else :
        return((revenu-158)*45/100+(158122-73517*41/100+(73516-25711)*30/100+(25710-10085) * 11/100))