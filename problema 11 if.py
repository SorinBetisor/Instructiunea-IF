#Se dau trei numere. Să se afişeze aceste numere unul sub altul, afişând în dreptul fiecăruia unul dintre cuvintele PAR sau
#IMPAR. Exemplu : Date de intrare : 45 3 24 Date de ieşire : 45 impar 3 impar 24 par.
nr1=int(input('Nr 1 = '))
nr2=int(input('Nr 2 = '))
nr3=int(input('Nr 3 = '))
if (nr1%2==0):
    print (nr1,' par')
else:
    print (nr1,' impar')
if (nr2%2==0):
    print (nr2,' par')
else:
    print (nr2,' impar')
if (nr3%2==0):
    print (nr3,' par')
else:
    print (nr3,' impar')