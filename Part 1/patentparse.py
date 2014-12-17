import pandas as pd
import sys

df = pd.read_csv(sys.argv[1])
df1 = df[['2001', '2002', '2003', '2004', '2005']]
df1['Average'] = df1.mean(1)
#df1 = df.groupby(['2001', '2002', '2003', '2004', '2005']).mean()
#df1 = df1['Index']
df['Average'] = df1['Average']
print df.head()
df.to_csv(sys.argv[2])