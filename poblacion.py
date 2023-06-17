import random

import encoder_decoder as coder
import individuo

class Poblacion:
    def __init__(self, tam_poblacion, dimensiones, intervalo, funcion):
        
        #Parametros de la clase
        self.dimensiones = dimensiones
        self.intervalo = intervalo
        self.funcion = funcion
        self.tam_poblacion = tam_poblacion
        
        #Creamos las variables de codificacion
        self.cromosomas_length = coder.calculate_lenght(intervalo, 3)
        self.num_steps = coder.calculate_num_steps(self.cromosomas_length)
        self.step_size = coder.calculate_step_size(intervalo, self.num_steps)
        
        #Poblacion
        self.poblacion = [] 
        
    def inicializar_poblacion(self):
        self.poblacion = []
        
        for _ in range(self.tam_poblacion):
            new_individuo = individuo.Cromosoma(self.intervalo, self.dimensiones, self.step_size, self.num_steps, self.cromosomas_length)
            new_individuo.randomInitialization()
            new_individuo.evaluateFunction(self.funcion)
            new_individuo.best_local_fitness = new_individuo.fitness
            self.poblacion.append(new_individuo)
            
        pass
    
    def setAllFitness(self, funcion):
        for individuo in self.poblacion:
            #Evaluamos la funcion
            individuo.evaluateFunction(self.funcion)
            
    def printPoblacion(self):
        for individuo in self.poblacion:
            individuo.printCromosoma()
    
    
    def getBest(self):
        #Primero asignamos todos los fitness a cada cromosoma
        poblacion_ordenada = sorted(self.poblacion, key= lambda x: x.fitness)
        best = poblacion_ordenada[0]
        return best
    
    def getWorst(self, funcion):
        #Primero asignamos todos los fitness a cada cromosoma
        poblacion_ordenada = sorted(self.poblacion, key= lambda x: x.fitness)
        best = poblacion_ordenada[-1]
        return best
    
    def getProm(self):
        sumatoria = 0
        for individuo in self.poblacion:
            sumatoria += individuo.fitness
        prom = sumatoria / len(self.poblacion)
        return prom
        