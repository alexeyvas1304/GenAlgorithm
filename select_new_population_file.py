def elite (population, fitness_one,d):
    size = d["size_of_population"]
    population.sort(key = lambda osob : fitness_one(osob),reverse = True)
    population = population[:size]
    return population