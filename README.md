# Laboratorio 2
Questo laboratorio è un ripasso di ciò che è stato spiegato il primo anno nel corso di informatica. 
E' presente un unico esercizio tratto da un tema d'esame.


## Ghiaccio
Adam Trask vuole trasportare via treno lattuga da Los Angeles ad altre parti degli USA, refrigerando i vagoni con del ghiaccio.
Ci sono varie città interessate all'acquisto, che offrono prezzi diversi.

Il file *listino.txt* contiene su ogni riga separati da spazi: 

```
lettera identificativa di una città, nome della città, prezzo di acquisto
```

La città di partenza, Los Angeles, si trova nella prima riga ed è associata alla lettera a.
Il restante contenuto del file non è noto a priori.

Il file *distanze.txt* contiene un elenco di tratte ferroviarie che si diramano partendo da Los Angeles.
Ogni riga descrive una tratta nel seguente formato: 

```
<lettera identificativa della città di partenza>-<lettera identificativa della città di arrivo>:<numero intero indicante la distanza in km>
```

Ogni riga introduce, nello stesso ordine, il tratto per raggiungere una nuova città del file *listino.txt*.
Il percorso per raggiungere la città di partenza di un tratto è già stato descritto nelle righe precedenti.
Esiste un unico percorso per connettere Los Angeles ad ogni altra città. 

Stampare: 

- l'elenco delle città direttamente connesse a Los Angeles.
- il nome e quanti km servono per raggiungere la città con l'offerta migliore in assoluto.
- la città con il peggior rapporto offerta/ore percorrenza, escludendo Los Angeles.
- Supponendo di avere ghiaccio per 4000 km, stampare il nome della città raggiungibile con la migliore offerta.



### Esempio

*listino.txt*
```
a Los Angeles 5
b San Diego 9
c San Francisco 11
d Sacramento 12
e Portland 14
f Seattle 15
g Albuquerque 18
h Kansas City 20
i Denver 19
l Chicago 25
m Boston 40
n Washington 41
o New Orleans 30
p Miami 23
```

*distanze.txt*
```
a-b:200
a-c:720
a-d:610
d-e:1080
e-f:270
a-g:1340
g-h:1600
d-i:1800
h-l:780
l-m:1800
l-n:1060
l-o:1450
n-p:1450
```

*output*
```
Città direttamente connesse a Los Angeles:
San Diego
San Francisco
Sacramento
Albuquerque

Per raggiungere l'offerta migliore, Washington, servono: 4780 km
La citta' con il peggior rapporto è Miami
La migliore offerta entro 4000 km è a Chicago
```

