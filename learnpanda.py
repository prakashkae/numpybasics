#load data in pandas\

import pandas as pd 
df = pd.read_csv('pokemon_data.csv')
#print(df.head(3))
#print(df['Name'][0:5])

#df_xlsx = pd.read_excel('pokemon_data.xlsx')
#print(df_xlsx.head(3))

#df = pd.read_csv('pokemon_data.txt', delimiter='\t')
#print(df.head(5))


# Reading data in pandas

#print(df.iloc[2,1])
#print(df.loc[df['Type 1'] == 'Grass'])

#print(df.describe())

#sort values
#print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))


    #making changes in data

#print(df.head(5))    
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#print(df['Total'])



#for saving

df.to_csv('modified.csv',index=False)