import random
import math

def calculate_num_steps(chromosome_length):
    return 2 ** chromosome_length

def calculate_step_size(intervalo, num_steps):
    min_value, max_value = intervalo
    
    min_value -= 0.001
    max_value += 0.001
    
    return (max_value - min_value) / num_steps

#Calculamos la longitud de la cadena binaria
def calculate_lenght(intervalo, precision):
    
    #Obtenemso el minimo  y el máximo valor del intervalo de valores
    min_value, max_value = intervalo
    
    min_value -= 0.001
    max_value += 0.001
    
    #Calulamos el argumento 10^numero_decimales
    argument = 10 ** precision
    
    #Calculamos la longitud total en base a la formula
    length = math.log2((max_value * argument) - (min_value * argument))
    
    #Redondeamos hacia arriba un posible valor decimal
    length = math.ceil(length)
    
    #Retornamos la longitud
    return int(length)

# Función para codificar una solución en un cromosoma binario
def encode_solution(solution, chromosome_length, step_size, min_value):
    #Inicializamos el cromosma como una cadena vacía. 
    chromosome = ""
    
    for dimension in solution:
        # Convertir el valor en la dimensión en un paso discreto
        rounded_value = round(dimension, 3)
        
        step = int(round((rounded_value - min_value) / step_size))
        
        # Convertir el paso discreto en una cadena binaria
        binary = bin(step)[2:].zfill(chromosome_length)
        
        chromosome += binary
    
    return chromosome

# Función para decodificar una solución a partir de un cromosoma binario
def decode_solution(chromosome, chromosome_length, min_value, step_size):
    
    
    solution = []
    for i in range(0, len(chromosome), chromosome_length):
        # Obtener la cadena binaria para la dimensión actual
        binary = chromosome[i:i+chromosome_length]
        # Convertir la cadena binaria en un paso discreto
        step = int(binary, 2)
        # Convertir el paso discreto en un valor en la dimensión
        dimension_value = min_value + (step * step_size) + (step_size / 2)
        dimension_value = round(dimension_value, 3)
        solution.append(dimension_value)
        
    
    return solution