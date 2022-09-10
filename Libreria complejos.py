import Tarea 1 CNYT as op
import math
import unittest

def producto_tensor(z,w):
"""Calcula el producto tensor entre dos matrices/vectores complejas y arroja
otra matriz
    (z,w) --> tensorial
"""
    xz = len(z)
    xw = len(w)
    tensorial = xz*xw
    return tensorial
def matriz_transpuesta (o):
""" toma un matriz y devuelve su matriz transpuesta
    (o) --> (o**T)
"""
    fila = len(o)
    columna = len(o[0])
    f = [(0,0)] * columna
    transponerla = [f] * fila
    for i in range (fila):
        f = [(0,0)] * columna
        transponerla[i] = f
        for j in range (columna):
            transponerla[i][j] = o[j][i]
    return transponerla
def matriz_conjugada(o):
""" Toma una matriz y retorna su respectiva matriz conjugada
    (o) --> (o**--)
"""
    fila = len(o)
    columna = len(o[0])
    f = [(0,0)] * columna
    conjugarla = [f] * fila
    for i in range (fila):
        f = [(0,0)] * columna
        conjugarla[i] = f
        for j in range (columna):
            conjugarla[i][j] = op.conjugado(o[i][j])
    return conjugarla
    
def matriz_adjunta(o):
""" Toma una matriz y devuelve su adjunta
    (0) --> (o**t)
"""
    fila = len(o)
    columa = len(o[0])
    operacion = [(0,0)] *columna
    adjuntarla = [operacion] * fila
    j = matriz_conjugada(matriz_transpuesta(o))
    for i in range (fila):
        operacion = [(0,0)] *columna
        adjuntarla[i] = operacion
        for j in range (columna):
            adjuntarla[i][j] = 0[i][j]
    return adjuntarla

def matriz_hermitiana(x):
"""Recibe una matriz y determina si es hermitiana o no es hermitiana
    (x)---> (x)
    """
    longitud = len(x)
    k = [[(0,0) for i in range (longitud)] for i in range (longitud)]
    adj = matriz_adjunta(x)
    h = adj == x
    return x
def producto_entre_matrices(x,y):
""" Toma dos matrices complejas y realiza su producto 
    (x,y) --> (x*y)
"""
    fi = len(x)
    co= len(y)
    producto = [[(0,0) for k in range (co)]for l in range (fi)]
    for m in range (fi):
        for n in range(co):
            for o in range(fi):
                producto[m][n] = op.suma(producto[m][n],op.multiplicacion(x[m][o],w[o][n]))
    return producto
                
def matriz_unitaria(r):
""" Determina si una matriz es unitaria o no es unitaria
    (r) --> (r)
"""
    fila = len(r)
    b = [[(0,0) for k in range(fila)] for k in range (fila)]
    c = [[(0,0) for j in range(fila)] for j in range(fila)]
    for k in range (fila):
        b = producto_entre_matrices(matriz_adjunta(r),r)
    for k in range (fila):
        c = [j][j] = (1,0)
        unitaria = b == c
    return unitaria
def distancia_entre_vectores(v,q):
""" Toma dos vectores y determina la distancia entre ellos
    (v,q) --> (z)
"""
    distancia = len(v)
    z = 0
    for i in range (distancia):
        z = z + (op.modulo(op.suma(v[i],q[i])))**2
    z = z **(1/2)
    return z
def norma_de_un_vector(h):
""" determina la norma de un vector
    (h) ---> (int)
"""
    norma = len(h)
    e = (0,0)
    for k in range (norma):
        e = op.suma(op.producto(h[k],h[k]),e)
    e = op.modulo(e)
    return e
def sumar_matrices (s,d):
""" Toma dos matrices y realiza la respectiva suma retornando otra matriz
    (s,d) ---> (sumar)
    """
    longitud = len(s)
    lon = len(s[0])
    f= [(0,0) *lon
    sumar = [f] *longitud
    for k in range (longitud):
        fila = [(0,0)* lon
        sumar[k] = fila
        for j in range (lon):
            sumar[k][j] = op.suma(s[k][j],d[k][j])
    return sumar

def inverso_adictivo(u):
    """ recibe un matriz compleja y retorna su inverso aditivo correspondiente
    (u) ---> (u**-1)
"""
    fila = len(u)
    columna(len(u[0])
    filas = [(0,0)] *columna
    inverso = [filas] * fila
    for i in range (fila):
        filas = [(0,0)] *columna
        inverso[i] = filas
        for h in range (columna):
            inverso[i][h] = op.producto((-1,0),u[i][h])
    return inverso

def producto_escalar_vector(w):
    f = int(input())
    escalar = len(w)
    s = [(0,0)] * num
    for i in range (num):
        s[i] = op.producto((-1,0),v[i])
    return (s)
def inversa_vector(d):
    numero = len(v)
    si = [(0,0)] * numero
    for i in range (numero):
        si[i] = op.producto((-1,0),d[i])
    return (si)
    
        
