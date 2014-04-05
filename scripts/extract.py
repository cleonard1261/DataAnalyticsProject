#!/usr/bin/python


from  dateutil import parser
import pandas as pd

df = pd.read_csv('../data/SRC__from03_06_2014__to03_06_2014.csv')

df['row_ind'] = 1

x = list(df['SERVICEORDERDATE'])


for y in x:
	dt = str(parser.parse(y).date())

df['date_key'] = dt.replace('-','')


#print df.columns

grouped = df.groupby(['SERVICECODE', 'date_key']).row_ind.sum()

print grouped

#x = df['SERVICEORDERDATE'][1:].split(' ',0)

