import random

def mutation_probabilistic(individual, mutation_prob):
    # Crear una copia del individuo para no modificarlo directamente
    mutated_individual = ""
    for bit in individual:
        random_prob = random.random()
        if random_prob < mutation_prob:
            mutated_individual += str(1 - int(bit))
        else: mutated_individual += str(bit)
    
    return mutated_individual
