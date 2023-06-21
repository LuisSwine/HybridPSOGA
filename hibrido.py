"""
DESARROLLADORES:
    - LUIS ANGEL LOPEZ ALVAREZ
    - JESUS SAYEB PEREZ REYES
    
PROYECTO DE ALGORITMOS BIOINSPIRADOS - HIBRIDO PSO - GA

MODULO: PRINICIPAL HIBRIDACION
"""
#Comenzamos importando las librerías necesarias
import copy

#Despues importamos todos los modulos requeridos
import poblacion
import individuo
import reparation_mod
import parents_selection as ps
import survivors_selection as ss
import cruza
import mutacion

#Definimos la funcion principal con sus respectivos parametros
def particulas_geneticas(tam_poblacion, dimensiones, intervalo, funcion, w, c1, c2, prob_cruza, prob_mutacion):
    
    #PASO 1: INICIALIZAMOS LA POBLACION
    swarm = poblacion.Poblacion(tam_poblacion, dimensiones, intervalo, funcion)
    swarm.inicializar_poblacion()
    
    #Despues obtenemos el mejor individuo y se almacena
    mejor_inidividuo = swarm.getBest()
    
    #Inicializamos nuestro contador de generaciones
    generacion = 0
    
    hitorial_mejores = []
    historial_peores = []
    historial_promedio = []
    
    mejor = swarm.getBest()
    peor = swarm.getWorst()
    promedio = swarm.getProm()
    
    hitorial_mejores.append(mejor.fitness)
    historial_peores.append(peor.fitness)
    historial_promedio.append(promedio)
    
    
    #PASO 2: COMENZAMOS CON LAS ITERACIONES HASTA EL CRITERIOR DE PARO
    while mejor_inidividuo.fitness > 0.001 or generacion > 10000:
        
        #Imprimimos la generacion en la que se encuentra el agoritmo
        print(f"Generacion: {generacion}")
        #Incrementamos el contador de generaciones
        generacion+=1
        #Imprimimos el fitness del mejor individuo
        print(mejor_inidividuo.fitness)
        
        #PRIMERO HACEMOS LA ACTUALIZACION DE LA VELOCIDAD Y LA POSICION (ETAPA PSO)
        #Iteramos todas las particulas del cumulo
        for particula in swarm.poblacion:
            #Para cada particula actualizamos su posicion utilizando el respectivo método
            particula.update_position(w, c1, c2, mejor_inidividuo.vector_solution)
            #Una vez actualizada la posicion ajustamos sus valores con el modulo de reparacion
            particula.vector_solution = reparation_mod.repair_solution(particula.vector_solution, intervalo)
            
            #Evaluamos la aptitud de la nueva posicion
            particula.evaluateFunction(funcion)
            #Codificamos la solución para asignarla a la codificacion del individuo
            particula.encode()
            
            #Validamos si actualizamos los optimos locales y el global
            if particula.fitness <= particula.best_local_fitness:
                #Actualizamos el óptimo local
                particula.best_local_fitness = particula.fitness                #Actualizamos aptitud
                particula.best_local_vector = particula.vector_solution.copy()  #Actualizamos vector
            if particula.fitness <= mejor_inidividuo.fitness:
                #Actualizamos el óptimo global
                mejor_inidividuo = copy.copy(particula)
        
        #SEGUNDO (ETAPA GENETICA)
        #Seleccionamos a los padres usando el modulo de seleccion
        indices_padres = ps.seleccion_torneo(swarm.poblacion, 4)

        #Hacemos la cruza utilizando el modulo de cruza
        hijos = cruza.cruza_uniforme_bin(swarm.poblacion, indices_padres, prob_cruza)

        #Crreamos una lista vacía para almacenar a los hijos codificados
        cromosomas_hijos = []
        #Iteramos los hijos creados
        for hijo in hijos:
            #Transformamos cada hijo en un individuo con sus respectivos parametros
            new_hijo = individuo.Cromosoma(
                intervalo, 
                dimensiones, 
                swarm.step_size, 
                swarm.num_steps, 
                swarm.cromosomas_length
                )
            #Codificamos el vector solución de cada hijo
            new_hijo.bin_code = hijo
            #Ajustamos los valores del vector generado
            new_hijo.ajustarValores()
            #Añadimos cada objeto hijo a la lista de hijos
            cromosomas_hijos.append(new_hijo)
        #Para optimizar el uso de memoria vacíamos la lista anterior de hiijos
        hijos = []
        
        #Ahora aplicamos la mutación a cada hijo
        for hijo in cromosomas_hijos:
            #Primero obtenemos la codificacion binaria del vector_solution
            binary_code = hijo.bin_code
            #Ahora aplicamos la mutación binaria
            mutated = mutacion.mutation_probabilistic(binary_code, prob_mutacion)
            #Asignamos el valor mutado al cromosoma
            hijo.bin_code = mutated
            #Por ultimo ajusramos la mutacion para el cromosoma no quede fuera de los parametros
            hijo.ajustarValores()
            #Calculamos el fitness de cada hijo 
            hijo.evaluateFunction(funcion)
            #Inicializamos de forma aleatoria la velocidad de cada particula
            hijo.iniciar_velocidad()
            #Asignamos el mejor vector local
            hijo.best_local_vector = hijo.vector_solution
            #Asiganmos el mejor fitness local
            hijo.best_local_fitness = hijo.fitness
            #Agregamos los hijos mutados y ajustados a la poblacion
            swarm.poblacion.append(hijo)
    
        #SELECCIONAMOS A LOS SOBREVIVIENTES CON EL RESPECTIVO MODULO
        swarm.poblacion = ss.seleccion_por_extincion(swarm.poblacion, tam_poblacion)
        
        mejor = swarm.getBest()
        peor = swarm.getWorst()
        promedio = swarm.getProm()
        
        hitorial_mejores.append(mejor.fitness)
        historial_peores.append(peor.fitness)
        historial_promedio.append(promedio)
    
    return generacion, mejor.fitness, peor.fitness, promedio, mejor.vector_solution, hitorial_mejores, historial_peores, historial_promedio
    
    
