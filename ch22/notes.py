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


try:
    l = [1,2,3]
    l[10]           # causa un errore
    print('ciao')   # non viene esguita
except:
    print('errore gestito')
# Out: errore gestito

def load_page(url):
    '''Ritorna la pagina HTML dato un URL.'''
    return ''

def get_links(url, html):
    '''Ritorna i links in un HTML.'''
    return []

def web_crawl(url, maxvisits=5):
    '''Visita il grafo del web a partire dall'url 
    url e stampa i siti visitati. Visita al massimo
    maxvisits.'''
    # URL visitati
    visited = set()           
    # URL da visitare
    active = set([url])       
    # Finchè ci sono nodi attivi
    while active and len(visited) < maxvisits: 
        # Insieme dei nuovi attivi    
        newactive = set()                          
        # Finchè ci sono nodi attivi,
        while active and len(visited) < maxvisits:
            # estrai un nodo da active 
            url = active.pop()           
            # se già visitato, continua
            if url in visited: continue  
            # scarica la pagina, aggiungi a visitati
            print('loading page:',url)
            html = load_page(url)        
            visited.add(url)             
            # verifica se lo scaricamento è ok
            if not html: continue        
            # trova i link
            links = get_links(url,html)  
            # per ogni pagina linkata e non visitata   
            for link in links:           
                if link not in visited:
                    # aggiungi ai nuovi attivi
                    newactive.add(link)
        # I nuovi attivi diventano gli attivi
        active = newactive      
    return visited

import requests

def load_page(url):
    '''Ritorna la pagina HTML dato un URL.'''
    try:
        page = requests.get(url,timeout=1)
        if page.encoding:
            return page.content.decode(
                page.encoding)
        else:
            return page.content.decode('utf8')
    except:
        return ''

sites = web_crawl('http://python.org')
# Out: loading page: http://python.org

import html5lib
import urllib

def get_links(url,html):
    '''Ritorna i links in un HTML.'''
    try:
        links = []
        document = html5lib.parse(html,
            namespaceHTMLElements=False)
        for link_elem in document.iter('a'):
            link = link_elem.get('href')
            # Manca l'url del link
            if not link: continue       
            # ignoriamo referenze interne
            if '#' in link: continue    
            # link locale, aggiungiamo l'url
            if '://' not in link:       
                link = urllib.parse.urljoin(url,
                    link)
            # ci sono ancora errori, saltiamo
            if '://' not in link: continue
            # normalizziamo url
            link = urllib.parse.urljoin(link,'.') 
            links += [link]
        return links
    except:
        return []

sites = web_crawl('http://python.org',maxvisits=15)
# Out: loading page: http://python.org

