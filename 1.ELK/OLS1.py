import numpy as np
import matplotlib.pyplot as plt
import pandas
import pandas as pd
from statsmodels.formula.api import ols
#import statsmodels.api as sm
#from scipy import linspace,polyval,polyfit,sqrt,stats,randn,optimize
from statsmodels.stats.anova import anova_lm
from scipy import stats
#import statsmodels as sm

import csv
with open('/home/user/development/hello_python/1.ELK/ELK21_oringnal.csv') as csvfile:
    reader=pd.read_csv(csvfile)

    Z=reader.Dia_C_Xdisp
    A=reader.TC1_Temp_Z0
    B=reader.TC1_Temp_Z5
    C=reader.TC1_temp_melt
    D=reader.TC1_pressure_melt



       # print(B)
       # print(C)
       # print(D)
       # print(Z)

#input date (all need to be nx1 array)
#df_list=[]
#for df in pd.read_csv(u"data\aqi\ELK11.csv"):
#print (df.Dia_C_Xdisp)
#X=np.array([10,20,30,40,50,60,70,80,85,90])
#Y=np.array([5,10,15,20,25,30,35,40,45,50])


#Dep. Variable
#Z=np.array([99,91,81,70,62,51,44,36,25,17])


#正規化資料

#    A_1=stats.zscore(A)


#    print(Z)
    A=stats.zscore(A)
    B=stats.zscore(B)
    C=stats.zscore(C)
    D=stats.zscore(D)
    Z=stats.zscore(Z)
#    print(Z)
    data = pandas.DataFrame({'a': A, 'b': B, 'c': C, 'd': D, 'z': Z})
#    print(data)
# Fit the model 前面的字串代表線性相關式

    model = ols("z ~ a + b + c + d", data).fit()
#model = polyfit("z ~ x + y", data).fit()
#model=sm.OLS(X,Y,Z).fit()


# Print the summary
    print(model.summary())

    print("\nRetrieving manually the parameter estimates:")
    print(model._results.params)

# ANOVA Table
    anova_results = anova_lm(model)

    print('\nANOVA results')
    print(anova_results)

    plt.show()

#Key Words： standard coeficent, linear regression