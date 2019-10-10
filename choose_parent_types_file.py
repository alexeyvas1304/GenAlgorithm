import random

def roulette_wheel (population,fitnesses):
    probabilities = [fitnesses[i]/sum(fitnesses) for i in range(len(fitnesses))] # придумать что-то лучше
    for i in range(1,len(probabilities)):
        probabilities[i]+=probabilities[i-1]
    c1 = random.random()
    for i in range(len(probabilities)):
        if c1<probabilities[i]:
            parent1 = i
            break
    c2 = random.random()
    for i in range(len(probabilities)):
        if c2<probabilities[i]:
            parent2 = i
            break
    return [parent1,parent2]


def hamming_dist(osob1,osob2):
    dist = 0
    for i in range(len(osob1)):
        if osob1[i]!=osob2[i]:
            dist+=1
    return dist


def inbriding_phenotype(population,fitnesses):
    parent1 = random.randint(0,len(population)-1)
    min_dist = float("Inf")
    for i in range (len(population)):
        if i != parent1:
            dist = hamming_dist(population[parent1], population[i])
            if dist < min_dist:
                min_dist = dist
                parent2 = i
    return [parent1,parent2]


def inbriding_genotype(population,fitnesses):
    parent1 = random.randint(0,len(population)-1)
    min_abs_diff = float("Inf")
    for i in range (len(fitnesses)):
        if i != parent1:
            diff = abs(fitnesses[parent1]-fitnesses[i])
            if diff < min_abs_diff:
                min_abs_diff = diff
                parent2 = i
    return [parent1,parent2]

# С аутбридингом аналогично

    
def panmixy(population,fitnesses):
    parent1 = random.randint(0,len(fitnesses)-1)
    parent2 = random.randint(0,len(fitnesses)-1)
    return [parent1, parent2]