import pandas as pd
import numpy as np
import sys
import os

names = os.listdir(sys.argv[1])
os.chdir(sys.argv[1])
c = 0
for i in names:
	df = pd.read_csv(i)
	#print df.head()
	if c == 0:
		df1 = df[['Class', 'Total']]
		df1 = df1.sort(['Total'], ascending = True)
		df1.rename(columns={'Total':i[:-4]}, inplace=True)
	else:
		df2 = df[['Class', 'Total']]
		df2 = df2.sort(['Total'], ascending = True)
		df1 = pd.merge(df2, df1, how = 'outer', left_on = 'Class', right_on = 'Class')
		df1.rename(columns={'Total':i[:-4]}, inplace=True)
	c += 1
df1 = df1.fillna(0)
last_row = df1.ix[df1.last_valid_index()]
df1 = df1[last_row.argsort()]
#df1.set_index('Class')
print df1.head()
os.chdir('..')
df1.to_csv(sys.argv[2])