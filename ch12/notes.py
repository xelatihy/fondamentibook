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


bianco = (255,255,255)
nero = (0,0,0)
arancio = (255,128,0)
print(arancio)
# Out: (255, 128, 0)
r, g, b = arancio
print(r, g, b)
# Out: 255 128 0

colori = [(255,0,0),(0,255,0),(0,0,255)]

# colore è una tupla
for colore in colori:
    print(colore)       
# Out: (255, 0, 0)
# Out: (0, 255, 0)
# Out: (0, 0, 255)

# unpacking delle tuple esplicito
for r, g, b in colori:           
    r, g, b = colore
    print(r, g, b)
# Out: 0 0 255
# Out: 0 0 255
# Out: 0 0 255

# unpacking delle tuple implicito
for r, g, b in colori:           
    print(r, g, b)
# Out: 255 0 0
# Out: 0 255 0
# Out: 0 0 255

img = [ 
    [ (255,0,0), (  0,255,0) ], 
    [ (0,0,255), (255,128,0) ] 
]
print(img)
# Out: [[(255, 0, 0), (0, 255, 0)], [(0, 0, 255), (255, 128, 0)]]

# prima riga (riga 0)
print(img[0])      
# Out: [(255, 0, 0), (0, 255, 0)]
# seconda riga (riga 1)
print(img[1])      
# Out: [(0, 0, 255), (255, 128, 0)]

# secondo elemento, prima riga (riga 0, colonna 1)
print(img[0][1])   
# Out: (0, 255, 0)
# primo elemento, seconda riga (riga 1, colonna 0)
print(img[1][0])   
# Out: (0, 0, 255)

def width(img):
    '''Ritorna la larghezza dell'immagine img.'''
    return len(img[0])

def height(img):
    '''Ritorna l'altezza dell'immagine img.'''
    return len(img)

w, h = width(img), height(img)
print(w, h)
# Out: 2 2

# iteriamo sulle righe
for riga in img:
    # iteriamo sulle colonne
    for colore in riga:
        print(colore)
# Out: (255, 0, 0)
# Out: (0, 255, 0)
# Out: (0, 0, 255)
# Out: (255, 128, 0)

import png

def save(filename, img):
    '''Salva un'immagine in formato PNG.'''
    pyimg = png.from_array(img, 'RGB')
    pyimg.save(filename)

save('img_small.png', img)

def create(iw, ih, c=(0,0,0)):
    '''Crea e ritorna un'immagine di larghezza iw, 
    altezza ih e riempita con il colore c'''
    
    # L'immagine inizialmente vuota
    img = []
    # Per ogni riga,                
    for _ in range(ih):
         # inizializza la riga vuota     
        row = []
        # e per ogni pixel della riga,
        for _ in range(iw):
            # aggiunge un pixel di colore c. 
            row.append(c)   
        # Aggiunge la riga all'immagine
        img.append(row)     
    return img

img = create(256, 128)
save('img_create.png', img)

def draw_quad_simple(img, x, y, w, h, c):
    '''Disegna su img un rettangolo con lo spigolo in
    alto a sinistra in (x, y), larghezza w, altezza h
    e di colore c. Va in errore se il rettangolo
    fuoriesce dall'immagine.'''
    
    # Per ogni riga j del rettangolo,
    for j in range(y, y+h):      
        # per ogni colonna i della riga j,
        for i in range(x, x+w):  
            # imposta il colore del pixel a c
            img[j][i] = c        

img = create(256,128)
draw_quad_simple(img, 16, 16, 224, 96, arancio)
save('img_quad_simple.png', img)

# Begin error-generating code --- using try/expect
try:
    draw_quad_simple(img, 16, 16, 512, 512, arancio)
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error:   File "<input>", line 12, in draw_quad_simple
    # Error: IndexError: list assignment index out of range
except:
    pass
# End error-generating code

def inside(img, i, j):
    '''Ritorna True se il pixel (i, j) è dentro 
    l'immagine img, False altrimenti'''
    iw, ih = width(img), height(img)
    return 0 <= i < iw and 0 <= j < ih

def draw_quad(img, x, y, w, h, c):
    '''Disegna su img un rettangolo con lo spigolo
    in alto a sinistra in (x, y), larghezza w, 
    altezza h e di colore c.'''
    for j in range(y,y+h):
        for i in range(x,x+w):
            # Disegna il pixel solo se è dentro
            if inside(img,i,j):   
                img[j][i] = c

img = create(256, 128)
draw_quad(img, 16, 16, 512, 512, arancio)
save('img_quad.png',img)

def draw_checkers(img, s, c0, c1):
    '''Disegna su img una scacchiera di quadratini,
    ognuno di lato s, coi colori c0 e c1'''
    # Per ogni indice di riga,
    for jj in range(height(img)//s):    
        # per ogni indice di colonna    
        for ii in range(width(img)//s): 
            # seleziona il colore
            if (ii + jj) % 2: c = c1     
            else: c = c0
            # e disegna il quadratino
            draw_quad(img,ii*s,jj*s,s,s,c)  

img = create(256, 128)
draw_checkers(img, 32, (0,0,0), (255,255,255))
# Begin error-generating code --- using try/expect
try:
    save('img_checkers.png',img)
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error:   File "<input>", line 4, in save
    # Error:   File "/Users/fabio/Documents/Work/books/fondamentibook/ch12/png.py", line 1279, in save
    # Error:     w.write(file, self.rows)
    # Error:   File "/Users/fabio/Documents/Work/books/fondamentibook/ch12/png.py", line 620, in write
    # Error:     nrows = self.write_passes(outfile, rows)
    # Error:   File "/Users/fabio/Documents/Work/books/fondamentibook/ch12/png.py", line 778, in write_passes
    # Error:     extend(row)
    # Error: KeyboardInterrupt
except:
    pass
# End error-generating code

def draw_gradienth(img, c0, c1):
    '''Disegna su img un gradiente di colore da
    sinistra a destra, dal colore c0 al colore c1'''
    r0, g0, b0 = c0
    r1, g1, b1 = c1
    for j in range(height(img)):
        for i in range(width(img)):
            # float da 0 a 1
            u = i / width(img)             
            # Interpola i canali
            r = round(r0 * (1-u) + r1 * u) 
            g = round(g0 * (1-u) + g1 * u)
            b = round(b0 * (1-u) + b1 * u)
            img[j][i] = (r,g,b)

img = create(256, 128)
draw_gradienth(img, (255,0,0), (0,255,0))
save('img_gradienth.png',img)

def draw_gradientv(img, c0, c1):
    '''Disegna su img un gradiente di colore dall'
    alto in basso, dal colore c0 al colore c1'''
    r0, g0, b0 = c0
    r1, g1, b1 = c1
    for j in range(height(img)):
        for i in range(width(img)):
            v = j / height(img)
            r = round(r0 * (1-v) + r1 * v)
            g = round(g0 * (1-v) + g1 * v)
            b = round(b0 * (1-v) + b1 * v)
            img[j][i] = (r,g,b)

img = create(256, 128)
draw_gradientv(img, (255,0,0), (0,255,0))
save('img_gradientv.png',img)

def draw_gradient_quad(img, c00, c01, c10, c11):
    '''Disegna un gradiente di colore combinato
    orizzontale e verticale con c00 in alto a 
    sinistra, c01 in basso a sinistra, c10 in 
    alto a destra e c11 in basso a destra'''
    for j in range(height(img)):
        for i in range(width(img)):
            u = i / width(img)
            v = j / height(img)
            c = [0,0,0]
            for k in range(3):
                c[k] = round(c00[k]*(1-u)*(1-v) +
                             c01[k]*(1-u)*v +
                             c10[k]*u*(1-v) +
                             c11[k]*u*v)
            img[j][i] = tuple(c)

img = create(256, 128)
# Begin error-generating code --- using try/expect
try:
    draw_gradient_quad(img, (255,0,0), (0,255,0), 
                            (0,0,255), (255,255,255))
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 2, in <module>
    # Error:   File "<input>", line 15, in draw_gradient_quad
    # Error: KeyboardInterrupt
except:
    pass
# End error-generating code
save('img_gradientq.png',img)

def load(filename):
    '''Carica l'immagine in formato PNG dal file 
    filename, la converte nel formato a matrice 
    di tuple e la ritorna'''
    with open(filename,'rb') as f:
        # legge l'immagine come RGB a 256 valori
        r = png.Reader(file=f)
        iw, ih, png_img, _ = r.asRGB8()
        # converte in lista di liste di tuple
        img = []
        for png_row in png_img:
            row = []
            # l'immagine PNG ha i colori in 
            # un'unico array quindi li leggiamo 
            # tre alla volta in una tupla
            for i in range(0,len(png_row),3):
                row.append( ( png_row[i+0], 
                              png_row[i+1],
                              png_row[i+2] ) )
            img.append( row )
    return img

img = load('photo.png')
save('img_photo.png',img)

def copy(dst, src, dx, dy, sx, sy, w, h):
    '''Copia la porzione rettangolare dell'immagine
    src con spigolo in alto a sinistra in (sx, sy)
    e dimensioni w, h sull'immagine dst a partire 
    da (dx, dy)'''
    for j in range(h):
        for i in range(w):
            di, dj = i+dx, j+dy
            si, sj = i+sx, j+sy
            if (inside(dst, di, dj) and 
                  inside(src, si, sj)):
                dst[dj][di] = src[sj][si]

def border(img, s, c):
    '''Ritorna una nuova immagine che è l'immagine
    img contornata da una cornice di spessore s 
    e colore c'''
    w, h = width(img), height(img)
    ret = create(w+s*2, h+s*2, c)
    copy(ret, img, s, s, 0, 0, w, h)
    return ret

# Begin error-generating code --- using try/expect
try:
    save('img_border.png', border(img, 8, (0,0,0)))
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error:   File "<input>", line 7, in border
    # Error:   File "<input>", line 8, in copy
    # Error: KeyboardInterrupt
except:
    pass
# End error-generating code

def fliph(img):
    '''Ritorna una nuova immagine che e' l'immagine 
    img ruotata intorno al suo asse verticale, cioè
    i pixels sono scambiati orizzontalmente'''
    w, h = width(img), height(img)
    ret = create(w, h)
    for j in range(h):
        for i in range(w):
            ret[j][i] = img[j][w - 1 - i]
    return ret

save('img_fliph.png',fliph(img))

def flipv(img):
    '''Ritorna una nuova immagine che è l'immagine
    img ruotata intorno al suo asse orizzontale, 
    cioè i pixels sono scambiati verticalmente'''
    w, h = width(img), height(img)
    ret = create(w, h)
    for j in range(h):
        for i in range(w):
            ret[j][i] = img[h - 1 - j][i]
    return ret
        
save('img_flipv.png',flipv(img))

def rotate(img):
    '''Ritorna una nuova immagine che è l'immagine
    img ruotata intorno all'angolo inferiore 
    sinistro, equivalente a scambiare le righe 
    con le colonne'''
    w, h = width(img), height(img)
    # altezza e larghezza sono invertite
    ret = create(h, w) 
    for j in range(h):
        for i in range(w):
            ret[i][j] = img[h-1-j][i]
    return ret

save('img_rotate.png',rotate(img))

def invert(img):
    '''Ritorna una nuova immagine che è l'immagine
    img con colori invertiti'''
    w, h = width(img), height(img)
    ret = create(w, h, (0,0,0))
    for j in range(h):
        for i in range(w):
            r, g, b = img[j][i]
            ret[j][i] = (255 - r, 255 - g, 255 - b)
    return ret

# Begin error-generating code --- using try/expect
try:
    save('img_invert.png',invert(img))
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error:   File "<input>", line 9, in invert
    # Error: KeyboardInterrupt
except:
    pass
# End error-generating code

def filter(img,func):
    '''Ritorna una nuova immagine che è l'immagine
    img con colori filtrati da func'''
    w, h = width(img), height(img)
    ret = create(w, h, (0,0,0))
    for j in range(h):
        for i in range(w):
            r, g, b = img[j][i]
            ret[j][i] = func(r, g, b)
    return ret

def invertf(r,g,b):
    return 255 - r, 255 - g, 255 - b

save('img_invertf.png',filter(img,invertf))

def grayf(r,g,b):
    gray = (r + g + b) // 3
    return gray, gray, gray

# Begin error-generating code --- using try/expect
try:
    save('img_grayf.png',filter(img,grayf))
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error:   File "<input>", line 4, in save
    # Error:   File "/Users/fabio/Documents/Work/books/fondamentibook/ch12/png.py", line 1279, in save
    # Error:     w.write(file, self.rows)
    # Error:   File "/Users/fabio/Documents/Work/books/fondamentibook/ch12/png.py", line 620, in write
    # Error:     nrows = self.write_passes(outfile, rows)
    # Error:   File "/Users/fabio/Documents/Work/books/fondamentibook/ch12/png.py", line 789, in write_passes
    # Error:     compressed = compressor.compress(tostring(data))
    # Error: KeyboardInterrupt
except:
    pass
# End error-generating code

def contrastf(r,g,b):
    return ( max(0,min(255, (r - 128) * 2 + 128)),
             max(0,min(255, (g - 128) * 2 + 128)),
             max(0,min(255, (b - 128) * 2 + 128)))

# Begin error-generating code --- using try/expect
try:
    save('img_contrastf.png',filter(img,contrastf))
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error:   File "<input>", line 9, in filter
    # Error:   File "<input>", line 3, in contrastf
    # Error: KeyboardInterrupt
except:
    pass
# End error-generating code

def mosaic_nearest(img, s):
    '''Ritorna una nuova immagine ottenuta dividendo
    l'immagine img in quadrati di lato s e riempendo
    ogni quadrato con il colore del suo angolo in
    alto a sinistra'''
    w, h = width(img), height(img)
    ret = create(w, h)
    # itera sui possibili quadrati
    for jj in range(h//s):
        for ii in range(w//s):
            # colore dell'angolo in alto-sinistra
            c = img[jj*s][ii*s]  
            draw_quad(ret, ii*s, jj*s, s, s, c)
    return ret

save('img_mosaicn.png',mosaic_nearest(img,16))

def average(img, i, j, w, h):
    '''Calcola la media dei valori dell'area 
    [i,w-1]x[j,h-1].'''
    c = [0,0,0]
    for jj in range(j,j+h):
        for ii in range(i,i+w):
            for k in range(3):
                c[k] += img[jj][ii][k]
    for k in range(3):
        c[k] //= w*h
    return tuple(c)

def mosaic_average(img, s):
    '''Ritorna una nuova immagine ottenuta dividendo
    l'immagine img in quadrati di lato s e riempendo
    ogni quadratino con la media dei suoi colori.'''
    w, h = width(img), height(img)
    ret = create(w, h)
    # itera sui possibili quadrati
    for jj in range(h//s):
        for ii in range(w//s):
            # colore medio dell'immagine
            c = average(img,ii*s,jj*s,s,s)  
            draw_quad(ret, ii*s, jj*s, s, s, c)
    return ret

save('img_mosaica.png',mosaic_average(img,16))

def mosaic_size(img, s):
    '''Ritorna una nuova immagine ottenuta dividendo
    l'immagine img in quadratini di lato s e
    disegnando all'interno di ognuno di essi, 
    su sfondo nero, un quadratino centrale bianco di
    lato proporzionale alla luminosità media del 
    corrispondente quadratino'''
    w, h = width(img), height(img)
    ret = create(w, h)
    # itera sui possibili quadrati
    for jj in range(h//s):
        for ii in range(w//s):
            # colore medio dell'immagine
            c = average(img,ii*s,jj*s,s,s)
            # lato del quadratino bianco
            r = round(s*(c[0]+c[1]+c[2])/(3*255))
            draw_quad(ret, ii*s+(s-r)//2, 
                jj*s+(s-r)//2, r, r, (255,255,255))
    return ret

save('img_mosaics.png',mosaic_size(img,16))

import random

def scramble(img, d, s):
    '''Ritorna una nuova immagine ottenuta colorando
    ogni pixel (i, j) con il colore di un pixel
    scelto a caso nel quadratino centrato in (i, j)
    di lato 2*d + 1'''
    # settiamo il seed per generare la stessa 
    # sequenza di numeri casuali
    random.seed(s)    
    w, h = width(img), height(img)
    ret = create(w, h)
    for j in range(h):
        for i in range(w):
             # sceglie a caso un pixel nel quadrato
            ri = i + random.randint(-d,d)   
            rj = j + random.randint(-d,d)
            # evitando che si esca dall'immagine
            ri = max(0, min(w-1, ri))   
            rj = max(0, min(h-1, rj))
            ret[j][i] = img[rj][ri]
    return ret

save('img_scramble.png',scramble(img,16,0))

import math

def lens(img, x, y, r, p):
    '''Ritorna una nuova immagine ottenuta dall'
    immagine img applicando una lente di raggio r,
    centrata in (x, y) e di power p. Se p = 1.0 la
    lente non distorce, se p > 1.0 la lente 
    ingrandisce e se p < 1.0 riduce.'''
    w, h = width(img), height(img)
    ret = create(w, h)
    for j in range(h):
        for i in range(w):
            di, dj = i - x, j - y
            # distanza al quadrato da (x, y)
            d2 = di*di + dj*dj   
            # se è nel raggio della lente
            if d2 < r*r:         
                rr = math.sqrt(d2) / r
                if rr > 0:
                    ratio = (rr ** p) / rr
                else:
                    ratio = 1.0
                li = int((i-x)*ratio+x)
                lj = int((j-y)*ratio+y)
                if inside(img, li, lj):
                    ret[j][i] = img[lj][li]
                else:
                    ret[j][i] = (0,0,0)
            else:
                ret[j][i] = img[j][i]
    return ret

save('img_lenss.png',lens(img,128,128,100,0.5))
save('img_lensb.png',lens(img,128,128,100,2.0))

