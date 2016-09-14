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


primi = [2, 3, 5, 7, 11, 13, 17, 19]
print(primi)
# Out: [2, 3, 5, 7, 11, 13, 17, 19]
colori = ['blu', 'rosso', 'verde', 'giallo']
print(colori)
# Out: ['blu', 'rosso', 'verde', 'giallo']
misc = ['red', 2, 3.14, 'blue']
print(misc)
# Out: ['red', 2, 3.14, 'blue']

lista_vuota = []
print(lista_vuota)
# Out: []

print(type(colori))
# Out: <class 'list'>

tupla = ('ciao', 1, 2)
print(tupla)
# Out: ('ciao', 1, 2)

tupla_vuota = ()
print(tupla_vuota)
# Out: ()

print(type( (1,2) ))
# Out: <class 'tuple'>

def quoziente_resto(x,y):
    return x // y, x % y

q = quoziente_resto(5,2)
print(q)
# Out: (2, 1)
print(type(q))
# Out: <class 'tuple'>

saluto = 'Buon ' + 'giorno'
print(saluto)
# Out: Buon giorno
boom = 'tic tac '*5 + 'BOOM!'
print(boom)
# Out: tic tac tic tac tic tac tic tac tic tac BOOM!
len(boom)
# Out: 45

primi = [2, 3, 5, 7, 11, 13, 17, 19]
primi2 = primi + [23, 29]
print(primi2)
# Out: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
[1, 2, 3]*4
# Out: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
len(primi)
# Out: 8

persone = ('Bruno', 'Luisa') + ('Anna', 'Mario')
print(persone)
# Out: ('Bruno', 'Luisa', 'Anna', 'Mario')
len(persone)
# Out: 4

sum([2,3,4])
# Out: 9
all([False,True])
# Out: False
any([False,True])
# Out: True

lst = [10,1,20]
print( min(lst) )
# Out: 1
print( max(lst) )
# Out: 20
print( sorted(lst) )
# Out: [1, 10, 20]

rubrica = ['Bruno', 'Sofia', 'Anna', 'Mario']
print( sorted(rubrica) )
# Out: ['Anna', 'Bruno', 'Mario', 'Sofia']

# conversione in liste e tuple
print(tuple([1,2]))
# Out: (1, 2)
print(list(('Bruno','Luisa')))
# Out: ['Bruno', 'Luisa']
print(list('Anna'))
# Out: ['A', 'n', 'n', 'a']

lst = [1, 2, 'abc', 5]
print(lst == [1, 2, 'abc', 5])
# Out: True
print(lst < [1, 2, 'abcd'])
# Out: True

seq = [1, 2, 3, 5, 8]
print(5 in seq)
# Out: True
print(4 in seq)
# Out: False
print('mela' in ['noce', 'mela', 'banana'])
# Out: True
print(4 not in seq)
# Out: True

def stampa_vuoto(x):
    if x:
        print('valore non nullo')
    else:
        print('valore nullo')

stampa_vuoto([])
# Out: valore nullo
stampa_vuoto([2,3,5])
# Out: valore non nullo
stampa_vuoto((2,3))
# Out: valore non nullo

def frutto(x):
    if x == 'mela':
        return True
    elif x == 'pera':
        return True
    elif x == 'uva':
        return True
    else:
        return False
        
x = 'melo'
y = 'uva'
print(frutto('melo'))
# Out: False
print(frutto('uva'))
# Out: True

def frutto2(x):
    return x in ['mela', 'pera', 'uva']
    
print(frutto2('melo'))
# Out: False
print(frutto2('uva'))
# Out: True

def check_date(mese, giorno):
    if giorno < 1: return False
    if mese == 'feb':
        return giorno <= 28
    elif mese in ['apr', 'giu', 'set', 'nov']:
        return giorno <= 30
    elif mese in ['gen', 'mar', 'mag', 'lug',
                  'ago', 'ott', 'dic']:
        return giorno <= 31
    else:
        return False
    
print(check_date('gen', 31))
# Out: True
print(check_date('feb', 29))
# Out: False
print(check_date('dic', 0))
# Out: False
print(check_date('mir', 1))
# Out: False

colori = ['blu', 'rosso', 'verde', 'giallo']
print(colori[0])
# Out: blu
persone = ('Bruno', 'Sofia', 'Mario')
print(persone[1])
# Out: Sofia
stringa = 'abracadabra'
print(stringa[2])
# Out: r

# Begin error-generating code --- using try/expect
try:
    print(colori[10])
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: IndexError: list index out of range
except:
    pass
# End error-generating code

colori = ['blu', 'rosso', 'verde', 'giallo']

# L'elemento in ultima posizione
print(colori[-1])    
# Out: giallo
# Quello in penultima posizione
print(colori[-2])   
# Out: verde

colori = ['blu', 'rosso', 'verde', 'giallo']
colori[1] = 'nero'
print(colori)
# Out: ['blu', 'nero', 'verde', 'giallo']

# Begin error-generating code --- using try/expect
try:
    persone[1] = 'Sara'
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: TypeError: 'tuple' object does not support item assignment
except:
    pass
# End error-generating code
# Begin error-generating code --- using try/expect
try:
    stringa[5] = 'z'
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: TypeError: 'str' object does not support item assignment
except:
    pass
# End error-generating code

persone = ('Bruno', 'Sofia', 'Mario')
print(persone)
# Out: ('Bruno', 'Sofia', 'Mario')

# sequence unpacking
p1, p2, p3 = persone
print(p1, p2, p3)
# Out: Bruno Sofia Mario

# non si accede con numero di variabili diverso
# Begin error-generating code --- using try/expect
try:
    p1, p2 = persone
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: ValueError: too many values to unpack (expected 2)
except:
    pass
# End error-generating code

# tupla senza parentesi tonde, seguito da unpacking
a, b = 'primo', 'secondo'
print(a, b)
# Out: primo secondo

# scambio di valori
b, a = a, b
print(a, b)
# Out: secondo primo

def quoziente_resto(a, b):
    return a/b, a%b    
q, r = quoziente_resto(5, 3)
print(q, r)
# Out: 1.6666666666666667 2

colori = ['blu', 'rosso', 'verde', 'giallo']

# sottolista dalla posizione 1 alla 2
print(colori[1:3])
# Out: ['rosso', 'verde']
# sottolista dall'inizio alla penultima
print(colori[0:-1])
# Out: ['blu', 'rosso', 'verde']
# sottolista dalla posizione 2 in poi
print(colori[2:])  
# Out: ['verde', 'giallo']
# sottolista dall'inizio alla pos. 2
print(colori[:2])
# Out: ['blu', 'rosso']
# copia dell'intera lista  
print(colori[:])
# Out: ['blu', 'rosso', 'verde', 'giallo']

s = 'Questa è proprio una bella giornata.'
# sottostringa dalla posizione 0 alla 5
print(s[0:6])   
# Out: Questa
# sottostringa dalla posizione 7 in poi
print(s[7:])   
# Out: è proprio una bella giornata.
# sottostringa dall'inizio fino alla posizione 15
print(s[:16])
# Out: Questa è proprio

colori = ['blu', 'rosso', 'verde', 'giallo']

# cambiamento di valori
colori[1:3] = ['arancio', 'viola']
print(colori)
# Out: ['blu', 'arancio', 'viola', 'giallo']

# inserimento di valori
colori[1:1] = ['nero']
print(colori)
# Out: ['blu', 'nero', 'arancio', 'viola', 'giallo']

# cancellazione di valori
colori[1:2] = []
print(colori)
# Out: ['blu', 'arancio', 'viola', 'giallo']

def print_cf(cf):
    print('Cognome (tre lettere):', cf[0:3])
    print('Nome (tre lettere):', cf[3:6])
    print('Data di nascita e sesso:', cf[6:11])
    print('Comune di nascita:', cf[11:15])
    print('Carattere di controllo:', cf[-1])

# codice fiscale fasullo
print_cf('COGNOMDATASCOMUX')
# Out: Cognome (tre lettere): COG
# Out: Nome (tre lettere): NOM
# Out: Data di nascita e sesso: DATAS
# Out: Comune di nascita: COMU
# Out: Carattere di controllo: X

