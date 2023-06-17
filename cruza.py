import random

def cruza_dos_puntos_bin(poblacion, indices):
    
    #Obtenemos la longitud de la poblacion
    tam_poblacion = len(poblacion)
    
    hijos = []
    
    for i in range(0, tam_poblacion, 2):
        
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

        hijos.append(child1)
        hijos.append(child2)

    return hijos

def cruza_uniforme_bin(poblacion, indices, prob_cruza):
    
    tam_poblacion = len(poblacion)
    hijos = []
    
    for i in range(0, tam_poblacion, 2):
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

        hijos.append(child1)
        hijos.append(child2)
    
    return hijos