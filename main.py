import funciones_objetivo
import hibrido

if __name__ == '__main__':
    
    #Parametros de configuración del problema
    dimensiones = range(10)
    intervalo = [-32.768,32.768] 
    #intervalo = [-2.048,2.048] 
    funcion = funciones_objetivo.ackleyFunction 
    #funcion = funciones_objetivo.rosenbrock
    
    #Parametros que deben configurarse con IRACE
    tam_poblacion = 50
    w = 0.9
    c1 = 1.5
    c2 = 2.5
    prob_cruza = 0.5
    prob_mutacion = 0.3

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