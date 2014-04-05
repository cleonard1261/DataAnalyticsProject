#!/usr/bin/python



import pandas as pd

df = pd.read_csv('../data/SRC__from03_06_2014__to03_06_2014.csv')


df['row_ind'] = 1

print pd.columns
