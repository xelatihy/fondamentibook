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


colori = ['blu', 'rosso', 'verde', 'giallo']
for colore in colori:
    print(colore)
# Out: blu
# Out: rosso
# Out: verde
# Out: giallo

def somma(valori):
    '''Ritorna la somma dei valori.'''
    s = 0
    for valore in valori:
        s += valore
    return s

print(somma([1,2,3]))
# Out: 6

def somma_stampa(valori):
    s = 0
    for valore in valori:
        print('aggiungi',valore,'a',s)
        s += valore
        print('valore aggiunto',s)
    return s

print(somma_stampa([1,2,3]))
# Out: aggiungi 1 a 0
# Out: valore aggiunto 1
# Out: aggiungi 2 a 1
# Out: valore aggiunto 3
# Out: aggiungi 3 a 3
# Out: valore aggiunto 6
# Out: 6

def lunghezza(valori):
    '''Ritorna la lunghezza di una sequenza.'''
    l = 0
    for valore in valori:
        l += 1
    return l

print(lunghezza([1,2,3]))
# Out: 3

def cubi(valori):
    '''Ritorna una nuova lista che contiene i cubi 
    dei valori della lista di input.'''
    cubi = []
    for valore in valori:
        cubi += [valore**3]
    return cubi

primi = [2, 3, 5, 7, 11, 13]
cubi_primi = cubi(primi)
print(primi)
# Out: [2, 3, 5, 7, 11, 13]
print(cubi_primi)
# Out: [8, 27, 125, 343, 1331, 2197]

def cubi_stampa(valori):
    '''Ritorna una nuova lista che contiene i cubi 
    dei valori della lista di input.'''
    cubi = []
    for valore in valori:
        cubo = valore**3
        print('aggiungi',cubo,'a',cubi)
        cubi += [cubo]
        print('valore aggiunto',cubi)
    return cubi

primi = [2, 3, 5]
cubi_primi = cubi_stampa(primi)
# Out: aggiungi 8 a []
# Out: valore aggiunto [8]
# Out: aggiungi 27 a [8]
# Out: valore aggiunto [8, 27]
# Out: aggiungi 125 a [8, 27]
# Out: valore aggiunto [8, 27, 125]

def concatena(valori1,valori2):
    valori = []
    for valore in valori1:
        valori += [valore]
    for valore in valori2:
        valori += [valore]
    return valori

print(concatena([1,2,3],[4,5,6]))
# Out: [1, 2, 3, 4, 5, 6]

for i in range(3):
    print(i)
# Out: 0
# Out: 1
# Out: 2

for i in range(2,5):
    print(i)
# Out: 2
# Out: 3
# Out: 4

for i in range(2,5,2):
    print(i)
# Out: 2
# Out: 4

list(range(2,20,3))
# Out: [2, 5, 8, 11, 14, 17]

def crea_cubi(n):
    """Ritorna una lista che contiene i cubi degli 
    interi da 1 a n."""
    lst = []
    for i in range(1, n + 1):
        lst = lst + [i**3]
    return lst
    
lst = crea_cubi(10)
print(lst)
# Out: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

primi = [2, 3, 5, 7, 11, 13]
for indice in range(len(primi)):
    primi[indice] = primi[indice] ** 2

print(primi)
# Out: [4, 9, 25, 49, 121, 169]

def setta_cubi(lst):
    """Modifica la lista di input elevando al
    cubo tutti i suoi valori."""
    for i in range(len(lst)):
        lst[i] = lst[i]**3
    
primi = [2, 3, 5, 7, 11, 13]
print(primi)
# Out: [2, 3, 5, 7, 11, 13]

setta_cubi(primi)
print(primi)
# Out: [8, 27, 125, 343, 1331, 2197]

def appartiene(valore_test, valori):
    '''Ritorna True se valore_test è in valori, 
    False altrimenti.'''
    for valore in valori:
        if valore == valore_test:
            # usciamo dal ciclo e dalla funzione 
            # inserendo return nel ciclo
            return True
    return False

lst = ['mela', 'pera', 'uva']
print('arancia' in lst, appartiene('arancia',lst))
# Out: False False
print('mela' in lst, appartiene('mela',lst))
# Out: True True

def valore_massimo(valori):
    '''Ritorna il valore massimo di una lista.'''
    if not valori: return None # lista vuota
    massimo = valori[0]
    for valore in valori:
        if valore > massimo:
            massimo = valore
    return massimo

print(valore_massimo([10,1,20]))
# Out: 20

def indice(valori,elemento):
    '''Ritorna l'indice di un elemento, 
    o -1 se non esite.''' 
    for i in range(len(valori)):
        if valori[i] == elemento:
            return i
    return -1

print(indice([10,1,20],20))
# Out: 2
print(indice([10,1,20],30))
# Out: -1

def ordinata(lst):
    '''Ritorna True se la list lst è ordinata,
    altrimenti False.'''
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

lst = [2,3,1]
print(ordinata(lst))
# Out: False
print(ordinata(sorted(lst)))
# Out: True

def elemento_non_ordinato(lst):
    '''Ritorna l'indice del primo valore che non
    rispetta l'ordinamento.'''
    for i in range(len(lst)):
        if lst[i] > lst[i+1]:
            return i
    return -1
    
print(elemento_non_ordinato([1,2,3,2]))
# Out: 2
print(elemento_non_ordinato(['abc','abcc','ab']))
# Out: 1

def media_esclusiva(lst, nolst):
    '''Media degli elementi in lst e non in nolst'''
    total = 0
    count = 0
    for s in lst:
        if s in nolst: 
            # Salta alla prossima iterazione
            continue      
        total += s
        count += 1
    return total / count

print(media_esclusiva([2,3,4],[3]))    
# Out: 3.0

def media_esclusiva2(lst):
    total = 0
    count = 0
    for s in lst:
        if s < 0: 
            # Esci dal ciclo
            break      
        total += s
        count += 1
    return total / count

print(media_esclusiva2([2,3,4,-1,10,20]))    
# Out: 3.0

def primo(n):  
    '''Ritorna True se il numero è primo.'''
    k = 2
    while k < n and (n % k) != 0:
        k += 1
    return k == n
    
print(primo(10))
# Out: False
print(primo(13))
# Out: True

def primo_minimo(m):  
    '''Ritorna il più piccolo primo >= m.'''
    while not primo(m):
        m += 1
    return m

print(primo_minimo(10))
# Out: 11

numeri = [(1,'uno'),(2,'due')]

# numero è una tupla
for numero in numeri:
    print(numero)       
# Out: (1, 'uno')
# Out: (2, 'due')

# unpacking delle tuple esplicito
for numero in numeri:           
    valore, stringa = numero
    print(valore, stringa)
# Out: 1 uno
# Out: 2 due

# unpacking delle tuple implicito
for valore, stringa in numeri:           
    print(valore, stringa)
# Out: 1 uno
# Out: 2 due

colori = ['blu', 'rosso', 'verde', 'giallo']
for indice, colore in enumerate(colori):
    print(indice, colore)
# Out: 0 blu
# Out: 1 rosso
# Out: 2 verde
# Out: 3 giallo

# lista dei quadrati dei numeri tra 1 e 5
quadrati = [i ** 2 for i in range(5)]
print(quadrati)
# Out: [0, 1, 4, 9, 16]

# sottolista dei numeri pari
pari = [i for i in quadrati if i % 2 == 0]
print(pari)
# Out: [0, 4, 16]

