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


from random import random, uniform, randint
from math import pi, sqrt, sin, cos

class vec2f(object):
    '''Vettore bidimensionale di float'''
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    def __add__(self,other):
        '''Somma di vettori'''
        return vec2f(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        '''Somma con vettore opposto'''
        return vec2f(self.x-other.x,self.y-other.y)
    def __neg__(self):          
        '''Vettore opposto'''
        return vec2f(-self.x,-self.y)
    def __mul__(self,other):
        '''Prodotto per scalare'''
        return vec2f(self.x*other,self.y*other)
    def __truediv__(self,other):
        '''Divisione per scalare'''
        return vec2f(self.x/other,self.y/other)
    def length(self):           
        '''Lunghezza del vettore'''
        return sqrt( self.x*self.x + self.y*self.y )
    def normalized(self):       
        '''Vettore normalizzato'''
        l = self.length()
        if l < 0.000001:
            return vec2f(0,0)
        else: 
            return vec2f(self.x/l,self.y/l)
    def clamped(self,maxlen):
        '''Vettore con lunghezza massima maxlen'''
        l = self.length()
        if l > maxlen:
            return self * maxlen / l
        else:
            return vec2f(self.x,self.y)

# funzioni utili su vettori
def length(v): return v.length()
def normalize(v): return v.normalized()
def clamp(v,maxlength): return v.clamped(maxlength)

def dot(v0,v1):  
    '''Prodotto scalare'''
    return v0.x*v1.x+v0.y*v1.y

def random_pos(x0, y0, x1, y1): 
    '''Vettore random tra i valori dati'''
    return vec2f(uniform(x0,x1), uniform(y0,y1))

def random_dir():         
    '''Vettore random di lunghezza 1'''
    a = uniform(0,2*pi)
    return vec2f(cos(a),sin(a))

def random_vec(maxlen):
    '''Vettore random di lunghezza al più maxlen'''
    return random_dir() * random() * maxlen

# Dimensioni dello spazio di simulazione
size = vec2f(500, 300)   

class Particle(object):
    '''Rappresenta una particella tramite i suoi''' 
    def __init__(self):
        '''parametri di simulazione'''
        # Raggio
        self.radius = 25.0    
        # Posizione, inizialmente al centro
        self.pos = size/2     
        # Velocità, inizialmente 0
        self.vel = vec2f(0,0) 
        # Accelerazione, inizialmente 0
        self.acc = vec2f(0,0)
        # Massa
        self.mass = 1.0      
        # Se simulata calcoleremo il moto
        self.simulated = True 
        # Colore
        self.color = QColor(128,128,128,200)    
        # Colore quando non simulata
        self.color_paused = QColor(128,255,128,200)
        # Timer, se 0 disattivato
        self.timer = 0           
        # Attiva le collisioni tra particelle
        self.collisions = False 

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from gwidget import run_app

# Lista delle particelle
particles = []      

def init():
    '''Crea e inizializza le particelle, 
    per adesso una sola particella immobile'''
    global particles
    particles = [Particle()]

def update():    
    '''Aggiorna posizioni e moto delle particelle'''
    pass         

def v2qt(v):
    '''Converte un vec2f v in un vettore di Qt'''
    return QPointF(v.x, v.y)

def clear(painter):         
    '''Pulisce lo schermo'''
    painter.fillRect(0,0,size.x,size.y,
        QColor(255,255,255))

def set_color(painter,c):
    '''Setta il color di brush e pen'''
    painter.setPen(QPen(QColor(0,0,0,c.alpha()),2))
    painter.setBrush(c)    

def draw(painter):          
    '''Disegna le particelle'''
    clear(painter)
    for p in particles:
        if p.simulated:
            set_color(painter,p.color)
        else:
            set_color(painter,p.color_paused)
        painter.drawEllipse(v2qt(p.pos), 
            p.radius, p.radius)
        # Disegna una linea dal centro della particella
        # che ne indica la velocità
        painter.drawLine(v2qt(p.pos), 
            v2qt(p.pos+normalize(p.vel)*p.radius))
                         
def paint(painter):  
    '''Aggiorna la simulazione ad ogni frame'''
    # Aggiorna posizioni e moto delle particelle
    update()         
    # Disegna il nuovo stato della simulazione
    draw(painter)    

# Inizializza le particelle
init()   

# Esegue la simulazione chiamando paint ogni frame
run_app(paint, int(size.x), int(size.y))

def handle_walls():    
    '''Gestisce le collisioni particelle-bordi'''
    for p in particles:
        # Bordo sinistro    
        if p.pos.x < p.radius:           
            p.pos.x = p.radius
            p.vel.x = abs(p.vel.x)
        # Bordo destro
        if p.pos.x > size.x - p.radius:  
            p.pos.x = size.x - p.radius
            p.vel.x = -abs(p.vel.x)
        # Bordo alto 
        if p.pos.y < p.radius:          
            p.pos.y = p.radius
            p.vel.y = abs(p.vel.y)
        # Bordo basso
        if p.pos.y > size.y - p.radius:  
            p.pos.y = size.y - p.radius
            p.vel.y = -abs(p.vel.y)    
    
def update():         
    '''Aggiorna posizioni e moto delle particelle'''
    for p in particles:
        # salta se non simulata
        if not p.simulated: continue
        # aggiorna posizione con la velocità
        p.pos += p.vel
    # Gestisce le collisioni particelle-bordi     
    handle_walls() 

def init_particle():            
    '''Crea e inizializza una particella'''
    p = Particle()              
    p.vel = vec2f(1,4)          
    return p

def init():
    '''Crea e inizializza le particelle'''
    global particles                
    particles = [init_particle()]  

init()
run_app(paint, int(size.x), int(size.y))

class Params:    
    '''Parametri della simulazione'''
    def __init__(self):
        # Numero particelle
        self.num = 4                     
        # Minimo e massimo raggio
        self.radius_min = 25.0           
        self.radius_max = 25.0           
        # Massima intensità delle velocità
        self.vel = 4.0                   
        # Densità
        self.density = 1.0/(pi*25*25)
        # Fattore d'attrazione verso il mouse    
        self.force_mouse = 0.0     
        # Fattore di decelerazione
        self.force_drag = 0.002    
        # Max intensità forza casuale
        self.force_random = 0.0    
        # Accelerazione di gravità
        self.force_gravity = 0.0   
        # Dissolvenza dei movimenti precedenti
        self.fade = True           
        # Posizione relativa al mouse
        self.mouse = False         
        # Max timer
        self.timer = 0              

# Parametri della simulazione
params = Params()   

def init_particle():       
    '''Crea e inizializza una particella'''
    p = Particle()
    # Raggio random
    p.radius = uniform(params.radius_min, 
        params.radius_max)    
    # Posizione random
    p.pos = random_pos(0, 0, size.x, size.y)     
    # Velocita' random ma limitata            
    p.vel = random_vec(params.vel)               
    # Massa = area x densità
    p.mass = pi*(p.radius**2)*params.density           
    return p

def init():                 
    '''Crea e inizializza le particelle'''
    global particles
    particles = []
    # Ora ci sono più particelle
    for _ in range(params.num):    
        particles += [init_particle()]

def clear(painter):    
    '''Pulisce lo schermo'''
    if params.fade:
        fade = 8
    else:
        fade = 255
    painter.fillRect(0,0,size.x,size.y,
        QColor(255,255,255,fade))

init()
run_app(paint, int(size.x), int(size.y))

def handle_forces(mouse_pos):
    '''Aggiorna l'accelerazione di ogni particella'''
    for p in particles:     
        # salta se non simulata
        if not p.simulated: continue 
        # Parte da accelerazione 0
        p.acc = vec2f(0,0)    
        # Accelerazione proporzionale alla distanza
        # dal mouse
        p.acc += (normalize(mouse_pos - p.pos) * 
            params.force_mouse)
        # Accelerazione casuale
        p.acc += (random_vec(params.force_random) / 
            p.mass)
        # Decelerazione proporzionale alla velocità
        p.acc += -p.vel*params.force_drag / p.mass
        # Accelerazione di gravità
        p.acc += vec2f(0, params.force_gravity) 

def update(mouse_pos):    
    '''Aggiorna posizioni e moto delle particelle'''
    # Aggiorna l'accelerazione di ogni particella
    handle_forces(mouse_pos)
    # Aggiorna velocità e posizione
    for p in particles:       
        if not p.simulated: continue
        p.vel += p.acc        
        p.pos += p.vel
    # Gestisce le collisioni particelle-bordi        
    handle_walls() 

def paint(painter):        
    '''Aggiorna la simulazione ad ogni frame'''
    # Aggiorna posizioni e moto delle particelle, 
    # tenendo anche conto del mouse
    update(vec2f(painter.info.mouse_x, 
        painter.info.mouse_y))
    draw(painter)

params = Params()
params.force_gravity = 0.5

init()
run_app(paint, int(size.x), int(size.y))

params = Params()
params.force_random = 0.5

init()
run_app(paint, int(size.x), int(size.y))

params = Params()
params.force_mouse = 0.5

init()
run_app(paint, int(size.x), int(size.y))

# Eventuale particella presa con il mouse
grabbed = None      

def grab(mouse_pressed, mouse_pos, mouse_lpos):
    '''Gestisce la particella selezionata'''
    global grabbed
    # Se il mouse è premuto
    if mouse_pressed:     
        # Se non c'è una particella presa
        if not grabbed:       
            # Controlla per ogni particella se
            for p in particles:    
                # Se è vicina al mouse
                if length(p.pos-mouse_pos)<p.radius:
                    # prendila
                    grabbed = p
                    # e escludila dalla simulaazione
                    grabbed.simulated = False  
                    grabbed.vel = vec2f(0,0)
                    break
        # Se c'è una particella presa,
        else:                 
            # spostala con il mouse
            grabbed.pos += mouse_pos - mouse_lpos   
    # Il mouse non è premuto e una particella è presa
    elif grabbed:         
        # Rimettila in simulazione lanciandola con
        # velocità dipendente dal mouse
        grabbed.simulated = True    
        v = mouse_pos - mouse_lpos  
        grabbed.vel = clamp(v, 16)
        grabbed = None            

def paint(painter):     
    '''Aggiorna la simulazione ad ogni frame'''
    # Gestisci la presa di una particella con il mouse
    grab(painter.info.mouse_pressed,  
        vec2f(painter.info.mouse_x, 
            painter.info.mouse_y),   
        vec2f(painter.info.mouse_px, 
            painter.info.mouse_py))
    update(vec2f(painter.info.mouse_x, 
        painter.info.mouse_y))
    draw(painter)    

params = Params()

init()
run_app(paint, int(size.x), int(size.y))

params = Params()

params.num = 120
params.radius_min = 5.0
params.radius_max = 5.0
params.force_gravity = 0.1
params.fade = False
params.mouse = True
params.timer = 120 
params.Fade = False

def init_particle(mouse_pos=vec2f(0,0), p=None):
    '''Crea e inizializza una particella, o inizializza
    una particella già esistente, inizializza la 
    posizione con quella del mouse o random e
    imposta un timer'''
    # Reusa la particella se già esistente
    if not p: p = Particle()                 
    # Timer
    p.timer = randint(params.timer/2, params.timer)   
    p.radius = uniform(params.radius_min, 
        params.radius_max)    
    # Posizione relativa al mouse o casuale
    if params.mouse:
        p.pos = vec2f(mouse_pos.x, mouse_pos.y)
    else:
        p.pos = random_pos(0,0,size.x,size.y)
    p.vel = random_vec(params.vel)    
    p.mass = pi*(p.radius**2)*params.density
    return p

def handle_timers(mouse_pos): 
    '''Gestisce il timer delle particelle'''
    for p in particles:
        if not p.simulated: continue
        # Se non temporizzata, ignorala
        if not p.timer: continue    
        # decrementa il timer   
        p.timer -= 1         
        # e se e' arrivato a zero
        # rinizializza la particella
        if p.timer < 1:      
            init_particle(mouse_pos, p)

def update(mouse_pos):     
    '''Aggiorna posizioni e moto delle particelle'''
    # Gestisce il timer delle particelle
    handle_timers(mouse_pos)  
    handle_forces(mouse_pos)
    for p in particles: 
        if not p.simulated: continue
        p.vel += p.acc
        p.pos += p.vel
    handle_walls()

def draw(painter):          
    '''Disegna le particelle'''
    clear(painter)
    for p in particles:
        # La trasparenza dipende dal timer 
        if p.timer:
            set_color(painter, QColor(p.color.red(),
                p.color.green(), p.color.blue(),
                p.timer*2))
        elif p.simulated:
            set_color(painter,p.color)
        else:
            set_color(painter,p.color_paused)
        painter.drawEllipse(v2qt(p.pos), 
            p.radius, p.radius)
        painter.drawLine(v2qt(p.pos), 
            v2qt(p.pos+normalize(p.vel)*p.radius))

init()
run_app(paint, int(size.x), int(size.y))

def handle_collisions():    
    '''Gestisce le collisioni tra particelle'''
    if not params.collisions:    
        return                   
    for p in particles:            
        for p1 in particles: 
            if p1 is p: continue
            # Versore tra i centri delle particelle
            pp = normalize(p1.pos - p.pos) 
            # Distanza dei centri delle particelle
            d = length(p1.pos - p.pos)     
            # Somma dei raggi
            rr = p1.radius + p.radius
            # Se la distanza è maggiore dei raggi      
            if d >= rr:     
                # non c'è collisione
                continue        
            # Se la seconda particella è simulata
            if p1.simulated:    
                # Punto medio dei centri
                m = (p.pos + p1.pos)/2   
                # Posiziona le particelle in modo
                p.pos = m - pp * rr/2    
                # che siano tangenti
                p1.pos = m + pp * rr/2   
                # Determina le velocità
                vo0 = pp*dot(p.vel, pp)
                vp0 = p.vel - vo0
                vo1 = pp*dot(p1.vel, pp)
                vp1 = p1.vel - vo1
                if dot(vo1 - vo0, pp) < 0:
                    m = p1.mass+p.mass
                    vn0 = ( vo0 * (p.mass-p1.mass) + 
                        vo1*2*p1.mass) / m
                    vn1 = ( vo1 * (p1.mass-p.mass) +
                        vo0*2*p.mass) / m
                    p.vel = vn0 + vp0
                    p1.vel = vn1 + vp1
            # Se la seconda particella non è simulata
            else:              
                p.pos = p1.pos - pp * rr
                vo0 = pp * dot(p.vel, pp)
                vp0 = p.vel - vo0
                if dot(-vo0, pp) < 0:
                    p.vel = vp0 - vo0

def update(mouse_pos):     
    '''Aggiorna posizioni e moto delle particelle'''
    # Gestisce il timer delle particelle
    handle_timers(mouse_pos)  
    # Aggiorna l'accelerazione di ogni particella
    handle_forces(mouse_pos)  
    # Aggiorna posizione e velocità
    for p in particles:
        if not p.simulated: continue
        p.vel += p.acc        
        p.pos += p.vel        
    handle_walls() 
    # Gestisce le collisioni tra particelle
    handle_collisions() 

params = Params()
params.collisions = True
params.num = 10

init()
run_app(paint, int(size.x), int(size.y))

