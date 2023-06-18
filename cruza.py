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

#Definimos la funcion de cruza en dos puntos que recibe como parametro la poblacion y los indices de los padres
def cruza_dos_puntos_bin(poblacion, indices):
    
    #Obtenemos la longitud de la poblacion
    tam_poblacion = len(poblacion)
    
    #Inicializamos una lista vacía donde iremos añadiendo los hijos generados
    hijos = []
    
    #Iteramos sobre la poblacion en intervalos de 2
    for i in range(0, tam_poblacion, 2):
        
        #Obtenemos a los padres con los indices de 2 en 2
        parent1 = str(poblacion[indices[i]].bin_code)
        parent2 = str(poblacion[indices[i + 1]].bin_code)
    
        # Seleccionar dos puntos de corte aleatorios
        point1 = random.randint(0, len(parent1) - 1)
        point2 = random.randint(0, len(parent1) - 1)

        # Ordenar los puntos de menor a mayor
        start = min(point1, point2)
        end = max(point1, point2)

        # Crear los descendientes
        child1 = parent1[:start] + parent2[start:end] + parent1[end:]
        child2 = parent2[:start] + parent1[start:end] + parent2[end:]

        #Añadimos los hijos a la lista
        hijos.append(child1)
        hijos.append(child2)

    #Retornamos a los hijos creados
    return hijos

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