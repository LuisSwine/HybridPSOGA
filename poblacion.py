"""
DESARROLLADORES:
    - LUIS ANGEL LOPEZ ALVAREZ
    - JESUS SAYEB PEREZ REYES
    
PROYECTO DE ALGORITMOS BIOINSPIRADOS - HIBRIDO PSO - GA

MODULO: CLASE POBLACION
"""
#Comenzamos importando los modulos necesarios
import encoder_decoder as coder
import individuo

#Definimos nuestra clase población
class Poblacion:
    def __init__(self, tam_poblacion, dimensiones, intervalo, funcion):
        
        #Parametros de la clase
        self.dimensiones = dimensiones      #Número de dimensiones o variables del problema
        self.intervalo = intervalo          #Intervalo de soluciones
        self.funcion = funcion              #Funcion a minimizar
        self.tam_poblacion = tam_poblacion  #Tamaño de la población
        
        #Creamos las variables de codificacion binaria utilizando el modulo correspondiente
        self.cromosomas_length = coder.calculate_lenght(intervalo, 3)           #Longitud de cada cromosoma
        self.num_steps = coder.calculate_num_steps(self.cromosomas_length)      #Calculo del numero de pasos
        self.step_size = coder.calculate_step_size(intervalo, self.num_steps)   #Calcuo del tamao de paso
        
        #Lista que almacenara todos los individuos de la población
        self.poblacion = []
        
        pass
    
    #Definimos el método para inicializar la población    
    def inicializar_poblacion(self):
        #Limpiamos la lista con la población
        self.poblacion = []
        
        #Iteramos a trab+es del tamaño de población
        for _ in range(self.tam_poblacion):
            #Creamos un nuevo objeto de la clase cromosoma pasando sus respectivos parametros
            new_individuo = individuo.Cromosoma(self.intervalo, self.dimensiones, self.step_size, self.num_steps, self.cromosomas_length)
            #Utilizamos el método randomInitialization para inicializar el objeto
            new_individuo.randomInitialization()
            #Asignamos el fitness
            new_individuo.evaluateFunction(self.funcion)
            #Como parte de la hibridación con PSO asignamos el óptimo local
            new_individuo.best_local_fitness = new_individuo.fitness
            #Añaimos el objeto a la población
            self.poblacion.append(new_individuo)
        pass
    
    #Definimos el método para actualizar el fitness de cada individuo o particula
    def setAllFitness(self):
        #Recorremos la población
        for individuo in self.poblacion:
            #Evaluamos la funcion con el método de cada cromosoma
            individuo.evaluateFunction(self.funcion)
        pass
            
    #Definimos el método para imprimir de forma directa toda la población
    def printPoblacion(self):
        #Recorremos la población
        for individuo in self.poblacion:
            #Para cada individuo llamamos a su método printCromosoma
            individuo.printCromosoma()
        pass
    
    #Definimos el método para obtener al mejor individuo de la población
    def getBest(self):
        #Ordenamos a los individuos con base en su aptutud de forma ascendente
        poblacion_ordenada = sorted(self.poblacion, key= lambda x: x.fitness)
        #Al ser una optimización de minimización el mejor fitness el menor, osea el primer individuo
        best = poblacion_ordenada[0]
        #Retornamos al mejor cromosoma
        return best
    
    #Definimos el método para obtener el peor individuo de la población
    def getWorst(self):
        #Ordenamos a los individuos con base en su aptitud de forma ascendente
        poblacion_ordenada = sorted(self.poblacion, key= lambda x: x.fitness)
        #Recuperamos el último objeto, es decir aquel que tiene la aptitud más alta
        best = poblacion_ordenada[-1]
        #Retornamos el peor cromosoma
        return best
    
    #Definimos el método para obtener el promedio de los fitness
    def getProm(self):
        sumatoria = 0
        for individuo in self.poblacion:
            sumatoria += individuo.fitness
        prom = sumatoria / len(self.poblacion)
        return prom
        