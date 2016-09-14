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

def print_dir(dirpath):
    '''Stampa i percorsi di file e directory 
    contenute nella directory dirpath'''
    for name in os.listdir(dirpath):
        # per evitare file nascosti
        if name.startswith('.'): continue   
        print(os.path.join(dirpath, name))

print_dir('Informatica')
# Out: Informatica/Hardware
# Out: Informatica/Software

print_dir('Informatica/Hardware')
# Out: Informatica/Hardware/Cache.txt
# Out: Informatica/Hardware/CPU.txt
# Out: Informatica/Hardware/RAM.txt

print_dir('Informatica/Software')
# Out: Informatica/Software/Linguaggi
# Out: Informatica/Software/SistemiOperativi

def print_dir_tree(dirpath):
    '''Stampa i percorsi di tutti i file e directory
    contenuti, a qualsiasi livello, nella directory
    dirpath'''
    for name in os.listdir(dirpath):
        # per evitare file nascosti
        if name.startswith('.'): continue
        pathname = os.path.join(dirpath, name)
        print(pathname)
        # se e' una directory
        if os.path.isdir(pathname):    
            # chiama ricorsivamente la funzione
            print_dir_tree(pathname)   

print_dir_tree('Informatica')
# Out: Informatica/Hardware
# Out: Informatica/Hardware/Cache.txt
# Out: Informatica/Hardware/CPU.txt
# Out: Informatica/Hardware/RAM.txt
# Out: Informatica/Software
# Out: Informatica/Software/Linguaggi
# Out: Informatica/Software/Linguaggi/C.txt
# Out: Informatica/Software/Linguaggi/Java.txt
# Out: Informatica/Software/Linguaggi/JavaScript.txt
# Out: Informatica/Software/Linguaggi/Python.txt
# Out: Informatica/Software/SistemiOperativi
# Out: Informatica/Software/SistemiOperativi/Linux.txt
# Out: Informatica/Software/SistemiOperativi/MacOS.txt
# Out: Informatica/Software/SistemiOperativi/Windows.txt

def permute(seq):
    '''Ritorna la lista di tutte le permutazioni
    della sequenza seq'''
    if len(seq) <= 1:
        perms = [seq]
    else:
        perms = []
        for i in range(len(seq)):
            # genera ricorsivamente le permutazioni
            # degli elementi escluso l'i-esimo
            sub = permute(seq[:i]+seq[i+1:]) 
            for p in sub:     # mette in testa l'i-esimo elemento
                perms.append(seq[i:i+1]+p)
    return perms

print(permute([1,2,3]))
# Out: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

def permute_print(seq):
    '''Ritorna la lista di tutte le permutazioni
    della sequenza seq'''
    print('  '*(3-len(seq)),'chiamata',seq)
    if len(seq) <= 1:
        perms = [seq]
    else:
        perms = []
        for i in range(len(seq)):
            sub = permute_print(seq[:i]+seq[i+1:]) 
            for p in sub:
                perms.append(seq[i:i+1]+p)
    print('  '*(3-len(seq)),'ritorna',perms)
    return perms

permute_print([1,2,3])
# Out:  chiamata [1, 2, 3]
# Out:    chiamata [2, 3]
# Out:      chiamata [3]
# Out:      ritorna [[3]]
# Out:      chiamata [2]
# Out:      ritorna [[2]]
# Out:    ritorna [[2, 3], [3, 2]]
# Out:    chiamata [1, 3]
# Out:      chiamata [3]
# Out:      ritorna [[3]]
# Out:      chiamata [1]
# Out:      ritorna [[1]]
# Out:    ritorna [[1, 3], [3, 1]]
# Out:    chiamata [1, 2]
# Out:      chiamata [2]
# Out:      ritorna [[2]]
# Out:      chiamata [1]
# Out:      ritorna [[1]]
# Out:    ritorna [[1, 2], [2, 1]]
# Out:  ritorna [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# Out: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

def somma2(x):
    x += 2
    return x

class FSNode(object):
    def __init__(self, path):
        self.path = path
        self.content = [] # lista dei nodi figli
    def __str__(self):
        return 'FSNode("'+self.path+'")'

def gen_fstree(path):
    '''Genera l'albero partendo dal percorso path e
    ritorna il nodo radice'''
    node = FSNode(path)
    if os.path.isdir(path):
        for name in os.listdir(path):
            if name.startswith('.'): continue
            fullpath = os.path.join(path, name)
            node.content += [gen_fstree(fullpath)]
    return node

tree = gen_fstree('Informatica')
print(tree)
# Out: FSNode("Informatica")

def print_fstree(node, level):
    '''Stampa l'albero con radice node'''
    # os.path.basename ritorna l'ultima componente
    print('  '*level + os.path.basename(node.path))
    # stampa ricorsivamente i sottoalberi dei nodi figli
    for child in node.content:           
        print_fstree(child, level + 1)

print_fstree(tree, 0)
# Out: Informatica
# Out:   Hardware
# Out:     Cache.txt
# Out:     CPU.txt
# Out:     RAM.txt
# Out:   Software
# Out:     Linguaggi
# Out:       C.txt
# Out:       Java.txt
# Out:       JavaScript.txt
# Out:       Python.txt
# Out:     SistemiOperativi
# Out:       Linux.txt
# Out:       MacOS.txt
# Out:       Windows.txt

def count_fstree(node):
    '''Ritorna il numero di nodi dell'albero di
    radice root'''
    count = 1
    # per ogni nodo figlio, 
    for child in node.content:       
        # conta i nodi nel suo sottoalbero
        count += count_fstree(child)
    return count

print(count_fstree(tree))
# Out: 15

def count_fstree_print(node,level):
    '''Ritorna il numero di nodi dell'albero di
    radice root'''
    print('  '*level + os.path.basename(node.path))
    count = 1
    for child in node.content:
        count += count_fstree_print(child,level+1)
    print('  '*level,'->',count)
    return count

print(count_fstree_print(tree,0))
# Out: Informatica
# Out:   Hardware
# Out:     Cache.txt
# Out:      -> 1
# Out:     CPU.txt
# Out:      -> 1
# Out:     RAM.txt
# Out:      -> 1
# Out:    -> 4
# Out:   Software
# Out:     Linguaggi
# Out:       C.txt
# Out:        -> 1
# Out:       Java.txt
# Out:        -> 1
# Out:       JavaScript.txt
# Out:        -> 1
# Out:       Python.txt
# Out:        -> 1
# Out:      -> 5
# Out:     SistemiOperativi
# Out:       Linux.txt
# Out:        -> 1
# Out:       MacOS.txt
# Out:        -> 1
# Out:       Windows.txt
# Out:        -> 1
# Out:      -> 4
# Out:    -> 10
# Out:  -> 15
# Out: 15

def find_fstree(node, name):
    '''Ritorna una lista dei nodi dell'albero di 
    radice root con nome name'''
    ret = []
    if os.path.basename(node.path) == name:
        ret += [node]
    # per ogni nodo figlio, 
    for child in node.content:
        # cerca ricorsivamente nel suo sottoalbero
        ret += find_fstree(child, name) 
    return ret

print(find_fstree(tree, 'Python.txt')[0])
# Out: FSNode("Informatica/Software/Linguaggi/Python.txt")

