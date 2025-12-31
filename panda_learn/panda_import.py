import pandas as pd

df = pd.read_csv(r"C:\Users\Prakash\Desktop\Python learn\panda_learn\data.csv",index_col="Name")
#print(df[["Height","Name","Weight"]].to_string())


#Selection By rows


print(df.loc["Charizard"])
