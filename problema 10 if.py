#La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr de boabe de porumb. Cele care nu pot
#fi împărţite vor fi primite de curcanul Clapon. Să se spună cine a primit mai multe boabe şi cu cât. În caz de egalitate, se va
#afişa numărul de boabe primite şi cuvântul "egalitate". Datele se vor citi în următoarea ordine: numărul de găini, iar dupa aceea
#numărul de boabe de porumb. Exemplu: Date de intrare 100 4050 Date de ieşire: Curcanul mai mult cu 10 boabe.
gaini=int(input('Nr de gaini = '))
graunte=int(input('Nr de graunte = '))
t1=(graunte//gaini)
t2=(t1*gaini)
clapon=(graunte-t2)
if (clapon==0):
    print ('egalitate, fiecare are ',t1,' boabe')
else:
    print("Curcanul are cu ",clapon,' boabe mai mult')

