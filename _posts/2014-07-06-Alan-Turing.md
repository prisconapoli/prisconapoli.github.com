---
layout: post
category : lesson
tags: [Programmers' theoretical minimum, C++, struct, class]
---
{% include JB/setup %}

**Turing, Godel, Von Neumann: thoughts about a thinking machine**

<!--more-->

###Quando una funzione si dice calcolabile

I matematici Church e Turing enunciarono una tesi indimostrabile per cui le funzioni calcolabili sono quelle per cui posso inventare un algoritmo risolvibile da una macchina di Turing, sostanzialmente un computer.
Il teorema matematico della calcolabilità si basa sul concetto di "intuitivamente" calcolabile e di algoritmo (cioè processo di calcolo o insieme di passaggi) per giungere al risultato.

Una funzione si dice calcolabile se rispetta una delle seguenti condizioni:

1) sono in grado di calcolarla

2) posso inventare un metodo per calcolarla

La funzione che elenca tutti i numeri decimali compresi in un intervallo è un classico esempio di funzione non calcolabile, perché l'algoritmo non termina in un numero finito di passi.
Ci sono molte classi di funzioni non calcolabili, l'esempio classico sono le enumerazioni. Una funzione che elenca tutti i numeri interi non è calcolabile. Una funzione che elenca tutte le combinazioni delle lettere dell'alfabeto, con numero arbitrario di posizioni, non è calcolabile.

Un altro esempio classico è una funzione che stabilisca se una equazione a coefficienti interi di grado arbitrario ammette soluzione intere, detto decimo problema di Hilbert.

###Il test di Touring
Intorno al 1950, Alan Turing pubblico sulla rivista Mind un articolo che avrebbe storia. L'articolo, intitolato “Computing Machinery and Intelligence”, poneva una semplice quanto inusuale domanda: “Le macchine possono pensare?”

Questa semplice domanda ha dato vita ad un incredibile dibattito che ancora oggi prosegue, coinvolgendo fisici, matematici, filosofi, religiosi e semplici appassionati come me.

Turing era coscente del datto che proporre una misura "quantitativa" del pensiero era pressochè impossibile. Nessuno infatti può conoscere profondamente come una persona pensa. Il pensiero può essere dedotto soltanto osservandone le manifestazioni esteriori. L’unico pensiero di cui possiamo avere una prova certa è il nostro proprio pensiero. Del pensiero altrui vediamo solo la superficie. Nient’altro.

Visto che il pensiero non si osserva, non si fotografa, non si misura. Touring propose una soluzione operativa: pensa ciò che sembra pensare. Poiché il pensiero posso inferirlo solo dalle manifestazioni esteriori, se quelle manifestazioni sono le stesse per un uomo e per una macchina… allora la macchina pensa. In sostanza, se sembra cosciente, allora è cosciente. Fra una simulazione perfetta e la realtà non c’è alcuna differenza. Ciò che appare… è.

La soluzione proposta da Turing prede il nome di test di Turing. E' molto semplice da spiegare. è sufficiente prendere una persona e posizionarla davanti a due monitor, al di là dei quali sono collegati un essere umano e il computer da sottoporre al test. Lo sperimentatore deve discutere con entrambi sottoponendo varie tipi di domande: letteratura, cinema, sport, politica. Non vi sono limiti di argomento. 
Lo scopo dello sperimentatore è riuscire a distinguere l’umano dalla macchina. Se non ci riesce, allora possiamo dire che la macchina pensa come l’uomo.

Il test di Turing è ancora attuale e non smetterà mai di esserlo. Esso infatti è un test che coinvolge la filosofia oltre che la tecnologia, che continua a dar riflettere su come nasca la capacità di pensioero, la coscienza e l'anima. 
"Chi altri può pensare oltre a me?”"
“Quand’è che uno schema percettivo diventa coscienza?
""Quand’è che una simulazione di personalità diventa il grumo sofferente di un’anima?”

Nel 1966 Joseph Weizembaum scrisse un programma denominato Eliza, in grado di sostenere più che una conversazione: una seduta di psicoterapia nei panni di uno psicologo. Ciò che accadde è che non solo Eliza passò a più riprese il test di Turing, anche con testers di un certo livello culturale, ma le persone iniziavano a confessare al programma anche i loro segreti più intimi.



 
##Further Information



