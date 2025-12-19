import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('netflix.csv')
print(df.head())

plt.show()  

# just for update

print(df.info())

#for update again

print(df.isnull().sum())

# for update again

print(df['director'].value_counts())

# for update again

print(df['cast'].value_counts())
#for update again

print(df['country'].value_counts())


#for update again

print(df['listed_in'].value_counts())