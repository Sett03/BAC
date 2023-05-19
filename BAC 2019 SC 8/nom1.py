from numpy import array
#Nomination
#saise
def saisie():
    N=int(input ("Donner le nombre de produits : "))
    while not (3<=N<=20):
        N=int(input ("Donner le nombre de produits : "))
    return N
#lire nom
def LNom(N):
    T=array([str]*N)
    for i in range (N) :
        T[i]=input("Donner le nom du produit n° "+str(i)+" : ")
        L=len(T[i])
        while not (L==10 and T[i]== T[i].upper()):
            Nom[i]=input("Donner le nom du produit n° ", i, " : ")
    return T
def Sp(ch):
    n=len(ch)
    ch1=""
    A=ch
    for i in range  (n//2):
        ch1=ch1+A[n-i-1]+A[i]
    if n%2==1:
        ch1=ch1+ch[n//2]
    ch=ch1
    return ch
def Spirale (T, N):
    P=int(input("saisir P:"))
    while not 0<P<11:
        P=int(input("saisir P:"))
    ch=""
    for i  in range(N):
        a=T[i]
        ch=ch+a[P-1]
    Tp=array([str]*N)
    for i in range(N):
        ch=Sp(ch)
        Tp[i]=ch
    return Tp
def affiche(Tp,N):
    for i in range (N):
        print (Tp[i])
N=saisie()
T=LNom(N)
Tp=Spirale(T,N)
affiche(Tp,N)
