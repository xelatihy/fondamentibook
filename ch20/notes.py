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


import os

# percorso del file todo
filename = 'todo.txt'

def load():
    '''Carica la lista dei promemoria e ritorna la
    lista delle linee del file'''
    with open(filename) as f:
        return f.read().splitlines()

def save(lst):
    '''Salva la lista di promemoria come testo'''
    with open(filename,'w') as f:
        return f.write('\n'.join(lst))

def init(clear=True):
    '''Inizializza il file dei promemoria'''
    if clear:
        save([])
    else:
        if os.path.exists(filename): return
        save('')

def next_uid(lst):
    '''Calcola un nuovo identificativo univoco'''
    max_uid = 0
    for line in lst:
        uid = line.split()[2]
        num = int(uid[1:])
        if num > max_uid:
            max_uid = num
    return '@{:04}'.format(max_uid+1)

def find(lst, uid):
    '''Ritorna l'indice di riga del promemoria 
    con identificativo uid'''
    for i, line in enumerate(lst):
        if uid in line.lower().split():
            return i
    return -1

def add(title,uid=None):
    '''Aggiunge un promemoria alla lista'''
    lst = load()
    if not uid:
        uid = next_uid(lst)
    lst += ['- [_] {} {}\n'.format(uid,title.strip())]
    save(lst)
    return True

def print_txt(checked=False,search=None):
    '''Stampa la lista. Se checked è falso, esclude
    i promemoria completati. Se search non è None,
    includi solo i promemoria che la contengono'''
    lst = load()
    for line in lst:
        if (not checked and 
            '[x]' in line.lower()): continue
        if (search and (search.lower() not in 
            line.lower().split())): continue
        print(line)
    return True

def check(uid,checked):
    '''Setta la stato del promemoria uid come
    spuntato o no'''
    lst = load()
    pos = find(lst,uid)
    if pos < 0: return False
    if checked:
        lst[pos] = lst[pos].replace('[_]','[x]')
    else:
        lst[pos] = lst[pos].replace('[x]','[_]')
    save(lst)
    return True

# inizializziamo il sistema
if __name__ == '__console__':
    init()                              

# aggiungiamo due todo
if __name__ == '__console__':
    add('scrivere un libro')            
    add('mangiare un gelato buono')
    add('andare a pescare')
    print_txt()
# Out: True
# Out: True
# Out: True
# Out: - [_] @0001 scrivere un libro
# Out: - [_] @0002 mangiare un gelato buono
# Out: - [_] @0003 andare a pescare
# Out: True

# spunta una todo
if __name__ == '__console__':
    check('@0002',True)                 
    print_txt()
# Out: True
# Out: - [_] @0001 scrivere un libro
# Out: - [_] @0003 andare a pescare
# Out: True

# stampa
if __name__ == '__console__':
    print_txt(checked=True)
# Out: - [_] @0001 scrivere un libro
# Out: - [x] @0002 mangiare un gelato buono
# Out: - [_] @0003 andare a pescare
# Out: True

if __name__ == '__console__':
    check('@0002',False)
    print_txt(search='pescare') 
# Out: True
# Out: - [_] @0003 andare a pescare
# Out: True

if __name__ == '__console__':
    print_txt(search='@0001')
# Out: - [_] @0001 scrivere un libro
# Out: True

def up(uid):
    '''Muove in sù un promemoria'''
    lst = load()
    pos = find(lst,uid)
    if pos < 0: return False
    if pos == 0: return False
    lst[pos], lst[pos-1] = lst[pos-1], lst[pos]
    save(lst)
    return True

def down(uid):
    '''Muove in giù un promemoria'''
    lst = load()
    pos = find(lst,uid)
    if pos < 0: return False
    if pos == len(lst)-1: return False
    lst[pos], lst[pos+1] = lst[pos+1], lst[pos]
    save(lst)
    return True

def erase(uid):
    '''Cancella un promemoria'''
    lst = load()
    pos = find(lst,uid)
    if pos < 0: return False
    lst = lst[:pos] + lst[pos+1:]
    save(lst)
    return True

# facciamo alcuni tests
if __name__ == '__console__':
    print_txt()
# Out: - [_] @0001 scrivere un libro
# Out: - [_] @0002 mangiare un gelato buono
# Out: - [_] @0003 andare a pescare
# Out: True

if __name__ == '__console__':
    up('@0002')
    print_txt()
# Out: True
# Out: - [_] @0002 mangiare un gelato buono
# Out: - [_] @0001 scrivere un libro
# Out: - [_] @0003 andare a pescare
# Out: True

if __name__ == '__console__':
    erase('@0001')
    print_txt()
# Out: True
# Out: - [_] @0002 mangiare un gelato buono
# Out: - [_] @0003 andare a pescare
# Out: True

if __name__ == '__console__':
    down('@0002')
    print_txt()
# Out: True
# Out: - [_] @0003 andare a pescare
# Out: - [_] @0002 mangiare un gelato buono
# Out: True

import click

@click.group()
def cli():
    '''Funzione vuota che raggruppa i comandi'''
    pass

# definisce il comando: add title [-u uid]
@cli.command('add')
@click.argument('title', required=True)
@click.option('-u','--uid',default=None)
def add_cli(title,uid=None):
    '''interfaccia cli per add'''
    if add(title,uid): print('add new')
    else: print('add error')

# definisce il comando: print [-s search] [-c]
@cli.command('print')
@click.option('-s', '--search', default=None)
@click.option('-c', '--checked', is_flag=True, 
    default=False)
def print_cli(search=None,checked=False):
    '''interfaccia cli per print'''
    print_txt(search=search,checked=checked)

# definisce il comando: check uid
@cli.command('check')
@click.argument('uid', required=True)
def check_cli(uid):
    '''interfaccia cli per check'''
    if check(uid,True): print('check',uid)
    else: print('check error')

# definisce il comando: uncheck uid
@cli.command('uncheck')
@click.argument('uid', required=True)
def uncheck_cli(uid):
    '''interfaccia cli per check'''
    if check(uid,False): print('uncheck',uid)
    else: print('uncheck error')

# definisce il comando: up uid
@cli.command('up')
@click.argument('uid', required=True)
def up_cli(uid):
    '''interfaccia cli per up'''
    if up(uid): print('up',uid)
    else: print('up error')

# definisce il comando: down uid
@cli.command('down')
@click.argument('uid', required=True)
def down_cli(uid):
    '''interfaccia cli per down'''
    if down(uid): print('down',uid)
    else: print('down error')

# definisce il comando: erase uid
@cli.command('erase')
@click.argument('uid', required=True)
def erase_cli(uid):
    '''interfaccia cli per erase'''
    if erase(uid): print('erase',uid)
    else: print('erase error')

# comando per lanciare l'applicazione web
# definito successivamente
@cli.command('web')
def web_cli():
    '''lancia l'applicazione web'''
    global run_web
    run_web = True

# chiama click se stiamo eseguendo come todo.py
if __name__ == '__main__':
    run_web = False
    cli(standalone_mode=False)

web_search = ''

template_html = '''
<!DOCTYPE html>
<htlm lang="it">
    <head>
        <title>todo.py</title>
        <meta charset="utf-8">
    </head>
    <body>
        <form action="/add" method="get">
        <p><input type="text" name="title" formaction="/add">Aggiungi</p>
        </form>
        <form action="/search" method="get">
        <p><input type="text" name="title" value="{web_search}">Cerca</p>
        </form>
        <form>
        {items}
        </form>
    </body>
</html>
'''

template_item = '''
<p>
    <input type="submit" value={checked} formaction="/{checkcmd}/{uid}">
    <input type="submit" value="U" formaction="/up/{uid}">
    <input type="submit" value="D" formaction="/down/{uid}">
    <input type="submit" value="X" formaction="/erase/{uid}">
    {title}
</p>
'''

def print_html():
    '''Ritorna la pagina HTML dell'applicazione'''
    lst = load()
    items = ''
    for line in lst:
        if (web_search and (web_search.lower() 
            not in line.lower().split())): continue
        _, checked, uid, title = line.split(maxsplit=3)
        if checked == '[x]': checkcmd = 'uncheck'
        else: checkcmd = 'check'
        items += template_item.format(uid=uid,
            title=title, checked=checked,
            checkcmd=checkcmd)
    return template_html.format(items=items,
        web_search=web_search)

import bottle

# comando add con titolo in request.query['title']
@bottle.route('/add')
def add_web():
    '''interfaccia web per add'''
    title = bottle.request.query.get('title')
    add(title)
    return print_html()

# setta la stringa di ricerca da request.query['title']
@bottle.route('/search')
def search_web():
    '''interfaccia web per settare il filtro
    di visualizzazione'''
    global web_search
    title = bottle.request.query.get('title')
    web_search = title
    return print_html()

# comando check uid
@bottle.route('/check/<uid>')
def check_web(uid):
    '''interfaccia web per check'''
    check(uid,True)
    return print_html()

# comando uncheck uid
@bottle.route('/uncheck/<uid>')
def uncheck_web(uid):
    '''interfaccia web per check'''
    check(uid,False)
    return print_html()

# comando up uid
@bottle.route('/up/<uid>')
def up_web(uid):
    '''interfaccia web per up'''
    up(uid)
    return print_html()

# comando down uid
@bottle.route('/down/<uid>')
def down_web(uid):
    '''interfaccia web per down'''
    down(uid)
    return print_html()

# comando erase uid
@bottle.route('/erase/<uid>')
def erase_web(uid):
    '''interfaccia web per erase'''
    erase(uid)
    return print_html()

# pagina dell'applicazione
@bottle.route('/')
def print_web():
    '''interfaccia web per print_html'''
    return print_html()

if __name__ == '__main__' and run_web:
    bottle.run(debug=True)

