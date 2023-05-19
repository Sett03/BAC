def saisie(ch):
    x=int(input("saisir un numero '"+ch+"' >2 : "))
    while not (x>2):
        x=int(input("saisir un numero"+ch+" >2 : "))
    return x
def premier(x):
    if x == 2:
        return True
    else:
        a=True
        i=2
        valid = False
        while valid == False:
            if x%i==0:
                a=False
            else:
                i=i+1
            if i==x-1 or a==False:
                valid = True
            return a
def sp(a):
    x="semi premier"
    i=2
    valid = False
    while valid == False:
        if a%i==0 :
            check=premier(i)
            if check == False :
                x="n'est pas semi premier"
        i=i+1
        if i==a-1 or x =="n'est pas semi premier":
            valid =True
    return x


#main
a=saisie("a")
x=sp(a)
print (x)