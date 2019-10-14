import random
import numpy as np

def binary(dictionary, osob):
    c = random.randint(0,len(osob)-1)
    osob[c] = 1 - osob[c]
    return osob 

def mutation_nn(dictionary, osob):
    
    F = dictionary['data'].shape[0]
    params = {
            #размер отложенной выборки для валидации
            'valid_size': [float(x) for x in list(np.arange(0.1, 0.3, 0.0001))],
            #число нейронов на скрытом слое, доля от k
            'num_of_hidden' : range(round(F*0.5), round(F*0.9), 1),
            #функция активации на скрытом слое
            'func_hidden' : ['sigm', 'tanh'],  
            #функция активации на выходном слое
            'func_out' : ['sigm', 'tanh']  
    }
    param_keys = list(params.keys())

    c = random.randint(0, len(osob)-1)
    key = param_keys[c]
    osob[c] = random.choice(params[key])
    return osob 