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


# tipi base
print(type('stringa'))
# Out: <class 'str'>
print(type(13))
# Out: <class 'int'>
print(type(12345678901234))
# Out: <class 'int'>
print(type(13.0))
# Out: <class 'float'>
print(type([1,2,3]))
# Out: <class 'list'>

x = [1, 2]
y = [1, 2]

print(id(x))          
# Out: 4348597768
print(id(y))
# Out: 4348588936

# gli oggetti x e y hanno lo stesso valore
# ma hanno identità differenti

print(x == y)
# Out: True
print(id(x) == id(y))
# Out: False

x = 'stringa'
y = 'stringa'
print(id(x))
# Out: 4348612312
print(id(y))
# Out: 4348612312
# x e y sono lo stesso oggetto

print(int('00123'))
# Out: 123
print(int(12.3))
# Out: 12
print(str(12.3))
# Out: 12.3
print(list())
# Out: []

x = None
print(x)
# Out: None
print(type(x))
# Out: <class 'NoneType'>

# la funzione non ritorna nulla
def printme(val):
    val + 1

print(printme(1))
# Out: None

def cubo(x): return x**3
def quadrato(x): return x**2

print(cubo)
# Out: <function cubo at 0x10332d1e0>
print(id(cubo))
# Out: 4348629472
print(type(cubo))
# Out: <class 'function'>
cubo == quadrato
# Out: False

# memorizza una funzione in una variabile
f = cubo
# chiama la funzione usando il nome della variabile
f(3)
# Out: 27

# funzioni come argomento
def print_f(f,x):
    print(f(x))

# passaggio di funzioni come argomenti
print_f(cubo,5)
# Out: 125
print_f(quadrato,5)
# Out: 25

l1 = [1,2]
l2 = [1,2]
l3 = l1 

# l1 e l3 si riferiscono allo stesso oggetto
print(id(l1),id(l2),id(l3))
# Out: 4348622088 4348588936 4348622088

# le modiche di l1 saranno visibili on l3
print(l1,l2,l3)
# Out: [1, 2] [1, 2] [1, 2]
l1[0] = -1
print(l1,l2,l3)
# Out: [-1, 2] [1, 2] [-1, 2]

x = 1.5
print(x, x.is_integer())
# Out: 1.5 False
x = 1.0
print(x, x.is_integer())
# Out: 1.0 True
y = 13
# Begin error-generating code --- using try/expect
try:
    print(y, y.is_integer())
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: AttributeError: 'int' object has no attribute 'is_integer'
except:
    pass
# End error-generating code

lst = ['uno', 1, 'uno', 'due', 2, 1]
print(lst.count(1))
# Out: 2
print(lst.count('uno'))
# Out: 2

# ritorna l'indice della prima occorrenza di 'due'
print(lst.index('due'))    
# Out: 3
# inizia la ricerca dalla posizione 2
print(lst.index(1, 2))
# Out: 5

# errore: non trova il valore 3
# Begin error-generating code --- using try/expect
try:
    print(lst.index(3))
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: ValueError: 3 is not in list
except:
    pass
# End error-generating code

lst = ['uno', 1, 'uno', 'due', 2, 1]
lst.append('tre')
print(lst)
# Out: ['uno', 1, 'uno', 'due', 2, 1, 'tre']
lst1 = lst + ['quattro']
lst == lst1
# Out: False

# inserisce 'sei' in posizione 2, spostando gli
lst.insert(2, 'sei')   
print(lst)                    
# Out: ['uno', 1, 'sei', 'uno', 'due', 2, 1, 'tre']
lst.insert(0, 'primo')
print(lst)
# Out: ['primo', 'uno', 1, 'sei', 'uno', 'due', 2, 1, 'tre']

lst.remove('uno')
print(lst)
# Out: ['primo', 1, 'sei', 'uno', 'due', 2, 1, 'tre']

x = lst.pop()
print(lst)
# Out: ['primo', 1, 'sei', 'uno', 'due', 2, 1]
x = lst.pop(2)
print(lst)
# Out: ['primo', 1, 'uno', 'due', 2, 1]

def rot(lst):
    '''Ruota la lista data di una posizione 
    a destra.'''
    last = lst.pop()
    lst.insert(0, last)
    
lst = [1,2,3,4,5]
rot([1,2,3,4,5])
print(lst)
# Out: [1, 2, 3, 4, 5]

def rotate(lst, k):
    '''Ruota la lista data di k posizioni 
    a destra.'''
    for _ in range(k):
        rot(lst)
        
def test_rotate(lst, k):
    print(lst, "  k =", k)
    rotate(lst, k)
    print(lst)
    
lst = [1,2,3,4,5]
rotate(lst, 3)
print(lst)
# Out: [3, 4, 5, 1, 2]

