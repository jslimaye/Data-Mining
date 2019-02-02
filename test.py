import pandas as pd
import numpy as np 

df = pd.read_csv('Salaries.csv')

df2 = df
'''
bins = list()
for n,data in enumerate(df2['TotalPay']):
	if int(data) <= 50000:
		df2['TotalPay'][n] = "very low"
	elif (data > 50000) & (data <= 200000):
	        df2['TotalPay'][n] = "low"
	elif (data > 200000) & (data <= 350000):
		df2['TotalPay'][n] = "medium"
	elif (data > 350000) & (data <= 500000):
        	df2['TotalPay'][n] = "high"
	else:
	        df2['TotalPay'][n] = "very high"

'''
df2.head(5)
        
