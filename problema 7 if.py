#Se consideră trei numere întregi. Dacă toate sunt pozitive, să se afişeze numărul mai mare dintre al doilea şi al treilea număr, în
#caz contrar să se calculeze suma primelor două numere. Exemple: Date de intrare 45 23 100 date de ieşire 100 ; Date de
#intrare 34 -25 10 Date de ieşire 9.
n1=int(input('Introduceti primul nr = '))
n2=int(input('Introduceti al doilea nr = '))
n3=int(input('Introduceti al treilea nr = '))
if (n1>=0) and (n2>=0) and (n3>=0):
    if (n2>n3):
        print (n2)
    elif (n3>n2):
        print (n3)
elif (n1<0) or (n2<0) or (n3<0):
    print (n1+n2)

