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


def area_cilindro(raggio, altezza):
    pigreco = 3.14159
    area = pigreco * raggio ** 2
    circonferenza = 2 * pigreco * raggio
    return 2 * area + altezza * circonferenza

print(area_cilindro(10, 5))
# Out: 942.477
print(area_cilindro(20, 10))
# Out: 3769.908

# Begin error-generating code --- using try/expect
try:
    print(circonferenza)
    # Error: Traceback (most recent call last):
    # Error:   File "<input>", line 1, in <module>
    # Error: NameError: name 'circonferenza' is not defined
except:
    pass
# End error-generating code

print(abs(-5))
# Out: 5
print(abs(-3.6))
# Out: 3.6
print(round(5.8))
# Out: 6
print(round(5.3))
# Out: 5

def hms(nsec):
    hh = nsec // 3600
    nsec = nsec % 3600
    mm = nsec // 60
    ss = nsec % 60
    return hh, mm, ss

print(hms(4000))
# Out: (1, 6, 40)
print(hms(100000))
# Out: (27, 46, 40)

def area_cilindro(raggio=1,altezza=1):
    pigreco = 3.14159
    area = pigreco * raggio ** 2
    circonferenza = 2 * pigreco * raggio
    return 2 * area + altezza * circonferenza

# equivelente a area_cilindro(1,1)
print(area_cilindro())    
# Out: 12.56636

# equivelente a area_cilindro(2,1)
print(area_cilindro(2))   
# Out: 37.699079999999995

# equivelente a area_cilindro(2,3)
print(area_cilindro(2,3))
# Out: 62.831799999999994

# equivelente a area_cilindro(1,2)
print(area_cilindro(altezza=2))    
# Out: 18.849539999999998

print(round(3.125))
# Out: 3
print(round(3.125,2))
# Out: 3.12

import modulo

print(modulo.area_sfera(10))
# Out: 1256.0
print(modulo.volume_sfera(10))
# Out: 4186.666666666667

from modulo import area_sfera
print(area_sfera(10))
# Out: 1256.0

from modulo import *
print(volume_sfera(10))
# Out: 4186.666666666667

import math

# logaritmo
print(math.log(10))
# Out: 2.302585092994046

# pi greco
print(math.pi)
# Out: 3.141592653589793

# fattoriale
print(math.factorial(20))
# Out: 2432902008176640000

print(dir(math))
# Out: ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']

help(math.log)
# Out: Help on built-in function log in module math:
# Out: 
# Out: log(...)
# Out:     log(x[, base])
# Out:     
# Out:     Return the logarithm of x to the given base.
# Out:     If the base not specified, returns the natural logarithm (base e) of x.
# Out: 

def cubo(x):
    '''Calcola il cubo di un numero.'''
    return x ** 3

print(cubo(5))
# Out: 125

help(cubo)
# Out: Help on function cubo:
# Out: 
# Out: cubo(x)
# Out:     Calcola il cubo di un numero.
# Out: 

