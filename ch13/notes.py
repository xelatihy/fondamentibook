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


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

# Creazione di un oggetto di tipo Color
c1 = Color(255,0,0)   
print(type(c1))
# Out: <class '__console__.Color'>

# Valore dell'attributo r dell'oggetto creato
print(c1.r)
# Out: 255
print(c1.g)
# Out: 0
print(c1.b)
# Out: 0

# Un altro oggetto di tipo Color
c2 = Color(0,255,0)   
print(type(c2))
# Out: <class '__console__.Color'>

# Il valore dell'attributo r è diverso
print(c2.r)
# Out: 0
print(c2.g)
# Out: 255
print(c2.b)
# Out: 0

# Infatti i due oggetti hanno identità differenti
print(id(c1))            
# Out: 4335068048
print(id(c2))
# Out: 4335068104

# Begin error-generating code --- using try/expect
try:
    print(c1.z)
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: AttributeError: 'Color' object has no attribute 'z'
except:
    pass
# End error-generating code

# Modifica l'attributo g dell'oggetto in c1
c1.g = 128      
print(c1.g)
# Out: 128

# Il corrispondente attributo di c2 non è cambiato
print(c2.g)     
# Out: 255

class Color:
    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b
    def inverse(self):
        return Color(255 - self.r, 
            255 - self.g, 255 - self.b)

c = Color(255,0,0)
print(c.r, c.g, c.b)
# Out: 255 0 0
ci = c.inverse()
print(ci.r, ci.g, ci.b)
# Out: 0 255 255

# Creiamo due colori
c1 = Color(255,0,0)    
c2 = Color(0,255,0)

# Proviamo a stamparli
print(c1)               
# Out: <__console__.Color object at 0x10263e320>
print(c1.r, c1.g, c1.b)
# Out: 255 0 0

# Proviamo a sommarli
# Begin error-generating code --- using try/expect
try:
    c3 = c1 + c2           
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: TypeError: unsupported operand type(s) for +: 'Color' and 'Color'
except:
    pass
# End error-generating code

class Color:
    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b
    def inverse(self):
        return Color(255 - self.r, 
            255 - self.g, 255 - self.b)
    def __str__(self):
        return 'Color({},{},{})'.format(
            self.r,self.g,self.b)
    def __add__(self, other):
        return Color(self.r+other.r,
            self.g+other.g,self.b+other.b)
    def __mul__(self, f):
        return Color(self.r*f, self.g*f, self.b*f)

# Creiamo due colori
c1 = Color(255,0,0)     
c2 = Color(0,255,0)

# Stampa di un colore
print(c1)               
# Out: Color(255,0,0)

# Operazioni su colori
c3 = c1 + c2            
print(c3)
# Out: Color(255,255,0)
c4 = c3*0.7             
print(c4)
# Out: Color(178.5,178.5,0.0)

import png

class Image:
    def __init__(self, w, h):
        '''Crea un'immagine di dimensioni w x h 
        riempita con colore nero'''
        # L'attributo _pixels deve rimanere nascosto
        self._pixels = []    
        for j in range(h):
            row = []
            for i in range(w):
                row.append(Color(0,0,0))
            self._pixels.append(row)
    def width(self):
        '''Ritorna la larghezza dell'immagine'''
        return len(self._pixels[0])
    def height(self):
        '''Ritorna l'altezza dell'immagine'''
        return len(self._pixels)
    def set_pixel(self, i, j, color):
        '''Imposta il colore del pixel (i, j)'''
        if (0 <= i < self.width() and 
            0 <= j < self.height()):
            self._pixels[j][i].r = color.r
            self._pixels[j][i].g = color.g
            self._pixels[j][i].b = color.b
    def get_pixel(self, i, j):
        '''Ritorna l'oggetto Color del pixel (i,j)'''
        if (0 <= i < self.width() and 
            0 <= j < self.height()):
            return self._pixels[j][i]
    def load(self, filename):
        '''Carica l'immagine dal file filename'''
        with open(filename,'rb') as f:
            r = png.Reader(file=f)
            iw, ih, png_img, _ = r.asRGB8()
            img = []
            for png_row in png_img:
                row = []
                for i in range(0,len(png_row),3):
                    row.append( Color(png_row[i+0],
                        png_row[i+1],png_row[i+2]) )
                img.append( row )
    def save(self, filename):
        '''Salva l'immagine nel file filename'''
        pixels = []
        for j in range(self.height()):
            pixels.append([])
            for i in range(self.width()):
                c = self.get_pixel(i,j)
                pixels[-1] += [c.r,c.g,c.b]
        pyimg = png.from_array(pixels, 'RGB')
        pyimg.save(filename)
    def draw_quad(self, x, y, w, h, c):
        '''Disegna sull'immagine un rettangolo con
        spigolo in (x,y), dimensioni wxh e 
        colore c'''
        for j in range(y, y+h):
            for i in range(x, x+w):
                self.set_pixel(i,j,c)
    def draw_gradienth(self, c0, c1):
        '''Disegna sull'immagine un gradiente 
        orizzontale dal colore c0 al colore c1'''
        for j in range(self.height()):
            for i in range(self.width()):
                u = float(i) / float(self.width())
                self.set_pixel(i,j,c0*(1-u)+c1*u)
    def __str__(self):
        return 'Image@{}x{}'.format(
            self.width(),self.height())

img = Image(256,128)
img.draw_gradienth(Color(255,128,128),
    Color(128,255,128))
img.draw_quad(32,32,64,64,Color(0,200,255))
img.save('img_draw.png')
print(img)
# Out: Image@256x128

