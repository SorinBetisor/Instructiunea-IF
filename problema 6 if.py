
n1=int(input('Introduceti prima nota = '))
n2=int(input('Introduceti a doua nota = '))
n3=int(input('Introduceti a treia nota = '))
if (n1>0) and (n2>0) and (n3>0) and (n1<=10) and (n2<=10) and (n3<=10):
    if n3>=8:
        print (n1,n2,n3)
    elif (n3<8) and (n1<n2):
        print (n2)
    elif (n3<8) and (n1>n2):
        print (n1)
else:
    print ('Eroare')