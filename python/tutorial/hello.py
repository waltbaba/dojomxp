# Ciao Tommaso, benvenuto al tutorial di papa' su python!
# In questa parte della finestra puoi scrivere il codice ed eseguirlo con il tasto "play" in alto a dx.
# Ogni volta che premi "play" nella finestra in basso "TERMINAL" vedrai il risultato del tuo programma o delle scritte 
# rosse in caso contenga errori.
# Tutto quello che scrivi viene automaticamente salvato, non c'e' bisogno che salvi manualmente.

# una riga che inizia con il cancelletto e' un commento
# puoi scriverci quello che vuoi, non sono istruzioni eseguite dal programma
# tipicamente puoi indicare nei commenti cosa fa l'istruzione che hai scritto


# il comando print() stampa quello che gli metti all'interno delle virgolette tra le due parentesi 
print('hello world') # questo stampa hello world (come puoi notare i commenti si posso scrivere in qualsiasi punto)
print('una cosa' + ' ' + 'seconda cosa')
print()  # se non metti niente nelle parentesi stampa una riga vuota

# le variabili si dichiarano con un nome a tuo piacere (tutto minuscolo senza spazi) e con un uguale gli metti il valore
nuova_variabile = 'contenuto della variabile'
altra_variabile = 45 # le variabili possono contenere testo, numeri o booleani (True o False)
variabile_booleana_falsa = False
variabile_booleana_vera = True

print(nuova_variabile) # se passi una variabile al comando print() ti stampa il contenuto della variabile

print('Scrivi qualcosa:')
# il comando input() attende che scrivi qualcosa con la tastiera e premi invio, tutto il testo verra'
# memorizzato in una variabile
risposta = input() 
print('bravo hai scritto: ' + risposta) # puoi unire del testo che scrivi tu e il contenuto di una variabile con il +

# il se allora si fa cosi' (attento ai due punti :)
if(risposta == 'thepoointhesea'):
    print()
    print('Hai scritto thepoointhesea')

