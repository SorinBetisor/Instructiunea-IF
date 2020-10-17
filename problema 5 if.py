#Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane,
#exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi. Exemplu : Date
#de intrare data curenta 2005 10 25 data nasterii 1960 11 2 Date de ieşre 44 ani.

ac=int(input('Introduceti anul curent = '))
lc=int(input('Introduceti luna curenta = '))
zc=int(input('Introduceti ziua curenta = '))
an=int(input('Introduceti anul nasterii = '))
ln=int(input('Introduceti luna nasterii = '))
zn=int(input('Introduceti ziua nasterii = '))
varsta=(ac-an)
if (ac>an):
    if lc<ln :
     print ((varsta-1),' ani')
    elif (lc==ln) and (zc<zn):
     print ((varsta-1),' ani')
    elif (lc==ln) and (zc>=zn):
     print ((varsta),' ani')
    elif lc>ln :
        print (varsta, ' ani')
else:
    print ('Eroare')
#Nota: La introducerea lunii introduceti sub formatul : 4,5,6 ; ci nu : 04,05,06
