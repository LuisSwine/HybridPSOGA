"""
DESARROLLADORES:
    - LUIS ANGEL LOPEZ ALVAREZ
    - JESUS SAYEB PEREZ REYES
    
PROYECTO DE ALGORITMOS BIOINSPIRADOS - HIBRIDO PSO - GA

MODULO: ESTRATEGIAS DE SELECCION DE PADRES
"""
#Comenzamos importando las librerías necesarias
import random

#Definimos la estrategia de selección por ruleta
def seleccion_por_ruleta(population):
    
    #Obtenemos la longitud de la población
    tam_poblacion = len(population)
    
    #Creamos una lista vacia donde iremos guardando los indices de los padres seleccionados
    indices = []

    # 1. Calcular la suma total de todos los valores de aptitud de la población.
    total_fitness = 0
    for individuo in population:
        total_fitness += individuo.fitness
        
    # 2. Calcular la probabilidad de selección de cada individuo como su valor de aptitud dividido por la suma total de aptitudes.
    selection_probabilities = []
    for individuo in population:
        valor = individuo.fitness / total_fitness
        selection_probabilities.append(valor)

    for i in range(tam_poblacion):
        # 3. Generar un número aleatorio entre 0 y 1.
        r = random.random()

        # 4. Iterar sobre la población y sumar las probabilidades de selección de cada individuo hasta que la suma sea mayor que el número aleatorio generado en el paso anterior.
        cumulative_probability = 0
        for i in range(len(selection_probabilities)):
            cumulative_probability += selection_probabilities[i]
            if cumulative_probability >= r:
                selected_parent = i
                break

        # 5. Devolver el individuo correspondiente a la última probabilidad de selección sumada.
        indices.append(selected_parent)
    
    #Retornamos los indices generados
    return indices

#Definimos la estrategia de selección uniforme
def uniform_selection(tam_population):
    #Creamos una lista vacía donde almacenaremos los indices de los padres seleccionados
    indices = []
    
    #Iteramos sobre el tamaño de la población
    for _ in range(tam_population):
        #Generamos un numero aleatorio entre 0 y el tamaño de la población
        indice_padre = random.randint(0, tam_population-1)
        #El numero generado corresponde al indice del padre seleccionado
        indices.append(indice_padre)
    
    #Retornamos la lista de indices generada
    return indices

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