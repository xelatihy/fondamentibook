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


from gwidget import run_app
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Dizionario dei colori
colors = { 'r': QColor(255,128,128), 
           'g': QColor(128,255,128),
           'b': QColor(128,128,255), 
           'c': QColor(128,255,255),
           'm': QColor(255,128,255), 
           'y': QColor(255,255,128), 
           'o': QColor(255,128,0) }
	
# Lista delle matrici delle forme dei pezzi 
pieces = [    
   [ ['c','c'], ['c',''], ['c',''] ],
   [ ['','r'], ['r','r'], ['r',''] ],
   [ ['o','o'], ['','o'], ['','o'] ],
   [ ['g',''], ['g','g'], ['','g'] ],
   [ ['b'], ['b'], ['b'], ['b'] ],
   [ ['m','m'], ['m','m'] ],
   [ ['y',''], ['y','y'], ['y',''] ]
]

# Dimensioni matrice di gioco
board_w, board_h = 22, 10      
# Matrice di gioco, inizializzata    
board = []                         
for _ in range(board_h):           
    board.append( ['']*board_w )               

# Forma del pezzo corrente
piece = pieces[0]             
# Larghezza e altezza del pezzo corrente     
piece_w = len(piece[0])            
piece_h = len(piece)               
# Posizione pezzo corrente
piece_x, piece_y = board_w//2, 0   
# Conteggio frames per la caduta del pezzo
frame_count = 0                    

# Dimensione in pixel di un blocchetto
block_size = 16             

def paint_blocks(painter, blocks, x, y, w, h):
    '''Disegna gli elementi della matrice blocks di
    dimensioni w, h, con l'angolo in alto a sinistra
    nel pixel di posizione x, y'''
    for j in range(h):
        for i in range(w):
            c = blocks[j][i]
            # Se non è una celletta vuota
            if not c: continue  
            painter.setBrush(colors[c])
            painter.drawRect(
                (i+x)*block_size, (j+y)*block_size, 
                block_size, block_size)

def update(key):
    '''Aggiorna lo stato del gioco tenendo conto 
    dell'eventuale tasto key'''
    # indica la funzione vuota
    pass 

def paint(painter):    
    '''Aggiorna un frame del gioco'''
    # Aggiorna lo stato del gioco
    update(painter.info.key) 
    # Ripulisce la variabile della tastiera   
    painter.info.key = ''       
    # Ripulisci la finestra
    painter.setBrush(QColor(128,128,128))   
    painter.drawRect(0, 0, 
        block_size*board_w, block_size*board_h)
    # Disegna i pezzi
    paint_blocks(painter, board, 0, 0, 
        board_w, board_h)
    # Disegna il pezzo corrente
    if piece:  
        paint_blocks(painter, piece, 
            piece_x, piece_y, piece_w, piece_h)

# Crea la GUI (la finestra) e chiama la funzione
# paint() ad ogni frame
run_app(paint, board_w*block_size, 
    board_h*block_size)

def move(key):
    '''Muovi (eventualmente) il pezzo corrente con
    tasto key, se possibile'''
    pass

def update(key):
    '''Aggiorna lo stato del gioco tenendo conto
    dell'eventuale tasto key'''
    # Se e' stato premuto un tasto,
    if key:      
        # gestisci il tasto premuto    
        move(key)    
    # aggiornamento caduta del pezzo corrente ...
    pass 

# Numero frames per caduta del pezzo
frames_droppiece = 30       
# Frame corrente
frame_count = 0             

def hit():
    '''Ritorna True se il pezzo corrente collide'''
    pass
    
def resolveboard():
    '''Aggiorna la matrice di gioco aggiungendo il
    pezzo corrente, che è arrivato, ed elimina le 
    eventuali righe piene.'''
    pass
    
def newpiece():
    '''Crea un nuovo pezzo'''
    pass
    
def start():
    '''Inizializza la matrice di gioco vuota e crea
    un nuovo pezzo'''
    pass

def update(key):
    '''Aggiorna lo stato del gioco tenendo conto 
    dell'eventuale tasto key'''
    if key:          
        move(key)    
    global piece_x, piece_y, frame_count
    # Incrementa il conteggio dei frames
    frame_count += 1               
    # fai cadere il pezzo solo se sono passati 
    # frames_droppiece frames
    if frame_count < frames_droppiece:
        return          
    # Muovi il pezzo corrente in basso               
    piece_y += 1        
    # Se adesso il pezzo collide,
    if hit():           
        # riportalo indietro e aggiorna il gioco
        piece_y -= 1    
        resolveboard()  
        # Crea un nuovo pezzo
        newpiece()
        # Se già collide, game over      
        if hit():       
            start()
    frame_count = 0

piece_x, piece_y = board_w//2, 0
run_app(paint, board_w*block_size, 
    board_h*block_size)

def hit():
    '''Ritorna True se il pezzo corrente collide'''
    # Collisione bordi verticali
    if not (0 <= piece_x <= board_w-piece_w):    
        return True
    # Collisione bordi orizzontali
    if not (0 <= piece_y <= board_h-piece_h):    
        return True
    # Controlla se collide coi pezzi già caduti
    for j in range(piece_h):    
        for i in range(piece_w):
            if (piece[j][i] and 
                board[j+piece_y][i+piece_x]):
                return True
    return False	    	    	    	    

def resolveboard():
    '''Aggiorna la matrice di gioco aggiungendo il
    pezzo corrente, che è arrivato, ed elimina le 
    eventuali righe piene.'''
    # Aggiungi il pezzo alla matrice di gioco
    for j in range(piece_h):    
        for i in range(piece_w):
            if piece[j][i]:
                pj, pi = j+piece_y, i+piece_x
                board[pj][pi] = piece[j][i]
    # Cerca se ci sono righe piene da eliminare      
    for j in range(board_h):
         # Se la riga j e' piena,    
        if all(board[j]):                
            # fai cadere le righe superiori
            for jj in range(j,0,-1):      
                for ii in range(board_w):
                    board[jj][ii] = board[jj-1][ii]
                # e vuota la prima riga
                for ii in range(board_w):     
                    board[0][ii] = ''

piece_x, piece_y = board_w//2, 0   
run_app(paint, board_w*block_size, 
    board_h*block_size)

from random import choice

def newpiece():
    '''Crea un nuovo pezzo'''
    global piece, piece_x, piece_y, piece_w, piece_h
    # Scegli in modo casuale il nuovo pezzo  
    piece = choice(pieces)             
    # Imposta la posizione iniziale del pezzo         
    piece_x, piece_y = board_w//2, 0   
    piece_w, piece_h = len(piece[0]), len(piece)
    
def start():
    '''Inizializza la matrice di gioco vuota e crea
    un nuovo pezzo'''
    for j in range(board_h):
        for i in range(board_w):
            board[j][i] = ''
    newpiece()

start()
run_app(paint, board_w*block_size, 
    board_h*block_size)

def rotater():
    '''Ruota a destra il pezzo corrente'''
    pass
    
def rotatel():
    '''Ruota a sinistra il pezzo corrente'''
    pass

def move(key):
    '''Muovi (eventualmente) il pezzo corrente con
    tasto key, se possibile'''
    global piece_x, piece_y
    # A sinistra
    if key == 'a':      
        piece_x -= 1
        if hit(): piece_x += 1
    # A destra
    elif key == 'd':    
        piece_x += 1
        if hit(): piece_x -= 1
    # In alto
    elif key == 'w':    
        piece_y -= 1
        if hit(): piece_y += 1
    # In basso
    elif key == 's':    
        piece_y += 1
        if hit(): piece_y -= 1
    # Rotazione a sinistra
    elif key == 'q':    
        rotatel()
        if hit(): rotater()
    # Rotazione a destra
    elif key == 'e':    
        rotater()
        if hit(): rotatel()
    # Caduta immediata
    elif key == ' ':    
        while not hit(): piece_y += 1
        piece_y -= 1
    # Inizia un nuovo gioco
    elif key == 'g':    
        start()

start()
run_app(paint, board_w*block_size, 
    board_h*block_size)

def rotater():
    '''Ruota a destra il pezzo corrente'''
    global piece, piece_w, piece_h
    # Crea e inizializza vuota la matrice
    newp = []                  
    # per il pezzo ruotato 
    for _ in range(piece_w):   
        newp.append( ['']*piece_h )
    # Riempi la matrice con i valori ruotati
    for j in range(piece_h):      
        for i in range(piece_w):  
            newp[i][j] = piece[piece_h-1-j][i]
    piece_w, piece_h = piece_h, piece_w
    piece = newp

def rotatel():
    '''Ruota a sinistra il pezzo corrente'''
    global piece, piece_w, piece_h
     # Crea e inizializza vuota la matrice 
    newp = []                 
    for _ in range(piece_w):  
        newp.append( ['']*piece_h )
    # Riempi la matrice con i valori ruotati
    for j in range(piece_h):      
        for i in range(piece_w):  
            newp[i][j] = piece[j][piece_w-1-i]
    piece_w, piece_h = piece_h, piece_w
    piece = newp

start()
run_app(paint, board_w*block_size, 
    board_h*block_size)

