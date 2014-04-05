#!/usr/bin/python


from  dateutil import parser
import pandas as pd

df = pd.read_csv('../data/SRC__from03_06_2014__to03_06_2014.csv')

df['row_ind'] = 1

x = list(df['SERVICEORDERDATE'])

def create_key(f):
    date_key = int(str(parser.parse(f).date()).replace('-',''))
    return date_key


df['date_key'] = df['SERVICEORDERDATE'].map(create_key)

print df[['SERVICEORDERDATE','date_key' ]][2230:]


#print df.columns

grouped = df.groupby(['SERVICECODE', 'date_key']).row_ind.sum()

#print grouped

#x = df['SERVICEORDERDATE'][1:].split(' ',0)

