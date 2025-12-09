import pandas as pd

df = pd.read_csv('pokemon_data.csv')

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
print(new_df)

#new_df.to_csv('filtered_data.csv', index=False)

new_df = new_df.reset_index(drop=True)
print(new_df)