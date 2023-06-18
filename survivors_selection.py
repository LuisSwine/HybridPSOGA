"""
DESARROLLADORES:
    - LUIS ANGEL LOPEZ ALVAREZ
    - JESUS SAYEB PEREZ REYES
    
PROYECTO DE ALGORITMOS BIOINSPIRADOS - HIBRIDO PSO - GA

MODULO: SELECCION DE SOBREVIVIENTES
"""
#Definimos la estrategia elitista por extinción
def seleccion_por_extincion(poblacion, tamano_seleccion):
    #Ordenamos la poblacion de forma ascendente con base en su aptitud
    sorted_population = sorted(poblacion, key = lambda x: x.fitness)
    #Conservamos unicamente a los n mejores individuos
    new_population = sorted_population[:tamano_seleccion]
    #Retornamos la nueva población
    return new_population
