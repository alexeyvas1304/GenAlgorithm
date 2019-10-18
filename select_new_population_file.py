import random 
import collections


def elite (population, fitnesses,dictionary):
    
    size = dictionary["size_of_population"]
    d = list(zip(fitnesses, population))
    d.sort(key = lambda d:d[0],reverse = True)
    population = [d[i][1] for i in range(len(d))][:size]
    fitnesses = [d[i][0] for i in range(len(d))][:size]
    return [population,fitnesses]


def trunc(population, fitnesses, dictionary):
    threshold = dictionary["trunc_threshold"]
    size = dictionary["size_of_population"]
    d = list(zip(fitnesses, population))
    d.sort(key = lambda d:d[0],reverse = True)
    d = d[:round(threshold*len(d))]
    result_pop = []
    result_fit = []
    for i in range(size):
        result_pop.append(random.choice(d)[1])
        result_fit.append(random.choice(d)[0])
    return [result_pop,result_fit]


def exclusion(population, fitnesses, dictionary):
    size = dictionary["size_of_population"]
    d = list(zip(fitnesses, population))
    d.sort(key = lambda d:d[0],reverse = True)
    result_pop = []
    result_fit = []
    for element in d:
        if element[1] not in result_pop:
            result_pop.append(element[1])
            result_fit.append(element[0])
    result_pop.extend([d[i][1] for i in range(len(d))])
    result_fit.extend([d[i][0] for i in range(len(d))])
    return [result_pop[:size],result_fit[:size]]