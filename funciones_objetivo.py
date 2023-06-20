"""
DESARROLLADORES:
    - LUIS ANGEL LOPEZ ALVAREZ
    - JESUS SAYEB PEREZ REYES
    
PROYECTO DE ALGORITMOS BIOINSPIRADOS - HIBRIDO PSO - GA

MODULO: FUNCIONES OBJETIVO
"""
#Comenzamos importando las librerías necesarias
import numpy as np
import math
from functools import reduce
from operator import mul

#Definimos nuestra funcion Ackley
def ackleyFunction(x):
    n = len(x)
    a = 20
    b = 0.2
    c = 2 * np.pi
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += x[i] ** 2
        sum2 += np.cos(c*x[i])
    
    term1 = -a * np.exp(-b * np.sqrt(1/n * sum1))
    term2 = -np.exp(1/n * sum2)
    result = term1 + term2 + a + np.exp(1)
    
    #Retornamos el valor con una precision de 3 decimales
    return round(result, 3)

def rastrigin(vector):
    n = len(vector)
    A = 10
    sum = 0

    for i in range(n):
        x = vector[i]
        sum += x**2 - A * math.cos(2 * math.pi * x)

    new_r = A * n + sum
    
    return round(new_r,3)

def griewang(vector):
    n = len(vector)
    sum_sq = sum([(x ** 2) / 4000 for x in vector])
    prod_cos = reduce(mul, [math.cos(x / math.sqrt(i+1)) for i, x in enumerate(vector)])
    result = 1 + sum_sq - prod_cos
    return round(result, 3)

#Definimos nuestra función rosenbrock
def rosenbrock(x):
    sumatoria = 0
    for i in range(len(x)-1):
        sumatoria += 100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2
        
    #Retornamos el valor con una precision de 3 decimales
    return round(sumatoria, 3)