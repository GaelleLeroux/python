def Syracus(x):
    L=[x]
    u=[]
    max=x
    while u!=[1,4,2] :
        if x%2==0:
            x=x/2
            L.append(x)
            
            if x==1:
                u.append(x)
            elif x==4 and u==[1]:
                u.append(x)
            elif x==2 and u==[1,4]:
                u.append(x)
            else:
                u=[]
        else:
            x=x*3+1
            L.append(x)
            
            if x==1:
                u.append(x)
            elif x==4 and u==[1]:
                u.append(x)
            elif x==2 and u==[1,4]:
                u.append(x)
            else:
                u=[]
    for i in range(0,len(L)-3):
        if L[i]>max:
            max=L[i]
    return(max,len(L)-3,L)


def TempDeVol(min,max):
    u=0
    Tmax=0
    for i in range(min,max+1):
        n,p,q=Syracus(i)
        if p>Tmax:
            Tmax=p
            u=i
    return(u,Tmax)

def AltitudeMax(min,max):
    u=0
    Amax=0
    for i in range(min,max+1):
        n,p,q=Syracus(i)
        if n>Amax:
            Amax=n
            u=i
    return(u,Amax)
            
            
        
            
        