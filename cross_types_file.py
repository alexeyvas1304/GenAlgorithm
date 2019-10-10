import random

def one_point(parent1,parent2):
    border = random.randint (0,len(parent1)-2)
    child1 = parent1[:border+1] + parent2[border+1:]
    child2 = parent2[:border+1] + parent1[border+1:]
    return [child1,child2]

