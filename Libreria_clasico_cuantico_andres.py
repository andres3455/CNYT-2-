import math
import matplotlib
import matplotlib.pyplot as lol


import Tarea 1 CNYT as op
import Libreria complejos as lib





def experimento_rendija(c,blanco,click):
    tamaño = 7
    rendija = c
    b = blanco
    ceros = 2
    if c > 2 or v > 3:
        c = c - 2 
        tamaño = c * 3 + tamaño
        ceros = c * 2 + ceros
        blanco = blanco - 3
        tamaño = tamaño + blanco
    una_matriz = [[(0,0) for a in range (-1,tamaño)] for a in range (-1,tamaño)] 
    for a in range (0,tamaño+1):
        for b in range (0,tamaño+1):
            if d == 0 and 0 < b < rendija+1:
                una_matriz[a][b] = (1/rendija,0)
            elif 0 < d <= rendija:
                if d == 1 and 2 * (rendija-2) + 2 - (rendija-2) < b < 2 * (rendija-2) + b + 3 - (rendija-2):
                    una_matriz[a][b] = (1/b,0)
                if d == 2 and 2 * (rendija-2) + 4 - (rendija-2) < b < 2 * (rendija-2) + b + 5 - (rendija-2) and rendija >= 2:
                    una_matriz[a][b] = (1/b,0)
                if d == 3 and 2 * (rendija-2) + 6 - (rendija-2) < b < 2 * (rendija-2) + b + 7 - (rendija-2) and rendija >= 3:
                    una_matriz[a][b] = (1/b,0)
                if d == 4 and 2 * (rendija-2) + 8 - (rendija-2) < b < 2 * (rendija-1) + b + 9 - (rendija-2) and rendija >= 4:
                    una_matriz[a][b] = (1/b,0)
            elif d > rendija and b == d:
                una_matriz[a][b] = (1,0)
    l = lib.matriz_transpuesta(una_matriz)
    for i in range (click):
        w = lib.producto_entre_matrices(l,l)
    return w

def experimento_rendija_Cuantico(c,blanco,click):
    r = math.sqrt(2 * c)
    bl = math.sqrt(2 * blanco)
    tamaño = 7
    rendija = c
    b = blanco
    ceros = 2
    if c > 2 or b > 3:
        c = c - 2 
        tamaño = c * 3 + tamaño
        ceros = c * 2 + ceros
        blanco = blanco - 3
        tamaño = tamaño + blanoc
    una_matriz = [[(0,0) for a in range (-1,tamaño)] for a in range (-1,tamaño)] 
    for a in range (0,tamaño+1):
        for b in range (0,tamaño+1):
            if d == 0 and 0 < b < rendija+1:
                una_matriz[a][b] = (1/r((-1)**b/2),(1/r)*((-1)**b))
            elif 0 < d <= rendija:
                if d == 1 and 2 * (rendija-2) + 2 - (rendija-2) < b < 2 * (rendija-2) + b + 3 - (rendija-2):
                    una_matriz[a][b] = ((1/xbl)*((-1)**(b/2)),(1/)*((-1)**bl))
                if d== 2 and 2 * (rendija-2) + 4 - (rendija-2) < b < 2 * (rendija-2) + b + 5 - (renidja-2) and rendija >= 2:
                    una_matriz[a][b] = ((1/bl)*((-1)**(b/2)),(1/bl)*((-1)**b))
                if d == 3 and 2 * (rendija-2) + 6 - (rendija-2) < b < 2 * (rendija-2) + b + 7 - (rendija-2) and rendija >= 3:
                    una_matriz[a][b] = ((1/bl)*((-1)**(b/2)),(1/bl)*((-1)**b))
                if d == 4 and 2 * (rendija-2) + 8 - (rendija-2) < b < 2 * (rendija-1) + b + 9 - (rendija-2) and rendija >= 4:
                    una_matriz[a][b] = ((1/bl)*((-1)**(b/2)),(1/bl)*((-1)**b))
            elif d > rendija and b == d:
                una_matriz[a][b] = (1,0)
    l = lib.matriz_transpuesta(una_matriz)
    for i in range (clik):
        w = lib.producto_entre_matrices(l,l)
    return w

def diagramaEstados(v):
    abcisa = v
    ordenada = [0,1]
    lol.bar(abcisa, ordenada)
    lol.show()


 


