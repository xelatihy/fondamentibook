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


15 + 3
# Out: 18
10 - 25
# Out: -15
3*7
# Out: 21

15.7 + 3
# Out: 18.7
18.0 * 5
# Out: 90.0

15 // 2
# Out: 7
15.0 // 2
# Out: 7.0
15 / 2
# Out: 7.5
15.0 / 2
# Out: 7.5

(12/5)*(16 - 2*3)
# Out: 24.0

24 % 7
# Out: 3
27 % 9
# Out: 0
27 % 7.5
# Out: 4.5
2**8
# Out: 256
2**0.5
# Out: 1.4142135623730951

2**100
# Out: 1267650600228229401496703205376
2.0**100
# Out: 1.2676506002282294e+30

print(1+1)
# Out: 2

print(2+3,5+6)
# Out: 5 11

'ciao'
# Out: 'ciao'
print('ciao')
# Out: ciao

print("L'altra mattina")
# Out: L'altra mattina

# stringa vuota
''
# Out: ''
print('')
# Out: 

print(repr('ciao'))
# Out: 'ciao'

print('''Questo testo
va a capo.''')
# Out: Questo testo
# Out: va a capo.

print(repr('''Questo testo
va a capo.'''))
# Out: 'Questo testo\nva a capo.'

print('né così né cosà')
# Out: né così né cosà

saluto = 'Buon ' + 'giorno'
print(saluto)
# Out: Buon giorno
boom = 'tic tac '*5 + 'BOOM!'
print(boom)
# Out: tic tac tic tac tic tac tic tac tic tac BOOM!

print(type(5 + 2))
# Out: <class 'int'>
print(type(10 + 5 / 2))
# Out: <class 'float'>
print(type('ciao'))
# Out: <class 'str'>

# Begin error-generating code --- using try/expect
try:
    print('stringa' + 5)
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: TypeError: Can't convert 'int' object to str implicitly
except:
    pass
# End error-generating code

# conversione in stringhe
print('stringa' + str(5))
# Out: stringa5

# conversione in numeri
print(10 + int('5'))
# Out: 15

# conversione non valida
# Begin error-generating code --- using try/expect
try:
    print(int('ciao'))
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: ValueError: invalid literal for int() with base 10: 'ciao'
except:
    pass
# End error-generating code

pigreco = 3.14

# area di un cerchio di raggio 10
raggio = 10
area = pigreco * raggio ** 2
print(area)
# Out: 314.0

 # ricalcolo dell'area con raggio 20
raggio = 20
area = pigreco * raggio ** 2
print(area)
# Out: 1256.0

# Begin error-generating code --- using try/expect
try:
    print(2 * non_definita)
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: NameError: name 'non_definita' is not defined
except:
    pass
# End error-generating code

saluto = "ciao"
print(repr(saluto))
# Out: 'ciao'
print(saluto)
# Out: ciao

stringa_vuota = ''
print(stringa_vuota)
# Out: 

variabile = 10
print(type(variabile))
# Out: <class 'int'>

variabile = 'ciao'
print(type(variabile))
# Out: <class 'str'>

# raddoppia il raggio
print(raggio)
# Out: 20
raggio = raggio * 2
print(raggio)
# Out: 40

# raddoppia l'altezza
print(raggio)
# Out: 40
raggio *= 2
print(raggio)
# Out: 80

