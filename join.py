import sys
import pandas as pd

df1 = pd.read_csv(sys.argv[1])
df2 = pd.read_csv(sys.argv[2])
print df1.head()
print df2.head()
merged = pd.merge(df1,df2, how = 'inner', left_on = 'GeoFips', right_on = 'FIPS')
print merged.head()