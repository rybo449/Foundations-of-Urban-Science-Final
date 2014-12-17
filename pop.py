import sys
import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv(sys.argv[1])
df = df[["GeoFips","2001","2002","2003","2004","2005"]]
df['Average'] = df.mean(1)
print df.head()
df.to_csv(sys.argv[2])
