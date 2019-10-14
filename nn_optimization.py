import numpy as np
import random
from mlp_class import NET
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score, balanced_accuracy_score, precision_score, \
                            recall_score, f1_score, roc_auc_score
# Генерация популяции

def generate(dictionary):

    def get_params(d):   
        tmp_params = {}
        for key, value in d.items():
            tmp_params[key] = random.choice(value)    
        return tmp_params

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

    # формируем первоначальную популяцию, выбирая случайным образом параметры особей из словаря params
    new_individs = []
    for i in range(dictionary['size_of_population']):
        new_individs.append([v for k, v in get_params(params).items()])
    
    return new_individs


# Проверка на допустимость значений
def validation(dictionary, osob):

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

    flg = max([0 if x in v else 1 for x, (k, v) in zip(osob, params.items())])
    if flg: 
        return False
    else: 
        return True


# Рассчет функции приспособленности
def fitness_one(dictionary, osob):
    
    # Проверка входных данных
    def check_input_matrix(data, target_col='target'):
        flag = True
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        # проверка типов данных
        for t in data.dtypes.iloc[:-1: 1]:
            if t not in numerics:
                raise ValueError('Wrong data: Признаки должны иметь численный тип')  
        if data[target_col].dtype not in numerics:
            raise ValueError('Wrong data: Целевое значение должно быть целочисленным')  
        if data.isnull().sum().sum() > 0:
            raise ValueError('Wrong data: Есть пропуски в данных') 
            
        return True
    
    
    # Обучение MLP
    def train_nn(d, o):

        data = dictionary["data"]
        target_col = dictionary["target_name"]
        
        if check_input_matrix(data, target_col): 
            X = data.drop(target_col, axis=1)
            y = data[target_col]
        else:
            raise ValueError('Wrong data')
        
        X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=o[0], random_state=1)
        
        model = NET(epoch=d['n_epoch_mlp'],
                    eps=d['eps_mlp'],
                    eta=d['eta_mlp'],
                    hidden=o[1],
                    func_hidden=o[2],
                    func_out=o[3]
                   )
        
        model.fit(X_train, y_train)
        pred_train = model.predict(X_train)
        pred_valid = model.predict(X_valid)
        
        return y_train, y_valid, pred_train, pred_valid
    
     # Функция для оценки качества классификации
    def evaluate(y_true, y_pred, d):
        try:
            acc = balanced_accuracy_score(y_true, y_pred)
            prc = precision_score(y_true, y_pred)
            rec = recall_score(y_true, y_pred)
            f1 = f1_score(y_true, y_pred)
        except:
            return 0
        
        if   d['quality_type'] == 1: 
            return acc
        elif d['quality_type'] == 2: 
            return prc
        elif d['quality_type'] == 3: 
            return rec
        elif d['quality_type'] == 4: 
            return f1
    
    y_train, y_valid, pred_train, pred_valid = train_nn(dictionary, osob)
        
    return evaluate(y_valid, pred_valid, dictionary)