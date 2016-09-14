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


import png

def save(filename,img):
    pyimg = png.from_array(img, 'RGB')
    pyimg.save(filename)

def load(filename):
    '''Carica l'immagine in formato PNG dal file filename, la converte nel
    formato a matrice di tuple e la ritorna'''
    with open(filename,'rb') as f:
        # legge l'immagine come RGB a 256 valori tramite l'oggetto Reader
        iw, ih, png_img, _ = png.Reader(file=f).asRGB8()
        # converte l'immagine in lista di liste di tuple
        img = []
        for png_row in png_img:
            row = []
            # l'immagine PNG ha i colori come un unico array
            # quindi li leggiamo tre alla volta e impacchettiamo in una tupla
            for i in range(0,len(png_row),3):
                row.append( (png_row[i+0],png_row[i+1],png_row[i+2]) )
            img.append( row )
    return img
