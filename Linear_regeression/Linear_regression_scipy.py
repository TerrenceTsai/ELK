import pandas as pd
import matplotlib.pyplot as plt
#using sympy
from sympy import *
import numpy as np
from scipy import optimize


def get_headers(dataframe):
    """
    Get the headers name of the dataframe
    :param dataframe:
    :return:
    """
    return dataframe.columns.values


def residuals(p):
    k,b= p
    return Y-(k*X+b)

input_path = '/home/user/development/hello_python/Linear_regeression/BS11_copy_over_2.csv'
dataset = pd.read_csv(input_path,encoding = "utf8")

dataset_headers = get_headers(dataset)
print ("Dataset Headers :: ", dataset_headers)

X=dataset[dataset_headers[4]]
Y=dataset[dataset_headers[5]]
print(X,Y)
r=optimize.leastsq(residuals,[1,0])
k,b=r[0]
print("k=",k,'b=',b)

