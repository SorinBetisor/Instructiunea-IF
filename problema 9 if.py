#Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze
#câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând
#numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor. Exemplu: Date de intrare Nr. bile albe mici: 2
#Nr. bile albe mari: 3 Nr. bile rosii mici: 1 Nr. bile rosii mari: 4 Nr. bile verzi mici: 3 Nr. bile verzi mari: 4 Date de ieşire Totalul
#bilelor: 17 Mari: 11 bile Verzi: 7 bile .
bamari=int(input('Nr de bile albe mari = '))
bamici=int(input('Nr de bilea albe mici = '))
brmari=int(input('Nr de bile rosii mari = '))
brmici=int(input('Nr de bile rosii mici = '))
bvmari=int(input('Nr de bile verzi mari = '))
bvmici=int(input('Nr de bile verzi mici = '))
total=bamari+bamici+brmari+brmici+bvmari+bvmici
totalmici=bamici+brmici+bvmici
totalmari=bamari+brmari+bvmari
totalverzi=bvmari+bvmici
totalrosii=brmari+brmici
totalalbe=bamari+bamici
print ('Totalul = ',total)
if (bamari>=0) and (bamici>=0) and (brmari>=0) and (bamici>=0) and (bvmari>=0) and (bvmici>=0):
    if (totalmici>totalmari):
        print (totalmici, 'mici')
    elif (totalmari>totalmici):
        print (totalmari, 'mari')
    if (totalalbe>totalrosii) and (totalalbe>totalverzi):
        print (totalalbe, 'albe')
    elif (totalrosii>totalalbe) and (totalrosii>totalverzi):
        print (totalrosii, 'rosii')
    elif (totalverzi>totalalbe) and (totalverzi>totalrosii):
        print (totalverzi, 'verzi')
    elif (totalrosii==totalalbe) and (totalrosii>totalverzi):
        print ('Nr maxim de bile rosii este egal cu cel de bile albe= ',totalrosii)
    elif (totalverzi==totalalbe) and (totalverzi>totalrosii):
        print ('Nr maxim de bile albe este egal cu cel de bile verzi= ',totalverzi)
    elif (totalrosii==totalverzi) and (totalrosii>totalalbe):
        print ('Nr maxim de bile rosii este egal cu cel de bile verzi= ',totalrosii)
else:
    print ('Eroare')