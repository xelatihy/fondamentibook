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


# Importa tutte le classi per costruire GUI con Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *  
from PyQt5.QtWebEngineWidgets import *

# Crea un'applicazione Qt
app = QApplication([])    

# Crea una finestra (ma non e' visibile)
window = QWidget()        

# Imposta dimensione e titolo della finestra
window.resize(500, 300)   
window.setWindowTitle('Fondamenti di Programmazione')

# Mostra la finestra
window.show()             

# Lancia l'interazione con l'utente
app.exec_()               
# Out: 0

def init():
    '''Crea un'applicazione Qt e una finestra'''
    # verifica se l'applicazione è già esistente
    app = QApplication.instance()
    # o ne crea una nuova
    if not app: app = QApplication([])
    window = QWidget()
    window.resize(500, 300) 
    window.setWindowTitle(
        'Fondamenti di Programmazione')
    return app, window

def run(app, window):
    '''Rende la finestra visibile e lancia 
    l'applicazione'''
    window.show()    
    app.exec_()

# Crea un bottone sulla finestra
app, window = init()
button = QPushButton('Button', window)    
run(app, window)

# Definisce la callback del bottone
def button_callback():    
    print('Clicked')
    
app, window = init()

# Crea un bottone sulla finestra
button = QPushButton('Print', window)    

# Imposta la callback in risposta all'evento 
# clicked del bottone
button.clicked.connect(button_callback)

run(app, window)

app, window = init()

# Crea un layout verticale
layout = QVBoxLayout()            

# Crea due bottoni
button1 = QPushButton('Exit')     
button2 = QPushButton('Print')

# Aggiunge i bottoni al layout
layout.addWidget(button1)         
layout.addWidget(button2)

# Imposta il layout come layout della finestra
window.setLayout(layout)          

# Definisce una semplice callback
def print_callback():             
    print('ciao')

# Imposta le callback dei due bottoni
button1.clicked.connect(app.quit)    
button2.clicked.connect(print_callback)

run(app, window)

app, window = init()

# Crea i layout per la finestra e la toolbar
layout = QVBoxLayout()               
tlayout = QHBoxLayout()

# Crea i tre bottoni
button_open = QPushButton('Open')   
button_save = QPushButton('Save')
button_exit = QPushButton('Exit')

# Aggiunge i bottoni al layout della toolbar
tlayout.addWidget(button_open) 
tlayout.addWidget(button_save)
tlayout.addWidget(button_exit)

# Aggiunge la toolbar al layout della finestra
layout.addLayout(tlayout)      

# Crea un'area per editare testo
textedit = QTextEdit('')
# Aggiunge l'area testo al layout della finestra
layout.addWidget(textedit)  

# Imposta il layout della finestra
window.setLayout(layout)    

run(app, window)

# Definisce la callback per aprire un file
def open_callback():    
    filename, _ = QFileDialog.getOpenFileName(window)
    # Verifuca se l'utente ha scelto "Cancel"
    if not filename: return    
    with open(filename) as f:
        textedit.setText(f.read())

# Definisce la callback per salvare il file
def save_callback():    
    filename, _ = QFileDialog.getSaveFileName(window)
    # Veriuca se l'utente ha scelto "Cancel"
    if not filename: return    
    with open(filename, 'w') as f:
        f.write(textedit.toPlainText())

# Imposta le callback dei tre bottoni
button_open.clicked.connect(open_callback) 
button_save.clicked.connect(save_callback)
button_exit.clicked.connect(app.exit)

run(app, window)

app, window = init()

# Crea il layout per la finestra
layout = QVBoxLayout()      

# Crea il layout per la toolbar
tlayout = QHBoxLayout() 
    
# Crea la navigation bar e i bottoni di navigazione
text_bar = QLineEdit('')             
button_back = QPushButton('<')
button_forward = QPushButton('>')

# Aggiunge i widgets alla toolbar
tlayout.addWidget(button_back)      
tlayout.addWidget(button_forward)
tlayout.addWidget(text_bar)

# Aggiunge la toolbar alla finestra
layout.addLayout(tlayout)   

# Crea un widget per visualizzare pagine web
web_view = QWebEngineView() 
# Aggiunge al layout della finestra
layout.addWidget(web_view)  

# Imposta il layout della finestra
window.setLayout(layout)    

run(app,window)

# La callback per caricare una pagina
def load_page():    
    if text_bar.text() == web_view.url().toString():
        return
    text = text_bar.text()
    if ' ' in text or '.' not in text:
        text = ('http://google.com/search?q=' + 
            '+'.join(text.split()))
    elif '://' not in text:
        text = 'http://'+text
    web_view.setUrl(QUrl(text))

# La callback per il nuovo url nella navigation bar
def set_url():     
    text_bar.setText(web_view.url().toString())
        
# Imposta la callback della navigation bar 
text_bar.returnPressed.connect(load_page) 
# Imposta la callback della web_view 
web_view.urlChanged.connect(set_url)
# Imposta le callback dei due bottoni
button_back.clicked.connect(web_view.back)
button_forward.clicked.connect(web_view.forward)

run(app, window)

