#Într-o tabără, băieţii sunt cazaţi câte 4 într-o căsuţă, în ordinea sosirii. Ionel a sosit al n-lea. În a câta căsuţă se va afla?
#Exemplu : date de intrare : n=69 date de ieşire : casuta 17.
n=int(input('Nr sosirii lui Ionel = '))
if n>0:
    if (n%4==0):
        print ('Casuta ',n//4)
    elif (n%4!=0):
        print ('Casuta ',(n//4)+1)
else:
    print('Eroare')
