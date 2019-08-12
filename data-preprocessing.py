### Data preprocessing ###

# I import the libraries
import pandas as pd
import numpy as np

url = "C:/Users/mellisos/Desktop/Programming/Python/python-course/train.csv"

df = pd.read_csv(url)
print(df.head())

print('######################################################')

print(df.tail())

# I save the data 
route = "C:/Users/mellisos/Desktop/Programming/Python/python-course/titanic.csv"

df.to_csv(route)


print('######################## Type of data ##############################')

# Type of data
print(df.dtypes)

print('################### Mathematical analysis ###########################a')
# Mathematical analysis

print(df.describe(include="all"))


print('################### Vizualice 60 rows ###########################a')
# Vizualice 60 rows

print(df.info)


print('################### Replace NaN of age ###########################a')
# I replace NaN of age

print(df['Age'].mean())

meanAge = 30

print(df['Age'].replace(np.nan, meanAge))


print('################### Change categoric variables #######################')
# I change categoric variables for numeric variables

print(pd.get_dummies(df, columns = ["Sex"], drop_first = True))


print('################### To group data Age #######################')
# I group the Age data

bins = [0, 5, 12, 18, 35, 60, 100]

names = ["1","2","3","4","5","6"]

df["Age"] = pd.cut(df["Age"], bins, labels = names)
print(df)
