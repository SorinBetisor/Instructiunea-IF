#Să se afişeze cel mai mare număr par dintre doua numere introduse în calculator. Exemple : Date de intrare 23 45 Date de
#ieşire nu exista numar par ; Date de intrare 28 14 Date de ieşire 28 ; Date de intrare 77 4 Date de ieşire 4.
n1=int(input('Introduceti primul nr = '))
n2=int(input('Introduceti al doilea nr = '))
if ((n2%2)==0) and ((n1%2)==0):
    if (n2>n1):
        print (n2)
    else:
        print (n1)
if ((n2%2)==0) and ((n1%2)!=0):
    print (n2)
elif ((n1%2)==0) and ((n2%2)!=0):
    print (n1)
if ((n1%2)!=0) and ((n2%2)!=0):
    print ('Nu exista numar par')
