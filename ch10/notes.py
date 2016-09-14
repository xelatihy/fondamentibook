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


f = open('alice.txt')
# qualcosa col file ...
f.close()

# Begin error-generating code --- using try/expect
try:
    f = open('non_esiste.txt')
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: FileNotFoundError: [Errno 2] No such file or directory: 'non_esiste.txt'
except:
    pass
# End error-generating code

with open('alice.txt') as f:
    print('aperto')
    # fai qualcosa col file ...
# Out: aperto

import os

print(os.getcwd())
# Out: /Users/fabio/Documents/Work/books/fondamentibook/ch10

f = open('alice.txt')

testo = f.read()
print(len(testo))
# Out: 163781

print(testo[686:1020])
# Out: CHAPTER I. Down the Rabbit-Hole
# Out: 
# Out: Alice was beginning to get very tired of sitting by her sister on the
# Out: bank, and of having nothing to do: once or twice she had peeped into the
# Out: book her sister was reading, but it had no pictures or conversations in
# Out: it, 'and what is the use of a book,' thought Alice 'without pictures or
# Out: conversations?

print(f.read())
# Out: 
f.close()

with open('alice.txt') as f:
    testo = f.read()
    print(len(testo))
# Out: 163781

with open('alice.txt') as f:
    first = f.readline()
    print(repr(first))
# Out: "\ufeffProject Gutenberg's Alice's Adventures in Wonderland, by Lewis Carroll\n"

with open('alice.txt', encoding='utf-8-sig') as f:
    print(repr(f.readline()))
# Out: "Project Gutenberg's Alice's Adventures in Wonderland, by Lewis Carroll\n"

with open('alice_it.txt', encoding='utf-8-sig') as f:
    print(repr(f.readline()))
# Out: "The Project Gutenberg eBook of Le avventure d'Alice nel paese delle\n"

with open('alice.txt', encoding='utf-8-sig') as f:
    linee = f.readlines()
    print(len(linee))
    print(linee[200])
    print(linee[400])
# Out: 3735
# Out: she felt a little nervous about this; 'for it might end, you know,' said
# Out: 
# Out: anything had happened.) So she began again: 'Ou est ma chatte?' which
# Out: 

def ricerca_linee(nome_file, encoding, stringa):
    '''Ritorna la lista dei numeri delle linee del 
    file nome_file in cui appare la stringa.'''
    with open(nome_file, encoding=encoding) as f:
        lista_indici = []
        indice_corrente = 1
        for linea in f:
            if linea.find(stringa) != -1:
                lista_indici.append(indice_corrente)
            indice_corrente += 1
        return lista_indici

indici = ricerca_linee('alice.txt', 'utf-8-sig', 'Turtle')
print(indici)
# Out: [2213, 2353, 2355, 2357, 2371, 2389, 2396, 2402, 2409, 2410, 2414, 2419, 2421, 2425, 2431, 2438, 2441, 2448, 2452, 2456, 2463, 2468, 2483, 2485, 2493, 2499, 2508, 2520, 2532, 2536, 2550, 2559, 2563, 2571, 2577, 2583, 2587, 2594, 2626, 2632, 2638, 2640, 2679, 2684, 2689, 2696, 2707, 2712, 2740, 2746, 2751, 2774, 2782, 2784, 2786, 2789, 2812, 3347, 3357]
indici = ricerca_linee('alice.txt', 'utf-8-sig', 'Alice')
print(len(indici))
# Out: 396

with open('testo.txt', 'w') as f:
    f.write('Questo è il contenuto del file.')
# Out: 31

with open('testo.txt') as f:
    print(f.read())
# Out: Questo è il contenuto del file.

with open('lista.txt', 'w') as f:
    f.writelines(['Linea1\n','Linea2\n'])

with open('lista.txt') as f:
    print(f.read())
# Out: Linea1
# Out: Linea2
# Out: 

with open('append.txt', 'w') as f:
    f.write('Linea1.\n')
# Out: 8

with open('append.txt', 'a') as f:
    f.write('Linea2.\n')
# Out: 8

with open('append.txt') as f:
    print(f.read())
# Out: Linea1.
# Out: Linea2.
# Out: 

import json

# definisce i dati
dati = [
  { 'nome':'Sofia', 'anno':1973, 'tel':'5553546' },
  { 'nome':'Bruno', 'anno':1981, 'tel':'5558432' },
  { 'nome':'Mario', 'anno':1992, 'tel':'5555092' },
  { 'nome':'Alice', 'anno':1965, 'tel':'5553546' },
]

# salva i dati su disco
with open('dati.json','w') as f:
    json.dump(dati,f)

# per verificare il salvataggio, rileggiamo i dati
with open('dati.json') as f:
    nuovi_dati = json.load(f)
print(dati == nuovi_dati)
# Out: True

from urllib.request import urlopen

# apre una pagina web
# Begin error-generating code --- using try/expect
try:
    with urlopen('http://python.org') as f:
        page = f.read()
    # Error: Traceback (most recent call last):
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 1254, in do_open
    # Error:     h.request(req.get_method(), req.selector, req.data, headers)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1106, in request
    # Error:     self._send_request(method, url, body, headers)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1151, in _send_request
    # Error:     self.endheaders(body)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1102, in endheaders
    # Error:     self._send_output(message_body)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 934, in _send_output
    # Error:     self.send(msg)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 877, in send
    # Error:     self.connect()
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 849, in connect
    # Error:     (self.host,self.port), self.timeout, self.source_address)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/socket.py", line 693, in create_connection
    # Error:     for res in getaddrinfo(host, port, 0, SOCK_STREAM):
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/socket.py", line 732, in getaddrinfo
    # Error:     for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
    # Error: socket.gaierror: [Errno 8] nodename nor servname provided, or not known
    # Error: 
    # Error: During handling of the above exception, another exception occurred:
    # Error: 
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 163, in urlopen
    # Error:     return opener.open(url, data, timeout)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 466, in open
    # Error:     response = self._open(req, data)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 484, in _open
    # Error:     '_open', req)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 444, in _call_chain
    # Error:     result = func(*args)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 1282, in http_open
    # Error:     return self.do_open(http.client.HTTPConnection, req)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 1256, in do_open
    # Error:     raise URLError(err)
    # Error: urllib.error.URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
except:
    pass
# End error-generating code

# dati in binario
# Begin error-generating code --- using try/expect
try:
    print(page[:50])
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: NameError: name 'page' is not defined
except:
    pass
# End error-generating code

# dati come testo
# Begin error-generating code --- using try/expect
try:
    page = page.decode('utf8')
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: NameError: name 'page' is not defined
except:
    pass
# End error-generating code
# Begin error-generating code --- using try/expect
try:
    print(page[:50])
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: NameError: name 'page' is not defined
except:
    pass
# End error-generating code

url = ('https://upload.wikimedia.org/wikipedia/' +
       'commons/thumb/d/df/Face-plain.svg/' + 
       '200px-Face-plain.svg.png')
# Begin error-generating code --- using try/expect
try:
    with urlopen(url) as f:
        img = f.read()
    # Error: Traceback (most recent call last):
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 1254, in do_open
    # Error:     h.request(req.get_method(), req.selector, req.data, headers)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1106, in request
    # Error:     self._send_request(method, url, body, headers)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1151, in _send_request
    # Error:     self.endheaders(body)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1102, in endheaders
    # Error:     self._send_output(message_body)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 934, in _send_output
    # Error:     self.send(msg)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 877, in send
    # Error:     self.connect()
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 1252, in connect
    # Error:     super().connect()
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py", line 849, in connect
    # Error:     (self.host,self.port), self.timeout, self.source_address)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/socket.py", line 693, in create_connection
    # Error:     for res in getaddrinfo(host, port, 0, SOCK_STREAM):
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/socket.py", line 732, in getaddrinfo
    # Error:     for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
    # Error: socket.gaierror: [Errno 8] nodename nor servname provided, or not known
    # Error: 
    # Error: During handling of the above exception, another exception occurred:
    # Error: 
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 163, in urlopen
    # Error:     return opener.open(url, data, timeout)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 466, in open
    # Error:     response = self._open(req, data)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 484, in _open
    # Error:     '_open', req)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 444, in _call_chain
    # Error:     result = func(*args)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 1297, in https_open
    # Error:     context=self._context, check_hostname=self._check_hostname)
    # Error:   File "/Users/fabio/homebrew/Cellar/python3/3.5.2_1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py", line 1256, in do_open
    # Error:     raise URLError(err)
    # Error: urllib.error.URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
except:
    pass
# End error-generating code

# Begin error-generating code --- using try/expect
try:
    with open('face.png', 'wb') as f:
        f.write(img)
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 2, in <module>
    # Error: NameError: name 'img' is not defined
except:
    pass
# End error-generating code

