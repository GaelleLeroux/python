
def mesImpots():
    revenu=int(input("vos revenus : "))
    L=[10084,25710,73516,158122]
    I=[0,11/100,30/100,41/100,45/100]
    u=False
    z=0
    impot=0
    l=1
    while u==False and l<len(L):
        if revenu<=L[l] and revenu>=L[l-1]:
            impot=(revenu-L[l-1])*I[l]
            u=True
        l=l+1
    if u==False:
        return(0)
    else:
        for i in range(1,l-1):
            u=L[i]
            p=L[i-1]
            o=I[i]
            m=(L[i]-L[i-1])*I[i]
            impot=impot+(L[i]-L[i-1])*I[i]
        return(impot)
    