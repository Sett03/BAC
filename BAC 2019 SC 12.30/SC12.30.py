from numpy import array
#saisie
def saisie():
    N=int(input("Saisir le nombre des adhérents:"))
    while not (5<=N<=30):
        N=int(input("Saisir le nombre des adhérents:"))
    return N
#remplir
def remplir(N):
    TA=array([str]*N)
    for i in range (N):
        TA[i]=input("saisir le numéro d'abonnement "+str(i)+" :")
        while not ((len(TA[i])==10) and ((TA[i][0]=="A")or( TA[i][0]=="J")or (TA[i][0]=="E"))and (2000<=int(TA[i][1:5])<=2019) and (1<=int(TA[i][5:7])<=12) and (TA[i][7:10]!=TA[i-1][7:10])):
            TA[i]=input("saisir le numéro d'abonnement "+str(i)+" :")
    return TA
#calculs de bonus
def bonusCal(ch):
    A=2018-int(ch[1:5])
    M=17-int(ch[5:7])
    B=(12*A)+M
    return str(B)
def bonus(N,TA):
    S=input("saisir une catégorie d’adhérents: ")
    for i in range (N):
        if ((TA[i][0]==S) and(int(TA[i][1:4])<2015)) :
            B=bonusCal(TA[i])
            print("le numero d'abonnement "+TA[i]+" a un bonus de: "+B+" heures")
#PP
N=saisie()
TA=remplir(N)
bonus(N,TA)
