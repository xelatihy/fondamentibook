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


import html

class HTMLNode(object):
    def __init__(self,tag,attr,content,closed=True):
        self.tag = tag
        # dizionario degli attributi
        self.attr = attr
        # testo per nodi _text_ o lista dei figli
        self.content = content  
        # True se il nodo ha la chiusura
        self.closed = closed    
    
    # per distinguere i nodi testo
    def istext(self):           
        return self.tag == '_text_'
    
    def open_tag(self):
        '''Ritorna la stringa del tag di inizio.'''
        if self.istext():
            return self.tag
        s = '<'+self.tag
        for k, v in self.attr.items():
            # usiamo escape per i valori 
            s += ' {}="{}"'.format(
                k, html.escape(v,True))
        s += '>'
        return s
    
    def close_tag(self):
        '''Ritorna la stringa del tag di fine.'''
        return '</'+self.tag+'>'
    
    def print_tree(self, level=0):
        '''Stampa l'albero mostrando la struttura
        tramite indentazione'''
        if self.istext():
            print('  '*level + '_text_ ' +
                repr(self.content))
        else:
            print('  '*level + str(self))
            for child in self.content:
                child.print_tree(level+1)
    
    def to_string(self):
        '''Ritorna la stringa del documento HTML che
        corrisponde all'albero di questo nodo.'''
        if self.istext():
            # usiamo escape per i caratteri speciali
            return html.escape(self.content,False)
        s = self.open_tag()
        doc = self.open_tag()
        if self.closed:
            for child in self.content:
                doc += child.to_string()
            doc += self.close_tag()
        return doc
                
    def __str__(self):
        '''Ritorna una rappresentazione semplice
        del nodo'''
        if self.istext(): return self.tag
        else: return '<{}>'.format(self.tag)

doc = HTMLNode('html',{},[
  HTMLNode('body',{},[
    HTMLNode('p',{},[
      HTMLNode('_text_',{},'Un paragrafo con '),
      HTMLNode('em',{},[
        HTMLNode('_text_',{},'enfasi')
      ]),
      HTMLNode('_text_',{},' e un\'immagine'),
      HTMLNode('img',{'src':'img_logo.png'},
          [],closed=False)
    ])
  ])
])

# stampa la struttura nell'albero
doc.print_tree()
# Out: <html>
# Out:   <body>
# Out:     <p>
# Out:       _text_ 'Un paragrafo con '
# Out:       <em>
# Out:         _text_ 'enfasi'
# Out:       _text_ " e un'immagine"
# Out:       <img>

# stampa la stringa HTML corrispodente
print(doc.to_string())
# Out: <html><body><p>Un paragrafo con <em>enfasi</em> e un'immagine<img src="img_logo.png"></p></body></html>

import html.parser

class _MyHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        '''Crea un parser per la class HTMLNode'''
        # inizializza la class base super()
        super().__init__()
        self.root = None
        self.stack = []
    def handle_starttag(self, tag, attrs):
        '''Metodo invocato per tag aperti'''
        closed = tag not in ['img','br']
        node = HTMLNode(tag,dict(attrs),[],closed)
        if not self.root:
            self.root = node
        if self.stack: 
            self.stack[-1].content.append(node)
        if closed:
            self.stack.append(node)
    def handle_endtag(self, tag):
        '''Metodo invocato per tag chiusi'''
        if self.stack and self.stack[-1].tag == tag:
            self.stack[-1].opentag = False
            self.stack = self.stack[:-1]
    def handle_data(self, data):
        '''Metodo invocato per il testo'''
        if not self.stack: return
        self.stack[-1].content.append(
            HTMLNode('_text_',{},data))
    def handle_comment(self, data):
        '''Metodo invocato per commenti HTML'''
        pass
    def handle_entityref(self, name):
        '''Metodo invocato per caratteri speciali'''
        if name in name2codepoint:
            c = unichr(name2codepoint[name])
        else:
            c = '&'+name
        if not self.stack: return
        self.stack[-1].content.append(
            HTMLNode('_text_',{},c))
    def handle_charref(self, name):
        '''Metodo invocato per caratteri speciali'''
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        if not self.stack: return
        self.stack[-1].content.append(
            HTMLNode('_text_',{},c))
    def handle_decl(self, data):
        '''Metodo invocato per le direttive HTML'''
        pass

def parse(html):
    '''Esegue il parsing HTML del testo html e
    ritorna la radice dell'albero.'''
    parser = _MyHTMLParser()
    parser.feed(html)
    return parser.root

def fparse(fhtml):
    '''Esegue il parsing HTML del file fhtml e
    ritorna la radice dell'albero .'''
    with open(fhtml) as f:
        root = parse(f.read())
    return root

# Proviamo a fare il parsing del semplice file
# che abbiamo visto sopra.
doc = fparse('page_simple.html')

doc.print_tree()
# Out: <html>
# Out:   _text_ '\n'
# Out:   <body>
# Out:     _text_ '\n'
# Out:     <h1>
# Out:       _text_ 'Un Semplice Documento'
# Out:     _text_ '\n'
# Out:     <p>
# Out:       _text_ 'Un paragrafo con testo '
# Out:       <em>
# Out:         _text_ 'enfatizzato'
# Out:       _text_ '.'
# Out:     _text_ '\n'
# Out:     <p>
# Out:       _text_ 'Un paragrafo con un link a '
# Out:       <a>
# Out:         _text_ 'Wikipedia'
# Out:       _text_ " e un'immagine a seguire."
# Out:     _text_ '\n'
# Out:     <img>
# Out:     _text_ '\n'
# Out:   _text_ '\n'

print(doc.to_string())
# Out: <html>
# Out: <body>
# Out: <h1>Un Semplice Documento</h1>
# Out: <p>Un paragrafo con testo <em>enfatizzato</em>.</p>
# Out: <p>Un paragrafo con un link a <a href="http://en.wikipedia.org/">Wikipedia</a> e un'immagine a seguire.</p>
# Out: <img src="photo.png">
# Out: </body>
# Out: </html>

def count(node):
    '''Ritorna il numero di nodi dell'albero di
    questo nodo'''
    cnt = 1
    if not node.istext():
        for child in node.content:
            cnt += count(child)
    return cnt

print('Numero di nodi:', count(doc))
# Out: Numero di nodi: 22

def height(node):
    '''Ritorna l'altezza dell'albero con radice
    questo nodo, cioè il massimo numero di nodi
    in un cammino radice-foglia'''
    h = 1
    if not node.istext():
        for child in node.content:
            h = max(h, height(child) + 1)
    return h

print('Altezza:', height(doc))
# Out: Altezza: 5

def find_by_tag(node, tag):
    '''Ritorna una lista dei nodi che hanno il tag'''
    ret = []
    if node.tag == tag: ret += [node]
    if not node.istext():
        for child in node.content:
            ret += find_by_tag(child,tag)
    return ret

for node in find_by_tag(doc,'a'):
    print(node.to_string())
# Out: <a href="http://en.wikipedia.org/">Wikipedia</a>
for node in find_by_tag(doc,'p'):
    print(node.to_string())
# Out: <p>Un paragrafo con testo <em>enfatizzato</em>.</p>
# Out: <p>Un paragrafo con un link a <a href="http://en.wikipedia.org/">Wikipedia</a> e un'immagine a seguire.</p>

def remove_by_tag(node, tag):
    '''Rimuove dall'albero tutti i nodi con il tag,
    esclusa la radice, cioè il nodo su cui è invocato
    il metodo.'''
    if node.istext(): return
    for child in node.content:
        remove_by_tag(child,tag)
    newcont = []
    for child in node.content:
        if child.tag == tag:
            if not child.istext():
                newcont += child.content
        else:
            newcont += [child]
    node.content = newcont

remove_by_tag(doc,'a')
print(doc.to_string())
# Out: <html>
# Out: <body>
# Out: <h1>Un Semplice Documento</h1>
# Out: <p>Un paragrafo con testo <em>enfatizzato</em>.</p>
# Out: <p>Un paragrafo con un link a Wikipedia e un'immagine a seguire.</p>
# Out: <img src="photo.png">
# Out: </body>
# Out: </html>

remove_by_tag(doc,'_text_')
print(doc.to_string())
# Out: <html><body><h1></h1><p><em></em></p><p></p><img src="photo.png"></body></html>

from urllib.request import urlopen

def print_stats(url):
    '''Stampa alcune statistiche della pagina web
    all'url specificato.'''
    with urlopen(url) as f:
        page = f.read().decode('utf8')
    doc = parse(page)
    print('Numero di nodi:', count(doc))
    print('Altezza:', height(doc))
    print('Numero di links:', len(find_by_tag(doc,'a')))
    print('Numero di immagini:', len(find_by_tag(doc,'img')))

# Begin error-generating code --- using try/expect
try:
    print_stats('http://python.org')
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
    # Error:   File "<input>", line 4, in print_stats
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

# Begin error-generating code --- using try/expect
try:
    print_stats('https://en.wikipedia.org/wiki/Python_(programming_language)')
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
    # Error:   File "<input>", line 4, in print_stats
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

