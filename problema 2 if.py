#La ora de matematică Gigel este scos la tablă. Profesoara îi dictează trei numere şi îi cere să verifice dacă cele trei numere pot fi
#laturile unui triunghi. Ajutaţi-l pe Gigel să afle rezultatul. Scrieţi un program care primeşte numerele lui Gigel, care sunt mai mici
#ca 32000, şi returnează DA sau NU. Observaţie: Trei numere pot fi laturile unui triunghi numai dacă fiecare este mai mic ca
#suma celorlalte două. Exemple: Date de intrare 3 5 7 Date de ieşire Da Date de intrare 2 5 9 Date de ieşire Nu. 
l1=int(input("Prima latura= "))
l2=int(input("A doua latura= "))
l3=int(input("A treia latura latura= "))
if (l1<32000) and (l2<32000) and (l3<32000):
    if (l1<(l2+l3)) and (l2<(l1+l3)) and (l3<(l2+l1)):
     print ('DA')
    else:
     print ('NU')
else:
    print ('Restrictiile nu sunt respectate')