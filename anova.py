"""
DESARROLLADORES:
    - LUIS ANGEL LOPEZ ALVAREZ
    - JESUS SAYEB PEREZ REYES
    
PROYECTO DE ALGORITMOS BIOINSPIRADOS - HIBRIDO PSO - GA

MODULO PRINCIPAL DE EJECUCION PARA MUESTRAS DE ANOVA
"""
#Comenzamos importando los modulos necesarios
import funciones_objetivo
import hibrido
import matplotlib.pyplot as plt

#Definimos la funcion para ejecutar el sistema
def run_anova(prefijo, dimensiones, intervalo, funcion, tam_poblacion, w, c1, c2, prob_cruza, prob_mutacion):
    
    #Definimos la ruta del archivo de estadísticas
    ruta_archivo = f"{prefijo}results.txt"
    #Abrimos el archivo
    archivo = open(ruta_archivo, 'w')
    #Escribimos los encabezados
    archivo.write('EJECUCION,GENERACIONES,MEJOR,PEOR,PROMEDIO,MEJOR_VECTOR')
    #Cerramos el archivo
    archivo.close()
    
    #Definimos el numero de ejecuciones a realizar en el range del siguiente for
    for i in range(1):
        #Abrimos el archivo en modo append para no sobreescribirlo
        archivo = open(ruta_archivo, 'a')
        #Ejecutamos nuestro sistema
        generacion, mejor, peor, promedio, vector_mejor, historial_mejores, historial_peores, historial_promedio = hibrido.particulas_geneticas(tam_poblacion,dimensiones, intervalo,funcion,w,c1,c2,prob_cruza,prob_mutacion)
    
        #Añadimos los resultados de la ejecución al archivo de salida
        texto = f"\n{i+1},{generacion},{mejor},{peor},{promedio},'{vector_mejor}'"
        archivo.write(texto)
        #Cerramos el archivo para no perder progreso de ejecuciones previas en caso de alguna interrupcion 
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

        #Guardamos la gráfica como imagen con el número de ejecución
        ruta = prefijo + str(i+1) + '.png'
        plt.savefig(ruta)
    
    pass

if __name__ == '__main__':
    
    #Configurciones de las funciones
    """ #ACKLEY 
    dimensiones = range(10)
    intervalo = [-32.768,32.768] 
    funcion = funciones_objetivo.ackleyFunction  """
    
    #GRIEWANK
    dimensiones = range(10)
    intervalo = [-600,600] 
    funcion = funciones_objetivo.griewang
    
    
    #Parametros
    #tam_poblacion = 50
    tam_poblacion = 100
    
    w = 0.9
    #w = 0.5
    
    c1 = 1.5
    #c1 = 1
    
    #c2 = 2.5
    c2 = 3
    
    #prob_cruza = 0.5
    prob_cruza = 0.25
    
    #prob_mutacion = 0.3 
    prob_mutacion = 0.09
    
    #Se recomienda crear una carpeta objetivo y escribir el prefijo en la siguiente variable
    prefijo = 'Griewank_100_09_15_3_025_009/'
    
    #Ejecutamos el sistema
    run_anova(prefijo,dimensiones, intervalo, funcion, tam_poblacion, w, c1, c2, prob_cruza, prob_mutacion)
    
    pass