import random

def one_point(parent1, parent2):
    border = random.randint(0,len(parent1)-2)
    child1 = parent1[:border+1] + parent2[border+1:]
    child2 = parent2[:border+1] + parent1[border+1:]
    return [child1,child2]


def discret_recombination_nn(parent1, parent2):
    num_of_params = len(parent1)
    schema = ''.join(random.choice('01') for i in range(num_of_params))
    child1 = []
    child2 = []
    for gen_choice in range(len(schema)):
        if schema[gen_choice] == '0':
            child1.append(parent1[gen_choice])
            child2.append(parent2[gen_choice])
        else:
            child1.append(parent2[gen_choice])
            child2.append(parent1[gen_choice])
    return [child1,child2]