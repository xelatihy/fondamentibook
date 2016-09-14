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
        self.image = QImage(self.width(), self.height(), QImage.Format_ARGB32)
        self.paint_handler = None
        self.info = PaintInfo()
        self.info.size = self.width(), self.height()
        self.setMouseTracking(True)
    def drawing(self):
        painter = QPainter(self.image)
        painter.setRenderHints(QPainter.Antialiasing,True)
        painter.setRenderHints(QPainter.SmoothPixmapTransform,True)
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
        self.image = QImage(self.width(), self.height(), QImage.Format_ARGB32)
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
        if not event.text(): super().keyPressEvent(event)
        self.info.key = event.text()
    def keyReleaseEvent(self,event):
        self.info.key = ''

def run_app(paint,w,h):
    app = QApplication.instance()
    if not app:
        app = QApplication([])
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
