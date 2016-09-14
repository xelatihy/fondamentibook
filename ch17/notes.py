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


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *  

class PaintInfo:
    def __init__(self):
        self.mouse_pressed = False
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_px = 0
        self.mouse_py = 0
        self.key = ''
        self.size = (0, 0)

class _GWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.image = QImage(self.width(), 
            self.height(), QImage.Format_ARGB32)
        self.paint_handler = None
        self.info = PaintInfo()
        self.info.size = self.width(), self.height()
        self.setMouseTracking(True)
    def drawing(self):
        painter = QPainter(self.image)
        painter.setRenderHints(
            QPainter.Antialiasing,True)
        painter.setRenderHints(
            QPainter.SmoothPixmapTransform,True)
        painter.info = self.info
        self.paint_handler(painter)
        self.info.mouse_px = self.info.mouse_x
        self.info.mouse_py = self.info.mouse_y
        self.update()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)
    def resizeEvent(self,event):
        prev_img = self.image
        self.image = QImage(self.width(), 
            self.height(), QImage.Format_ARGB32)
        self.image.fill(QColor(0,0,0).rgb())
        painter = QPainter(self.image)
        painter.drawImage(0, 0, prev_img)
        self.info.size = self.width(), self.height()
        self.update()
    def mousePressEvent(self,event):
        self.info.mouse_pressed = True
    def mouseReleaseEvent(self,event):
        self.info.mouse_pressed = False
    def mouseMoveEvent(self,event):
        self.info.mouse_x = event.x()
        self.info.mouse_y = event.y()
    def keyPressEvent(self,event):
        if not event.text():
            super().keyPressEvent(event)
        self.info.key = event.text()
    def keyReleaseEvent(self,event):
        self.info.key = ''

def run_app(paint,w,h):
    app = QApplication.instance()
    if not app: app = QApplication([])
    widget = _GWidget()
    widget.resize(w,h)
    widget.setWindowTitle('Fondamenti di Programmazione')
    widget.paint_handler = paint
    timer = QTimer()
    timer.setInterval(1000/60)
    timer.timeout.connect(widget.drawing)
    widget.show()
    timer.start()
    app.exec_()

from random import randint

def random_color(a=128,b=255):
    '''Colore casuale tra a e b'''
    return randint(a,b), randint(a,b), randint(a,b)

def paint(painter):    
    '''Disegna un cerchio casuale'''
    # Dimensioni della finestra
    width, height = painter.info.size   
    # Colore scelto in modo casuale
    r, g, b = random_color()
    # Colore del contorno e dell'interno 
    painter.setPen(QColor(r//2,g//2,b//2)) 
    painter.setBrush(QColor(r,g,b))
    # Diametro e posizione casuali
    s = randint(10, 150)                
    x = randint(-s, width+s)            
    y = randint(-s, height+s)
    # Disegna il cerchio
    painter.drawEllipse(x, y, s, s)     

run_app(paint,500,300)

def paint(painter):
    '''Disegna un rettangolo casuale'''
    width, height = painter.info.size
    r, g, b = random_color()
    painter.setPen(QColor(r//2,g//2,b//2))
    painter.setBrush(QColor(r,g,b))
    # Lato e posizione del quadrato casuale
    s = randint(50, 150)                
    x = randint(-s, width+s)            
    y = randint(-s, height+s)
    # Disegna il quadrato
    painter.drawRect(x, y, s, s)        

run_app(paint,500,300)

def paint(painter):    
    '''Disegna una linea casuale'''
    width, height = painter.info.size
    r, g, b = random_color()
    # Spessore della linea casuale
    lw = randint(1, 10)                 
    painter.setPen(QPen(QColor(r,g,b), lw))
    # Estremi della linea casuali
    x1 = randint(-20, width+20)         
    y1 = randint(-20, height+20)
    x2 = randint(-20, width+20)
    y2 = randint(-20, height+20)
    # Disegna la linea
    painter.drawLine(x1, y1, x2, y2)    

run_app(paint,500,300)

def paint(painter):
    '''Disegna un carattere casuale'''
    width, height = painter.info.size
    r, g, b = random_color()
    # Dimensione del font casuale
    fw = randint(12, 196)                    
    # Imposta la fonte
    painter.setFont(QFont('Helvetica', fw))  
    painter.setPen(QColor(r,g,b))
    # Posizione random
    x = randint(-20, width+20)               
    y = randint(-20, width+20)
    # Carattere random
    c = chr(randint(ord('A'),ord('z')))     
    # Disegna il carattere 
    painter.drawText(x, y, c)                

run_app(paint,500,300)

# Carica l'immagine da file
img = QImage('photo.png')     

def paint(painter):    
    '''Disegna l'immagine img in posizione casuale'''
    width, height = painter.info.size
    # Posizione casuale
    x = randint(-img.width(), width+img.width())     
    y = randint(-img.height(), height+img.height())
    # Disegna l'immagine img con l'angolo in 
    # alto a sinitra in (x,y)
    painter.drawImage(x, y, img)

run_app(paint,500,300)

def clear(painter,a=255):    
    '''Pulisce l'immagine della finestra con
    trasparenza a'''
    width, height = painter.info.size     
    painter.setPen(QColor(0,0,0,a))       
    painter.setBrush(QColor(0,0,0,a))     
    painter.drawRect(0, 0, width, height)    

def paint(painter):
    '''Pulisce la finestra poi disegna'''
    clear(painter)
    width, height = painter.info.size
    r, g, b = random_color()
    painter.setPen(QColor(r//2,g//2,b//2))
    painter.setBrush(QColor(r,g,b))    
    s = randint(10, 150)               
    x = randint(-s, width+s)           
    y = randint(-s, height+s)
    painter.drawEllipse(x, y, s, s)    

run_app(paint,500,300)

def paint(painter):    
    '''Decolora la finestra prima di disegnare'''
    # Pulissce la finestra parzialmente
    clear(painter,4)                    
    width, height = painter.info.size
    r, g, b = random_color()
    painter.setPen(QColor(r//2,g//2,b//2))
    painter.setBrush(QColor(r,g,b))
    s = randint(10, 150)                
    x = randint(-s, width+s)            
    y = randint(-s, height+s)
    painter.drawEllipse(x, y, s, s)     

run_app(paint,500,300)

def paint(painter):      
    '''Disegna un cerchio centrato nel mouse''' 
    clear(painter, 2)   
    painter.setPen(QColor(0,0,0))
    if painter.info.mouse_pressed:
        color = (128,255,128)
    else:
        color = (255,128,128)
    painter.setBrush(QColor(*color))
    painter.drawEllipse(painter.info.mouse_x - 25, 
        painter.info.mouse_y - 25, 50, 50)

run_app(paint,500,300)

def paint(painter):    
    '''Disegna una linea seguendo il mouse'''
    clear(painter, 2)
    if painter.info.mouse_pressed:
        color = (128,255,128)
    else:
        color = (255,128,128)
    painter.setPen(QPen(QColor(*color),4))
    painter.drawLine(
        painter.info.mouse_px,painter.info.mouse_py, 
        painter.info.mouse_x,painter.info.mouse_y)

run_app(paint,500,300)

def paint(painter):
    '''Disegna il carattere premuto sulla tastiera'''
    clear(painter, 2)
    if painter.info.mouse_pressed:
        color = (128,255,128)
    else:
        color = (255,128,128)
    painter.setPen(QColor(*color))
    painter.setFont(QFont('Helvetica',300))
    painter.drawText(painter.info.mouse_x,
        painter.info.mouse_y,painter.info.key)

run_app(paint,500,300)

# Modalita' di disegno, default cerchi
scribblemode = 'c'    

def paint(painter):
    '''Disegna forme controllate della tastiera'''
    # Per poter modificare il valore della variabile
    global scribblemode    
    if painter.info.key in ['c','l','t','s']:
        scribblemode = painter.info.key
        painter.info.key = ''
    # Blocca il disegno e la dissolvenza
    if scribblemode == 's':       
        return
    clear(painter, 2)
    if painter.info.mouse_pressed:
        color = (128,255,128)
    else:
        color = (255,128,128)
    # Cerchi
    if scribblemode == 'c':       
        painter.setPen(QColor(0,0,0))
        painter.setBrush(QColor(*color))
        painter.drawEllipse(painter.info.mouse_x-25,
            painter.info.mouse_y-25,50,50)
    # Linee
    elif scribblemode == 'l':     
        painter.setPen(QPen(QColor(*color),4))
        painter.drawLine(painter.info.mouse_px, 
            painter.info.mouse_py, 
            painter.info.mouse_x,
            painter.info.mouse_y)
    # Caratteri
    elif scribblemode == 't':     
        painter.setPen(QColor(*color))
        painter.setFont(QFont('Helvetica',300))
        painter.drawText(painter.info.mouse_x,
            painter.info.mouse_y,painter.info.key)

run_app(paint,500,300)

def paint(painter):
    '''Disegna un'immagine in (x, y), che per 
    testare seguone il mouse'''
    clear(painter)
    width, height = painter.info.size
    x = painter.info.mouse_x
    y = painter.info.mouse_y
    painter.setPen(QPen(QColor(255,255,255),4))
    painter.drawLine(-width+x,y,width+x,y)
    painter.drawLine(x,-height+y,x,height+y)
    painter.drawImage(-img.width()/2+x, 
        -img.height()/2+y, img)

run_app(paint,500,300)

def paint(painter):
    '''Disegna un'immagine ruotata al centro'''
    clear(painter)
    width, height = painter.info.size
    x = painter.info.mouse_x
    y = painter.info.mouse_y
    # Angolo della rotazione (in gradi)
    a = 45                    
    # Traslazione che porta l'origine in (x,y)
    painter.translate(x,y)    
    # Rotazione intorno all'origine di angolo a
    painter.rotate(a)         
    painter.setPen(QPen(QColor(255,255,255),4))
    painter.drawLine(-width,0,width,0)
    painter.drawLine(0,-height,0,height)
    painter.drawImage(-img.width()/2, 
        -img.height()/2, img)

run_app(paint,500,300)

def paint(painter):
    '''Disegna un'immagine con rotazione e
    posizione casuale'''
    clear(painter, 8)
    width, height = painter.info.size
    # Centro casuale
    x, y = randint(0,width), randint(0,height) 
    # Angolo di rotazione casuale  
    a = randint(0,360)                          
    painter.translate(x,y)
    painter.rotate(a)
    painter.drawImage(-img.width()/2, 
        -img.height()/2, img)

run_app(paint,500,300)

