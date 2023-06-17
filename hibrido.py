import copy

import poblacion
import individuo
import reparation_mod
import parents_selection as ps
import survivors_selection as ss
import cruza
import mutacion

def particulas_geneticas(tam_poblacion, dimensiones, intervalo, funcion, w, c1, c2, prob_cruza, prob_mutacion):
    
    #PASO 1: INICIALIZAMOS LA POBLACION
    swarm = poblacion.Poblacion(tam_poblacion, dimensiones, intervalo, funcion)
    swarm.inicializar_poblacion()
    
    mejor_inidividuo = swarm.getBest()
    
    generacion = 0
    #PASO 2: COMENZAMOS CON LAS ITERACIONES
    while mejor_inidividuo.fitness > 0.001:
        print(f"Generacion: {generacion}")
        generacion+=1
        print(mejor_inidividuo.fitness)
        #PRIMERO HACEMOS LA ACTUALIZACION DE LA VELOCIDAD Y LA POSICION (ETAPA PSO)
        for particula in swarm.poblacion:
            particula.update_position(w, c1, c2, mejor_inidividuo.vector_solution)
            particula.vector_solution = reparation_mod.repair_solution(particula.vector_solution, intervalo)
            
            particula.evaluateFunction(funcion)
            particula.encode()
            if particula.fitness <= particula.best_local_fitness:
                particula.best_local_fitness = particula.fitness
                particula.best_local_vector = particula.vector_solution.copy()
            if particula.fitness <= mejor_inidividuo.fitness:
                mejor_inidividuo = copy.copy(particula)
        
        #SEGUNDO (ETAPA GENETICA)
        #Seleccionamos a los padres
        indices_padres = ps.seleccion_sobrevivientes_torneo(swarm.poblacion, 4)

        #Hacemos la cruza
        hijos = cruza.cruza_uniforme_bin(swarm.poblacion, indices_padres, prob_cruza)

        cromosomas_hijos = []
        for hijo in hijos:
            new_hijo = individuo.Cromosoma(
                intervalo, 
                dimensiones, 
                swarm.step_size, 
                swarm.num_steps, 
                swarm.cromosomas_length)
            new_hijo.bin_code = hijo
            new_hijo.ajustarValores()
            cromosomas_hijos.append(new_hijo)
        hijos = []
        
        #Ahora aplicamos la mutacion a cada hijo
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
            hijo.iniciar_velocidad()
            hijo.best_local_vector = hijo.vector_solution
            hijo.best_local_fitness = hijo.fitness
            #Agregamos los hijos mutados y ajustados a la poblacion
            swarm.poblacion.append(hijo)
    
        #SELECCIONAMOS A LOS SOBREVIVIENTES
        swarm.poblacion = ss.seleccion_por_extincion(swarm.poblacion, tam_poblacion)
        #mejor_inidividuo = swarm.getBest()
    mejor_inidividuo.printCromosoma()
    
    pass