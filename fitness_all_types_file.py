def minimum(population,fitness_one):
    return min(fitness_one(osob) for osob in population)

def maximum(population,fitness_one):
    return max(fitness_one(osob) for osob in population)

def average(population,fitness_one):
    return sum(fitness_one(osob) for osob in population)/len(population)