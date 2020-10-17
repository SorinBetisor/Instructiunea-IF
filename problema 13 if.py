#La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această
#secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi? Exemplu : date de intrare : x=38 date de ieşire :
#rosie.
x=int(input('Nr concurentului = '))
if (x<100):
    if (x%4==1):
        print('alb')
    elif (x%4==2):
        print('rosie')
    elif (x%4==3):
        print('albastru')
    elif (x%4==0):
        print('negru')
else :
    print('Eroare')