# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 15:59:43 2016
"""

def normalizar(texto):
    tn = ""
    for letra in texto:
        indx = ord(letra)
        if 97 <= indx <= 122:
            indx = indx - 32
            tn = tn + chr(indx)
        elif 65 <= indx <= 90:
            tn = tn + letra
    return tn
            

def cesar(texto):
    tn = normalizar(texto)
    tc = ""
    for letra in tn:
        indx = ord(letra) + 1
        if indx == 91:
            indx = 65
        tc = tc + chr(indx)
    return tc
    
def fac(n):
    if n == 0:
        return 0
    else:
        return fac(n - 1) * n
