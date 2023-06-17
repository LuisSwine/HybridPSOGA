import random

def seleccion_por_ruleta(population):
    
    #Obtenemos la longitud
    tam_poblacion = len(population)
    
    #Creamos una lista vacia donde iremos guardando los indices de los padres
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
    
    return indices

def uniform_selection(tam_population):
    indices = []
    for i in range(tam_population):
        indice_padre = random.randint(0, tam_population-1)
        indices.append(indice_padre)
    return indices


def seleccion_sobrevivientes_torneo(poblacion, emparejamiento):
    indices = []
    while len(indices) < len(poblacion):
        top = len(poblacion) - 1
        subconjunto = random.sample(range(0, top), emparejamiento)
        
        indice_mejor = subconjunto[0]
        for i in range(1, len(subconjunto)):
            if poblacion[i].fitness < poblacion[indice_mejor].fitness:
                indice_mejor = i
        
        indices.append(indice_mejor)
        
    return indices