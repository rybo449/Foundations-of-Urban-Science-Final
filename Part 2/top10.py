import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
df = pd.read_csv(sys.argv[1])

df = df.sort(['Total'], ascending = False)
df1 = df[['Class','Class Title','Total']].head(10)
df1.to_csv('NY.csv')
df = pd.read_csv(sys.argv[2])
df = df.sort(['Total'], ascending = False)
df1 = df[['Class','Class Title','Total']].head(10)
df1.to_csv('San Jose.csv')
df = pd.read_csv(sys.argv[3])
df = df.sort(['Total'], ascending = False)
df1 = df[['Class','Class Title','Total']].head(10)
df1.to_csv('LA.csv')
df = pd.read_csv(sys.argv[4])
df = df.sort(['Total'], ascending = False)
df1 = df[['Class','Class Title','Total']].head(10)
df1.to_csv('Boston.csv')