# ciao io sono un ciclo for,
# ripeto le cose che metti al mio interno quante volte vuoi!

print('-------- parte 1 --------')
# Per esempio, siccome sono molto intelligente posso ripeterlo 10 volte
for indice in range(10):
    print('sono intelligente!')


print('-------------------------\n')
print('-------- parte 2 --------')
# range() ti permette di dirmi quante volte vuoi che ripeta le cose
# indice e' una variabile (la puoi chiamare come vuoi) e conta il numero della volta durante le ripetizioni
for indice in range(10):
    print('e` la volta numero: ' + str(indice))
    print('sono intelligente!')

# avrai notato che mettendo 10 nel range(), il numero delle volte va da 0 a 9
# lo zero si conta come primo numero, quindi per fare 10 numeri si arriva a 9
# i range partono sempre da zero!

print('-------------------------\n')
print('-------- parte 3 --------')
# esiste un'istruzione magica che si chiama break
# che mi fa fermare di colpo appena la incontro
for indice in range(10000000):
    print('sono intelligente!')
    if indice == 2:
        print('meno male che con il break mi fermo altrimenti arrivavo a 10000000!!!')
        break
# ha stampato solo 3 volte 'sono intelligente!' perche` indice ha assunto i valori 0, 1, 2 e poi e' entrato nell'if