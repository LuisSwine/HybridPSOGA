"""
DESARROLLADORES:
    - LUIS ANGEL LOPEZ ALVAREZ
    - JESUS SAYEB PEREZ REYES
    
PROYECTO DE ALGORITMOS BIOINSPIRADOS - HIBRIDO PSO - GA

MODULO: FUNCIONES DE MUTACIÓN
"""
#Comenzamos importando las librerías necesarias
import random

#Definimos nuestra función de mutación probabilística
def mutation_probabilistic(individual, mutation_prob):
    
    #Iniciamos una nueva cadena del individuo para almacenar el resultado
    mutated_individual = ""
    
    #Iteramos sobre los caracteres de nuestra cadena binaria del individuo
    for bit in individual:
        #Creamos una probabilidad aleatoria entre 0 y 1
        random_prob = random.random()
        #Si la probabilidad es menor igual a la probabilidad de mutación cambiamos el valor de 0 a 1 o viceversa
        if random_prob < mutation_prob:
            mutated_individual += str(1 - int(bit))
        else: #Caso contrario añadimos el bit sin alteración 
            mutated_individual += str(bit)
    
    #Retornamos nuestro individuo mutado
    return mutated_individual
