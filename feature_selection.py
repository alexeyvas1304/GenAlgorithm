import random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def generate (d):
        dataset = d["dataset"]
        size = d['size_of_population']
        data = pd.read_csv(dataset, index_col= 0)
        n_features = len(data.columns)-1
        population = []
        while len(population)<size:
            osob = [0]*n_features
            for i in range(n_features):
                osob[i] = random.randint(0,1)
            population.append(osob)
        return population
    
def fitness_one (d,osob):
    dataset = d['dataset']
    data = pd.read_csv(dataset, index_col= 0)
    tmp = data.shape[1]-1
    slicer = []
    for i in range (len(osob)):
        if osob[i] ==1:
            slicer.append(i) 
    data = data.iloc[:,slicer+[-1]]
    X_train,X_test,y_train,y_test = train_test_split (data.drop(columns = 'target'),data['target'],test_size = 0.3,random_state = 42)
    clf = LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial').fit(X_train, y_train)
    y_pred_test = clf.predict(X_test)
    #print(accuracy_score(y_test,y_pred_test),'-',1/(tmp-sum(osob)))
    return accuracy_score(y_test,y_pred_test)- 1/(tmp-sum(osob))

def validation(d,osob):
    if osob is None or max(osob) == 0:
        return False
    else:
        return True