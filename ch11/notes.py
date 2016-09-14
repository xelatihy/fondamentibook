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


s = 'Il Numero 1000'
print(s.lower())
# Out: il numero 1000
print(s.upper())
# Out: IL NUMERO 1000

a = "Ma che bella giornata."
print(a.count('e'))
# Out: 2
print(a.count('z'))
# Out: 0
print(a.count('giornata'))
# Out: 1

# conta dalla posizione 9 in poi
print(a.count('i', 9))     
# Out: 1
# dalla posizione 6 alla 9 esclusa
print(a.count('i', 6, 9))
# Out: 0

def conta_vocali(s):
    '''Conta le vocali non accentate in s.'''
    # Per contare anche le vocali maiuscole
    s = s.lower()
    count = 0
    for v in 'aeiou':
        count += s.count(v)
    return count

print(conta_vocali("che bello andare a spasso"))
# Out: 9
print(conta_vocali("Nn c sn vcl"))
# Out: 0

s = 'che bello andare a spasso'
print(s.find('bello'))
# Out: 4
# cerca a partire dalla posizione 4
print(s.find('e', 4))
# Out: 5
# cerca tra le posizioni 10 e 20 esclusa
print(s.find('bello', 10, 20))   
# Out: -1

testo = '''Prima linea,
seconda linea
e terza linea.'''
print(testo.splitlines())
# Out: ['Prima linea,', 'seconda linea', 'e terza linea.']
print(testo.splitlines(True))
# Out: ['Prima linea,\n', 'seconda linea\n', 'e terza linea.']

s = "Una frase d'esempio, non    troppo lunga"
# il separatore di default è lo spazio
print(s.split())
# Out: ['Una', 'frase', "d'esempio,", 'non', 'troppo', 'lunga']

# altri separatori
print(s.split(','))
# Out: ["Una frase d'esempio", ' non    troppo lunga']
print(s.split('p'))
# Out: ["Una frase d'esem", 'io, non    tro', '', 'o lunga']
print(s.split('pp'))
# Out: ["Una frase d'esempio, non    tro", 'o lunga']

# fa al massimo 2 separazioni
print(s.split('p', 2))
# Out: ["Una frase d'esem", 'io, non    tro', 'po lunga']

# differenza per le stringhe ripetute
print(s.split(' '))
# Out: ['Una', 'frase', "d'esempio,", 'non', '', '', '', 'troppo', 'lunga']

s = ' spazio prima e dopo '
print(repr(s))
# Out: ' spazio prima e dopo '
print(repr(s.strip()))
# Out: 'spazio prima e dopo'

s = "Ciao Bruno come stai?"
print(s.replace('Bruno', 'Sara'))
# Out: Ciao Sara come stai?
print(s.replace('bruno', 'sara'))
# Out: Ciao Bruno come stai?
print(s.replace('come ', '').replace('?',' bene?'))
# Out: Ciao Bruno stai bene?

'{} per {} uguale {}'.format(5,3,5*3)
# Out: '5 per 3 uguale 15'
'{nome} nato in {indirizzo} nel {anno}'.format(
    nome='Mario', indirizzo='Italia', anno='1974')
# Out: 'Mario nato in Italia nel 1974'

def ricerca(elenco, nome):
    '''Ritorna il numero di telefono nell'elenco
    per la riga con nome nome.'''
    nome = nome.lower()
    elenco = elenco.lower().splitlines()
    for e in elenco:
        e_nome, e_num = e.split(':')
        if nome == e_nome.strip():
            return e_num.strip()
    return 'Non esiste'
    
elenco = '''Marco: 5551234
Luisa: 5557653
Sara: 5558723'''

print(ricerca(elenco, 'Marco'))
# Out: 5551234
print(ricerca(elenco, 'Luisa'))
# Out: 5557653
print(ricerca(elenco, 'Giuseppe'))
# Out: Non esiste

def rubrica_to_dict(elenco):
    '''Converte un elenco da testo a tabella.'''
    d = {}
    elenco = elenco.lower().splitlines()
    for e in elenco:
        nome, numero = e.split(':')
        d[nome.strip()] = numero.strip()
    return d

elenco = '''Marco: 5551234
Luisa: 5557653
Sara: 5558723'''

dizionario = rubrica_to_dict(elenco)

from pprint import pprint
pprint(dizionario)
# Out: {'luisa': '5557653', 'marco': '5551234', 'sara': '5558723'}

def camel(s):
    for c in 'ABCDEFGHILMNOPQRSTUVWXYZ':
        s = s.replace(c, " "+c.lower())
    return s.split()
    
print(camel('fraseSenzaSpazi'))
# Out: ['frase', 'senza', 'spazi']
print(camel('sentenceWithoutSpaces'))
# Out: ['sentence', 'without', 'spaces']

def noalpha(s):
    '''Ritorna una stringa contenente tutti i
    caratteri non alfabetici contenuti in s, 
    senza ripetizioni'''
    noa = ''
    for c in s:
        if not c.isalpha() and c not in noa:
            noa += c
    return noa
            
print(noalpha("Frase con numeri 0987"))
# Out:  0987
print(noalpha("Frase con simboli vari [],{} %&#@"))
# Out:  [],{}%&#@
print(noalpha("FraseSenzaCaratteriNonAlfabetici"))
# Out: 

def words(s):
    '''Ritorna la lista delle parole contenute 
    nella stringa s'''
    noa = noalpha(s)
    for c in noa:
        s = s.replace(c, ' ')
    return s.lower().split()

print(words("Che bel tempo, usciamo!"))
# Out: ['che', 'bel', 'tempo', 'usciamo']

def fwords(fname,encoding):
    with open(fname, encoding=encoding) as f:
        testo = f.read()
    return words(testo)

parole = fwords('alice.txt','utf-8-sig')
print(len(parole))
# Out: 30419
print(parole[1000:1005])
# Out: ['bats', 'eat', 'cats', 'for', 'you']

parole_italiano = fwords('alice_it.txt','utf-8-sig')
print(len(parole_italiano))
# Out: 27794
print(parole_italiano[1000:1005])
# Out: ['era', 'in', 'fondo', 'e', 'andando']

parole_uniche = set(fwords('alice.txt','utf-8-sig'))
print(len(parole_uniche))
# Out: 3007

parole_uniche_italiano= set(fwords('alice_it.txt','utf-8-sig'))
print(len(parole_uniche_italiano))
# Out: 5180

def wfreq(fname, ricerca, enc):
    '''Ritorna un dizionario che ad ogni parola nella
    lista ricerca associa la sua frequenza 
    percentuale nel file fname. Il file è 
    decodificato tramite la codifica enc.'''
    
    # ottiene la lista delle parole
    parole = fwords(fname, enc)
    # prepare il dizionario delle frequenze
    frequenze = {}
    # per orgni parole nella ricerca
    for parola in ricerca:
        # calcola le occorrenze
        occ = parole.count(parola.lower())
        # calcola frequenza percentuale
        freq = occ*100/len(parole)
        # aggiorna il dizionario
        frequenze[parola] = round(freq,3)
    return frequenze

fname = 'alice.txt'
ricerca = ['alice','rabbit','turtle','king']
freq = wfreq(fname, ricerca, 'utf-8-sig')
print(freq)
# Out: {'alice': 1.325, 'turtle': 0.194, 'rabbit': 0.168, 'king': 0.207}

def scores(fnames, ricerca, enc):
    '''Ritorna un dizionario che ad ogni nome di file
    in fnames associa il suo punteggio relativamente 
    alla lista di parole ricerca. I file sono 
    decodificati tramite la codifica enc.'''
    frequenze = {}
    for fname in fnames:
        # dizionario delle frequenze di fname
        f = wfreq(fname, ricerca, enc)    
        # score arrotondata
        frequenze[fname] = round(sum(f.values()), 3)
    return frequenze

fnames = [ 'alice.txt', 'holmes.txt', 
          'frankenstein.txt', 'prince.txt', 
          'mobydick.txt', 'treasure.txt' ]

ricerca = [ 'monster', 'horror', 'night' ]
pprint(scores(fnames, ricerca, 'utf-8-sig'))
# Out: {'alice.txt': 0.016,
# Out:  'frankenstein.txt': 0.216,
# Out:  'holmes.txt': 0.119,
# Out:  'mobydick.txt': 0.103,
# Out:  'prince.txt': 0.023,
# Out:  'treasure.txt': 0.066}

def extract_value(kv): return kv[1]
def searchdocument(fnames, ricerca, enc):
    '''Ritorna la lista ordindata per score dei
    documenti in fnames per le parole in ricerca.'''
    s = scores(fnames, ricerca, enc)
    return sorted(s.items(), key=extract_value, 
        reverse=True)

ricerca = [ 'monster', 'horror', 'night' ]
pprint(searchdocument(fnames, ricerca, 'utf-8-sig'))
# Out: [('frankenstein.txt', 0.216),
# Out:  ('holmes.txt', 0.119),
# Out:  ('mobydick.txt', 0.103),
# Out:  ('treasure.txt', 0.066),
# Out:  ('prince.txt', 0.023),
# Out:  ('alice.txt', 0.016)]

