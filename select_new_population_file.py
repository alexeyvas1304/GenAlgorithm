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
    d = d[:round(threshold*size)]
    result_pop = []
    result_fit = []
    for i in range(size):
        c = random.randint(0,len(d)-1)
        result_pop.append(d[c][1])
        result_fit.append(d[c][0])
    return [result_pop,result_fit]


def exclusion(population, fitnesses, dictionary):
    size = dictionary["size_of_population"]
    d = list(zip(fitnesses, population))
    d.sort(key = lambda d:d[0],reverse = True)
    result_pop = []
    result_fit = []
    for i in range(len(population)-1,-1,-1):
        if d[i][1] not in result_pop:
            result_pop.append(d[i][1])
            result_fit.append(d[i][0])
            del d[i]
    result_pop.append([d[i][1] for i in range(len(d))])
    result_fit.append([d[i][0] for i in range(len(d))])
    return [result_pop[:size],result_fit[:size]]