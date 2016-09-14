#! /usr/bin/env python3 -B

#
# Codice eseguibile per i capitoli del libro 
# "Fondamenti di Programmazione in Python" di 
# Fabio Pellacini
#

#
# Released under the MIT license
#
# Copyright (c) 2016 Fabio Pellacini
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#


booleano = True
print(booleano)
# Out: True
print(type(booleano))
# Out: <class 'bool'>

# operazioni semplici
freddo = True
caldo = not freddo
print(caldo)
# Out: False

pioggia = False
nuvoloso = True
brutto_tempo = pioggia or nuvoloso
print(brutto_tempo)
# Out: True

vento = True
neve = True
tormenta = vento and neve
print(tormenta)
# Out: True

# combinazione di operazione semplici
bel_tempo = not pioggia and not nuvoloso and not neve
print(bel_tempo)
# Out: False

# una espressione equivalente
bel_tempo = not (pioggia or nuvoloso or neve)
print(bel_tempo)
# Out: False

# confronti semplici
print(3 < 5)
# Out: True
print(10 == 11)
# Out: False
print(10.0 == 10)
# Out: True
print(3.5 != 3.45)
# Out: True

# combinazione di confronti su espressione
x = 2
y = 5
z = 4
print("valori ordinati:", x <= y and y <= z)
# Out: valori ordinati: False
# versione compatto del doppio confronto
print("valori ordinati:", x <= y <= z)
# Out: valori ordinati: False

print('Mario' == 'Bruno')
# Out: False
print('Mario' > 'Bruno')
# Out: True
print('Ma' < 'Mario')
# Out: True

print('Stringa' < 'stringa')
# Out: True
print("stringa" == "Stringa")
# Out: False

esclamazione = 'Che bel tempo!'
print('C' in esclamazione)
# Out: True
print('c' in esclamazione)
# Out: False
print(' ' in esclamazione)
# Out: True
print('bel' in esclamazione)
# Out: True
print('ciao' not in esclamazione)
# Out: True

pioggia = False
nuvoloso = True
if pioggia or nuvoloso:
    print("usciamo con l'ombrello")
# Out: usciamo con l'ombrello

nuvoloso = False
if pioggia or nuvoloso:
    print("usciamo con l'ombrello")
# Non stampa nulla dato che la condizione è False

def stampa_ombrello(mal_tempo):
    if mal_tempo:
        print("usciamo con l'ombrello")
    else:
        print("usciamo senza l'ombrello")    

pioggia = False
nuvoloso = True
stampa_ombrello(pioggia or nuvoloso)
# Out: usciamo con l'ombrello

nuvoloso = False
stampa_ombrello(pioggia or nuvoloso)
# Out: usciamo senza l'ombrello

def commenti_voto(voto):
    print("Il voto e'", voto)
    if voto < 18:
        print("mi dispiace")
    elif voto == 18:
        print("appena sufficiente")
    elif voto < 24:
        print("OK, ma potevi fare meglio")
    elif voto == 30:
        print("congratulazioni!")
    else:
        print("bene!")
    
commenti_voto(15)
# Out: Il voto e' 15
# Out: mi dispiace
commenti_voto(18)
# Out: Il voto e' 18
# Out: appena sufficiente
commenti_voto(23)
# Out: Il voto e' 23
# Out: OK, ma potevi fare meglio
commenti_voto(27)
# Out: Il voto e' 27
# Out: bene!
commenti_voto(30)
# Out: Il voto e' 30
# Out: congratulazioni!

def stampa_vuoto(x):
    if x:
        print('valore non nullo')
    else:
        print('valore nullo')

stampa_vuoto(0)
# Out: valore nullo
stampa_vuoto(1)
# Out: valore non nullo
stampa_vuoto('')
# Out: valore nullo
stampa_vuoto('ciao')
# Out: valore non nullo

import programma
# Out: valore nullo
# Out: valore non nullo
# Out: valore nullo
# Out: valore non nullo

if __name__ == '__main__':
    stampa_vuoto(0)
    stampa_vuoto(1)
    stampa_vuoto('')
    stampa_vuoto('ciao')

import modulo

stampa_vuoto(0)
# Out: valore nullo

