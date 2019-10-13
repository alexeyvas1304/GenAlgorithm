def minimum(fitnesses):
    return min(fitnesses)

def maximum(fitnesses):
    return max(fitnesses)

def average(fitnesses):
    return sum(fitnesses)/len(fitnesses)


# def average(population,fitness_one):
#     return sum(fitness_one(osob) for osob in population)/len(population)