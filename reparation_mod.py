"""
DESARROLLADORES:
    - LUIS ANGEL LOPEZ ALVAREZ
    - JESUS SAYEB PEREZ REYES
    
PROYECTO DE ALGORITMOS BIOINSPIRADOS - HIBRIDO PSO - GA

MODULO DE REPARACION
"""
#Definimos la funcion para reajustar los vectores a los intervalos definidos
def repair_solution(solution, intervalo):
    #Extraemos el limite inferior y superior del intervalo de soluciones
    min_value, max_value = intervalo
    #Inicializamos una lista vacía par almacenar el vector ajustado
    solucion_ajustada = []
    #Ajustamos para cada dimension
    for dimension in solution:
        #Si el valor es menor al limite inferior asignamos el valor del limite inferior
        if dimension < min_value: solucion_ajustada.append(min_value)
        #Si el valor es menor al limite superior asignamos el valor del limite superior
        elif dimension > max_value: solucion_ajustada.append(max_value)
        #Caso contrario asignamos el valor directamente
        else: solucion_ajustada.append(dimension)
    
    #Retornamos el vector ajustado
    return solucion_ajustada