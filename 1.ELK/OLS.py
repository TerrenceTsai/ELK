import numpy as np
import matplotlib.pyplot as plt
import pandas
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from scipy import stats

#input date (all need to be nx1 array)

X=np.array([10,20,30,40,50])
Y=np.array([5,10,15,20,25])


#Dep. Variable
Z=np.array([99,85,66,44,30])


#!正規化資料
X=stats.zscore(X)
Y=stats.zscore(Y)
Z=stats.zscore(Z)

data = pandas.DataFrame({'x': X, 'y': Y, 'z': Z})

# Fit the model 前面的字串代表線性相關式
model = ols("z ~ x + y", data).fit()

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