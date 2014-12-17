import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np
from bokeh.plotting import *
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import statsmodels.api as sm

df = pd.read_csv(sys.argv[1])

z = np. polyfit(np.log(df['AVG. GDP/CAPITA']), np.log(df['AVG. PATENT INTENSITY']), 1)
f = np.poly1d(z)
x_new = np.linspace(min(np.log(df['AVG. GDP/CAPITA'])), max(np.log(df['AVG. GDP/CAPITA'])), 100)
y_new = f(x_new)


plt.scatter(np.log(df['AVG. GDP/CAPITA']), np.log(df['AVG. PATENT INTENSITY']))
plt.plot(np.log(df['AVG. GDP/CAPITA']), np.log(df['AVG. PATENT INTENSITY']), 'o', x_new,y_new)

'''plt.plot(df['LN AVG. GDP/CAPITA'], df['LN PATENT INTENSITY'],  'bo')
fit = np.polyfit(df['LN AVG. GDP/CAPITA'], df['LN PATENT INTENSITY'], 1)

fit_fn = np.poly1d(fit)

plt.plot(df['LN AVG. GDP/CAPITA'], df['LN PATENT INTENSITY'], fit_fn(df['LN AVG. GDP/CAPITA']), 'ro')
'''
#model = sm.OLS(df['LN AVG. GDP/CAPITA'], df['LN PATENT INTENSITY'])
#results = model.fit()
#prstd, iv_l, iv_u = wls_prediction_std(results)
#plt.plot(df['LN PATENT INTENSITY'], results.fittedvalues, 'r', label="OLS")
plt.show()