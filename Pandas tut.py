import numpy as np
import pandas as pd

def header(msg):

	header("Read file from text")
filename= 'Fremont_weather.txt'

# Reading from text file
df=pd.read_csv(filename)

# Print to check
print(df)

# Describe the status of the list,helps calculating needed data
print(df.describe())

# Sort the list according to a given coloumn
print(df.sort_values('record_high',ascending=False))

# Only prints one coloumn
print(df.loc[:,['record_high']])

#Prints the 10th row and only two columns
print(df.loc[9,['record_high','record_low']])

#Print the data type of the columns
print(df.dtypes)

# Slicing the table
print(df.iloc[3:5,[0,3]])

#For filtering according to a constraint
print(df[df.avg_precipitation>1.0])

# Assignment method
print(df[df['month'].isin(['Dec','Jan','Feb'])])

# changes value of a given location
df.loc[9,['avg_precipitation']]=4.00
print(df.loc[9:11,['record_high','record_low']])
print(df)

# assigns not a number to a given location
df.loc[9,['avg_precipitation']]=np.nan
print(df)

# Creating a new column
df['avg_day']=(df.avg_low+df.avg_high)/2
print(df)

# Renaming a single coloumn

df=df.rename(columns={'avg_precipitation':'avg_rain'})
print(df)

# Renaming all coloumns
df.columns = ['month','av_hi','av_low','rec_high','rec_low','av_rain','av_day']
print(df)

# Iterating in a dataframe
for index,row in df.iterrows():
	print(index,row["month"],row["av_rain"])

