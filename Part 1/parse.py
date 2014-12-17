import pandas as pd


f = open('1.txt', 'rU')
l = []
c = 0
for i in f:
	temp = []
	token = i.strip('\t').split(' \t\n\r')
	print token
	if c == 0:
		for j in token:
			temp.append(j)
		header = temp
	else:
		for j in token:
			temp.append(j)
		l.append(temp)
	c += 1

df = pd.DataFrame(l)
df.columns = header
print df.head()
df.to_csv('output.csv')