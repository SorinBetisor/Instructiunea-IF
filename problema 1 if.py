#Se introduc trei date de forma număr curent elev, punctaj. Afişaţi numărul elevului cu cel mai mare punctaj. Exemplu : Date de
#intrare nr crt 7 punctaj 120 nr crt 3 punctaj 100 nr crt 4 punctaj 119 Date de ieşire punctaj maxim are elevul cu nr crt 7.
nr1=int(input("Introduceti nr curent al primului elev= "))
pj1=int(input("Introduceti punctajul primului elev= "))
nr2=int(input("Introduceti nr curent celui de al doilea elev= "))
pj2=int(input("Introduceti punctajul celui de al doilea elev= "))
nr3=int(input("Introduceti nr curent celui de al treilea elev= "))
pj3=int(input("Introduceti punctajul celui de al treilea elev= "))
if (pj1>pj2) and (pj1>pj2):
    print ('Punctaj maxim are elevul cu nr',nr1)
elif (pj2>pj1) and (pj2>pj3):
    print ('Punctaj maxim are elevul cu nr',nr2)
elif (pj3>pj1) and (pj3>pj2):
    print ('Punctaj maxim are elevul cu nr',nr3)
elif (pj3==pj1) and (pj1==pj3) and (pj2==pj3):
    print ('Numarul de punctaj este egal la toti elevii')
elif (pj3==pj1) and (pj3>pj2):
    print ('Elevul ',nr1,' si ',nr3,' au un nr de punctaj maxim egal')
elif (pj2==pj1) and (pj2>pj3):
    print ('Elevul ',nr1,' si ',nr2,' au un nr de punctaj maxim egal')
elif (pj3==pj2) and (pj3>pj1):
    print ('Elevul ',nr2,' si ',nr3,' au un nr de punctaj maxim egal')
