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


class _GraphNode:
    '''Rappresenta un nodo del grafo. 
    Da usarsi solo all'interno di Graph.'''
    
    def __init__(self,name,adj,pos):
        self.name = name
        self.adj = set(adj)
        self.pos = pos

class Graph:
    '''Rappresenta un grafo.'''
    
    def __init__(self,colors=["black","black"]):
        '''Inizializza un grafo vuoto.'''
        self._nodes = {}
        self._colors = list(colors)
    
    def addNode(self, name, pos):
        '''Aggiunge un nodo name, se non esiste'''
        if name in self._nodes: return
        self._nodes[name]=_GraphNode(name,set(),pos)
    
    def addEdge(self, name1, name2):
        '''Aggiunge un arco che collega i nodi 
        name1 e name2'''
        if name1 not in self._nodes: return 
        if name2 not in self._nodes: return
        self._nodes[name1].adj.add(name2)
        self._nodes[name2].adj.add(name1)
    
    def adjacents(self, name):
        '''Ritorna una lista dei nomi dei nodi 
        adiacenti al nodo name, se il nodo non
        esiste, ritorna None'''
        if name not in self._nodes: return None
        return list(self._nodes[name].adj)
    
    def nodes(self):
        '''Ritorna una lista dei nomi dei nodi'''
        return list(self._nodes.keys())
    
    def edges(self):
        '''Ritorna una lista degli archi'''
        edges = set()
        for name, node in self._nodes.items():
            for adj in node.adj:
                # salta archi ripetuti 
                if (adj, name) in edges: 
                    continue
                edges.add( (name,adj) )
        return list(edges)
    
    def pos(self, name):
        '''Ritorna la posizione del nodo name'''
        if name not in self._nodes: return None
        return self._nodes[name].pos
    
    def colors(self):
        return list(self._colors)
    
    def setColors(self,colors):
        self._colors = list(colors)

g = Graph()

# aggiunge i nodi
g.addNode('Sara',(125,75))
g.addNode('Ciro',(0,75))
g.addNode('Marco',(225,0))
g.addNode('Andrea',(225,125))

# aggiunge gli archi
g.addEdge('Ciro', 'Sara')
g.addEdge('Marco', 'Sara')
g.addEdge('Andrea', 'Sara')

# Interroga il grafo
print(g.nodes())
# Out: ['Marco', 'Sara', 'Ciro', 'Andrea']
print(g.adjacents('Sara'))
# Out: ['Marco', 'Ciro', 'Andrea']

def size_graphs(graphs):
    '''Trova la dimensione di una lista di grafi'''
    w, h = 0, 0
    for g in graphs:
        for node in g.nodes():
            p = g.pos(node)
            if w < p[0]: w = p[0]
            if h < p[1]: h = p[1]
    return w, h

def dump_graph(g):
    '''Crea il codice SVG per il grafo g.'''   
    # formati
    circle_fmt = '<circle r="3" cx="{}" cy="{}" fill="{}"/>\n'
    line_fmt = '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="{}" stroke-width="2"/>\n'
    svg = ''
    node_color, edge_color = g.colors()
    if node_color:
        for name in g.nodes():
            pos = g.pos(name)
            svg += circle_fmt.format(pos[0], pos[1],
                g.colors()[0])
    if edge_color:
        for name1, name2 in g.edges():
            pos1 = g.pos(name1)
            pos2 = g.pos(name2)
            svg += line_fmt.format(pos1[0], pos1[1],
                pos2[0], pos2[1], g.colors()[1])
    return svg

def dump_graphs(graphs):
    '''Crea un'immagine SVG per i grafi graphs.'''
    # trova la dimensione del grafo
    w, h = size_graphs(graphs)
    # formati
    svg_fmt ='<svg xmlns="{}" width="{}" height="{}">\n'
    group_fmt = '<g transform="translate(5,5)">\n'
    # svg namespace 
    ns = "http://www.w3.org/2000/svg"
    svg = svg_fmt.format(ns, w+10, h+10)
    svg += group_fmt
    for g in graphs:
        svg += dump_graph(g)
    svg += '</g>\n'
    svg += '</svg>\n'
    return svg

def save_graphs(filename,graphs):
    '''Salva i grafi in SVG sul file filename'''
    with open(filename,'w') as f:
        f.write(dump_graphs(graphs))

print(dump_graphs([g]))
# Out: <svg xmlns="http://www.w3.org/2000/svg" width="235" height="135">
# Out: <g transform="translate(5,5)">
# Out: <circle r="3" cx="225" cy="0" fill="black"/>
# Out: <circle r="3" cx="125" cy="75" fill="black"/>
# Out: <circle r="3" cx="0" cy="75" fill="black"/>
# Out: <circle r="3" cx="225" cy="125" fill="black"/>
# Out: <line x1="125" y1="75" x2="225" y2="125" stroke="black" stroke-width="2"/>
# Out: <line x1="225" y1="0" x2="125" y2="75" stroke="black" stroke-width="2"/>
# Out: <line x1="125" y1="75" x2="0" y2="75" stroke="black" stroke-width="2"/>
# Out: </g>
# Out: </svg>
# Out: 

save_graphs('img_graph00.svg',[g])

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from gwidget import run_app

# grafo usato implicitamente da paint_graph
_paint_graphs = None

# variabile globale per disattivare il 
# disegno interattivo
skipui = True

def paint_graph(painter,g):
    '''Disegna un grafo con la libreria Qt.'''
    node_color, edge_color = g.colors()
    if node_color:
        painter.setPen(QColor(node_color))
        painter.setBrush(QColor(node_color))
        for name in g.nodes():                                                     
            pos = g.pos(name)
            painter.drawEllipse(
                QPoint(pos[0], pos[1]), 3, 3)
    if edge_color:
        painter.setPen(QColor(edge_color))
        painter.setBrush(QColor(edge_color))
        for name1, name2 in g.edges():
            pos1 = g.pos(name1)
            pos2 = g.pos(name2)
            painter.drawLine(
                QPoint(pos1[0], pos1[1]),
                QPoint(pos2[0], pos2[1]))

def paint_graphs(painter):
    '''Disegna una lista di grafi con la libreria
    Qt. I grafi sono memorizzati nella variabile
    globale _paint_graphs.'''
    size = painter.info.size
    painter.fillRect(0, 0, size[0], size[1],
        QColor(255,255,255))
    for g in _paint_graphs:
        paint_graph(painter,g)

def view_graphs(graphs):
    '''Visualizza i grafi graphs'''
    # velocizza l'esecuzione saltando la ui
    if skipui: return 
    global _paint_graphs
    _paint_graphs = graphs
    w, h = size_graphs(graphs)
    run_app(paint_graphs,w,h)
    _paint_graphs = None

view_graphs([g])

labyrinth = '''
+-+-+-+-+-+-+-+-+-+-+-+-+
|               |       |
+ +-+-+-+-+-+ + + +-+-+ +
|   |   |     |   |   | |
+-+ + +-+ +-+-+-+-+ + + +
|   |   |   |   |   | | |
+ +-+-+ +-+ +-+ + +-+ + +
|     |   |   | | | |   |
+-+-+ +-+ +-+ + + + +-+-+
|           | | |   |   |
+ +-+-+-+-+-+ + +-+ +-+ +
|   |     |   |   |     |
+-+ + +-+ + +-+ +-+-+-+ +
|   |   |   |           |
+-+-+-+-+-+-+-+-+-+-+-+-+
'''

def parse_labyrinth(text):
    '''Creare il grafo dei corridoi e il grafo dei
    muri a partire da un labirinto testulae.'''
    # lista delle linee del testo
    lines = text.strip().splitlines()       
    # Dimensioni del labirinto
    w, h = len(lines[0]), len(lines)        
    # grafo di corridoi e muri
    corridors = Graph(['red','red'])        
    walls = Graph(['','black'])
    # aggiunta dei nodi
    for j in range(h):                      
        for i in range(w):
            # calcola la posizione
            pos = (i*12, j*+12)       
            # aggiungi il nodo ai corridoi o muri
            if lines[j][i] == ' ':          
                corridors.addNode( (i,j), pos ) 
            else:
                walls.addNode( (i,j), pos )
    # aggiunta degli archi
    for j in range(h):                      
        for i in range(w):
            # itera sui possibili vicini
            adj = [(-1,0),(1,0),(0,-1),(0,1)]   
            for di, dj in adj:                  
                # coordinate vicino
                ii, jj = i + di, j + dj         
                if ii < 0 or jj < 0: continue
                if ii >= w or jj >= h: continue
                # verifica se entrambi sono corridoi
                if (lines[j][i] ==  ' ' and 
                    lines[jj][ii] == ' '):
                    corridors.addEdge((i,j),(ii,jj))
                # verifica se entrambi sono muri
                elif (lines[j][i] !=  ' ' and 
                      lines[jj][ii] != ' '):
                    walls.addEdge((i,j),(ii,jj))
    return corridors, walls

corridors, walls = parse_labyrinth(labyrinth)
view_graphs([corridors, walls])
save_graphs('img_graph01.svg',[corridors, walls])

def visit(g, name):
    '''Visita (tramite BFS) il grafo g a partire dal
    nodo name e ritorna l'insieme dei nomi dei nodi
    visitati'''
    # Inizializza l'insieme dei visitati
    visited = set([name])     
    # Inizializza l'insieme degli attivi
    active = set([name])      
    # Finchè ci sono nodi attivi,
    while active:             
        # Insieme dei nuovi attivi
        newactive = set()       
        # Finchè ci sono nodi attivi,
        while active:           
            # estrai un nodo da active 
            u = active.pop()             
            # e per ogni suo vicino,     
            for v in g.adjacents(u):     
                # se non è già visitato,
                if v not in visited:     
                    # aggiungilo ai visitati
                    visited.add(v)       
                    # e ai nuovi attivi
                    newactive.add(v)
        # I nuovi attivi diventano gli attivi     
        active = newactive      
    return visited

visited = visit(corridors, (1,1))
print(len(corridors.nodes()),len(visited))
# Out: 167 167
# Il labirinto è connesso a (1,1).

def make_node_graph(g, names, colors):
    '''Crea un grafo con i nodi in names e le
    posizioni in g'''
    ng = Graph(colors)
    for name in names:
         ng.addNode(name,g.pos(name))
    return ng

def visit_traced(g, name):
    '''Visita (tramite BFS) il grafo g a partire dal
    nodo name e ritorna l'insieme dei nomi dei nodi
    visitati. Traccia l'esecuzione con una lista di
    grafi.'''
    visited = set([name])     
    active = set([name])     
    # Traccia di eseguzione 
    trace = []                
    while active:             
        # Aggiorna la traccia
        trace += [ (          
            make_node_graph(g,visited,['blue','']), 
            make_node_graph(g,active,['yellow','']), 
        ) ]
        newactive = set()      
        while active:          
            u = active.pop()      
            for v in g.adjacents(u):
                if v not in visited:
                    visited.add(v)
                    newactive.add(v)
        active = newactive
    return visited, trace

visited, trace = visit_traced(corridors, (1,1))

# visualizziamo le iterazioni
for i in range(len(trace)):
    t = trace[i]
    save_graphs('img_graph01/v{:02}.svg'.format(i),
        [corridors, walls] + list(t)) 

_animated_graphs = None
_frame = 0
_frame_toswitch = 15

def paint_animated_graphs(painter):
    '''Disegna una lista di grafi con la libreria
    Qt. I grafi sono memorizzati nella variabile 
    globale _paint_graphs. I grafi da animare sono
    contenuti in _animated_graphs.'''
    size = painter.info.size
    painter.fillRect(0, 0, size[0], size[1],
        QColor(255,255,255))
    for g in _paint_graphs:
        paint_graph(painter,g)
    global _frame
    _frame += 1
    animateid = ((_frame // _frame_toswitch) % 
        len(_animated_graphs))
    for g in _animated_graphs[animateid]:
        paint_graph(painter,g)

def view_animated_graphs(graphs, animated):
    '''Visualizza i grafi graphs e i grafi animati
    animated_graphs'''
    if skipui: return 
    global _paint_graphs, _animated_graphs
    _paint_graphs = graphs
    _animated_graphs = animated
    w, h = size_graphs(graphs)
    run_app(paint_animated_graphs,w,h)
    _paint_graphs = None
    _animated_graph = None

view_animated_graphs([corridors, walls],trace)

labyrinth1 = '''
+-+-+-+-+-+-+-+-+-+-+-+-+
|                       |
+                 +-+-+ +
|             |   |   | |
+-+ + +-+     +-+-+ + + +
|   |   |       |       |
+   +-+     +-+     +-+-+
|     |     | |     |   |
+     |     | |         +
|     |     | |     |   |
+     |     | |     +-+ +
|   |     |             |
+-+ + +-+ +-+-+         +
|   |                   |
+-+-+-+-+-+-+-+-+-+-+-+-+
'''

corridors1, walls1 = parse_labyrinth(labyrinth1)
save_graphs('img_graph02.svg',[corridors1, walls1])
view_graphs([corridors1, walls1])

visited, trace = visit_traced(corridors1, (1,1))

# visualizziamo alcuni step
for i in range(len(trace)):
    t = trace[i]
    save_graphs('img_graph02/v{:02}.svg'.format(i),
        [corridors1, walls1] + list(t))  
    view_graphs([corridors1, walls1] + list(t))     

# visualizziamo l'animazione
view_animated_graphs([corridors1, walls1],trace)

labyrinth2 = '''
+-+-+-+-+-+-+-+-+-+-+-+-+
|               |       |
+ +-+-+-+-+-+ + + +-+-+ +
|   |   |     |   |   | |
+-+ + +-+ +-+-+-+-+-+ + +
|   |   |   |   |   | | |
+ +-+-+ +-+ +-+ + +-+ + +
|     |   |   | | | |   |
+-+-+ +-+ +-+ + + + +-+-+
|           | | |   |   |
+ +-+-+-+-+-+-+ +-+ +-+ +
|   |     |   |   |     |
+-+ + +-+ + +-+ +-+-+-+ +
|   |   |   |           |
+-+-+-+-+-+-+-+-+-+-+-+-+
'''

corridors2, walls2 = parse_labyrinth(labyrinth2)
view_graphs([corridors2, walls2])
save_graphs('img_graph03.svg',[corridors2, walls2])

visited2 = visit(corridors2, (1,1))
print(len(corridors2.nodes()),len(visited2))
# Out: 165 103

def subgraph(g, names):
    '''Ritorna il sottografo di g relativo ai nodi 
    in names'''
    subg = Graph(g.colors())
    for name in names:
        pos = g.pos(name)
        subg.addNode(name, pos)
    for name in names:
        for a in g.adjacents(name):
            if a in names:
                subg.addEdge(name, a)
    return subg

sub_corridors2 = subgraph(corridors2,visited2)
view_graphs([sub_corridors2, walls2])
save_graphs('img_graph04.svg',
    [sub_corridors2, walls2])

def subcomponents(g):
    '''Ritorna le component connesse di g'''
    
    # lista delle componenti connesse
    components = []         
    # sottografo rimasto, all'inizio g
    todo = g                
    # finchè il grafo non è vuoto
    while todo.nodes():     
        # sceglie un nodo a caso
        startnode = todo.nodes()[0] 
        # visita il grafo
        visited = visit(todo,startnode)    
        # estrae la component connessa
        component = subgraph(todo,visited) 
        # e la aggiunge alla lista
        components += [component]          
        # nodi rimanenti
        reminders = set(todo.nodes()) - set(visited)
        # aggiorna il sottografo
        todo = subgraph(todo,reminders)            
    
    # setta i colori da una lista di colori
    colors = ['red', 'green', 'blue', 'orange',
        'yellow', 'magenta', 'purple', 'cyan']
    for i, component in enumerate(components):
        color = colors[i % len(colors)]
        # setta i colori
        component._colors = [color,color]
    return components

components2 = subcomponents(corridors2)
view_graphs(components2 + [walls2])
save_graphs('img_graph05.svg',
    components2 + [walls2])

def distance(g, name):
    '''Ritorna un dizionario che ad ogni nodo
    visitato a partire dal nodo name associa la
    distanza da tale nodo'''
    visited = set([name])
    active = set([name]) 
    # Dizionario delle distanze
    dist = {name:0}           
    while active:
        newactive = set() 
        while active: 
            u = active.pop()      
            for v in g.adjacents(u):
                if v not in visited: 
                    visited.add(v) 
                    newactive.add(v)
                    # Distanza del nodo visitato
                    dist[v] = dist[u] + 1  
        active = newactive      
    return dist

distances = distance(corridors,(1,1))
print(distances[(23,13)])
# Out: 58

distances1 = distance(corridors1,(1,1))
print(distances1[(23,13)])
# Out: 34

distances2 = distance(corridors2,(1,1))
print(distances2[(1,13)])
# Out: 28

# non raggiungibile
distances2 = distance(corridors2,(1,1))
print((23,13) in distances2)
# Out: False

def visit_tree(g, name):
    '''Ritorna l'albero di visita tramite un 
    dizionario che ad ogni nodo visitato, a partire
    dal nodo name, associa il nome del nodo che lo
    ha scoperto, cioè il nodo genitore.'''
    visited = set([name])
    active = set([name]) 
    # Albero di visita
    tree = {name:None}         
    while active:
        newactive = set() 
        while active: 
            u = active.pop()      
            for v in g.adjacents(u):
                if v not in visited: 
                    visited.add(v) 
                    newactive.add(v)
                    # Associa al nodo v al genitore
                    tree[v] = u    
        active = newactive      
    return tree

def tree_to_graph(g,tree,colors=['blue','blue']):
    '''Converte un albero di visita in grafo.'''
    sg = Graph(colors)
    for node in tree:
        sg.addNode(node,g.pos(node))
    for node, parent in tree.items():
        if parent:
            sg.addEdge(node,parent)
    return sg

tree = visit_tree(corridors,(1,1))
save_graphs('img_graph06_0.svg',
    [walls,tree_to_graph(corridors,tree)])
view_graphs([walls,
    tree_to_graph(corridors,tree)])

tree1 = visit_tree(corridors1,(1,1))
save_graphs('img_graph06_1.svg',
    [walls1,tree_to_graph(corridors1,tree1)])
view_graphs([walls1,
    tree_to_graph(corridors1,tree1)])

tree2 = visit_tree(corridors2,(1,1))
save_graphs('img_graph06_2.svg',
    [walls2,tree_to_graph(corridors2,tree2)])
view_graphs([walls2,
    tree_to_graph(corridors2,tree2)])

def visit_path(tree, name):
    '''Ritorna una lista contenente il cammino dalla
    radice al nodo name dell'albero tree
    rappresentato come dizionario dei genitori'''
    root = None
    # Cerca la radice dell'albero
    for u, gen in tree.items():    
        if gen == None:
            root = u
            break
    # Se è presente nell'albero
    if name in tree:      
        # Costruisce il cammino risalendo
        path = [name]            
        # l'albero dal nodo name fino
        while name != root:      
            # alla radice
            name = tree[name]    
            path.insert(0, name)
        return path
    else:
        return []

def path_to_graph(g,path,colors=['blue','blue']):
    '''Converte un percorso in un grafo.'''
    sg = Graph(colors)
    for node in path:
        sg.addNode(node,g.pos(node))
    for i in range(len(path)-1):
        sg.addEdge(path[i],path[i+1])
    return sg

path = visit_path(tree,(23,13))
save_graphs('img_graph07_0.svg',
    [walls, path_to_graph(corridors, path)])
view_graphs([walls,
    tree_to_graph(corridors, tree)])

path1 = visit_path(tree1,(23,13))
save_graphs('img_graph07_1.svg',
    [walls1, path_to_graph(corridors1, path1)])
view_graphs([walls1,
    path_to_graph(corridors1, path1)])

path2 = visit_path(tree2,(1,13))
save_graphs('img_graph07_2.svg',
    [walls2, path_to_graph(corridors2, path2)])
view_graphs([walls2,
    path_to_graph(corridors2, path2)])

def make_grid_graph(w,h):
    '''Crea un grafo fatto a griglia con tutti i
    nodi connessi'''
    g = Graph()
    for j in range(h):
        for i in range(w):
            g.addNode((i,j),(i*20+10,j*20+10))
    adj = [(-1,0),(1,0),(0,-1),(0,1)]
    for i, j in g.nodes():
        for di, dj in adj:
            ii, jj = i + di, j + dj
            if ii < 0 or jj < 0: continue
            if ii >= w or jj >= h: continue
            g.addEdge( (i,j), (ii,jj) )
    return g

import random

def make_labyrith(g,name,seed=0):
    '''Crea un labirinto a partire da un grafo
    rimuovendo archi non voluti'''
    # Inizializza un grafo con i nodi di g
    labyrinth = Graph()    
    for node in g.nodes():
        labyrinth.addNode(node,g.pos(node))
    # Inizia la visita di g
    visited = set([name])             
    # Mantiene una lista di celle adiacenti
    active_adj = g.adjacents(name)    
    random.seed(seed)
    while active_adj:             
        newactive = set()
        # ordine di visita casuale
        random.shuffle(active_adj)          
        while active_adj:           
            u = active_adj.pop()
            adj = g.adjacents(u)
            # ordine di visita casuale
            random.shuffle(adj)    
            # aggiungi u se v è visitato   
            for v in adj:                
                if v in visited:       
                    visited.add(u)
                    labyrinth.addEdge(u,v)
                    break
            # aggiungi tutte gli altri ai candidati
            for v in adj:            
                if v not in visited:
                    newactive.add(v)
        active_adj = list(newactive)      
    return labyrinth

labyrinthr = make_labyrith(make_grid_graph(12,7),
    (0,0), seed=1)
save_graphs('img_graph08_0.svg',[labyrinthr])
view_graphs([labyrinthr])

def labyrith_to_text(g,w,h):
    '''Converte un grafo di corridoi in testo'''
    txt = '+-' * w + '+\n'
    for j in range(h):
        txt += '| '
        for i in range(1,w):
            if (i-1,j) in g.adjacents((i,j)):
                txt += '  '
            else:
                txt += '| '
        txt += '|\n'
        if j >= h-1: continue
        txt += '+'
        for i in range(w):
            if (i,j+1) in g.adjacents((i,j)):
                txt += ' +'
            else:
                txt += '-+'
        txt += '\n'
    txt += '+-' * w + '+\n'
    return txt     

labyrinthr_text = labyrith_to_text(labyrinthr,12,7)
print(labyrinthr_text)
# Out: +-+-+-+-+-+-+-+-+-+-+-+-+
# Out: |                       |
# Out: + + +-+ +-+ +-+ +-+ +-+-+
# Out: | |   |   |   |   |     |
# Out: + + + + + +-+ +-+ + +-+-+
# Out: | | | | |   |   | |     |
# Out: + + +-+ + +-+-+-+ +-+-+-+
# Out: | |   | |       |       |
# Out: + + + + +-+ + + +-+ +-+ +
# Out: | | | |   | | |   |   | |
# Out: + + + +-+ +-+ + + +-+ + +
# Out: | | |   |   | | |   | | |
# Out: + +-+-+-+ + + + + + +-+-+
# Out: |       | | | | | |     |
# Out: +-+-+-+-+-+-+-+-+-+-+-+-+
# Out: 

corridorsr, wallsr  = parse_labyrinth(labyrinthr_text)
treer = visit_tree(corridorsr,(1,1))
pathr = visit_path(treer,(23,13))
save_graphs('img_graph08_1.svg',
    [wallsr, path_to_graph(corridorsr, pathr)])
view_graphs([wallsr,
    tree_to_graph(corridorsr, treer)])

def similar_pixels(img,i,j,ii,jj,threshold):
    '''Verifica se la differenza in colore tra due
    pixel è inferiore a threshold'''
    w, h = len(img[0]), len(img)
    # verifica se i nodi sono nell'immagine
    if i < 0 or j < 0 or i >= w or j >= h:
            return False
    if ii < 0 or jj < 0 or ii >= w or jj >= h:
            return False
    # calcola la differenza dei colori
    c1 = img[j][i]      
    c2 = img[jj][ii]
    diff = (abs(c1[0]-c2[0]) + 
            abs(c1[1]-c2[1]) + 
            abs(c1[2]-c2[2])) // 3
    return diff <= threshold

def image_to_graph(img,threshold):
    '''Converte un'immagine in un grafo dove i nodi
    sono i pixel dell'immagine e due nodi sono
    adiacenti nel grafo se sono adiacenti 
    nell'immagine e la differenza dei colori è 
    inferiore a threshold.'''
    g = Graph()
    w, h = len(img[0]), len(img)
    # aggiunge i nodi
    for j in range(h):              
        for i in range(w):
            g.addNode((i,j),(i,j))
    # aggiunge gli archi
    for j in range(h):              
        for i in range(w):
            # itera sui vicini
            adj = [(-1,0),(1,0),(0,-1),(0,1)]
            for di, dj in adj:
                ii, jj = i + di, j + dj
                # se i colori sono simili,
                if similar_pixels(img, i, j, 
                    ii, jj, threshold):
                    # aggiungi un arco
                    g.addEdge( (i,j), (ii,jj) )
    return g

def draw_path(img,path,color=(255,0,0)):
    '''Scrive i pixel in path nell'immagine img con
    colore color.'''
    for i, j in path:
        img[j][i] = color

# funzioni dal capitolo sulle immagini
from image import load, save  

def compute_path(infilename, outfilename, start,
    end, threshold=10):
    '''Altera l'immagine nel file infilename
    colorando il percorso da start a end e 
    salvandola nel file outfilename. Usa le 
    funzioni load() e save() dal capitolo sulle
    immagini.'''
    img = load(infilename)
    g = image_to_graph(img,threshold)
    tree = visit_tree(g,start)
    path = visit_path(tree,end)
    draw_path(img,path)
    save(outfilename,img)

compute_path('in_maze00.png', 'img_maze00_0.png',
    (215,420), (215,251))

def visit_tree_image(img, start, end, threshold=10):
    '''Adatta la funzione visit_tree() al grafo 
    implicito di un'immagine.'''
    visited = set([start])
    active = set([start]) 
    tree = {start:None}
    while active:
        newactive = set() 
        while active: 
            # esce se ha già visitato end
            if end in visited: return tree    
            i, j = active.pop()
            # itera sui vicini 
            adj = [(-1,0),(1,0),(0,-1),(0,1)]      
            for di, dj in adj:
                ii, jj = i + di, j + dj
                # se non sono connessi, continua
                if not similar_pixels(img, i, j, 
                    ii, jj, threshold): continue
                if (ii,jj) not in visited: 
                    visited.add( (ii,jj) ) 
                    newactive.add( (ii,jj) )
                    tree[(ii,jj)] = (i,j)
        active = newactive  
    return tree

def compute_path_image(infilename, outfilename,
                       start, end, threshold=10):
    '''Altera l'immagine nel file infilename 
    colorando il percorso da start a end e 
    salvandola nel file outfilename. 
    Usa un grafo implicito.'''
    img = load(infilename)
    tree = visit_tree_image(img,start,end,threshold)
    path = visit_path(tree,end)
    draw_path(img,path)
    save(outfilename,img)

compute_path_image('in_maze00.png', 
    'img_maze00_1.png', (215,420), (215,251))

compute_path_image('in_maze01.png',
    'img_maze01_1.png', (270,290), (245,265))

compute_path_image('in_maze02.png',
    'img_maze02_1.png', (130,160), (674,588),25)

