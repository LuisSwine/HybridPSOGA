"""
DESARROLLADORES:
    - LUIS ANGEL LOPEZ ALVAREZ
    - JESUS SAYEB PEREZ REYES
    
PROYECTO DE ALGORITMOS BIOINSPIRADOS - HIBRIDO PSO - GA

MODULO PRINCIPAL DE EJECUCION
"""
#Comenzamos importando los modulos necesarios
import funciones_objetivo
import hibrido

def run(tam_poblacion, w, c1, c2, prob_cruza, prob_mutacion):
    #Parametros de configuración del problema Ackley
    dimensiones = range(10)
    intervalo = [-32.768,32.768] 
    funcion = funciones_objetivo.ackleyFunction 
    
    """
    dimensiones = range(10)
    intervalo = [-2.04800,2.048] 
    funcion = funciones_objetivo.rosenbrock
    
    dimensiones = range(10)
    intervalo = [-5.120,5.120] 
    funcion = funciones_objetivo.rastrigin
    
    dimensiones = range(10)
    intervalo = [-600,600] 
    funcion = funciones_objetivo.griewang
    """
    
    
    hibrido.particulas_geneticas(
        tam_poblacion, 
        dimensiones, 
        intervalo, 
        funcion,
        w,
        c1,
        c2,
        prob_cruza ,
        prob_mutacion 
    )
    pass
    
    

if __name__ == '__main__':
    
    #Parametros que deben configurarse con IRACE
    tam_poblacion = 50
    w = 0.9
    c1 = 1.5
    c2 = 2.5
    prob_cruza = 0.5
    prob_mutacion = 0.3 
   
    """ 
    #Rosenbrock
    tam_poblacion =150
    w = 1
    c1 = 1.5
    c2 = 3
    prob_cruza = 0.5
    prob_mutacion = 0.1 
    """
    
    """ 
    #Rastrigin
    tam_poblacion = 50
    w = 0.9
    c1 = 1.5
    c2 = 2.5
    prob_cruza = 0.5
    prob_mutacion = 0.3 
    """ 
    
    """ 
    #Griewank
    tam_poblacion = 50
    w = 0.9
    c1 = 1.5
    c2 = 2.5
    prob_cruza = 0.5
    prob_mutacion = 0.3 
    """
    
    run(tam_poblacion, w, c1, c2, prob_cruza, prob_mutacion)
   
    
    
    