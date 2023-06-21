#Comenzamos importando los modulos necesarios
import funciones_objetivo
import hibrido
import matplotlib.pyplot as plt


def run_anova(prefijo, dimensiones, intervalo, funcion, tam_poblacion, w, c1, c2, prob_cruza, prob_mutacion):
    
    ruta_archivo = f"{prefijo}results.txt"
    archivo = open(ruta_archivo, 'w')
    archivo.write('EJECUCION,GENERACIONES,MEJOR,PEOR,PROMEDIO,MEJOR_VECTOR')
    archivo.close()
    
    for i in range(10):
        archivo = open(ruta_archivo, 'a')
        generacion, mejor, peor, promedio, vector_mejor, historial_mejores, historial_peores, historial_promedio = hibrido.particulas_geneticas(tam_poblacion,dimensiones, intervalo,funcion,w,c1,c2,prob_cruza,prob_mutacion)
    
        texto = f"\n{i+1},{generacion},{mejor},{peor},{promedio},'{vector_mejor}'"
        
        archivo.write(texto)
        archivo.close()
        
        # Graficar los resultados
        generaciones = range(generacion+1)
        
        plt.clf()
        plt.plot(generaciones, historial_mejores, label='Mejores')
        plt.plot(generaciones, historial_peores, label='Peores')
        plt.plot(generaciones, historial_promedio, label='Promedio')

        plt.xlabel('Generaciones')
        plt.ylabel('Aptitud')
        plt.title('Resultados del algoritmo genético')
        plt.legend()

        ruta = prefijo + str(i+1) + '.png'
        plt.savefig(ruta)
    
    pass




if __name__ == '__main__':
    
    #Configurciones de las funciones
    #ACKLEY 
    dimensiones = range(10)
    intervalo = [-32.768,32.768] 
    funcion = funciones_objetivo.ackleyFunction 
    
    """ #GRIEWANK
    dimensiones = range(10)
    intervalo = [-600,600] 
    funcion = funciones_objetivo.griewang """
    
    
    #Parametros
    tam_poblacion = 50
    #tam_poblacion = 100
    
    w = 0.9
    #w = 0.5
    
    #c1 = 1.5
    c1 = 1
    
    c2 = 2.5
    #c2 = 3
    
    prob_cruza = 0.5
    #prob_cruza = 0.25
    
    #prob_mutacion = 0.3 
    prob_mutacion = 0.09
    
    prefijo = 'Ackley_50_09_1_25_05_009/'
    
    run_anova(prefijo,dimensiones, intervalo, funcion, tam_poblacion, w, c1, c2, prob_cruza, prob_mutacion)
    
    pass