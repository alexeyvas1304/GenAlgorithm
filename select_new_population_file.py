import random

def elite (population, fitness_one,d):
    size = d["size_of_population"]
    population.sort(key = lambda osob : fitness_one(osob),reverse = True)
    population = population[:size]
    return population


def exclusion(population, fitness_one, dictionary):
    size = dictionary["size_of_population"]
    result = []
    population.sort(key=lambda osob: fitness_one(osob), reverse=True)
    for individual in population:
        if individual not in result:
            result.append(individual)
    result.append(population)
    return result[:size]


def trunc(population, fitness_one, dictionary):
    threshold = dictionary["trunc_threshold"]
    size = dictionary["size_of_population"]
    population.sort(key=lambda individual: fitness_one(individual), reverse=True)
    return [random.choice(population[:round((1-threshold) * size)]) for _ in range(size)]
