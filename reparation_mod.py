def repair_solution(solution, intervalo):
    min_value, max_value = intervalo
    solucion_ajustada = []
    #Ajustamos para cada dimension
    for dimension in solution:
        if dimension < min_value: solucion_ajustada.append(min_value)
        elif dimension > max_value: solucion_ajustada.append(max_value)
        else: solucion_ajustada.append(dimension)
    
    return solucion_ajustada