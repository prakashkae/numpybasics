import pandas as pd

df = pd.read_csv('pokemon_data.csv')

#conditonal Changes

df.loc[df['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'


df = pd.read_csv('modified.csv')


#aggregate statistics

df = pd.read_csv('modified.csv')
df = df.groupby('Type 1').describe()
print(df)