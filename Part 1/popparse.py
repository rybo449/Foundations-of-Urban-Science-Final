import pandas as pd
import sys

df1 = pd.read_csv(sys.argv[1])
df2 = pd.read_csv(sys.argv[2])
df2 = df2.drop_duplicates('U.S. Regional Title').sort('U.S. Regional Title')
df2['Average'] = df2
df2.to_csv(sys.argv[5])
df1['Total Population 2000'] = df1['Total Population 2000'] + df1['Total Population 2000']*0.037
df1 = df1[['Total Population 2000', 'Area Name-Legal/Statistical Area Description']]

df1['Area Name-Legal/Statistical Area Description'] = df1['Area Name-Legal/Statistical Area Description']
splits = df1['Area Name-Legal/Statistical Area Description'].str.split(' ')
list1 = splits.str[:-1]
temp1 = []
#print list1
for i in list1:
	temp = ''
	c = 0
	for j in i:
		if c != 0:
			temp = str(temp)+" "+str(j)
		else:
			temp = str(j)
		c += 1
	print temp
	temp1.append(temp)
df1['Area Name-Legal/Statistical Area Description'] = temp1
#print df1.tail()
#print df1.head()
df1.to_csv(sys.argv[4])
#df1.to_csv(sys.argv[3])
df2 = df2.sort(['U.S. Regional Title'])
#df2['U.S. Regional Title'] = df2['U.S. Regional Title']
#df2 = df2[['Total Population 2010']]
#print df1.head()
#print df2.head()
merged = pd.merge(df1, df2, how = 'inner', left_on = 'Area Name-Legal/Statistical Area Description', right_on = 'U.S. Regional Title')
print merged.head()
#merged['Patent Intensity'] = merged['Average']/(merged['Total Population 2000'])*100000
#print merged.head()
merged.to_csv(sys.argv[3])
#print df1.head()
#print df2.head()
