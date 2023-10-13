# ciao io sono un array e sono una variabile contenitore di molti valori!
ricetta = ['uova', 'zucchero', 'farina', 'cioccolato']

contenitore_di_numeri = [0,1,2,3,4,5]

# puoi usare il ciclo for per stampare tutti i valori di un array
print("Per fare una torta servono:\n")
for ingrediente in ricetta:
    print(ingrediente)

# in verità se devi solo visualizzare il contenuto puoi usare il comando print (ma verrà tutto su una sola riga)
print('\n-------------------------')
print("Ricetta: " + str(ricetta))

# se vuoi ottenere uno solo dei valori devi indicare il numero dell'elemento tra parentesi quadre [] (ATTENTO! si parte a contare da 0)
print('\n-------------------------')
print("Il primo ingrediente è: " + ricetta[0])
print("Il secondo ingrediente è: " + ricetta[1])

#TODO: append di un valore
#TODO: ciclo for + input

    