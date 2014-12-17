import plotly.plotly as py
from plotly.graph_objs import *
import pandas as pd
import csv
import sys
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1])


cols = [col for col in df.columns if col not in ['Index', 'Class']]
df_list = []
for i in cols:
	df[i] = (df[i]> 0)
	df_list.append(df[i].tolist())

#plt.subplot(211)
#plt.imshow(df_list)
#plt.subplot(212)
#plt.imshow(df_list, cmap='Greys',  interpolation='nearest')
#plt.savefig('blkwht.png')

#plt.show()
#df1 = df[cols]

py.sign_in('Python-Demo-Account', 'gwt101uhh0')

data = Data([
    Heatmap(
        z=df_list,
        colorscale='YIGnBu'
    )
])
layout = Layout(
    title='YIGnBu'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='YIGnBu-heatmap')