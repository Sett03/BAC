from numpy import array
#saisie
def Saisie():
    N=int(input("Donner le nombre de joueurs: "))
    while not (2<=N<=20):
        N=int(input("Donner le nombre de joueurs: "))
    return N
#Nom
def Nom(N):
    T1=array([str]*N)
    for i in range (1,N+1,1):
        T1[i-1]=input("Donner le nom du joueur n°"+str(i)+": ")
        while not (Alpha(T1[i-1]) == True):
                T1[i-1]=input("Donner le nom du joueur n°"+str(i)+": ")
    return T1
#Alpha
def Alpha(ch):
    Alpha=True
    L=len(ch)
    if L<=30:
        for i in range (L):
            if not ((65<=ord(ch[i].upper())<=90) or( ch[i]==" ")):
                Alpha = False
    return Alpha
#Score
def Score(N,T1):
    S=0
    T2=array([int]*N)
    for i in range (N):
        S=0
        for j in range (1,4):
            E=int(input("Saisir le score de "+str(j)+" essai de "+str(T1[i])+": "))
            while not (0<=E<=10):
                E=int(input("Saisir le score de "+str(j)+" essai de "+str(T1[i])+": "))
            S=S+E
            E=0
        T2[i]=S
    valid = False
    while valid ==False:
        c=0
        for i in range (N-1):
            if T2[i]<T2[i+1]:
                T1[i],T1[i+1]=T1[i+1],T1[i]
                T2[i],T2[i+1]=T2[i+1],T2[i]
                c=c+1
        if c == 0:
            valid =True
    ch=""
    for b in range(N):
        ch=T1[b]+" avec un score de:"+str(T2[b])
        print (ch)

N=Saisie()
T1=Nom(N)
Score(N,T1)
