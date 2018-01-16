import pandas as pd
import matplotlib.pyplot as plt
#using sympy
from sympy import *
import numpy as np

def linear_regression(X, Y):
    a, b = symbols('a b')
    residual = 0
    for i in range(len(X)):
        residual += (Y[i] - (a * X[i] + b)) ** 2

    print(expand(residual))
    f1 = diff(residual, a)
    f2 = diff(residual, b)
    print(f1)
    print(f2)
    res = solve([f1, f2], [a, b])
    return res[a], res[b]

def get_headers(dataframe):
    """
    Get the headers name of the dataframe
    :param dataframe:
    :return:
    """
    return dataframe.columns.values

#input_path = '/home/user/development/Github/DataAspirant_codes-master/Simple_linear_regression/Inputs/input_data.csv'

input_path = '/home/user/development/hello_python/Linear_regeression/BS11_copy_over_2.csv'
dataset = pd.read_csv(input_path,encoding = "utf8")
   # Get the dataset header names
dataset_headers = get_headers(dataset)
print ("Dataset Headers :: ", dataset_headers)
print(dataset[dataset_headers[4]])
print(dataset[dataset_headers[5]])
#print(len(dataset[dataset_headers[4]]))
a, b = linear_regression(dataset[dataset_headers[4]], dataset[dataset_headers[5]])
print('a=Gain, b= Bias')
print(a,b)

LR_X = dataset[dataset_headers[4]]
h = lambda x: a*x + b
H = np.vectorize(h)
LR_Y = H(LR_X)


plt.plot(LR_X, LR_Y, 'g')
plt.plot(dataset[dataset_headers[4]],dataset[dataset_headers[5]],'ro')
plt.show()