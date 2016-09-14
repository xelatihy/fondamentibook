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


# dizionario con chiavi-valori
rubrica = { 'Sergio': '123456', 'Bruno': '654321' }
print(rubrica)
# Out: {'Sergio': '123456', 'Bruno': '654321'}
print(type(rubrica))
# Out: <class 'dict'>

# dizionari vuoti
print({})
# Out: {}

# valore associato a 'Sergio'
print(rubrica['Sergio'])
# Out: 123456

# valore associato a Bruno
print(rubrica['Bruno'])
# Out: 654321

# valore non estistente
# Begin error-generating code --- using try/expect
try:
    print(rubrica['Giovanni'])
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: KeyError: 'Giovanni'
except:
    pass
# End error-generating code

# aggiunge una nuova associazione
rubrica['Mario'] = '112233' 
print(rubrica)
# Out: {'Mario': '112233', 'Sergio': '123456', 'Bruno': '654321'}

# modifica un'associazione esistente
rubrica['Sergio'] = '214365' 
print(rubrica)
# Out: {'Mario': '112233', 'Sergio': '214365', 'Bruno': '654321'}

# rimuove un chiave e il corrispondente valore
x = rubrica.pop('Bruno')
print(rubrica)
# Out: {'Mario': '112233', 'Sergio': '214365'}

print('Sergio' in rubrica)
# Out: True
print('Luigi' in rubrica)
# Out: False
print('214365' in rubrica)
# Out: False
print(len(rubrica))
# Out: 2

# itera sulle chiavi di rubrica
for chiave in rubrica:            
    print(chiave, rubrica[chiave])
# Out: Mario 112233
# Out: Sergio 214365

# itera sulle chiavi di rubrica
for chiave in rubrica.keys():            
    print(chiave, rubrica[chiave])
# Out: Mario 112233
# Out: Sergio 214365

# itera sulle coppie chiavi-valori di rubrica
for chiave, valore in rubrica.items():            
    print(chiave, valore)
# Out: Mario 112233
# Out: Sergio 214365

# itera sui valori di rubrica
for valore in rubrica.values():            
    print(valore)
# Out: 112233
# Out: 214365

print(rubrica.keys())
# Out: dict_keys(['Mario', 'Sergio'])
print(rubrica.values())
# Out: dict_values(['112233', '214365'])
print(rubrica.items())
# Out: dict_items([('Mario', '112233'), ('Sergio', '214365')])

def aggiorna_dict(d, d2):
    '''Aggiunge a d gli elementi in d2.'''
    for k, v in d2.items():
        d[k] = v
            
rubrica = { 'Sergio': '112233',
            'Mario': '654321' }
           
rubrica2 = { 'Sergio': '333333',
             'Maria': '222222' }
       
aggiorna_dict(rubrica, rubrica2)
print(rubrica)
# Out: {'Mario': '654321', 'Maria': '222222', 'Sergio': '333333'}

cubi = { i: i**3 for i in range(3) }
print(cubi)
# Out: {0: 0, 1: 1, 2: 8}

# innsieme con due valori
insieme = { 5, 'five' }
print(insieme)
# Out: {5, 'five'}

# insiemi vuoti
print(set())
# Out: set()

insieme.add(6)
print(insieme)
# Out: {5, 'five', 6}

insieme.add(6)
print(insieme)
# Out: {5, 'five', 6}

insieme.remove('five')
print(insieme)
# Out: {5, 6}

for valore in insieme:
    print(valore)
# Out: 5
# Out: 6

print(5 in insieme)
# Out: True
print('six' in insieme)
# Out: False
print(len(insieme))
# Out: 2

print( set( ['rosso', 'verde', 'blu', 'rosso'] ) )
# Out: {'blu', 'rosso', 'verde'}

colori1 = {'rosso', 'verde', 'giallo'}
colori2 = {'rosso', 'blu'}
print(colori1 | colori2)
# Out: {'blu', 'rosso', 'verde', 'giallo'}
print(colori1 - colori2)
# Out: {'verde', 'giallo'}
print(colori1 & colori2)
# Out: {'rosso'}
print(colori1 ^ colori2)
# Out: {'blu', 'verde', 'giallo'}

# crea una lista dall'insieme
def intersezione_liste(lst1, lst2):
    inter = set(lst1) & set(lst2)
    return list(inter)  
    
primi = [2,3,5,7,11,13,17,19,23,29,31,37,41]
fib = [1,1,2,3,5,8,13,21,34,55,89]

print(intersezione_liste(primi, fib))
# Out: [13, 2, 3, 5]

w1 = [ 'quali', 'sono', 'le', 'parole', 'in', 'comune' ]
w2 = [ 'sono', 'le', 'parole', 'che', 'appaiono', 'sia','in', 'w1', 'che', 'in', 'w2' ]

print(intersezione_liste(w1, w2))
# Out: ['sono', 'le', 'in', 'parole']

colonne = ['nome', 'anno', 'telefono']

dati = [
  { 'nome':'Sofia', 'anno':1973, 'tel':'5553546' },
  { 'nome':'Bruno', 'anno':1981, 'tel':'5558432' },
  { 'nome':'Mario', 'anno':1992, 'tel':'5555092' },
  { 'nome':'Alice', 'anno':1965, 'tel':'5553546' },
]

print(dati)
# Out: [{'tel': '5553546', 'nome': 'Sofia', 'anno': 1973}, {'tel': '5558432', 'nome': 'Bruno', 'anno': 1981}, {'tel': '5555092', 'nome': 'Mario', 'anno': 1992}, {'tel': '5553546', 'nome': 'Alice', 'anno': 1965}]

from pprint import pprint
pprint(dati)
# Out: [{'anno': 1973, 'nome': 'Sofia', 'tel': '5553546'},
# Out:  {'anno': 1981, 'nome': 'Bruno', 'tel': '5558432'},
# Out:  {'anno': 1992, 'nome': 'Mario', 'tel': '5555092'},
# Out:  {'anno': 1965, 'nome': 'Alice', 'tel': '5553546'}]

def colonna(dati,chiave):
    '''Ritorna la lista dei valori per la colonna 
    specificata da chiave.'''
    valori = []
    for dato in dati:
        valori.append( dato[chiave] )
    return valori

nomi = colonna(dati,'nome')
pprint(nomi)
# Out: ['Sofia', 'Bruno', 'Mario', 'Alice']

def sottotabella(dati,chiavi):
    '''Ritorna la tabella che include solo le
    colonne specificate da chiavi.'''
    ndati = []
    for dato in dati:
        ndato = {}
        for chiave in chiavi:
            ndato[chiave] = dato[chiave]
        ndati.append( ndato )
    return ndati

pprint(sottotabella(dati,['nome','anno']))
# Out: [{'anno': 1973, 'nome': 'Sofia'},
# Out:  {'anno': 1981, 'nome': 'Bruno'},
# Out:  {'anno': 1992, 'nome': 'Mario'},
# Out:  {'anno': 1965, 'nome': 'Alice'}]

def ricerca(dati,nome,chiave):
    for dato in dati:
        if dato['nome'] == nome:
            return dato[chiave]
    return None

print(ricerca(dati,'Mario','tel'))
# Out: 5555092

indice = {}
for numero_riga, dato in enumerate(dati):
    indice[dato['nome']] = numero_riga

def ricerca_con_indice(dati,indice,nome,chiave):
    if nome in indice:
        numero_riga = indice[nome]
        dato = dati[numero_riga]
        return dato[chiave]
    else:
        return None

print(ricerca_con_indice(dati,indice,'Mario','tel'))
# Out: 5555092

# dati non ordinati
pprint(dati)
# Out: [{'anno': 1973, 'nome': 'Sofia', 'tel': '5553546'},
# Out:  {'anno': 1981, 'nome': 'Bruno', 'tel': '5558432'},
# Out:  {'anno': 1992, 'nome': 'Mario', 'tel': '5555092'},
# Out:  {'anno': 1965, 'nome': 'Alice', 'tel': '5553546'}]

# dati ordinati per nome
def nome_dato(dato): return dato['nome']
pprint(sorted(dati,key=nome_dato))
# Out: [{'anno': 1965, 'nome': 'Alice', 'tel': '5553546'},
# Out:  {'anno': 1981, 'nome': 'Bruno', 'tel': '5558432'},
# Out:  {'anno': 1992, 'nome': 'Mario', 'tel': '5555092'},
# Out:  {'anno': 1973, 'nome': 'Sofia', 'tel': '5553546'}]

# dati ordinati per anno di nascita
def anno_dato(dato): return dato['anno']
pprint(sorted(dati,key=anno_dato))
# Out: [{'anno': 1965, 'nome': 'Alice', 'tel': '5553546'},
# Out:  {'anno': 1973, 'nome': 'Sofia', 'tel': '5553546'},
# Out:  {'anno': 1981, 'nome': 'Bruno', 'tel': '5558432'},
# Out:  {'anno': 1992, 'nome': 'Mario', 'tel': '5555092'}]

# dati ordinati per anno di nascita inverso
pprint(sorted(dati,key=anno_dato,reverse=True))
# Out: [{'anno': 1992, 'nome': 'Mario', 'tel': '5555092'},
# Out:  {'anno': 1981, 'nome': 'Bruno', 'tel': '5558432'},
# Out:  {'anno': 1973, 'nome': 'Sofia', 'tel': '5553546'},
# Out:  {'anno': 1965, 'nome': 'Alice', 'tel': '5553546'}]

