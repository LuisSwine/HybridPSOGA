"""
DESARROLLADORES:
    - LUIS ANGEL LOPEZ ALVAREZ
    - JESUS SAYEB PEREZ REYES
    
PROYECTO DE ALGORITMOS BIOINSPIRADOS - HIBRIDO PSO - GA

MODULO: CRUZA

Aqui definos la(s) estrategias de cruza que estaremos utilizando
"""

#Comenzamos importando las clases necesarias
import random

#Definimos la función para la cruza uniforme binaria, recibimos como parámetros la población, los inidices de los padres y la probabilidad de cruza
def cruza_uniforme_bin(poblacion, indices, prob_cruza):
    
    #Obtenemos la longitud de la población
    tam_poblacion = len(poblacion)
    
    #Inicializamos una lista vacía donde almacenaremos los hijos creados
    hijos = []
    
    #Iteramos en intervalos de 2 en 2 sobre el tamaño de la población
    for i in range(0, tam_poblacion, 2):
        #Obtenemos las codificaciones binarias de los padres
        parent1 = poblacion[indices[i]].bin_code
        parent2 = poblacion[indices[i+1]].bin_code
    
        # Crear los descendientes
        child1 = ""
        child2 = ""

        # Cruzamiento uniforme
        for i in range(len(parent1)):
            if random.random() < prob_cruza:
                child1 += parent1[i]
                child2 += parent2[i]
            else:
                child1 += parent2[i]
                child2 += parent1[i]

        #Añadimos los hijos a la lista
        hijos.append(child1)
        hijos.append(child2)
    
    #Retornamos la lista con los hijos
    return hijos