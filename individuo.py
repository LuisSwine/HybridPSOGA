"""
DESARROLLADORES:
    - LUIS ANGEL LOPEZ ALVAREZ
    - JESUS SAYEB PEREZ REYES
    
PROYECTO DE ALGORITMOS BIOINSPIRADOS - HIBRIDO PSO - GA

MODULO: CLASE CROMOSOMA
"""

#Se importan las librerias necesarias de Python
import random
import numpy as np

#Se importan lo modulos necesariosen esta etapa
import encoder_decoder as coder #Modulo codificador y decodificador binario
import reparation_mod as ajust  #Modulos de ajuste de intervalos

#Comenzamos definiendo la clase
class Cromosoma:
    def __init__(self, intervalo, dimensiones, step_size, num_steps, cromosoma_length):
        
        #Carcateristicas
        self.vector_solution = []       #Vector que representa la posicion de la particula, es decir la solución candidata del individuo
        self.bin_code = ""              #Codificación binaria del vector solucion 
        self.fitness = 0                #Aptitud del vector solucion evaluado en la función objetivo
        self.velocidad = 0              #Velocidad de la parte partícula del individuo
        self.best_local_vector = []     #Mejor posición de solución de la particula encontrada
        self.best_local_fitness = 0     #Aptitud de la mejor solución encontrada por la particula
        
        #Variables para la codificacion
        self.step_size = step_size
        self.num_steps = num_steps
        self.cromosoma_length = cromosoma_length
        
        #Parametros de la clase
        self.intervalo = intervalo      #Intervalo de los valores de solución de la funcion objetivo
        self.dimensiones = dimensiones  #Numero de dimensiones del problema

    #FUNCION DE INICIALIZACION DEL INDIVIDUO
    def randomInitialization(self):
        
        #Inicializamos el vector solucion como una lista vacia
        self.vector_solution = []
        
        #Extraemos los limites del intervalo
        lim_inf, lim_sup = self.intervalo
        
        #Iniciamoz el vector solucion con valores aleatorios en el intervalo definido
        self.vector_solution = [round(random.uniform(lim_inf, lim_sup), 3) for _ in self.dimensiones]

        #Inicializamos el vector de velocidad con valores aleatorios
        self.velocidad = [round(random.uniform(lim_inf, lim_sup), 3) for _ in self.dimensiones]
    
        """
        Se añade pequeño parentesís para explicar la inicializacion de los vectores:
            - round(float numero, int decimales): redondea el valor flotante a n numero de decimales
            - random.uniform(lim_inf, lim_sup): genera un numero real en el intervalo dado
            - for _ in self.dimensiones: repetimos el proceso por cada dimension
        En resumen, generamos n numeros reales de 3 decimales, donde n es el numero de dimensiones
        """
        
        #Asignamos o mejor dicho inicializamos el mejor local con el mismo valor del vector solucion
        self.best_local_vector = self.vector_solution
    
        #Ya que tenemos el vector solucion, ahora lo codificamos a binario
        self.encode()
        
        pass
        
    #Funcion de inicializar velocidad para cuando generamos los individuos hijos
    def iniciar_velocidad(self):
        #Extraemos los limites del intervalo definido
        lim_inf, lim_sup = self.intervalo
        
        #Se repite la lógica de inicialización de la función de inicialización del individuo
        self.velocidad = [round(random.uniform(lim_inf, lim_sup), 3) for _ in self.dimensiones]
        
        pass
    
    #Función que ejecuta la codificación binaria
    def encode(self):
        
        #Asignamos al atributo de bin_code la salida de la funcion encode_solution, para detalles, consultar dicha funcion en el modulo encoder_decoder
        self.bin_code = coder.encode_solution(self.vector_solution, self.cromosoma_length, self.step_size, self.intervalo[0])
        
        #Retornamos la codificación binaria
        return self.bin_code
    
    #Función que ejecuta la decodificación binaria
    def decode(self):
        
        #Asignamos al vector solucion la salida de la funcion decode_solution, para mas detalles, consultar dicha funcion
        self.vector_solution = coder.decode_solution(self.bin_code, self.cromosoma_length, self.intervalo[0], self.step_size)
        
        #Retornamos el vector decodificado
        return self.vector_solution
    
    #Funcion que simplemente asigna el valor recibido al fitness del objeto
    def setFitness(self, value):
        self.fitness = value
        
    #Funcion que recibe la funcion objetivo como parametro y asigna la aptitud del vector solucion al fitness
    def evaluateFunction(self, function):
        self.fitness = function(self.vector_solution)
    
    #Función para mostrar los detalles del objeto cuando sea necesario
    def printCromosoma(self):
        print(f"Datos del cromosoma: \n"
              + f"Vector solucion {self.vector_solution} \n"
              + f"Fitness {self.fitness}\n"
              + f"Velocidad {self.velocidad}")
        
    #Funcion que ajusta los valores del vector solucion para verificar que no supere los limites definidos
    def ajustarValores(self):
        #Primero decodificamos la cadena binaria
        self.decode()
        #Ejecutamos nuestra funcion de ajustar valores, para más detalles consultas dicha funcion
        self.vector_solution = ajust.repair_solution(self.vector_solution, self.intervalo)
        #Codificamos la salida para reemplazar la anterior cadena binaria
        self.encode()
    
    #Funcion de PSO para actualizar la velocidad y la posicion de la particula
    def update_position(self, w, c1, c2, gBest):
        
        #Creamos los valores aleatorios entre 0 y 1
        r1 = np.random.rand()
        r2 = np.random.rand()
        
        #Creamos arreglos numpy para hacer más rapido las operaciones entre vectores
        V = np.array(self.vector_solution)  #Creamos un Numpy array con la informacion de la posicion
        X = np.array(self.vector_solution)  #Creamos un Numpy array con la informacion de la velocidad
        pBest = np.array(self.best_local_vector) #Creamos un numpy array con la informacion de la mejor posicion local
        gl_best = np.array(gBest)   #Creamos un Numpy array con la información de la mejor solución global
        
        #Actualizamos la velocida de la particula aplicando la formula del algoritmo
        V = (w * V) + (c1 * r1 * (pBest - X)) + (c2 * r2 * (gl_best - X))
        
        #Actualizamos la posicion
        X = X + V
        
        #Regresamos las numpy arrays a listas
        V.tolist()
        X.tolist()
        
        #Redondeamos los valores de la posicion y la velocidad a 3 decimales
        X = [round(elemento, 3) if isinstance(elemento, float) else elemento for elemento in X]
        V = [round(elemento, 3) if isinstance(elemento, float) else elemento for elemento in V]
        
        """
        Abrimos un pequeño parentesis para explicar como estamos redondeando los elementos de cada vector:
            - round(float, int): redondea el valor float a int numero de decimales
            - isinstance: validamos si el elemento es un valor flotante
            - elemento: iterador sobre nuestro vector
        En resumen asignamos a cada elemento del vector el elemento redondeado a 3 decimales, solo si el elemento
        es un valor flotante, en caso contrario, solo asignamos el elemento de forma directa
        """
        
        #Asignamos la nueva velocidad y el nuevo vector solucion o posicion
        self.velocidad = V
        self.vector_solution = X
        
        pass