import math

""" Toma dos pares ordenados y los pasa a  numeros complejos
"""
def complejos(z):
        print(str(z[0])+'+'+str(z[1])+'i')

""" Recibe dos numero complejos y realiza la suma
como tercer argumento a la hora de hacer una resta, se coloca "-"
"""
def suma(x,y,suma="+"):
        if suma=="+":
                parte_real=(x[0]+y[0])
                parte_imaginaria=(x[1]+y[1])
        else:
                parte_real = (x[0] - y[0])
                parte_imaginaria = (x[1] - y[1])
        return (parte_real,parte_imaginaria)

"""Recibe dos numero complejos y realiza la multiplicacion
"""
def multiplicacion(x,y):
        parte_real=(x[0]*y[0])-(x[1]*y[1])
        parte_imaginaria=(x[0]*y[1])+(x[1]*y[0])
        return (parte_real,parte_imaginaria)

"""Recibe dos numeros complejos y realiza la división
"""
def division(x,y):
        parte_real=((x[0]*y[0])+(x[1]*y[1]))/((x[0]**2)+(y[1]**2))
        parte_imaginaria=((y[0]*x[1])-(x[0]*y[1]))/((y[0]**2)+(y[1]**2))
        return (parte_real,parte_imaginaria)

""" Calcula el modulo
"""
def modulo(x):
        return math.sqrt((x[0]**2)+(x[1]**2))

"""Retorna el conjugado del factor dado
"""
def conjugado(z):
        return (z[0],-1*z[1])

""" Realiza la conversion de una representacion polar a cartesiana
"""
def polar_a_catersiano(x):
        parte_real=x[0]*math.cos(x[1])
        parte_imaginaria =x[0]*math.sin(x[1])
        return (parte_real,parte_imaginaria)

