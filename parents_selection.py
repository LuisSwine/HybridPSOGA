"""
DESARROLLADORES:
    - LUIS ANGEL LOPEZ ALVAREZ
    - JESUS SAYEB PEREZ REYES
    
PROYECTO DE ALGORITMOS BIOINSPIRADOS - HIBRIDO PSO - GA

MODULO: ESTRATEGIAS DE SELECCION DE PADRES
"""
#Comenzamos importando las librerías necesarias
import random

#Definimos la estrategia de seleccion de padres por torneo
def seleccion_torneo(poblacion, emparejamiento):
    #Creamos una lista vacía donde almacenaremos los indices de los padres seleccioandos
    indices = []
    
    #Mientras la lista no este completa
    while len(indices) < len(poblacion):
        #Obtenemos el indice limite superior
        top = len(poblacion) - 1
        #Generamos un subconjunto aleatorio de la población de tamaño acorde al emparejamiento especifciado
        subconjunto = random.sample(range(0, top), emparejamiento)
        
        #Obtenemos el indice del individuo con el mejor fitness
        indice_mejor = subconjunto[0]
        for i in range(1, len(subconjunto)):
            if poblacion[i].fitness < poblacion[indice_mejor].fitness:
                indice_mejor = i
        
        #Añadimos el indice a la lista de indices
        indices.append(indice_mejor)
        
    #Retornamos la lista de indices
    return indices